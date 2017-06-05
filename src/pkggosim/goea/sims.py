"""Objain one simulated FDR value by running many P-Value sims w/multiple-test correction."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import numpy as np
from pkggosim.goea.sim import GoeaSim


class ManyGoeaSims(object):
    """Run many simulations of a multiple-test correction run on a set of P-values."""

    expected_params = set(['num_sims', 'num_items', 'perc_null', 'num_null'])

    def __init__(self, params, pobj):
        self.params = params
        self.pobj = pobj
        assert set(params.keys()) == self.expected_params
        simobjs = self._init_simobjs() # List of N=num_sims GoeaSim objects
        self.nts_tfpn = [o.nt_tfpn for o in simobjs]

    def get_mean(self, key):
        """Returns the actual mean value for the set of P-Value simulations run in this class."""
        return np.mean([getattr(nt, key) for nt in self.nts_tfpn])

    def get_stderr(self, key):
        """Returns the actual stderr value for the set of P-Value simulations run in this class."""
        return np.std([getattr(nt, key) for nt in self.nts_tfpn])

    def prt_summary(self, prt=sys.stdout):
        """Print summary. Ex: ManyGoeaSims: 10 sims,  16 pvals/sim SET( 50% null)."""
        msg = [
            "    ManyGoeaSims:",
            "{SIMS} sims,".format(SIMS=self.params['num_sims']),
            "{HYPOTHS:3} study_genes/sim".format(HYPOTHS=self.params['num_items']),
            "SET({P:3.0f}% null)\n".format(P=self.params['perc_null']),
        ]
        prt.write(" ".join(msg))

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
            N=len(self.nts_tfpn), P=self.params['num_items'],
            PERCNULL=self.params['perc_null'],
            E=num_errsims, ERR_CNTS=errpat.format(I=num_errsimst1, II=num_errsimst2), DESC=desc))

    def get_percentile_strs(self, attr, percentiles):
        """Return percentile strings suitable for printing for 'attr' list."""
        vals = self.get_percentile_vals(attr, percentiles)
        fmt = "{:6.2f}" if attr[:3] == "per" else "{:4}"
        return [fmt.format(v) for v in vals]

    def _init_simobjs(self):
        """Simulate MANY multiple-test correction of P-values."""
        num_sims = self.params['num_sims']
        num_genes = self.params['num_items']
        num_null = self.params['num_null']
        return [GoeaSim(num_genes, num_null, self.pobj) for _ in range(num_sims)]

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
