"""Simulate multiple-test correction of P-values with randomly generated P-values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

# Controlling the False Discovery Rate: a Practical and Powerful Approach to Multiple Testing
# http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf

# The false discovery rate (FDR) is defined as the ratio of the number of Type I errors
# by the number of significant tests.

# Ignore these:
#   Module 'numpy.random' has no 'uniform' member
#   No name 'multipletest' in module 'statsmodels.sandbox.stats.multicomp'
#pylint: disable=no-member, no-name-in-module

import sys
import collections as cx
import numpy as np
from statsmodels.sandbox.stats.multicomp import multipletests

class PvalSim(object):
    """Simulate ONE multiple-test correction of P-values."""

    ntobj_pvaltype = cx.namedtuple(
        "NtMtAll", "num_pvals num_sig_actual ctr fdr_actual frr_actual "
        "sensitivity specificity pos_pred_val neg_pred_val "
        "num_correct num_Type_I num_Type_II num_Type_I_II "
        "perc_correct perc_Type_I perc_Type_II perc_Type_I_II")

    def __init__(self, num_pvalues, num_sig, multi_params, max_sigval):
        self.alpha = multi_params['alpha']
        iniobj = _Init(num_pvalues, num_sig, multi_params, max_sigval)
        self.nts_pvalmt = iniobj.get_nts_pvals()
        self.pvals = np.array(iniobj.pvals)
        self.pvals_corr = np.array(iniobj.pvals_corr)
        self.nt_tfpn = self.get_nt_tfpn()
        #if self.nt_tfpn.fdr_actual != 0:
        #    self.prt_pvals()

    def prt_pvals(self, prt=sys.stdout):
        """Print P-Values."""
        pat = "{I:3} {PVAL:6.4f}=pval {PVAL_CORR:6.4f}=corr {R:5}=reject {S:5}=sig {TF}\n"
        prt.write("{}\n".format(self.nt_tfpn))
        for idx, ntpval in enumerate(self.nts_pvalmt):
            prt.write(pat.format(
                I=idx, PVAL=ntpval.pval, PVAL_CORR=ntpval.pval_corr,
                R=ntpval.reject, S=ntpval.expsig, TF=ntpval.tfpn))
        prt.write("\n")

    @staticmethod
    def _calc_ratio(top, bot_ab):
        """Calculate ratios like sensitivity, specificicty, positive/negative predictive value."""
        bottom = sum(bot_ab)
        if bottom == 0:
            assert top == 0
            return 0.0
        return float(top)/bottom

    def get_perc_sig(self, attrname="pvals"): # "pvals" or "pvals_corr"
        """Calculate the percentage of p-values which are significant."""
        pvals = getattr(self, attrname)
        return self._get_perc_sig(pvals)[2]

    def _get_perc_sig(self, pvals):
        """Calculate the percentage of p-values which are significant."""
        num_pvals_sig = sum(pvals < self.alpha)
        num_pvals_tot = len(pvals)
        return num_pvals_sig, num_pvals_tot, 100.0*num_pvals_sig/num_pvals_tot

    def get_err_cnts(self):
        """Return counts of Type I Error, Type II Error, and  correct."""
        return cx.Counter([nt.tfpn for nt in self.nts_pvalmt])

    def get_nt_tfpn(self):
        """Calculate % of corrected p-values with errors: Type I or Type II, Type I, or Type II."""
        ctr = self.get_err_cnts()
        #pylint: disable=invalid-name
        TP, TN, FP, FN = [ctr[name] for name in ["TP", "TN", "FP", "FN"]]
        tot_errors = FP + FN # Count of Type I errors and Type II errors
        # tot_correct = TP + TN
        # Significant(Correct) or Type I Error (Not significant)
        tot_sig_y = sum(nt.reject for nt in self.nts_pvalmt)
        assert tot_sig_y == TP + FP
        # Not Significant(Correct) or Type II Error (significant)
        tot_sig_n = sum(not nt.reject for nt in self.nts_pvalmt)
        assert tot_sig_n == TN + FN
        num_pvals = len(self.nts_pvalmt)
        assert tot_sig_y + tot_sig_n == num_pvals
        #pylint: disable=bad-whitespace
        return self.ntobj_pvaltype(
            num_pvals      = len(self.nts_pvalmt),
            num_sig_actual = tot_sig_y,
            ctr            = ctr,
            # FDR: expected proportion of false discoveries (FP or Type I errors) among discoveries
            fdr_actual     = self._calc_ratio(FP, (TP, FP)), # typI(FP)/sig_y(FP+TP)
            frr_actual     = self._calc_ratio(FN, (TN, FN)), # typII(FN)/sig_n(TN+FN)
            # Not affected by prevalence
            sensitivity    = self._calc_ratio(TP, (TP, FN)), # TP/(TP+FN) screening
            specificity    = self._calc_ratio(TN, (TN, FP)), # TN/(TN+FP) confirmation
            # Affected by prevalence
            pos_pred_val   = self._calc_ratio(TP, (TP, FP)), # TP/(TP+FP)
            neg_pred_val   = self._calc_ratio(TN, (TN, FN)), # TN/(TN+FN)

            num_correct    = TP + TN,
            num_Type_I     = FP,
            num_Type_II    = FN,
            num_Type_I_II  = tot_errors,
            perc_correct   = 100.0*ctr[0]/num_pvals,
            perc_Type_I    = 100.0*ctr[1]/num_pvals,
            perc_Type_II   = 100.0*ctr[2]/num_pvals,
            perc_Type_I_II = 100.0*tot_errors/num_pvals)


class _Init(object):
    """Init PvalSim object: Create random P-Values, run multipletest correction"""

    # Multiple test correction results:
    #   1. statsmodels multiple test results for each P-value
    ntobj_mtsm = cx.namedtuple("NtMtStatmod", "reject pvals_corr alpha_sidak alpha_bonf")
    #   2. summarized results for each P-value
    ntobj_mt = cx.namedtuple("NtMtPvals", "pval pval_corr reject expsig tfpn")

    def __init__(self, num_pvalues, num_sig, multi_params, max_sigval):
        self.multi_params = multi_params
        # I. UNCORRECTED P-VALUES:
        self.max_sigval = max_sigval
        assert isinstance(self.max_sigval, float), "INVALID MAX P-VALUE({V})".format(
            V=self.max_sigval)
        self.pvals = None  # List of randomly-generated uncorrected P-values
        self.expsig = None # One bool per P-value. True -> P-value is intended to be significant
        self._init_pvals(num_pvalues, num_sig)
        assert len(self.pvals) == num_pvalues
        assert sum(self.expsig) == num_sig
        # II. P-VALUES CORRECTED BY MULTIPLE-TEST CORRECTION:
        # Run a multipletest correction on this set of pvals
        self.ntmult = self.ntobj_mtsm._make(multipletests(self.pvals, **self.multi_params))
        self._chk_reject()
        self.pvals_corr = self.ntmult.pvals_corr
        # nt flds for each pval: pval pval_corr reject expsig
        self._chk_conclusions(num_pvalues, num_sig)
        #print self.get_nt_tfpn()

    @staticmethod
    def get_result_desc(reject, expsig):
        """Return description of the result of one simulation."""
        # pylint: disable=multiple-statements, bad-whitespace
        #                          |Declared       | Declared      |
        #                          |non-significant| significant   | Total
        # -------------------------+---------------+-------------+--------
        # True null hypotheses     | U TN          | V FP (Type I) |   m(0)
        # Non-true null hypotheses | T FN (Type II)| S TP          | m - m(0)
        #                          |      m - R    |       R       |   m
        if     expsig and     reject: return "TP" # Correct:     Significant
        if not expsig and not reject: return "TN" # Correct: Not Significant
        if not expsig and     reject: return "FP" # Type  I Error (False Positive)
        if     expsig and not reject: return "FN" # Type II Error (False Negative)
        assert True, "UNEXPECTED ERROR TYPE"
        # Power = 1 - beta; Beta < 20% good
        # average power: the proportion of the false hypotheses which are correctly rejected
        #   TP/(FN + TP)

    def get_nts_pvals(self):
        """Combine data to return nts w/fields: pvals, pvals_corr, reject, expsig"""
        pvalsim_results = []
        items = zip(self.pvals, self.ntmult.pvals_corr, self.ntmult.reject, self.expsig)
        for pval_orig, pval_corr, reject, expsig in items:
            #pylint: disable=bad-whitespace
            pvalsim_results.append(self.ntobj_mt(
                pval      = pval_orig,
                pval_corr = pval_corr,
                reject    = reject,
                expsig    = expsig,
                tfpn      = self.get_result_desc(reject, expsig)))
        return pvalsim_results

    def _chk_conclusions(self, num_pvalues, num_sig):
        """Check conclusions of a single simulation."""
        alpha = self.multi_params['alpha']
        num_sig_by_chance = 0
        for idx, (pval, expsig) in enumerate(zip(self.pvals, self.expsig)):
            # 1. Check that pvals expected to be significant are significant
            if expsig:
                if pval >= alpha:
                    # print pval, expsig
                    # print self.pvals_corr
                    assert pval < alpha, "PVAL({P}) COR({C}) ALPHA({A:4.2})".format(
                        P=pval, C=self.pvals_corr[idx], A=alpha)
            # 2. Check that pvals not expected to be significant
            #    have expected numbers of pvals which are significant by chance.
            else:
                if pval < alpha: # pval shows as significant by random chance
                    num_sig_by_chance += 1
        # Report
        if num_sig_by_chance > alpha*(num_pvalues - num_sig):
            pass
            # sys.stdout.write("{ACT} <= {EXP}(alpha({ALPH})*({P}-{S})\n".format(
            #     ACT=num_sig_by_chance,
            #     EXP=alpha*(num_pvalues - num_sig),
            #     ALPH=alpha, P=num_pvalues, S=num_sig))

        ## If no P-values are explicitly set to be significant,
        ## Report the % found to be significant by rrandom chance.
        #if num_sig_set == 0:
        #    num_sig_act = sum(self.pvals_corr < self.multi_params['alpha'])
        #    #assert num_sig_act == 0, "{} {}".format(num_sig_act, self.pvals_corr)
        #    if num_sig_act != 0:
        #        for ntd in self.get_ntspvals():
        #            if ntd.pval_corr < self.multi_params['alpha']:
        #                print "PVALSIMCONCL", ntd
        #        # print "PVALSIMCONCL", self.get_nt_tfpn()

    def _init_pvals(self, num_pvalues, num_sig):
        """Generate 2 sets of P-values: Not intended significant & intended to be significant."""
        num_rand = num_pvalues - num_sig
        # 1. Generate random P-values: Significant and Random
        #   True  -> P-value is intended to be significant
        #   False -> If P-value is significant, it occured by chance
        pvals_sig = [(p, True) for p in np.random.uniform(0, self.max_sigval, size=num_sig)]
        pvals_rnd = [(p, False) for p in np.random.uniform(0, 1, size=num_rand)]
        # 2. Extract "P-values" and "intended significance" by transposing data
        pvals_expsig = list(pvals_sig) + list(pvals_rnd)
        self.pvals, self.expsig = zip(*pvals_expsig)

    def _chk_reject(self):
        """Check that all values marked with reject==True, have pval_corr < alpha."""
        alpha = self.multi_params['alpha']
        for reject, pval in zip(self.ntmult.reject, self.ntmult.pvals_corr):
            if reject:
                assert pval < alpha

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
