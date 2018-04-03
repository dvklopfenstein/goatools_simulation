"""Simulate a multiple-test correction on one set of randomly generated P-values."""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

# Controlling the False Discovery Rate: a Practical and Powerful Approach to Multiple Testing
# http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf

# The false discovery rate (FDR) is defined as the ratio of the number of Type I errors
# by the number of significant tests.

# Ignore these:
#   Module 'numpy.random' has no 'uniform' member
#   No name 'multipletest' in module 'statsmodels.sandbox.stats.multicomp'
#pylint: disable=no-member, bad-whitespace

import sys
import collections as cx
import numpy as np
from statsmodels.sandbox.stats.multicomp import multipletests
from pkggosim.common.true_positive import get_tfpn, calc_ratio

#pylint: disable=too-many-arguments,too-many-function-args
class HypothesesSim(object):
    """Simulate a multiple-test correction on one set of randomly generated P-values."""

    ntobj_pvaltype = cx.namedtuple(
        "NtMtAll", "num_pvals num_sig_actual ctr fdr_actual frr_actual "
        "sensitivity sensitivity_tgt "
        "specificity pos_pred_val neg_pred_val "
        "num_correct num_Type_I num_Type_II num_Type_I_II "
        "perc_correct perc_Type_I perc_Type_II perc_Type_I_II")

    def __init__(self, hypoth_qty, num_null, multi_params, max_sigval, pval_surge):
        self.alpha = multi_params['alpha']
        iniobj = _Init(hypoth_qty, num_null, multi_params, max_sigval, pval_surge)
        # List of info for each pval: pval pval_corr reject expsig tfpn
        self.nts_pvalnt = iniobj.get_nts_pvals()
        self.pvals = np.array(iniobj.pvals)
        self.pvals_corr = np.array(iniobj.ntmult.pvals_corr)
        # One namedtuple summarizing results of this P-Value simulation
        self.nt_tfpn = self.get_nt_tfpn()
        #if self.nt_tfpn.fdr_actual != 0:
        #    self.prt_pvals()

    def prt_pvals(self, prt=sys.stdout):
        """Print P-Values."""
        pat = "{I:3} {PVAL:6.4f}=pval {PVAL_CORR:6.4f}=corr {R:5}=reject {S:5}=sig {TF}\n"
        prt.write("{}\n".format(self.nt_tfpn))
        for idx, ntpval in enumerate(self.nts_pvalnt):
            prt.write(pat.format(
                I=idx, PVAL=ntpval.pval, PVAL_CORR=ntpval.pval_corr,
                R=ntpval.reject, S=ntpval.expsig, TF=ntpval.tfpn))
        prt.write("\n")

    def get_perc_sig(self, attrname="pvals"): # "pvals" or "pvals_corr"
        """Calculate the percentage of p-values which are significant."""
        pvals = getattr(self, attrname)
        return self._get_perc_sig(pvals)[2]

    def _get_perc_sig(self, pvals):
        """Calculate the percentage of p-values which are significant."""
        num_pvals_sig = sum(pvals < self.alpha)
        num_pvals_tot = len(pvals)
        return num_pvals_sig, num_pvals_tot, 100.0*num_pvals_sig/num_pvals_tot

    def get_nt_tfpn(self):
        """Calculate % of corrected p-values with errors: Type I or Type II, Type I, or Type II.

        From: "Controlling the False Discovery Rate:
               a Practical and Powerful Approach to Multiple Testing"
              1995; Yoav Benjamini and Yosef Hochberg

            The proportion of errors committed by falsely rejecting null hypothesis can
            be viewed through the random variable Q = V/(V+S) or Q = V/R where:
              V is the number of "True null hypotheses" which were "Declared significant"
                or the number of "False Positives" (FP)
              S is the number of "Non-true null hypotheses" which were "Declared significant"
                or the number of "True Positives" (TP)
              R is the number of hypotheses which were "Declared significant"
                or the number of all Positives (FP+TP)

            Note: A single simulation of a multipletest correction run on one set of P-Values
            will return a variable Q where Q is (Q=V/(V+S) or Q=V/R or Q=FP/(FP+TP)).

            The random variable Q cannot be controlled to be below a user-specified alpha at
            this level of simulation because if m(0)=m (all tests are "true null hypotheses")
            and even a single null hypotheses is rejected v/r=1 and Q cannot be controlled.

        To obtain an actual FDR which can be compared to the expected FDR, multiple sets
        of P-Values must be generated with each set of P-Values corrected for multiple testing.
        """
        ctr = cx.Counter([nt.tfpn for nt in self.nts_pvalnt]) # Counts of TP TN FP FN
        ctr2 = cx.Counter([(nt.tfpn, nt.desc) for nt in self.nts_pvalnt])
        #pylint: disable=invalid-name
        TP, TN, FP, FN = [ctr[name] for name in ["TP", "TN", "FP", "FN"]]
        tot_errors = FP + FN # Count of Type I errors and Type II errors
        # tot_correct = TP + TN
        # Significant(Correct) or Type I Error (Not significant)
        tot_sig_y = sum(nt.reject for nt in self.nts_pvalnt)
        assert tot_sig_y == TP + FP
        # Not Significant(Correct) or Type II Error (significant)
        tot_sig_n = sum(not nt.reject for nt in self.nts_pvalnt)
        assert tot_sig_n == TN + FN
        num_pvals = len(self.nts_pvalnt)
        assert tot_sig_y + tot_sig_n == num_pvals
        #print "FFFFFFFF", sens_tgt_tp
        return self.ntobj_pvaltype(
            num_pvals      = len(self.nts_pvalnt),
            num_sig_actual = tot_sig_y,
            ctr            = ctr,
            # FDR: expected proportion of false discoveries (FP or Type I errors) among discoveries
            fdr_actual     = calc_ratio(FP, (TP, FP)), # typI(FP)/sig_y(FP+TP)
            frr_actual     = calc_ratio(FN, (TN, FN)), # typII(FN)/sig_n(TN+FN)
            # SENSITIVITY & SPECIFICITY are not affected by prevalence
            # SENSITIVITY: "true positive rate", recall, "probability of detection"
            sensitivity    = calc_ratio(TP, (TP, FN)), # TP/(TP+FN) screening
            sensitivity_tgt= self._get_sensitivity_tgt(ctr2),
            # SPECIFICITY: "true negative rate"
            specificity    = calc_ratio(TN, (TN, FP)), # TN/(TN+FP) confirmation
            # "Positive predictive value" and "Negative predictive value" are affected by prevalence
            pos_pred_val   = calc_ratio(TP, (TP, FP)), # TP/(TP+FP)
            neg_pred_val   = calc_ratio(TN, (TN, FN)), # TN/(TN+FN)

            num_correct    = TP + TN,
            num_Type_I     = FP,
            num_Type_II    = FN,
            num_Type_I_II  = tot_errors,
            perc_correct   = 100.0*ctr[0]/num_pvals,
            perc_Type_I    = 100.0*ctr[1]/num_pvals,
            perc_Type_II   = 100.0*ctr[2]/num_pvals,
            perc_Type_I_II = 100.0*tot_errors/num_pvals)

    @staticmethod
    def _get_sensitivity_tgt(ctr):
        """Get the senstivity for the target genes."""
        tgt_tp = ctr[('TP', 'tgt')]
        tgt_fn = ctr[('FN', 'tgt')]
        return calc_ratio(tgt_tp, (tgt_tp, tgt_fn))

