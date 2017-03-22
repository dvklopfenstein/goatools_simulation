"""Simulate multiple-test correction of P-values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

from pkgsim.pval_sim import PvalSim

class PvalMtCorrSimsMany(object):
    """Simulate multiple-test correction of P-values."""

    def __init__(self, num_pvalues_list, num_sims, perc_sig_list):
        self.num_pvalues_list = num_pvalues_list
        self.num_sims = num_sims
        self.perc_sig_list = perc_sig_list

    def get_percsigs_simsets(self, alpha, method):
        """Do P-value and multiple test simulations. Return results."""
        percsig_simsets = []
        for perc_sig in self.perc_sig_list:
            numpvals_sims = []
            for num_pvals in self.num_pvalues_list:
                objsims = PvalSimMany(self.num_sims, num_pvals, perc_sig, alpha, method)
                # Save sets of simulations, stored according to num_pvals
                numpvals_sims.append((num_pvals, objsims))
            percsig_simsets.append((perc_sig, numpvals_sims))
        return percsig_simsets


class PvalSimMany(object):
    """Simulate MANY (N=num_sims) multiple-test correction of sets of P-values."""

    #pylint: disable=too-many-arguments
    def __init__(self, num_sims, num_pvals, perc_sig, alpha, method):
        self.num_sims = num_sims
        self.num_pvals = num_pvals
        self.perc_sig = perc_sig # perc_sig -> num_sig
        self.alpha = alpha
        self.method = method
        # Data members
        self.num_sig = int(round(float(self.perc_sig)*self.num_pvals/100.0))
        self.obj1sim_list = self._init_obj1sim_list(num_sims, num_pvals, alpha, method)

    def get_num_mksig(self):
        """Return the number of P-values intended to be significant."""
        return self.num_sig

    def get_num_mkrnd(self):
        """The number of randomly generated P-values, if any is significant, it is by chance."""
        return self.num_pvals - self.num_sig

    def _init_obj1sim_list(self, num_sims, num_pvals, alpha, method):
        """Simulate MANY multiple-test correction of P-values."""
        obj1sim_list = []
        for _ in range(num_sims):
            obj1sim = PvalSim(num_pvals, self.num_sig, alpha=alpha, method=method)
            obj1sim_list.append(obj1sim)
        return obj1sim_list

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
