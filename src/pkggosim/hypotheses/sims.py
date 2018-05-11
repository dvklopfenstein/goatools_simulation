"""Objain one simulated FDR value by running many P-Value sims w/multiple-test correction."""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import numpy as np
from pkggosim.hypotheses.sim import HypothesesSim


class ManyHypothesesSims(object):
    """Run many simulations of a multiple-test correction run on a set of P-values."""

    expected_params = set(['num_sims', 'num_items', 'perc_null',
                           'multi_params', 'num_null',
                           'max_sigpval', 'pval_surge'])

    def __init__(self, params):
        self.params = params
        assert set(params.keys()) == self.expected_params, \
            set(params.keys()).symmetric_difference(self.expected_params)
        # Data members
        hypothsimobjs = self._init_hypothsimobjs() # List of N=num_sims HypothesesSim objects
        self.nts_tfpn = [o.nt_tfpn for o in hypothsimobjs]
        # Print header for each set of simulations
        # self.prt_summary(prt=sys.stdout)
        # print "LLLLLLLLLL", self.params

    def get_mean(self, key):
        """Returns the actual mean value for the set of P-Value simulations run in this class."""
        return np.mean([getattr(nt, key) for nt in self.nts_tfpn])

    def get_stderr(self, key):
        """Returns the actual stderr value for the set of P-Value simulations run in this class."""
        return np.std([getattr(nt, key) for nt in self.nts_tfpn])/np.sqrt(len(self.nts_tfpn))

    def prt_summary(self, prt=sys.stdout):
        """Print summary of all num_sims simulations."""
        msg = [
            "    ManyHypothesesSims:",
            "{SIMS} sims,".format(SIMS=self.params['num_sims']),
            "{HYPOTHS:3} pvals/sim".format(HYPOTHS=self.params['num_items']),
            "SET({P:3.0f}% null)".format(P=self.params['perc_null']),
            "{M:5.2f} max sig;".format(M=self.params['max_sigpval']),
        ]
        if self.params['pval_surge'] is not None:
            k2v = self.params['pval_surge']
            msg.append('pval_surge({M:8.2e} surge sig'.format(M=k2v['max_sigpval']))
            msg.append('{M} Non-nulls'.format(M=k2v['qty']))
        prt.write("{TXT}\n".format(TXT=" ".join(msg)))

    def get_percentile_vals(self, attr, percentiles):
        """Return percentile values for 'attr' list."""
        return [np.percentile([getattr(nt, attr) for nt in self.nts_tfpn], p) for p in percentiles]

    def prt_num_sims_w_errs(self, prt=sys.stdout, desc=""):
        """Return the number of simulations that have errors."""
        msgpat = "{N} sims ({P:3} pvals/sim, {PERCNULL:3.0f}% True Null.) " \
                 "{E:5} had errs ({ERR_CNTS}) {DESC}\n"
        errpat = "{I:5} I, {II:5} II"
        err_cnts = [(nt.num_Type_I, nt.num_Type_II, nt.num_Type_I_II) for nt in self.nts_tfpn]
        t1s, t2s, t12s = zip(*err_cnts)
        num_errsims = sum([n != 0 for n in t12s])
        num_errsimst1 = sum([n != 0 for n in t1s])
        num_errsimst2 = sum([n != 0 for n in t2s])
        prt.write(msgpat.format(
            N=len(self.nts_tfpn), P=self.params['num_items'], PERCNULL=self.params['perc_null'],
            E=num_errsims, ERR_CNTS=errpat.format(I=num_errsimst1, II=num_errsimst2), DESC=desc))

    def get_percentile_strs(self, attr, percentiles):
        """Return percentile strings suitable for printing for 'attr' list."""
        vals = self.get_percentile_vals(attr, percentiles)
        fmt = "{:6.2f}" if attr[:3] == "per" else "{:4}"
        return [fmt.format(v) for v in vals]

    def _init_hypothsimobjs(self):
        """Simulate MANY multiple-test correction of P-values."""
        num_sims = self.params['num_sims']
        num_items = self.params['num_items']
        num_null = self.params['num_null']
        multi = self.params['multi_params']
        max_sigpval = self.params['max_sigpval']
        pval_surge = self.params['pval_surge']
        return [HypothesesSim(num_items, num_null, multi, max_sigpval, pval_surge) for _ in range(num_sims)]


# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
