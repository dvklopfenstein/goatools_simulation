"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
from random import shuffle
from pkggosim.goea_objbg import GoeaSimObj


class RunGoeas(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntdesc = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, multiparams, pop_genes, assc):
        self.objgoea = GoeaSimObj(multiparams['alpha'], multiparams['method'])
        self.pop_genes = pop_genes
        self.assc = assc

    def run_goeas(self, study_lens, study_genes, study_desc, perc_null):
        """Run GOEAs."""
        results_list = []
        num_genes = len(study_genes)
        runfnc = self.objgoea.run_random_assc if perc_null == 100 else self.objgoea.run_actual_assc
        for study_len in sorted(study_lens):
            shuffle(study_genes)
            results_list.append((
                self.ntdesc(name=study_desc, perc_null=perc_null, tot_study=len(study_genes)),
                runfnc(self.assc, self.pop_genes, study_genes[:study_len])))
            if num_genes <= study_len:
                return results_list
        return results_list

    def prt_results(self, results_sims, prt=sys.stdout):
        """Prints a summary of results from function, run_goeas."""
        itemfmt = "{G:6,}   {s:5}/{S:5} {PNULL:10}% {ASSC} {TOT_STUDY:6,} {NAME}\n"
        self.objgoea.prt_versions(prt)
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
            #self.objgoea.prt_results(prt, results)


# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
