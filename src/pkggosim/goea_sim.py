"""Simulate a Gene Ontology Enrichment Analysis (GOEA) on one set of randomly generated study genes."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
from random import shuffle
from goatools.go_enrichment import get_study_items
from pkggosim.utils import get_result_desc

class GoeaSim(object):
    """Simulate a Gene Ontology Enrichment Analysis (GOEA) on one set of randomly generated study genes."""

    ntobj_pvaltype = cx.namedtuple(
        "NtMtAll", "num_pvals num_sig_actual ctr fdr_actual frr_actual "
        "sensitivity specificity pos_pred_val neg_pred_val")

    def __init__(self, num_study_genes, num_null, study_genes_bg, objbg):
        #self.alpha = objbg['alpha']
        iniobj = _Init(num_study_genes, num_null, study_genes_bg, objbg)
#        # List of info for each pval: pval pval_corr reject expsig tfpn
#        self.nts_pvalmt = iniobj.get_nts_stugenes()
#        self.genes_stu = np.array(iniobj.pvals)
#        self.genes_stu_corr = np.array(iniobj.ntmult.pvals_corr)
#        # One namedtuple summarizing results of this P-Value simulation
#        self.nt_tfpn = self.get_nt_tfpn()
#
#    def prt_pvals(self, prt=sys.stdout):
#        """Print P-Values."""
#        pat = "{I:3} {PVAL:6.4f}=pval {PVAL_CORR:6.4f}=corr {R:5}=reject {S:5}=sig {TF}\n"
#        prt.write("{}\n".format(self.nt_tfpn))
#        for idx, ntpval in enumerate(self.nts_pvalmt):
#            prt.write(pat.format(
#                I=idx, PVAL=ntpval.pval, PVAL_CORR=ntpval.pval_corr,
#                R=ntpval.reject, S=ntpval.expsig, TF=ntpval.tfpn))
#        prt.write("\n")
#
#    def get_perc_sig(self, attrname="pvals"): # "pvals" or "pvals_corr"
#        """Calculate the percentage of p-values which are significant."""
#        pvals = getattr(self, attrname)
#        return self._get_perc_sig(pvals)[2]
#
#    def _get_perc_sig(self, pvals):
#        """Calculate the percentage of p-values which are significant."""
#        num_pvals_sig = sum(pvals < self.alpha)
#        num_pvals_tot = len(pvals)
#        return num_pvals_sig, num_pvals_tot, 100.0*num_pvals_sig/num_pvals_tot
#
#    @staticmethod
#    def _calc_ratio(top, bot_ab):
#        """Calc ratios: FDR, sensitivity, specificity, positive/negative predictive value."""
#        bottom = sum(bot_ab)
#        if bottom == 0:
#            # BH: "Return Q=0 if V+S=0 because no error of false rejection can be commited."
#            # True for other ratios as well
#            assert top == 0
#            return 0.0
#        return float(top)/bottom
#
#    def get_nt_tfpn(self):
#        """Calculate % of corrected p-values with errors: Type I or Type II, Type I, or Type II.
#
#        From: "Controlling the False Discovery Rate:
#               a Practical and Powerful Approach to Multiple Testing"
#              1995; Yoav Benjamini and Yosef Hochberg
#
#            The proportion of errors committed by falsely rejecting null hypothesis can
#            be viewed through the random variable Q = V/(V+S) or Q = V/R where:
#              V is the number of "True null hypotheses" which were "Declared significant"
#                or the number of "False Positives" (FP)
#              S is the number of "Non-true null hypotheses" which were "Declared significant"
#                or the number of "True Positives" (TP)
#              R is the number of hypotheses which were "Declared significant"
#                or the number of all Positives (FP+TP)
#
#            Note: A single simulation of a multipletest correction run on one set of P-Values
#            will return a variable Q where Q is (Q=V/(V+S) or Q=V/R or Q=FP/(FP+TP)).
#
#            The random variable Q cannot be controlled to be below a user-specified alpha at
#            this level of simulation because if m(0)=m (all tests are "true null hypotheses")
#            and even a single null hypotheses is rejected v/r=1 and Q cannot be controlled.
#
#        To obtain an actual FDR which can be compared to the expected FDR, multiple sets
#        of P-Values must be generated with each set of P-Values corrected for multiple testing.
#        """
#        ctr = cx.Counter([nt.tfpn for nt in self.nts_pvalmt]) # Counts of TP TN FP FN
#        #pylint: disable=invalid-name
#        TP, TN, FP, FN = [ctr[name] for name in ["TP", "TN", "FP", "FN"]]
#        tot_errors = FP + FN # Count of Type I errors and Type II errors
#        # tot_correct = TP + TN
#        # Significant(Correct) or Type I Error (Not significant)
#        tot_sig_y = sum(nt.reject for nt in self.nts_pvalmt)
#        assert tot_sig_y == TP + FP
#        # Not Significant(Correct) or Type II Error (significant)
#        tot_sig_n = sum(not nt.reject for nt in self.nts_pvalmt)
#        assert tot_sig_n == TN + FN
#        num_pvals = len(self.nts_pvalmt)
#        assert tot_sig_y + tot_sig_n == num_pvals
#        return self.ntobj_pvaltype(
#            num_pvals      = len(self.nts_pvalmt),
#            num_sig_actual = tot_sig_y,
#            ctr            = ctr,
#            # FDR: expected proportion of false discoveries (FP or Type I errors) among discoveries
#            fdr_actual     = self._calc_ratio(FP, (TP, FP)), # typI(FP)/sig_y(FP+TP)
#            frr_actual     = self._calc_ratio(FN, (TN, FN)), # typII(FN)/sig_n(TN+FN)
#            # SENSITIVITY & SPECIFICITY are not affected by prevalence
#            # SENSITIVITY: "true positive rate", recall, "probability of detection"
#            sensitivity    = self._calc_ratio(TP, (TP, FN)), # TP/(TP+FN) screening
#            # SPECIFICITY: "true negative rate"
#            specificity    = self._calc_ratio(TN, (TN, FP)), # TN/(TN+FP) confirmation
#            # "Positive predictive value" and "Negative predictive value" are affected by prevalence
#            pos_pred_val   = self._calc_ratio(TP, (TP, FP)), # TP/(TP+FP)
#            neg_pred_val   = self._calc_ratio(TN, (TN, FN))) # TN/(TN+FN)