class _Init(object):
    """Create random hypotheses test results(pvals), run multipletest correction."""
    #pylint: disable=too-few-public-methods

    # Multiple test correction results:
    #   1. statsmodels multiple test results for each P-value
    _ntobj_mtsm = cx.namedtuple("NtMtStatmod", "reject pvals_corr alpha_sidak alpha_bonf")
    #   2. summarized results for each P-value
    ntobj_mt = cx.namedtuple("NtMtPvals", "pval pval_corr reject expsig desc tfpn")

    def get_nts_pvals(self):
        """Combine data to return nts w/fields: pvals, pvals_corr, reject, expsig."""
        pvalsim_results = []
        items = zip(self.pvals, self.ntmult.pvals_corr, self.ntmult.reject, self.expsig, self.descs)
        for pval_orig, pval_corr, reject, expsig, desc in items:
            pvalsim_results.append(self.ntobj_mt(
                pval      = pval_orig,
                pval_corr = pval_corr,
                reject    = reject,
                expsig    = expsig, # False->True Null; True->Non-true null
                desc      = desc,   # bg tgt surge
                tfpn      = get_tfpn(reject, expsig))) # Ex: TP, TN, FP, or FN
        return pvalsim_results

    def __init__(self, hypoth_qty, num_null, multi_params, max_sigval, pval_surge):
        self.multi_params = multi_params
        # I. UNCORRECTED P-VALUES:
        self.max_sigval = max_sigval # Max P-Val for non-true null hypotheses. Ex: 0.05 0.03 or 0.01
        assert isinstance(self.max_sigval, float), "INVALID MAX P-VALUE({V})".format(
            V=self.max_sigval)
        self.pvals = None  # List of randomly-generated uncorrected P-values
        self.expsig = None # List of bool/P-value. True->Pval intended to be signif. (Non-true null)
        self.descs = None  # bg (True Null), tgt (not true Null), surge (unusually low pvals)
        self._init_pvals(num_null, hypoth_qty-num_null, pval_surge)
        assert len(self.pvals) == hypoth_qty
        assert hypoth_qty - sum(self.expsig) == num_null
        # II. P-VALUES CORRECTED BY MULTIPLE-TEST CORRECTION:
        # Run a multipletest correction on this set of pvals
        self.ntmult = self._ntobj_mtsm._make(multipletests(self.pvals, **self.multi_params))
        #self._chk_reject()

    def _init_pvals(self, num_null, num_ntnull, pval_surge):
        """Generate 2 sets of P-values: Not intended significant & intended to be significant."""
        # 1. Generate random P-values: Significant and Random
        #   True  -> P-value is intended to be significant
        #   False -> If P-value is significant, it occured by chance
        pos = self._get_notnulls(num_ntnull, pval_surge)
        neg = [(p, False, "bg") for p in np.random.uniform(0, 1, size=num_null)]
        pvals_expsig = pos + neg
        # 2. Extract "P-values" and "intended significance" by transposing data
        self.pvals, self.expsig, self.descs = zip(*pvals_expsig)

    def _get_notnulls(self, num_ntnull, pval_surge):
        """Generate Not-Null P-values: intended to be significant."""
        if pval_surge is None:
            return [(p, True, 'tgt') for p in np.random.uniform(0, self.max_sigval, size=num_ntnull)]
        bg_num = num_ntnull - pval_surge['qty']
        # print "PVAL_SURGE", pval_surge
        lo_num = pval_surge['qty']
        lo_max = pval_surge['max_sigpval']
        return [(p, True, 'tgt') for p in np.random.uniform(0, self.max_sigval, size=bg_num)] + \
               [(p, True, 'surge') for p in np.random.uniform(0, lo_max, size=lo_num)]

    def _chk_reject(self):
        """Check that all values marked with reject==True, have pval_corr < alpha."""
        alpha = self.multi_params['alpha']
        for reject, pval in zip(self.ntmult.reject, self.ntmult.pvals_corr):
            if reject:
                assert pval < alpha

# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
