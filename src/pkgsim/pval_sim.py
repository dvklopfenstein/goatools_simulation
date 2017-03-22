"""Simulate multiple-test correction of P-values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

# Controlling the False Discovery Rate: a Practical and Powerful Approach to Multiple Testing
# http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf

# Ignore these:
#   Module 'numpy.random' has no 'uniform' member
#   No name 'multipletest' in module 'statsmodels.sandbox.stats.multicomp'
#pylint: disable=no-member, no-name-in-module

import collections as cx
import numpy as np
from statsmodels.sandbox.stats.multicomp import multipletests

class PvalSim(object):
    """Simulate ONE multiple-test correction of P-values."""

    ntobj_mult = cx.namedtuple("NtMult", "reject pvals_corr alpha_sidak alpha_bonf")
    ntobj_info = cx.namedtuple("Nt", "pval pval_corr reject expsig")

    def __init__(self, num_pvalues, num_sig, multi_params): #, **kws):
        #self.fnc_maxsig = kws.get('fnc_maxsig', lambda pvals: self.alpha/len(pvals))
        self.multi_params = multi_params
        # Data members: P-value
        self.expsig = None # One for each P-value. True if P-value is intended to be significant.
        self.pvals = None  # List of randomly-generated uncorrected P-value
        self._init_pvals(num_pvalues, num_sig)
        # Data members: Multipletest correction
        self.ntmult = self._init_ntmult()
        self.pvals_corr = self.ntmult.pvals_corr

    def get_perc_sig(self, attrname="pvals"): # "pvals" or "pvals_corr"
        """Calculate the percentage of p-values which are significant."""
        pvals = getattr(self, attrname)
        return self._get_perc_sig(pvals)[2]

    def _get_perc_sig(self, pvals):
        """Calculate the percentage of p-values which are significant."""
        num_pvals_sig = sum(pvals < self.multi_params['alpha'])
        num_pvals_tot = len(pvals)
        return num_pvals_sig, num_pvals_tot, 100.0*num_pvals_sig/num_pvals_tot

    def get_zipped_data(self):
        """Combine data to return: pvals, pvals_corr, reject, expsig"""
        items = zip(self.pvals, self.ntmult.pvals_corr, self.ntmult.reject, self.expsig)
        return [self.ntobj_info._make(vs) for vs in items]

    @staticmethod
    def get_err_type(ntdata):
        """Return description of the result of one simulation."""
        reject = ntdata.reject
        expsig = ntdata.expsig
        # pylint: disable=multiple-statements, bad-whitespace
        if     expsig and     reject: return 0 # Correct:     Significant
        if not expsig and not reject: return 0 # Correct: Not Significant
        if not expsig and     reject: return 1 # Type  I Error (False Positive)
        if     expsig and not reject: return 2 # Type II Error (False Negative)
        assert True, "UNEXPECTED ERROR TYPE"

    def _init_pvals(self, num_pvalues, num_sig):
        """Create P-values randomly according to user-specified parameters."""
        num_rand = num_pvalues - num_sig
        #print "NNNNNNNNN", num_pvalues, "{}%".format(perc_sig), num_sig, num_rand, alpha
        # 1. Get random P-values and explicitly set P-value
        #   False -> If P-value is significant, it is by chance
        #   True  -> P-value is intended to be significant
        max_sig = 0.05/num_pvalues
        pvals_sig = [(p, True) for p in np.random.uniform(0, max_sig, size=num_sig)]
        pvals_rnd = [(p, False) for p in np.random.uniform(0, 1, size=num_rand)]
        # 2. Combine random P-values and explictly set P-value
        pvals_expsig = list(pvals_sig) + list(pvals_rnd)
        pvals_all, expsig = zip(*pvals_expsig)
        # 3. Set internal data members and do check
        self.expsig = expsig
        self.pvals = np.array(pvals_all)
        assert num_pvalues == len(self.pvals)

    def _init_ntmult(self):
        """Generate one set of random pvalues and do multipletest correction."""
        #pylint: disable=undefined-variable
        return self.ntobj_mult._make(multipletests(self.pvals, **self.multi_params))

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