class _Init(object):
    """Init GoeaSim object: Create random hypotheses test results(pvals), run multipletest correction."""

    #ntobj_mt = cx.namedtuple("NtMtPvals", "pval pval_corr reject expsig tfpn")
    ntobj_mt = cx.namedtuple("NtMtPvals", "study_gene     reject expsig tfpn")

    def get_nts_stugenes(self):
        """Combine data to return nts w/fields: pvals, pvals_corr, reject, expsig."""
        goeasim_results = []
        for study_gene, expsig in zip(self.genes_stu, self.expsig):
            reject = study_gene in self.genes_sig
            goeasim_results.append(self.ntobj_mt(
                study_gene = study_gene,
                reject     = reject,
                expsig     = expsig, # False->True Null; True->Non-true null
                tfpn       = get_result_desc(reject, expsig))) # Ex: TP, TN, FP, or FN
        return goeasim_results

    def __init__(self, num_study_genes, num_null, study_genes_bg, objbg):
        self.objbg = objbg
        # I. Genes in two groups: Different than population AND no different than population
        self.genes_stu = None  # List of randomly-generated gene lists
        self.expsig = None # List of bool/gene. True -> gene is intended to be significant (Non-true null)
        self._init_study_genes(num_study_genes, num_null, study_genes_bg)
        assert len(self.genes_stu) == num_study_genes
        assert num_study_genes - sum(self.expsig) == num_null
        goea_results = self._init_goea_results()
        self.genes_sig = get_study_items(goea_results)
        print "STUDY({}) SIG({}) NULL({})".format(len(self.genes_stu), len(self.genes_sig), num_null)
#        self.ntmult = self._ntobj_mtsm._make(multipletests(self.genes_stu, **self.objbg))

    def _init_goea_results(self):
        """Run Gene Ontology Analysis."""
        attrname = "p_{METHOD}".format(METHOD=self.objbg.objbg.method)
        alpha = self.objbg.objbg.alpha
        keep_if = lambda nt: getattr(nt, attrname) < alpha
        return self.objbg.objgoea.run_study(self.genes_stu, keep_if=keep_if)

    def _init_study_genes(self, num_study_genes, num_null, genes_study_bg):
        """Generate 2 sets of genes: Not intended significant & intended to be significant."""
        # Calculate the number of "Non-true null hypotheses":
        #   Study genes found to be different than the population genes likely not by chance
        num_ntnull = num_study_genes - num_null
        # 1. Generate random genes: Significant and Random
        #   True  -> gene is intended to be significant(different from the population)
        #   False -> If gene is determined significant, it occured by chance
        genes_pop_bg = list(self.objbg.pop_genes.difference(genes_study_bg))
        genes_study_bg = list(genes_study_bg)
        shuffle(genes_pop_bg)
        shuffle(genes_study_bg)
        genes_expsig = \
            [(g, True) for g in genes_study_bg[:num_ntnull]] + \
            [(g, False) for g in genes_pop_bg[:num_null]]
        # 2. Extract "genes" and "intended significance" by transposing data
        self.genes_stu, self.expsig = zip(*genes_expsig)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
