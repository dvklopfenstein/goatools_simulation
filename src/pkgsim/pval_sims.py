"""Run many simulations of a multiple-test correction run on a set of P-values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import numpy as np
from pkgsim.pval_sim import PvalSim


class PvalSimMany(object):
    """Run many simulations of a multiple-test correction run on a set of P-values."""

    def __init__(self, num_pvalsims, pval_qty, perc_sig, num_sig, multi_params, max_sigval):
        self.num_pvalsims = num_pvalsims
        self.pval_qty = pval_qty
        self.perc_sig = perc_sig # perc_sig -> num_sig
        self.multi_params = multi_params  # alpha and 'fdr_bh'
        self.max_sigval = max_sigval
        self.num_sig = num_sig
        # Data members
        pvalsimobjs = self._init_pvalsimobjs(num_pvalsims) # List of N=numsum PvalSim objects
        self.nts_tfpn = [o.nt_tfpn for o in pvalsimobjs]
        # Print header for each set of simulations
        #self.prt_summary(prt=sys.stdout)

    def get_fdr_actual(self):
        """Returns get the actual FDR value for the set of P-Value simulations run in this class."""
        return self.get_mean_actual(self, "fdr_actual")

    def get_mean_actual(self, key):
        """Returns get the actual mean value for the set of P-Value simulations run in this class."""
        return np.mean([getattr(nt, key) for nt in self.nts_tfpn])

    def prt_summary(self, prt=sys.stdout):
        """Print summary of all num_pvalsims simulations."""
        msg = [
            "    PvalSimMany:",
            "{SIMS} sims, {PVALS:3} pvals/sim".format(SIMS=self.num_pvalsims, PVALS=self.pval_qty),
            "SET({P:3.0f}% sig, {M:5.2f} max sig)\n".format(P=self.perc_sig, M=self.max_sigval),
        ]
        prt.write(" ".join(msg))

    def get_percentile_vals(self, attr, percentiles):
        """Return percentile values for 'attr' list."""
        return [np.percentile([getattr(nt, attr) for nt in self.nts_tfpn], p) for p in percentiles]

    def prt_num_pvalsims_w_errs(self, prt=sys.stdout):
        """Return the number of simulations that have errors."""
        pat = "{N} sims ({P:3} pvals/sim, {PSIG:3.0f}% set sig.), {E:5} had errors ({I:5} I, {II:5} II)\n"
        err_cnts = [(nt.num_Type_I, nt.num_Type_II, nt.num_Type_I_II) for nt in self.nts_tfpn]
        t1s, t2s, t12s = zip(*err_cnts)
        num_errsims = sum([n != 0 for n in t12s])
        num_errsimst1 = sum([n != 0 for n in t1s])
        num_errsimst2 = sum([n != 0 for n in t2s])
        prt.write(pat.format(
            N=len(self.nts_tfpn), P=self.pval_qty, PSIG=self.perc_sig,
            E=num_errsims, I=num_errsimst1, II=num_errsimst2))

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
        return self.pval_qty - self.num_sig

    def _init_pvalsimobjs(self, num_pvalsims):
        """Simulate MANY multiple-test correction of P-values."""
        pvalsimobjs = []
        for _ in range(num_pvalsims):
            obj1sim = PvalSim(self.pval_qty, self.num_sig, self.multi_params, self.max_sigval)
            pvalsimobjs.append(obj1sim)
        return pvalsimobjs

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
