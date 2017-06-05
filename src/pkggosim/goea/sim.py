"""Simulate a Gene Ontology Enrichment Analysis (GOEA) on a set of random study genes."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
from random import shuffle
from goatools.go_enrichment import get_study_items
from pkggosim.common.utils import get_result_desc, calc_ratio

class GoeaSim(object):
    """Simulate a Gene Ontology Enrichment Analysis (GOEA) on a set of random study genes."""

    ntobj = cx.namedtuple(
        "NtMtAll", "num_genes num_sig_actual ctr fdr_actual frr_actual "
        "sensitivity specificity pos_pred_val neg_pred_val")

    def __init__(self, num_study_genes, num_null, pobj):
        iniobj = _Init(num_study_genes, num_null, pobj)
        # List of info for each study gene: geneid reject expected_significance tfpn
        self.nts_goea_res = iniobj.get_nts_stugenes()
        # One namedtuple summarizing results of this GOEA simulation
        self.nt_tfpn = self.get_nt_tfpn()

    def get_nt_tfpn(self):
        """Calculate various statistical quantities of interest, including simulated FDR."""
        ctr = cx.Counter([nt.tfpn for nt in self.nts_goea_res]) # Counts of TP TN FP FN
        #pylint: disable=invalid-name, bad-whitespace
        TP, TN, FP, FN = [ctr[name] for name in ["TP", "TN", "FP", "FN"]]
        # Significant(Correct) or Type I Error (Not significant)
        tot_sig_y = sum(nt.reject for nt in self.nts_goea_res)
        assert tot_sig_y == TP + FP
        # Not Significant(Correct) or Type II Error (significant)
        tot_sig_n = sum(not nt.reject for nt in self.nts_goea_res)
        assert tot_sig_n == TN + FN
        num_genes = len(self.nts_goea_res)
        assert tot_sig_y + tot_sig_n == num_genes
        return self.ntobj(
            num_genes      = len(self.nts_goea_res),
            num_sig_actual = tot_sig_y,
            ctr            = ctr,
            # FDR: expected proportion of false discoveries (FP or Type I errors) among discoveries
            fdr_actual     = calc_ratio(FP, (TP, FP)), # typI(FP)/sig_y(FP+TP)
            frr_actual     = calc_ratio(FN, (TN, FN)), # typII(FN)/sig_n(TN+FN)
            # SENSITIVITY & SPECIFICITY are not affected by prevalence
            # SENSITIVITY: "true positive rate", recall, "probability of detection"
            sensitivity    = calc_ratio(TP, (TP, FN)), # TP/(TP+FN) screening
            # SPECIFICITY: "true negative rate"
            specificity    = calc_ratio(TN, (TN, FP)), # TN/(TN+FP) confirmation
            # "Positive predictive value" and "Negative predictive value" are affected by prevalence
            pos_pred_val   = calc_ratio(TP, (TP, FP)), # TP/(TP+FP)
            neg_pred_val   = calc_ratio(TN, (TN, FN))) # TN/(TN+FN)


class _Init(object):
    """Run GOEA on randomly-created "True Null" gene sets and "Non-true Null" gene sets."""

    ntobj = cx.namedtuple("NtGoeaRes", "study_gene reject expsig tfpn")

    def get_nts_stugenes(self):
        """Combine data to return nts w/fields: pvals, pvals_corr, reject, expsig."""
        goeasim_results = []
        for study_gene, expsig in zip(self.genes_stu, self.expsig):
            reject = study_gene in self.genes_sig
            #pylint: disable=bad-whitespace
            goeasim_results.append(self.ntobj(
                study_gene = study_gene,
                reject     = reject,
                expsig     = expsig, # False->True Null; True->Non-true null
                tfpn       = get_result_desc(reject, expsig))) # Ex: TP, TN, FP, or FN
        return goeasim_results

    def __init__(self, num_study_genes, num_null, pobj):
        self.pobj = pobj
        # I. Genes in two groups: Different than population AND no different than population
        self.genes_stu = None  # List of randomly-generated gene lists
        self.expsig = None # List of bool/gene. True:gene is intended to be signif.(Non-true null)
        self._init_study_genes(num_study_genes, num_null)
        assert len(self.genes_stu) == num_study_genes, "{} {}".format(len(self.genes_stu), num_study_genes)
        assert num_study_genes - sum(self.expsig) == num_null
        goea_results = self._init_goea_results()
        self.genes_sig = get_study_items(goea_results)
        num_study = len(self.genes_stu)
        num_sig = len(self.genes_sig)
        sys.stdout.write("NULL({NULL}) STUDY({STU}) EXP_SIG({EXP}) ACT_SIG({SIG})\n".format(
            STU=num_study, SIG=num_sig, EXP=num_study-num_null, NULL=num_null))

    def _init_goea_results(self):
        """Run Gene Ontology Analysis."""
        attrname = "p_{METHOD}".format(METHOD=self.pobj.objbase.method)
        keep_if = lambda nt: getattr(nt, attrname) < self.pobj.objbase.alpha
        genes_pop_masked = self.pobj.genes_null_bg.union(self.genes_stu)
        objgoea = self.pobj.objbase.get_goeaobj(genes_pop_masked, self.pobj.objassc.assc)
        return objgoea.run_study(self.genes_stu, keep_if=keep_if)

    def _init_study_genes(self, num_study_genes, num_null):
        """Generate 2 sets of genes: Not intended significant & intended to be significant."""
        # Calculate the number of "Non-true null hypotheses":
        #   Study genes found to be different than the population genes likely not by chance
        num_ntnull = num_study_genes - num_null
        # 1. Generate random genes: Significant and Random
        #   True  -> gene is intended to be significant(different from the population)
        #   False -> If gene is determined significant, it occured by chance
        genes_pop_bg = list(self.pobj.genes_null_bg)
        genes_study_bg = list(self.pobj.genes_study_bg)
        shuffle(genes_pop_bg)
        shuffle(genes_study_bg)
        genes_expsig = \
            [(g, True) for g in genes_study_bg[:num_ntnull]] + \
            [(g, False) for g in genes_pop_bg[:num_null]]
        # 2. Extract "genes" and "intended significance" by transposing data
        self.genes_stu, self.expsig = zip(*genes_expsig)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
