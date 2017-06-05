"""Runs a set of experiments to obtain a set of simulated FDR values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkggosim.hypotheses.sims import ManyHypothesesSims
from pkggosim.common.utils import get_hms


class ExperimentSet(object):
    """Run a set of experiments to obtain experimentally obtained frequencies of ratios."""

    expected_params = set(['multi_params', 'perc_null', 'num_items', 'num_experiments',
                           'num_sims', 'max_sigpval'])

    def __init__(self, params, tic):
        self.params = params
        self.alpha = params['multi_params']['alpha']
        assert set(params.keys()) == self.expected_params
        self.max_sigpval = params['max_sigpval']
        self.num_null = int(round(float(params['perc_null'])*params['num_items']/100.0))
        self.expset = self._init_experiments(tic) # returns list of ManyHypothesesSims objects

    def get_means(self, key):
        """Return list of means for a item like fdr_actual, frr_actual."""
        return [e.get_mean(key) for e in self.expset]

    def get_stderrs(self, key):
        """Return list of stderrs for a item like fdr_actual, frr_actual."""
        return [e.get_stderr(key) for e in self.expset]

    def get_desc(self, fmt="{SIGMAX:4.2f}=MaxSigPval "
                           "{PERCNULL:>3.0f}% True Null({TOTNULL:3} of {PVALQTY:4} P-Values)"):
        """Return string which succinctly describes this experiment set."""
        return fmt.format(
            SIGMAX=self.params['max_sigpval'],
            PERCNULL=self.params['perc_null'],
            EXP_ALPHA=float(self.params['perc_null'])/100.0*self.alpha,
            TOTNULL=self.num_null,
            PVALQTY=self.params['num_items'])

    def get_strhdr(self):
        """Return a short 1-line summary of this experiment set."""
        # Example: "ExperimentSet(10) 0.01=MaxSigPval   0% sig (N VALS),   20"
        return "ExperimentSet({N}) {EXP}".format(
            N=self.params['num_experiments'], EXP=self.get_desc())

    def prt_num_sims_w_errs(self, prt=sys.stdout):
        """Print if errors were seen in sims."""
        desc = self.get_desc()
        prt.write("\n") # Separate sets of experiments
        for experiment in self.expset:
            experiment.prt_num_sims_w_errs(prt, desc)

    def _init_experiments(self, tic):
        """Run a set of experiments."""
        expset = []
        sys.stdout.write("{EXPSET_DESC} HMS={HMS}\n".format(
            EXPSET_DESC=self.get_strhdr(), HMS=get_hms(tic)))
        shared_param_keys = ['num_sims', 'num_items', 'perc_null', 'multi_params']
        for _ in range(self.params['num_experiments']):
            experiment_params = {k:self.params[k] for k in shared_param_keys}
            experiment_params['num_null'] = self.num_null
            experiment_params['max_sigpval'] = self.max_sigpval
            # One ManyHypothesesSims is one experiment which can return one simulated FDR value
            expset.append(ManyHypothesesSims(experiment_params))
        return expset

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
