"""Runs GOEA Simulations. Holds background data/params, like GO-DAG & alpha."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import datetime
from pkggosim.utils import shuffle_associations
from goatools.base import get_godag
from goatools.go_enrichment import GOEnrichmentStudy, get_study_items

class GoeaSimObj(object):
    """Holds paramaters and data used in every GOEA Simulation."""

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

    def prt_versions(self, prt):
        """Report results GOEAs on actual associations and randon associations."""
        prt.write("\nSIMULATION RESULTS ON {DATE}:\n".format(DATE=datetime.date.today()))
        prt.write("\n  SETTINGS AND GO-DAG VERSION:\n")
        prt.write("    Multitest Params: {INFO}\n".format(INFO=self.get_str_mcorr()))
        prt.write("    GO-DAG version:   {INFO}\n".format(INFO=self.go_dag.version))
        prt.write("\n  SIMULATION RESULTS:\n")

    def run_actual_assc(self, assoc_ens2gos, genes_pop, genes_study_arg):
        """Simulate the significance of the user-provided study vs. the population gene sets."""
        genes_study = set(genes_study_arg)
        assc_desc = 'actual'
        goeaobj = self.get_goeaobj(genes_pop, assoc_ens2gos)
        goea_results = goeaobj.run_study(genes_study, keep_if=lambda nt: nt.p_fdr_bh < self.alpha)
        fout_txt = "goea_immune_sig_{N:04}.txt".format(N=len(genes_study))
        goeaobj.wr_txt(fout_txt, goea_results)
        genes_sig = get_study_items(goea_results)
        if genes_study != genes_sig:
            msg = "EXPECTED ALL {S} STUDY GENES TO SHOW SIGNIFICANT GO TERMS. FOUND {M}\n"
            sys.stdout.write(msg.format(
                S=len(genes_study), M=len(genes_study.difference(genes_sig))))
        return {'goea_results':goea_results, 'genes_sig':genes_sig, 'genes_study':genes_study,
                'assc_desc':assc_desc}

    def run_random_assc(self, assoc_ens2gos, genes_pop, genes_study_arg):
        """Simulate no significance"""
        genes_study = set(genes_study_arg)
        assc_desc = 'random'
        rand_assoc = shuffle_associations(assoc_ens2gos)
        goeaobj = self.get_goeaobj(genes_pop, rand_assoc)
        goea_results = goeaobj.run_study(genes_study, keep_if=lambda nt: nt.p_fdr_bh < self.alpha)
        fout_txt = "goea_immune_rnd_{N:04}.txt".format(N=len(genes_study))
        goeaobj.wr_txt(fout_txt, goea_results)
        genes_rnd = get_study_items(goea_results)
        assert len(goea_results) == 0, \
            "EXPECTED NO SIGNIFICANT GO TERMS IN RANDOM SIMULATION. FOUND {N}".format(
                N=len(goea_results))
        return {'goea_results':goea_results, 'genes_sig':genes_rnd, 'genes_study':genes_study,
                'assc_desc':assc_desc}

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
