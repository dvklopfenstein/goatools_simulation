"""Holds parameters used to create one set of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import timeit
import datetime
from pkgsim.randseed import RandomSeed32
from pkgsim.pval_sims import PvalSimMany

class ExperimentsParams(object):
    """Holds parameters used to create one set of experiments."""

    cls2parms = {
        'PvalSim':         # FDR is either 1.0 or 0.0 when all null hypotheses are true
          ['multi_params', 'max_sigpval',  'perc_sig',  'pval_qty',                     'fnc_maxsig', 'num_pvalsims'],

        'PvalSimMany':     # One instance is one experiment; Used to obtain one FDR ratio
          ['multi_params', 'max_sigpval',  'perc_sig',  'pval_qty',                     'fnc_maxsig', 'num_pvalsims'],

        'ExperimentSet':   # Used to calculate a set of FDR ratios
          ['multi_params', 'max_sigpval',  'perc_sig',  'pval_qty',  'num_experiments', 'fnc_maxsig', 'num_pvalsims'],

        'ExperimentsAll':  # Runs all experiements
          ['multi_params', 'max_sigpvals', 'perc_sigs', 'pval_qtys', 'num_experiments', 'fnc_maxsig', 'num_pvalsims'],
    }

    sim_params = {
        'multi_params'    : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals'    : [0.005, 0.01, 0.02, 0.03, 0.04, 0.05],
        'perc_sigs'       : [0, 5, 10, 20, 60, 80, 90, 95, 98, 100],
        'pval_qtys'       : [20, 100, 500],
        'num_experiments' : 100,
        'fnc_maxsig'      : None,
        'num_pvalsims'    : 100}


class ExperimentsAll(object):
    """Run all experiments having various: max_sigvals, perc_sigs, pval_qtys."""

    def __init__(self, params):
        self.seed = RandomSeed32(params.get('seed', None))
        self.params = params
        self.expsets = self._init()

    def _init(self):
        """Run all variations of Experiments."""
        expsets = []
        tic = timeit.default_timer()
        prms = self.params['multi_params']
        # Alpha(0.05) Method(fdr_bh) 10=Experiments 100=P-Value simulations/Experiment
        sys.stdout.write("Alpha({A}) Method({M}) ".format(A=prms['alpha'], M=prms['method']))
        sys.stdout.write("{E}=Experiments/Set {P}=P-Value simulations/Experiment\n".format(
            E=self.params['num_experiments'], P=self.params['num_pvalsims']))
        # Run all experiment sets
        for max_sigpval in self.params['max_sigpvals']:  # Ex: [0.005, 0.01, 0.02, 0.03, 0.04, 0.05]
            for perc_sig in self.params['perc_sigs']:   # Ex: [0, 5, 10, 20, 60, 80, 90, 95, 98, 100]
                for pval_qty in self.params['pval_qtys']:   # Ex: [20, 100, 500]
                    fnc_maxsig = self.params['fnc_maxsig']
                    fnc_maxsig.max_sig_pval = max_sigpval
                    exp_parms = {
                        'multi_params' : self.params['multi_params'],
                        'max_sigpval' : max_sigpval,
                        'perc_sig' : perc_sig,
                        'pval_qty' : pval_qty,
                        'num_experiments' : self.params['num_experiments'],
                        'num_pvalsims' : self.params['num_pvalsims'],
                        'fnc_maxsig' : fnc_maxsig}
                    expsets.append(ExperimentSet(exp_parms))
        return expsets
        sys.stdout.write("  ELAPSED TIME: {HMS}\n".format(HMS=self.get_hms(tic)))

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


class ExperimentSet(object):
    """Run a set of experiments to obtain experimentally obtained frequencies of ratios."""

    strsum = "{MAXSIG:4.2f}=MaxSigPval {PERCSIG:>3.0f}% sig({S:3} of {P:4} P-Values)"

    def __init__(self, params):
        self.params = params
        self.max_sigval = self._init_max_sigval()
        self.num_sig = int(round(float(params['perc_sig'])*params['pval_qty']/100.0))
        self.expset = self._init_expset()

    def get_desc_str(self):
        """Return string which describes this experiment set."""
        return self.strsum.format(
            MAXSIG=self.params['max_sigpval'],
            PERCSIG=self.params['perc_sig'],
            S=self.num_sig,
            P=self.params['pval_qty'])

    def _init_max_sigval(self):
        """Initialize maximum value of randomly determined P-Values intended to be significant."""
        fnc_maxsig = self.params['fnc_maxsig']
        pval_qty = self.params['pval_qty']
        alpha = self.params['multi_params']['alpha']
        return fnc_maxsig(num_pvalues=pval_qty, alpha=alpha)

    def _init_expset(self):
        """Run a set of experiments.""" 
        expset = []
        # ExperimentSet(10) 0.01=MaxSigPval   0% sig (N VALS),   20
        sys.stdout.write("ExperimentSet({N}) {M}=max_sigval {EXP}\n".format(
            N=self.params['num_experiments'], M=self.max_sigval, EXP=self.get_desc_str()))
        pval_qty = self.params['pval_qty']
        for _ in range(self.params['num_experiments']):
            params = {k:self.params[k] for k in ['num_pvalsims', 'pval_qty', 'perc_sig', 'multi_params']}
            params['num_sig'] = self.num_sig
            params['max_sigval'] = self.max_sigval
            expset.append(PvalSimMany(params))
        return expset 

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
