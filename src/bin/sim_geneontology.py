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

from pkgsim.data_geneids_rich_immune import geneids as geneids_immune
from pkgsim.utils import shuffle_associations

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


def main(prt=sys.stdout):
    """Return a list of all GO IDs associated with protein-coding mouse genes."""
    # 1. Get objects needed for a gene-ontology simulation: pop_genes, assc, GO-DAG
    obj = GoeaSimObj(alpha=0.05, method='fdr_bh')
    geneids_mus = set(ensm2sym.keys()) # Population genes
    tot_genes_immune = len(geneids_immune) # Study genes (genes rich in immune functions)
    assoc_ens2gos = GoatoolsDataMaker.get_assoc("gene_association.mgi", geneids_mus)
    # 2. SIMULATE SIGNIFICANCE TO IMMUNE:
    #   Run gene-ontology simulation with a set of genes rich in immune function:
    #     Population genes: All mouse genes
    #     Study genes:      Mouse genes rich in various immune GOs
    goeaobj_sig = obj.get_goeaobj(geneids_mus, assoc_ens2gos)
    goea_results_sig = goeaobj_sig.run_study(geneids_immune, keep_if=lambda nt: nt.p_fdr_bh < 0.05)
    goeaobj_sig.wr_txt("goea_immune_sig.txt", goea_results_sig)
    geneids_sig = get_study_items(goea_results_sig)
    assert geneids_immune == geneids_sig, \
        "EXPECTED ALL {S} STUDY GENES TO SHOW SIGNIFICANT GO TERMS. FOUND {M}".format(
            S=tot_genes_immune, M=len(geneids_immune.difference(geneids_sig)))
    # 3. SIMULATE NO SIGNIFICANCE:
    #   Run gene-ontology simulation with associations randomly shuffled
    #   to simulate no significant.
    # Randomize associations
    rand_assoc = shuffle_associations(assoc_ens2gos)
    # 4. Run Gene Ontology Enrichment Analysis with ranldy shuffled associations
    goeaobj_rnd = obj.get_goeaobj(geneids_mus, rand_assoc)
    goea_results_rnd = goeaobj_rnd.run_study(geneids_immune, keep_if=lambda nt: nt.p_fdr_bh < 0.05)
    goeaobj_rnd.wr_txt("goea_immune_rnd.txt", goea_results_rnd)
    assert len(goea_results_rnd) == 0, \
        "EXPECTED NO SIGNIFICANT GO TERMS IN RANDOM SIMULATION. FOUND {N}".format(
            N=len(goea_results_rnd))
    # 5. REPORT RESULTS:
    prt.write("\nSIMULATION RESULTS ON {DATE}:\n".format(DATE=datetime.date.today()))
    prt.write("\n  SETTINGS AND GO-DAG VERSION:\n")
    prt.write("    Multitest Params: {INFO}\n".format(INFO=obj.get_str_mcorr()))
    prt.write("    GO-DAG version:   {INFO}\n".format(INFO=obj.go_dag.version))
    prt.write("\n  SIMULATION RESULTS:\n")
    txt = "      {N:5,} significant GO terms found for {M} immune genes in {DESC} association\n"
    prt.write(txt.format(N=len(goea_results_sig), M=tot_genes_immune, DESC="actual"))
    prt.write(txt.format(N=len(goea_results_rnd), M=tot_genes_immune, DESC="random"))


if __name__ == '__main__':
    main()

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
