"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
import datetime
from random import shuffle
from goatools.go_enrichment import get_study_items
from pkggosim.goea.objbase import DataBase
from pkggosim.goea.objassc import DataAssc


class RunPrelim(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntobj = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, alpha, method, pop_genes, assc_file):
        self.objbase = DataBase(alpha, method)
        self.objassc = DataAssc(assc_file, pop_genes)
        self.maskout = None

    def prt_summary(self, prt):
        """Print summary of simulation parameters and background data."""
        prt.write("\nWRITTEN: {DATE}:\n\n".format(DATE=datetime.date.today()))
        self.objbase.prt_summary(prt)
        self.objassc.prt_summary(prt)

    def set_maskout(self, pop_maskout_genes):
        """Sets genes to mask out from population genes."""
        self.maskout = pop_maskout_genes

    def run_goeas(self, study_lens, study_genes, study_desc, perc_null):
        """Run GOEAs."""
        results_list = []
        study_genes = list(study_genes.intersection(self.objassc.pop_genes))
        num_genes = len(study_genes)
        runfnc = self.run_random_assc if perc_null == 100 else self.run_actual_assc
        for study_len in sorted(study_lens):
            shuffle(study_genes)
            ntdesc = self.ntobj(name=study_desc, perc_null=perc_null, tot_study=len(study_genes))
            results_list.append((ntdesc, runfnc(study_genes[:study_len], ntdesc)))
            if num_genes <= study_len:
                return results_list
        return results_list

    def prt_results(self, results_sims, prt=sys.stdout):
        """Prints a summary of results from function, run_goeas."""
        itemfmt = "{G:6,}   {s:5}/{S:5} {PNULL:10}% {ASSC} {TOT_STUDY:6,} {NAME}\n"
        self.objbase.prt_versions(prt)
        prt.write("Sig. GOs Study genes % True Null   assc Max Genes Study Name\n")
        prt.write("-------- ----------- ----------- ------ --------- ----------\n")
        for ntdesc, res in results_sims:
            prt.write(itemfmt.format(
                G=len(res['goea_results']),
                s=len(res['genes_sig']),
                S=len(res['genes_study']),
                NAME=ntdesc.name,
                PNULL=ntdesc.perc_null,
                TOT_STUDY=ntdesc.tot_study,
                ASSC=res['assc_desc']))
        prt.write("\n")

    def get_pop_genes_masked(self, genes_study):
        """Reduce set of population genes using the mask."""
        if self.maskout is None:
            return self.objassc.pop_genes
        return self.objassc.pop_genes.difference(self.maskout).union(genes_study)

    def run_actual_assc(self, genes_study_arg, ntdesc):
        """Simulate the significance of the user-provided study vs. the population gene sets."""
        genes_study = set(genes_study_arg)
        assc_desc = 'actual'
        alpha = self.objbase.alpha
        genes_pop_masked = self.get_pop_genes_masked(genes_study)
        goeaobj = self.objbase.get_goeaobj(genes_pop_masked, self.objassc.assc)
        goea_results = goeaobj.run_study(genes_study, keep_if=lambda nt: nt.p_fdr_bh < alpha)
        fout_txt = "goea_{DESC}_sig_{N:04}.txt".format(DESC=ntdesc.name, N=len(genes_study))
        goeaobj.wr_txt(fout_txt, goea_results)
        genes_sig = get_study_items(goea_results)
        # if genes_study != genes_sig:
        #     msg = "FOUND {STUSIG:4} OF {STU:4} {DESC} GENES TO BE SIGNIFICANT\n"
        #     genes_study_sig = genes_study.intersection(genes_sig)
        #     sys.stdout.write(msg.format(
        #         STU=len(genes_study), STUSIG=len(genes_study_sig), DESC=ntdesc.name))
        return {'goea_results':goea_results, 'genes_sig':genes_sig, 'genes_study':genes_study,
                'assc_desc':assc_desc}

    def run_random_assc(self, genes_study_arg, ntdesc):
        """Simulate no significance"""
        genes_study = set(genes_study_arg)
        assc_desc = 'random'
        alpha = self.objbase.alpha
        rand_assoc = self.objassc.shuffle_associations(self.objassc.assc)
        goeaobj = self.objbase.get_goeaobj(self.objassc.pop_genes, rand_assoc)
        goea_results = goeaobj.run_study(genes_study, keep_if=lambda nt: nt.p_fdr_bh < alpha)
        fout_txt = "goea_{DESC}_rnd_{N:04}.txt".format(DESC=ntdesc.name, N=len(genes_study))
        goeaobj.wr_txt(fout_txt, goea_results)
        genes_rnd = get_study_items(goea_results)
        assert len(goea_results) == 0, \
            "EXPECTED NO SIGNIFICANT GO TERMS IN RANDOM SIMULATION. FOUND {N}".format(
                N=len(goea_results))
        return {'goea_results':goea_results, 'genes_sig':genes_rnd, 'genes_study':genes_study,
                'assc_desc':assc_desc}

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
