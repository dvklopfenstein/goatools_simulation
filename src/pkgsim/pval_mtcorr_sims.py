"""Simulate multiple-test correction of P-values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import timeit
import datetime
import collections as cx
import numpy as np
from pkgsim.pval_sim import PvalSim
from goatools.statsdescribe import StatsDescribe

#pylint: disable=too-many-arguments

class PvalMtCorrSimsMany(object):
    """Simulate multiple-test correction of P-values."""

    def __init__(self, pval_qtys, num_sims, perc_sigs, multi_params, fnc_maxsig):
        self.pval_qtys = pval_qtys
        self.num_sims = num_sims
        self.perc_sigs = perc_sigs
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
        msg = "  PvalMtCorrSimsMany: Running {N} Pval Sims with {SIG:3.0f}% significance {HMS}\n"
        for perc_sig in self.perc_sigs:
            prt.write(msg.format(N=self.num_sims, SIG=perc_sig, HMS=self.get_hms(tic)))
            numpvals_sims = []
            for num_pvals in self.pval_qtys:
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
        self.max_sigval = fnc_maxsig(num_pvalues=num_pvals, alpha=multi_params['alpha'])
        self.num_sig = int(round(float(self.perc_sig)*self.num_pvals/100.0))
        self.pvalsimobjs = self._init_pvalsimobjs(num_sims)
        self.nterrs = self._init_nterrs()
        # Print header for each set of simulations
        self.prt_summary(prt=sys.stdout)

    def prt_summary(self, prt=sys.stdout):
        """Print summary of all num_sims simulations."""
        msg = "\n    PvalSimMany: {SIMS} sims, {PVALS:3} pvals/sim, {PERC:4.0f}% sig, {MAXS:5.2f} max sig\n"
        prt.write(msg.format(SIMS=self.num_sims, PVALS=self.num_pvals, PERC=self.perc_sig,
            MAXS=self.max_sigval))
        self.prt_err_stats(prt)

    def get_errtype2simvals(self):
        """Get counts for each P-value simuation: Type I Error, Type II Error, and Correct."""
        ctrs = [o.get_err_cnts() for o in self.pvalsimobjs]
        return cx.OrderedDict((errtyp, [ctr[errtyp] for ctr in ctrs]) for errtyp in [0, 1, 2])

    def prt_err_stats(self, prt):
        """Print stats for error types in set of simulation runs."""
        errtype2simvals = self.get_errtype2simvals()
        #for errtype, simvals in errtype2simvals.items():
        #    print len(simvals), errtype, simvals
        objstat = StatsDescribe("sims", "{:9.2f}")
        objstat.prt_hdr(prt)
        for errtype, simvals in errtype2simvals.items():
            objstat.prt_data(errtype, simvals, prt)

    def get_percentile_vals(self, attr, percentiles):
        """Return percentile values for 'attr' list."""
        return [np.percentile([getattr(nt, attr) for nt in self.nterrs], p) for p in percentiles]

    def get_num_sims_w_errs(self):
        """Return the number of simulations that have errors."""
        return sum([1 for nterr in self.nterrs if nterr.num_Type_I_II != 0])
        # num_sims = len(self.nterrs)
        # print "Of {} sims, {} had errors".format(num_sims, num_sims_err)

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
        return [obj1sim.get_perc_err() for obj1sim in self.pvalsimobjs]

    def _init_pvalsimobjs(self, num_sims):
        """Simulate MANY multiple-test correction of P-values."""
        pvalsimobjs = []
        for _ in range(num_sims):
            obj1sim = PvalSim(self.num_pvals, self.num_sig, self.multi_params, self.max_sigval)
            pvalsimobjs.append(obj1sim)
        return pvalsimobjs

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
