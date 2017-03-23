"""Simulate multiple-test correction of P-values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import timeit
import datetime
import numpy as np
from pkgsim.pval_sim import PvalSim

#pylint: disable=too-many-arguments

class PvalMtCorrSimsMany(object):
    """Simulate multiple-test correction of P-values."""

    def __init__(self, num_pvalues_list, num_sims, perc_sig_list, multi_params, fnc_maxsig):
        self.num_pvalues_list = num_pvalues_list
        self.num_sims = num_sims
        self.perc_sig_list = perc_sig_list
        self.percsig_simsets = self._init_percsig_simset_lst(multi_params, fnc_maxsig)

    def get_attr_percentile_vals(self, attrname="perc_Type_I_II", percentile=84.0):
        """Get values for 'attrname' at 'percentile' value."""
        vals = []
        for _, numpvals_objsims in self.percsig_simsets:
            for _, objsims in numpvals_objsims:
                vals.extend(objsims.get_percentile_vals(attrname, [percentile]))
        return vals

    def prt_num_sims_w_errs(self, prt=sys.stdout):
        """Return the number of simulations that have errors."""
        for _, numpvals_objsims in self.percsig_simsets:
            for _, objsims in numpvals_objsims:
                objsims.prt_num_sims_w_errs(prt)
            prt.write("\n")

    def _init_percsig_simset_lst(self, multi_params, fnc_maxsig, prt=sys.stdout):
        """Do P-value and multiple test simulations. Return results."""
        tic = timeit.default_timer()
        percsig_simsets = []
        msg = "  Running {N} Pval Sims with {SIG:3.0f}% significance {HMS}\n"
        for perc_sig in self.perc_sig_list:
            prt.write(msg.format(N=self.num_sims, SIG=perc_sig, HMS=self.get_hms(tic)))
            numpvals_sims = []
            for num_pvals in self.num_pvalues_list:
                objsims = PvalSimMany(self.num_sims, num_pvals, perc_sig, multi_params, fnc_maxsig)
                # Save sets of simulations, stored according to num_pvals
                numpvals_sims.append((num_pvals, objsims))
            percsig_simsets.append((perc_sig, numpvals_sims))
        prt.write("  ELAPSED TIME: {HMS}\n".format(HMS=self.get_hms(tic)))
        return percsig_simsets

    @staticmethod
    def get_hms(tic):
        """Print elapsed time as simulations run."""
        return str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))


class PvalSimMany(object):
    """Simulate MANY (N=num_sims) multiple-test correction of sets of P-values."""

    def __init__(self, num_sims, num_pvals, perc_sig, multi_params, fnc_maxsig):
        self.num_sims = num_sims
        self.num_pvals = num_pvals
        self.perc_sig = perc_sig # perc_sig -> num_sig
        self.multi_params = multi_params
        # Data members
        self.num_sig = int(round(float(self.perc_sig)*self.num_pvals/100.0))
        self.obj1sim_list = self._init_obj1sim_list(num_sims, num_pvals, multi_params, fnc_maxsig)
        self.nterrs = self._init_nterrs()
        # Print header for each set of simulations
        print
        print "{SIMS} sims, {PVALS} pvals/sim, {PERC:4.2f}%".format(
            SIMS=num_sims, PVALS=num_pvals, PERC=perc_sig)

    def get_percentile_vals(self, attr, percentiles):
        """Return percentile values for 'attr' list."""
        return [np.percentile([getattr(nt, attr) for nt in self.nterrs], p) for p in percentiles]

    def get_num_sims_w_errs(self):
        """Return the number of simulations that have errors."""
        num_sims = len(self.nterrs)
        return sum([1 for nterr in self.nterrs if nterr.num_Type_I_II != 0])
        print "Of {} sims, {} had errors".format(num_sims, num_sims_err)

    def prt_num_sims_w_errs(self, prt=sys.stdout):
        """Return the number of simulations that have errors."""
        prt.write("Of {} sims of {:3} pvals with {:3.0f}% set significance, {} had errors\n".format(
            len(self.nterrs), self.num_pvals, self.perc_sig, self.get_num_sims_w_errs()))

    def get_percentile_strs(self, attr, percentiles):
        """Return percentile strings suitable for printing for 'attr' list."""
        vals = self.get_percentile_vals(attr, percentiles)
        fmt = "{:6.2f}" if attr[:3] == "per" else "{:4}"
        return [fmt.format(v) for v in vals]

    def get_num_mksig(self):
        """Return the number of P-values intended to be significant."""
        return self.num_sig

    def get_num_mkrnd(self):
        """The number of randomly generated P-values, if any is significant, it is by chance."""
        return self.num_pvals - self.num_sig

    def _init_nterrs(self):
        """Get # and % Type I/II/Both for each sim."""
        return [obj1sim.get_perc_err() for obj1sim in self.obj1sim_list]

    def _init_obj1sim_list(self, num_sims, num_pvals, multi_params, fnc_maxsig):
        """Simulate MANY multiple-test correction of P-values."""
        obj1sim_list = []
        for _ in range(num_sims):
            obj1sim = PvalSim(num_pvals, self.num_sig, multi_params, fnc_maxsig)
            obj1sim_list.append(obj1sim)
        return obj1sim_list

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
