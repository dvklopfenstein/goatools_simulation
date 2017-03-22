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

    def __init__(self, num_pvalues, num_sig, alpha, method): #, **kws):
        #self.fnc_maxsig = kws.get('fnc_maxsig', lambda pvals: self.alpha/len(pvals))
        # Data members: P-value
        self.markers = None # One for each P-value. True if P-value is intended to be significant.
        self.pvals = None   # List of randomly-generated uncorrected P-value
        self._init_pvals(num_pvalues, num_sig)
        # Data members: Multipletest correction
        self.pvals_corr = None
        self.reject = None
        self.alpha_sidak = None
        self.alpha_bonf = None
        self._init_multisim(alpha, method)

    def get_zipped_data(self):
        """combine data to return: pvals, pvals_corr, reject, markers"""
        nto = cx.namedtuple("Nt", "pval pval_corr reject marker")
        return [nto._make(vs) for vs in zip(self.pvals, self.pvals_corr, self.reject, self.markers)]

    @staticmethod
    def get_err_type(ntdata):
        """Return one of: Good Result=0; Type I error=1; Type II error=2"""
        reject = ntdata.reject
        marker = ntdata.marker
        # pylint: disable=multiple-statements, bad-whitespace
        if     marker and     reject: return 0 # Correct:     Significant
        if not marker and not reject: return 0 # Correct: Not Significant
        if not marker and     reject: return 1 # Type  I Error
        if     marker and not reject: return 2 # Type II Error
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
        pvals_markers = list(pvals_sig) + list(pvals_rnd)
        pvals_all, markers = zip(*pvals_markers)
        # 3. Set internal data members and do check
        self.markers = markers
        self.pvals = np.array(pvals_all)
        assert num_pvalues == len(self.pvals)

    def _init_multisim(self, alpha, method):
        """Generate one set of random pvalues and do multipletest correction."""
        #pylint: disable=undefined-variable
        self.reject, self.pvals_corr, self.alpha_sidak, self.alpha_bonf = multipletests(
            self.pvals, alpha, method)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
