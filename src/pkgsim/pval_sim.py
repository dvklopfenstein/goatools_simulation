"""Simulate multiple-test correction of P-values with randomly generated P-values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

# Controlling the False Discovery Rate: a Practical and Powerful Approach to Multiple Testing
# http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf

# Ignore these:
#   Module 'numpy.random' has no 'uniform' member
#   No name 'multipletest' in module 'statsmodels.sandbox.stats.multicomp'
#pylint: disable=no-member, no-name-in-module

# import sys
import collections as cx
import numpy as np
from statsmodels.sandbox.stats.multicomp import multipletests

class PvalSim(object):
    """Simulate ONE multiple-test correction of P-values."""

    ntobj_pvaltype = cx.namedtuple(
        "NtMtAll", "act_sig_seen "
        "num_correct num_Type_I num_Type_II num_Type_I_II "
        "perc_correct perc_Type_I perc_Type_II perc_Type_I_II")

    def __init__(self, num_pvalues, num_sig, multi_params, max_sigval):
        self.alpha = multi_params['alpha']
        iniobj = _Init(num_pvalues, num_sig, multi_params, max_sigval)
        self.nts_pvalmt = iniobj.get_nts_pvals()
        self.pvals = np.array(iniobj.pvals)
        self.pvals_corr = np.array(iniobj.pvals_corr)

    def get_err_cnts(self):
        """Return counts of Type I Error, Type II Error, and  correct."""
        return cx.Counter([nt.err_type for nt in self.nts_pvalmt])

    def get_perc_err(self):
        """Calculate % of corrected p-values with errors: Type I or Type II, Type I, or Type II."""
        res_cnt = self.get_err_cnts()
        res_cnt[3] = res_cnt[1] + res_cnt[2] # Count of both error types
        num_pvals = len(self.nts_pvalmt)
        #pylint: disable=bad-whitespace
        return self.ntobj_pvaltype(
            act_sig_seen=sum(self.pvals_corr < self.alpha),
            num_correct    = res_cnt[0],
            num_Type_I     = res_cnt[1],
            num_Type_II    = res_cnt[2],
            num_Type_I_II  = res_cnt[3],
            perc_correct   = 100.0*res_cnt[0]/num_pvals,
            perc_Type_I    = 100.0*res_cnt[1]/num_pvals,
            perc_Type_II   = 100.0*res_cnt[2]/num_pvals,
            perc_Type_I_II = 100.0*res_cnt[3]/num_pvals)

    def get_perc_sig(self, attrname="pvals"): # "pvals" or "pvals_corr"
        """Calculate the percentage of p-values which are significant."""
        pvals = getattr(self, attrname)
        return self._get_perc_sig(pvals)[2]

    def _get_perc_sig(self, pvals):
        """Calculate the percentage of p-values which are significant."""
        num_pvals_sig = sum(pvals < self.alpha)
        num_pvals_tot = len(pvals)
        return num_pvals_sig, num_pvals_tot, 100.0*num_pvals_sig/num_pvals_tot


class _Init(object):
    """Init PvalSim object: Create random P-Values, run multipletest correction"""

    # Multiple test correction results:
    #   1. statsmodels multiple test results for each P-value
    ntobj_mtsm = cx.namedtuple("NtMtStatmod", "reject pvals_corr alpha_sidak alpha_bonf")
    #   2. summarized results for each P-value
    ntobj_mt = cx.namedtuple("NtMtPvals", "pval pval_corr reject expsig err_type")

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
        #print self.get_perc_err()

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
                err_type  = self.get_errtype(reject, expsig)))
        return pvalsim_results

    @staticmethod
    def get_errtype(reject, expsig):
        """Return description of the result of one simulation."""
        # pylint: disable=multiple-statements, bad-whitespace
        if     expsig and     reject: return 0 # Correct:     Significant
        if not expsig and not reject: return 0 # Correct: Not Significant
        if not expsig and     reject: return 1 # Type  I Error (False Positive)
        if     expsig and not reject: return 2 # Type II Error (False Negative)
        assert True, "UNEXPECTED ERROR TYPE"

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
        #        # print "PVALSIMCONCL", self.get_perc_err()

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
