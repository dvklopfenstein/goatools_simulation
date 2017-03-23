"""Simulate multiple-test correction of P-values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import numpy as np
from pkgsim.pval_sim import PvalSim

class PvalMtCorrSimsMany(object):
    """Simulate multiple-test correction of P-values."""

    def __init__(self, num_pvalues_list, num_sims, perc_sig_list, multi_params):
        self.num_pvalues_list = num_pvalues_list
        self.num_sims = num_sims
        self.perc_sig_list = perc_sig_list
        self.percsig_simsets = self._init_percsig_simset_lst(multi_params)

    def get_attr_percentile_vals(self, attrname="perc_Type_I_II", percentile=84.0):
        """Get values for 'attrname' at 'percentile' value."""
        vals = []
        for _, numpvals_objsims in self.percsig_simsets:
            for _, objsims in numpvals_objsims:
                vals.extend(objsims.get_percentile_vals(attrname, [percentile]))
        return vals

    def _init_percsig_simset_lst(self, multi_params, prt=sys.stdout):
        """Do P-value and multiple test simulations. Return results."""
        percsig_simsets = []
        msg = "  Running {N} Pval Sims with {SIG:3.0f}% significance\n"
        for perc_sig in self.perc_sig_list:
            prt.write(msg.format(N=self.num_sims, SIG=perc_sig))
            numpvals_sims = []
            for num_pvals in self.num_pvalues_list:
                objsims = PvalSimMany(self.num_sims, num_pvals, perc_sig, multi_params)
                # Save sets of simulations, stored according to num_pvals
                numpvals_sims.append((num_pvals, objsims))
            percsig_simsets.append((perc_sig, numpvals_sims))
        return percsig_simsets


class PvalSimMany(object):
    """Simulate MANY (N=num_sims) multiple-test correction of sets of P-values."""

    def __init__(self, num_sims, num_pvals, perc_sig, multi_params):
        self.num_sims = num_sims
        self.num_pvals = num_pvals
        self.perc_sig = perc_sig # perc_sig -> num_sig
        self.multi_params = multi_params
        # Data members
        self.num_sig = int(round(float(self.perc_sig)*self.num_pvals/100.0))
        self.obj1sim_list = self._init_obj1sim_list(num_sims, num_pvals, multi_params)
        self.nterrs = self._init_nterrs()

    def get_percentile_vals(self, attr, percentiles):
        """Return percentile values for 'attr' list."""
        return [np.percentile([getattr(nt, attr) for nt in self.nterrs], p) for p in percentiles]

    def get_num_mksig(self):
        """Return the number of P-values intended to be significant."""
        return self.num_sig

    def get_num_mkrnd(self):
        """The number of randomly generated P-values, if any is significant, it is by chance."""
        return self.num_pvals - self.num_sig

    def _init_nterrs(self):
        """Get # and % Type I/II/Both for each sim."""
        return [obj1sim.get_perc_err() for obj1sim in self.obj1sim_list]

    def _init_obj1sim_list(self, num_sims, num_pvals, multi_params):
        """Simulate MANY multiple-test correction of P-values."""
        obj1sim_list = []
        for _ in range(num_sims):
            obj1sim = PvalSim(num_pvals, self.num_sig, multi_params)
            obj1sim_list.append(obj1sim)
        return obj1sim_list

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
