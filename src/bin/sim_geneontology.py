#!/usr/bin/env python
"""Runs a gene ontology analyses on gene rich in immune functions.

#################################################################
GENE ONTOLOGY SIMULATION
#################################################################

Two GOEA simulations are run with a set of study genes that are rich in immune functions:

  1) Input: Current GO-geneid associations.
     Expected result: All study genes are enriched

  2) Input: Randomly shuffled GO-geneid associations
     Expected result:  No study genes are enriched


*****************************************************************
Results log from the run on May, 22, 2017:
*****************************************************************

SIMULATION RESULTS ON 2017-05-22:

  SETTINGS AND GO-DAG VERSION:
    Multitest Params: alpha(0.05) method(fdr_bh)
    GO-DAG version:   go-basic.obo: fmt(1.2) rel(2017-05-20) 48,661 GO Terms

  SIMULATION RESULTS:
      2,545 significant GO terms found for 2157 immune genes in actual association
          0 significant GO terms found for 2157 immune genes in random association

*****************************************************************
Discussion
*****************************************************************
Both gene ontology simulations produced the expected results:

The first simulation indicated that all study genes were enriched, as expected.

The second simulation indicated that no study genes were enriched, as expected.


"""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import datetime
from random import shuffle

#from pkgsim.data_geneids_rich_immune import geneids as genes_immune
from pkgsim.genes_immune import GENES
from pkgsim.utils import shuffle_associations
from pkgsim.randseed import RandomSeed32

from goatools_suppl.data.ensmusg2sym import ensm2sym
from goatools_suppl.proj_data import GoatoolsDataMaker

from goatools.base import get_godag
from goatools.go_enrichment import GOEnrichmentStudy, get_study_items

class GoeaSimObj(object):
    """Return GOEnrichmentStudy objects to run GOEA simulations."""

    def __init__(self, alpha, method):
        self.alpha = alpha
        self.method = method
        self.go_dag = get_godag()

    def get_goeaobj(self, pop_genes, assoc_geneid2gos):
        """Return a GOEnrichmentStudy specific for user-provided pop_genes and associations."""
        return GOEnrichmentStudy(
            pop_genes,
            assoc_geneid2gos,
            self.go_dag,
            propagate_counts=False,
            alpha=self.alpha,
            methods=[self.method])

    def get_str_mcorr(self):
        """Print parameters and versions of GO-DAG used in this simulation."""
        return "alpha({A}) method({M})".format(A=self.alpha, M=self.method)


def main(seed, prt=sys.stdout):
    """Return a list of all GO IDs associated with protein-coding mouse genes."""
    seed = RandomSeed32(seed)
    # 1. Get objects needed for a gene-ontology simulation: pop_genes, assc, GO-DAG
    obj = GoeaSimObj(alpha=0.05, method='fdr_bh')
    genes_mus = ensm2sym.keys()  # Population genes
    genes_immune = list(GENES)   # Study genes
    assoc_ens2gos = GoatoolsDataMaker.get_assoc_data("gene_association.mgi", genes_mus)
    # 2. SIMULATE SIGNIFICANCE TO IMMUNE: Population is all mouse genes
    results_sig = run_assc(run_actual_assc, obj, assoc_ens2gos, genes_mus, genes_immune)
    # 3. SIMULATE NO SIGNIFICANCE:
    results_rnd = run_assc(run_random_assc, obj, assoc_ens2gos, genes_mus, genes_immune)
    # 4. REPORT RESULTS:
    rpt_results(prt, obj, results_sig, results_rnd)
    seed.prt(prt)

def rpt_results(prt, obj, results_sig, results_rnd):
    """Report results GOEAs on actual associations and randon associations."""
    prt.write("\nSIMULATION RESULTS ON {DATE}:\n".format(DATE=datetime.date.today()))
    prt.write("\n  SETTINGS AND GO-DAG VERSION:\n")
    prt.write("    Multitest Params: {INFO}\n".format(INFO=obj.get_str_mcorr()))
    prt.write("    GO-DAG version:   {INFO}\n".format(INFO=obj.go_dag.version))
    prt.write("\n  SIMULATION RESULTS:\n")
    txt = "      {N:5,} significant GO terms found for {M} immune genes in {DESC} association\n"
    for sig in results_sig:
        prt.write(txt.format(N=len(sig['goea_results']), M=len(sig['genes']), DESC="actual"))
    for rnd in results_rnd:
        prt.write(txt.format(N=len(rnd['goea_results']), M=len(rnd['genes']), DESC="random"))

def run_assc(run_fnc, obj, assoc_ens2gos, genes_mus, genes_immune):
    """Run GOEAs on incrementing study sizes with randomly selected study genes."""
    results = []
    for exp in reversed(range(2, 12)):  # 4, 8, ..., 256, 512, 1024, 2048
        shuffle(genes_immune)
        qty = pow(2, exp)
        results.append(run_fnc(obj, assoc_ens2gos, genes_mus, genes_immune[:qty]))
    return results

def run_actual_assc(obj, assoc_ens2gos, genes_mus, genes_immune):
    """SIMULATE SIGNIFICANCE TO IMMUNE."""
    genes_immune = set(genes_immune)
    goeaobj = obj.get_goeaobj(genes_mus, assoc_ens2gos)
    goea_results = goeaobj.run_study(genes_immune, keep_if=lambda nt: nt.p_fdr_bh < 0.05)
    fout_txt = "goea_immune_{N:04}.txt".format(N=len(genes_immune))
    goeaobj.wr_txt(fout_txt, goea_results)
    genes_sig = get_study_items(goea_results)
    if genes_immune != genes_sig:
        msg = "EXPECTED ALL {S} STUDY GENES TO SHOW SIGNIFICANT GO TERMS. FOUND {M}\n"
        sys.stdout.write(msg.format(
            S=len(genes_immune), M=len(genes_immune.difference(genes_sig))))
    return {'goea_results':goea_results, 'genes':genes_sig}

def run_random_assc(obj, assoc_ens2gos, genes_mus, genes_immune):
    """SIMULATE NO SIGNIFICANCE."""
    rand_assoc = shuffle_associations(assoc_ens2gos)
    goeaobj = obj.get_goeaobj(genes_mus, rand_assoc)
    goea_results = goeaobj.run_study(genes_immune, keep_if=lambda nt: nt.p_fdr_bh < 0.05)
    fout_txt = "goea_immune_{N:04}.txt".format(N=len(genes_immune))
    goeaobj.wr_txt(fout_txt, goea_results)
    genes_rnd = get_study_items(goea_results)
    assert len(goea_results) == 0, \
        "EXPECTED NO SIGNIFICANT GO TERMS IN RANDOM SIMULATION. FOUND {N}".format(
            N=len(goea_results))
    return {'goea_results':goea_results, 'genes':genes_rnd}

if __name__ == '__main__':
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
