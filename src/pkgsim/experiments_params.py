"""Holds parameters used to create one set of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import timeit
import datetime
from pkgsim.randseed import RandomSeed32
from pkgsim.pval_sims import PvalSimMany
from goatools.statsdescribe import StatsDescribe


class ExperimentsAll(object):
    """Run all experiments having various: max_sigvals, perc_sigs, pval_qtys."""

    # Parameters Example:
    #
    #     params = {
    #         'seed'            : 0xdeadbeef,
    #         'multi_params'    : {'alpha' : 0.05, 'method' : 'fdr_bh'},
    #         'max_sigpvals'    : [0.005, 0.01, 0.02, 0.03, 0.04, 0.05],
    #         'perc_sigs'       : [0, 5, 10, 20, 60, 80, 90, 95, 98, 100],
    #         'pval_qtys'       : [20, 100, 500],
    #         'num_experiments' : 100,
    #         'fnc_maxsig'      : None,
    #         'num_pvalsims'    : 100}

    expected_params = set(['seed', 'multi_params', 'perc_sigs', 'max_sigpvals', 'pval_qtys',
                           'num_experiments', 'num_pvalsims', 'fnc_maxsig'])

    def __init__(self, params):
        self.seed = RandomSeed32(params.get('seed', None))
        self.params = params
        assert set(params.keys()) == self.expected_params
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
        for perc_sig in self.params['perc_sigs']:   # Ex: [0, 5, 10, 20, 60, 80, 90, 95, 98, 100]
            for max_sigpval in self.params['max_sigpvals']:  # Ex: [0.01, 0.02, 0.03, 0.04, 0.05]
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
        sys.stdout.write("  ELAPSED TIME: {HMS}\n".format(HMS=self.get_hms(tic)))
        return expsets

    @staticmethod
    def get_hms(tic):
        """Print elapsed time as simulations run."""
        return str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))

    def prt_summary(self, prt=sys.stdout, attrs=None):
        """Print stats for user-specified data in experiment sets."""
        if attrs is None:
            attrs = ["fdr_actual", "frr_actual", "num_Type_I", "num_Type_II", "num_correct"]
        #      "
        name = "Sig(% max) #pval" # Header for col0, the description of the statistic
        for attrname in attrs:
            prt.write("\n{ATTR} statistics:\n".format(ATTR=attrname))
            objstat = StatsDescribe("exps", "{:10.2f}" if attrname[:3] == "num" else "{:6.4f}")
            objstat.prt_hdr(prt, name)
            for exp in self.expsets:
                exp.prt_summary(attrname, objstat, prt)

class ExperimentSet(object):
    """Run a set of experiments to obtain experimentally obtained frequencies of ratios."""

    expected_params = set(['multi_params', 'perc_sig', 'pval_qty', 'num_experiments', 'num_pvalsims',
                           'max_sigpval', 'fnc_maxsig'])

    def __init__(self, params):
        self.params = params
        self.alpha = params['multi_params']['alpha']
        assert set(params.keys()) == self.expected_params
        # max_sigval<-fnc_maxsig(pval_qty, alpha) AND num_sig<-fnc(perc_sig, pval_qty)
        self.max_sigval = params['fnc_maxsig'](num_pvalues=params['pval_qty'], alpha=self.alpha)
        self.num_sig = int(round(float(params['perc_sig'])*params['pval_qty']/100.0))
        self.expset = self._init_expset()

    def get_fdr_actuals(self):
        """Return list of actaul FDR values for simulation."""
        return self.get_means("fdr_actual")

    def get_means(self, key):
        """Return list of means for a item like fdr_actual, frr_actual."""
        return [e.get_mean(key) for e in self.expset]

    def get_desc_str(self):
        """Return string which describes this experiment set."""
        return "{MAXSIG:4.2f}=MaxSigPval {PERCSIG:>3.0f}% sig({S:3} of {P:4} P-Values)".format(
            MAXSIG=self.params['max_sigpval'],
            PERCSIG=self.params['perc_sig'],
            S=self.num_sig,
            P=self.params['pval_qty'])

    def prt_summary(self, attrname, objstat, prt=sys.stdout):
        """Print summary of all num_pvalsims simulations."""
        name = "{PSIG:3}% {MAXSIG:5.3f} {EXPALPHA:5.3f} {NPVALS:5}".format(
            PSIG=self.params['perc_sig'],
            MAXSIG=self.params['max_sigpval'],
            EXPALPHA=float(100-self.params['perc_sig'])/100.0*self.alpha,
            NPVALS=self.params['pval_qty'])
        means = self.get_means(attrname)
        objstat.prt_data(name, means, prt)

    def get_strhdr(self):
        """Return a short 1-line summary of this experiment set."""
        # Example: "ExperimentSet(10) 0.01=MaxSigPval   0% sig (N VALS),   20"
        return "ExperimentSet({N}) {M}=max_sigval {EXP}".format(
            N=self.params['num_experiments'], M=self.max_sigval, EXP=self.get_desc_str())

    def _init_expset(self):
        """Run a set of experiments."""
        expset = []
        sys.stdout.write("{EXPSET_DESC}\n".format(EXPSET_DESC=self.get_strhdr()))
        shared_param_keys = ['num_pvalsims', 'pval_qty', 'perc_sig', 'multi_params']
        for _ in range(self.params['num_experiments']):
            experiment_params = {k:self.params[k] for k in shared_param_keys}
            experiment_params['num_sig'] = self.num_sig
            experiment_params['max_sigval'] = self.max_sigval
            expset.append(PvalSimMany(experiment_params))
        return expset

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
