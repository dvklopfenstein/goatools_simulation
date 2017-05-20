"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import timeit
from pkgsim.randseed import RandomSeed32
from pkgsim.experiments import ExperimentSet
from pkgsim.utils import get_hms
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
    #         'num_pvalsims'    : 100}

    expected_params = set(['seed', 'multi_params', 'perc_sigs', 'max_sigpvals', 'pval_qtys',
                           'num_experiments', 'num_pvalsims'])

    def __init__(self, params):
        self.seed = RandomSeed32(params.get('seed', None))
        self.params = params
        assert set(params.keys()) == self.expected_params
        self.expsets = self._init_experiment_sets()

    def _init_experiment_sets(self):
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
                    exp_parms = {
                        'multi_params' : self.params['multi_params'],
                        'max_sigpval' : max_sigpval,
                        'perc_sig' : perc_sig,
                        'pval_qty' : pval_qty,
                        'num_experiments' : self.params['num_experiments'],
                        'num_pvalsims' : self.params['num_pvalsims']}
                    expsets.append(ExperimentSet(exp_parms, tic))
        sys.stdout.write("  ELAPSED TIME: {HMS}\n".format(HMS=get_hms(tic)))
        return expsets

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

    def prt_num_pvalsims_w_errs(self, prt=sys.stdout):
        """Print if errors were seen in sims."""
        for experiment_set in self.expsets:
            experiment_set.prt_num_pvalsims_w_errs(prt)


# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
