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

from pkggosim.utils import shuffle_associations

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

    def rpt_versions(self, prt, results_sig, results_rnd):
        """Report results GOEAs on actual associations and randon associations."""
        prt.write("\nSIMULATION RESULTS ON {DATE}:\n".format(DATE=datetime.date.today()))
        prt.write("\n  SETTINGS AND GO-DAG VERSION:\n")
        prt.write("    Multitest Params: {INFO}\n".format(INFO=self.get_str_mcorr()))
        prt.write("    GO-DAG version:   {INFO}\n".format(INFO=self.go_dag.version))
        prt.write("\n  SIMULATION RESULTS:\n")

    def rpt_results(self, prt, results_dct):
        txt = "      {G:5,} significant GO terms found for {s:4}/{S:4} study genes in {DESC} association\n"
        for dct in results_dct:
            prt.write(txt.format(
                G=len(dct['goea_results']), s=len(dct['genes_dct']),
                S=len(dct['genes_study']), DESC="actual"))
        prt.write("\n")

    def run_actual_assc(self, assoc_ens2gos, genes_pop, genes_study_arg):
        """Simulate the significance of the user-provided study vs. the population gene sets."""
        genes_study = set(genes_study_arg)
        goeaobj = self.get_goeaobj(genes_pop, assoc_ens2gos)
        goea_results = goeaobj.run_study(genes_study, keep_if=lambda nt: nt.p_fdr_bh < self.alpha)
        fout_txt = "goea_immune_sig_{N:04}.txt".format(N=len(genes_study))
        goeaobj.wr_txt(fout_txt, goea_results)
        genes_sig = get_study_items(goea_results)
        if genes_study != genes_sig:
            msg = "EXPECTED ALL {S} STUDY GENES TO SHOW SIGNIFICANT GO TERMS. FOUND {M}\n"
            sys.stdout.write(msg.format(
                S=len(genes_study), M=len(genes_study.difference(genes_sig))))
        return {'goea_results':goea_results, 'genes_sig':genes_sig, 'genes_study':genes_study}

    def run_random_assc(self, assoc_ens2gos, genes_pop, genes_study_arg):
        """Simulate no significance"""
        genes_study = set(genes_study_arg)
        rand_assoc = shuffle_associations(assoc_ens2gos)
        goeaobj = self.get_goeaobj(genes_pop, rand_assoc)
        goea_results = goeaobj.run_study(genes_study, keep_if=lambda nt: nt.p_fdr_bh < self.alpha)
        fout_txt = "goea_immune_rnd_{N:04}.txt".format(N=len(genes_study))
        goeaobj.wr_txt(fout_txt, goea_results)
        genes_rnd = get_study_items(goea_results)
        assert len(goea_results) == 0, \
            "EXPECTED NO SIGNIFICANT GO TERMS IN RANDOM SIMULATION. FOUND {N}".format(
                N=len(goea_results))
        return {'goea_results':goea_results, 'genes_sig':genes_rnd, 'genes_study':genes_study}

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
