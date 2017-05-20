"""Simulate multiple-test correction of P-values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import timeit
import datetime
from pkgsim.pval_sims import PvalSimMany
from goatools.statsdescribe import StatsDescribe

class PvalExperiment(object):
    """Simulate multiple-test correction of P-values."""

    exp_params = set([
        'num_experiments',
        # Each experiment runs N pvalsims
        'num_pvalsims',
        # Multiple-test correction parameters: 1) method, like BH_FDR 2) alpha
        'multi_params',
        'perc_sigs',
        'pval_qtys',
        'fnc_maxsig'])

    def __init__(self, **sim_params):
        self.perc_sigs = sim_params['perc_sigs'] # Ex: [0, 15, 20, 40, 80]
        self.pval_qtys = sim_params['pval_qtys'] # Ex: [20, 100, 500]
        self.num_pvalsims = sim_params['num_pvalsims']   # Ex: 100
        self.multi_params = sim_params['multi_params']
        # [(persig, (numpvals, objsims)), (persig, (numpvals, objsims)), ...
        self.percsig_simsets = self._init_percsig_simset_lst(self.multi_params, sim_params['fnc_maxsig'])

    #### def get_attr_percentile_vals(self, attrname="perc_Type_I_II", percentile=84.0):
    ####     """Get values for 'attrname' at 'percentile' value."""
    ####     vals = []
    ####     for _, numpvals_objsims in self.percsig_simsets:
    ####         for _, objsims in numpvals_objsims:
    ####             vals.extend(objsims.get_percentile_vals(attrname, [percentile]))
    ####     return vals

    def prt_num_sims_w_errs(self, prt=sys.stdout):
        """Return the number of simulations that have errors."""
        for _, numpvals_objsims in self.percsig_simsets:
            for _, objsims in numpvals_objsims:
                objsims.prt_num_sims_w_errs(prt)

    @staticmethod
    def get_hms(tic):
        """Print elapsed time as simulations run."""
        return str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))

    def prt_summary(self, prt=sys.stdout, attrs=None):
        """Print summary of all num_pvalsims simulations."""
        if attrs is None:
            attrs = ["fdr_actual", "frr_actual", "num_Type_I", "num_Type_II", "num_correct"]
        pat0 = "{PSIG:2}% {NPVALS:5}"
        for attrname in attrs:
            objstat = StatsDescribe("sims", "{:9.2f}" if attrname[:3] == "num" else "{:6.4f}")
            prt.write("\n{ATTR}:".format(ATTR=attrname))
            objstat.prt_hdr(prt)
            for percsig, numpvals_objsims in self.percsig_simsets:
                for numpvals, objsims in numpvals_objsims:
                    name = pat0.format(PSIG=percsig, NPVALS=numpvals)
                    vals = [getattr(nt, attrname) for nt in objsims.nts_tfpn]
                    objstat.prt_data(name, vals, prt)

    def _init_percsig_simset_lst(self, multi_params, fnc_maxsig, prt=sys.stdout):
        """Do P-value and multiple test simulations. Return results."""
        tic = timeit.default_timer()
        percsig_simsets = []
        # msg = "  PvalExperiment: Running {N}-Pval SimSets with {SIG:3.0f}% significance {HMS}\n"
        for perc_sig in self.perc_sigs: # Ex: [0, 15, 20, 40, 80]
            # prt.write(msg.format(N=self.num_pvalsims, SIG=perc_sig, HMS=self.get_hms(tic)))
            numpvals_sims = []
            for num_pvals in self.pval_qtys: # Ex: [20, 100, 500]
                objsims = PvalSimMany(self.num_pvalsims, num_pvals, perc_sig, multi_params, fnc_maxsig)
                # Save sets of simulations, stored according to num_pvals
                numpvals_sims.append((num_pvals, objsims))
            percsig_simsets.append((perc_sig, numpvals_sims))
        prt.write("  ELAPSED TIME: {HMS}\n".format(HMS=self.get_hms(tic)))
        return percsig_simsets

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
