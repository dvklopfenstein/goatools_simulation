"""Runs a set of experiments to obtain a set of simulated FDR values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkggosim.goea_sims import ManyGoeaSims
from pkggosim.utils import get_hms


class ExperimentSet(object):
    """Run a set of experiments to obtain experimentally obtained frequencies of ratios."""

    expected_params = set(['perc_null', 'num_study_genes', 'num_experiments', 'num_sims'])

    def __init__(self, params, tic, study_genes_bg, objbg):
        self.params = params
        self.study_genes_bg = study_genes_bg
        self.objbg = objbg
        self.alpha = self.objbg.objbg.alpha
        assert set(params.keys()) == self.expected_params
        self.num_null = int(round(float(params['perc_null'])*params['num_study_genes']/100.0))
        self.expset = self._init_experiments(tic) # returns list of ManyGoeaSims objects

    def get_fdr_actuals(self):
        """Return list of actaul FDR values for simulation."""
        return self.get_means("fdr_actual")

    def get_means(self, key):
        """Return list of means for a item like fdr_actual, frr_actual."""
        return [e.get_mean(key) for e in self.expset]

    def get_desc(self, fmt="{PERCNULL:>3.0f}% True Null({TOTNULL:3} of {GOEAQTY:4} P-Values)"):
        """Return string which succinctly describes this experiment set."""
        return fmt.format(
            PERCNULL=self.params['perc_null'],
            EXP_ALPHA=float(self.params['perc_null'])/100.0*self.alpha,
            TOTNULL=self.num_null,
            GOEAQTY=self.params['num_study_genes'])

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
        sys.stdout.write("{DESC} HMS={HMS}\n".format(DESC=self.get_strhdr(), HMS=get_hms(tic)))
        shared_param_keys = ['num_sims', 'num_study_genes', 'perc_null']
        for _ in range(self.params['num_experiments']):
            experiment_params = {k:self.params[k] for k in shared_param_keys}
            experiment_params['num_null'] = self.num_null
            # One ManyGoeaSims is one experiment which can return one simulated FDR value
            expset.append(ManyGoeaSims(experiment_params, self.study_genes_bg, self.objbg))
        return expset

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
