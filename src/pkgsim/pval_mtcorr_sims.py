"""Simulate multiple-test correction of P-values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import timeit
import datetime
import numpy as np
from pkgsim.pval_sim import PvalSim
from goatools.statsdescribe import StatsDescribe

#pylint: disable=too-many-arguments

class PvalMtCorrSimsMany(object):
    """Simulate multiple-test correction of P-values."""

    def __init__(self, perc_sigs, pval_qtys, num_sims, multi_params, fnc_maxsig):
        self.perc_sigs = perc_sigs # Ex: [0, 15, 20, 40, 80]
        self.pval_qtys = pval_qtys # Ex: [20, 100, 500]
        self.num_sims = num_sims   # Ex: 100
        # [(persig, (numpvals, objsims)), (persig, (numpvals, objsims)), ...
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
        msg = "  PvalMtCorrSimsMany: Running {N}-Pval SimSets with {SIG:3.0f}% significance {HMS}\n"
        for perc_sig in self.perc_sigs: # Ex: [0, 15, 20, 40, 80]
            prt.write(msg.format(N=self.num_sims, SIG=perc_sig, HMS=self.get_hms(tic)))
            numpvals_sims = []
            for num_pvals in self.pval_qtys: # Ex: [20, 100, 500]
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

    def prt_summary(self, prt=sys.stdout):
        """Print summary of all num_sims simulations."""
        attrs = ["fdr_actual", "frr_actual"]
        pat0 = "Set ({PSIG:2}% sig, {NPVALS:5} pvals/sim):\n"
        pat0 = "{PSIG:2}% {NPVALS:5}"
        objstat = StatsDescribe("sims", "{:6.4f}")
        for attrname in attrs:
            prt.write("\n{ATTR}:".format(ATTR=attrname))
            objstat.prt_hdr(prt)
            for percsig, numpvals_objsims in self.percsig_simsets:
                for numpvals, objsims in numpvals_objsims:
                    name = pat0.format(PSIG=percsig, NPVALS=numpvals)
                    vals = [getattr(nt, attrname) for nt in objsims.nts_tfpn]
                    objstat.prt_data(name, vals, prt)




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
        self.pvalsimobjs = self._init_pvalsimobjs(num_sims) # List of N=numsum PvalSim objects
        self.nts_tfpn = [o.nt_tfpn for o in self.pvalsimobjs]
        # Print header for each set of simulations
        #self.prt_summary(prt=sys.stdout)

    def prt_summary(self, prt=sys.stdout):
        """Print summary of all num_sims simulations."""
        msg = [
            "    PvalSimMany:",
            "{SIMS} sims, {PVALS:3} pvals/sim".format(SIMS=self.num_sims, PVALS=self.num_pvals),
            "SET({P:3.0f}% sig, {M:5.2f} max sig)\n".format(P=self.perc_sig, M=self.max_sigval),
        ]
        prt.write(" ".join(msg))

    def get_percentile_vals(self, attr, percentiles):
        """Return percentile values for 'attr' list."""
        return [np.percentile([getattr(nt, attr) for nt in self.nts_tfpn], p) for p in percentiles]

    def prt_num_sims_w_errs(self, prt=sys.stdout):
        """Return the number of simulations that have errors."""
        num_errsims = sum([1 for nterr in self.nts_tfpn if nterr.num_Type_I_II != 0])
        num_t1errsims = sum([1 for nt in self.nts_tfpn if nt.num_Type_I != 0])
        num_t2errsims = sum([1 for nt in self.nts_tfpn if nt.num_Type_II != 0])
        prt.write("Of {} sims ({:3} pvals, {:3.0f}% set significance), {} had errors ({} I, {} II)\n".format(
            len(self.pvalsimobjs), self.num_pvals, self.perc_sig, num_errsims, num_t1errsims, num_t2errsims))

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

    def _init_pvalsimobjs(self, num_sims):
        """Simulate MANY multiple-test correction of P-values."""
        pvalsimobjs = []
        for _ in range(num_sims):
            obj1sim = PvalSim(self.num_pvals, self.num_sig, self.multi_params, self.max_sigval)
            pvalsimobjs.append(obj1sim)
        return pvalsimobjs

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
