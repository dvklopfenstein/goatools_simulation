"""Holds parameters used to create one set of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
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
        self.params = params

    def run(self):
        """Run all variations of Experiments."""
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
                    objexps = ExperimentSet(exp_parms)
                    objexps.run()

class ExperimentSet(object):
    """Run a set of experiments to obtain frequency of actual (experimentally obtained) ratios."""

    def __init__(self, params):
        self.params = params

    def run(self):
        """Run a set of experiments.""" 
        print "ExperimentSet", self.get_desc_str()
        for _ in range(self.params['num_experiments']):
            objexp = PvalSimMany(
                num_sims = self.params['num_pvalsims'],
                num_pvals = self.params['pval_qty'],
                perc_sig = self.params['perc_sig'],
                multi_params = self.params['multi_params'],
                fnc_maxsig = self.params['fnc_maxsig'])

    def get_desc_str(self):
        """Return string which describes this experiment set."""
        return "{MAXSIG:4.2f}=MaxSigPval {PERCSIG:>3.0f}% sig (N VALS), {NUMPVALS:4}".format(
            MAXSIG=self.params['max_sigpval'],
            PERCSIG=self.params['perc_sig'],
            NUMPVALS=self.params['pval_qty'])

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
