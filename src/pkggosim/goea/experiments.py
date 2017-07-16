"""Runs a set of experiments to obtain a set of simulated FDR values."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkggosim.goea.sims import ManyGoeaSims
from pkggosim.common.utils import get_hms


class ExperimentSet(object):
    """Run a set of experiments to obtain experimentally obtained frequencies of ratios."""

    expected_params = set(['perc_null', 'num_items', 'num_experiments', 'num_sims'])

    def __init__(self, params, pobj):
        self.params = params
        self.pobj = pobj # RunParams object
        assert set(params.keys()) == self.expected_params
        self.num_null = int(round(float(params['perc_null'])*params['num_items']/100.0))
        self.expset = self._init_experiments() # returns list of ManyGoeaSims objects

    def get_means(self, key, genes_goids='genes'):
        """Return list of means for a item like fdr_actual, frr_actual."""
        return [e.get_mean(key, genes_goids) for e in self.expset]

    def get_desc(self, fmt="{PERCNULL:>3.0f}% True Null({TOTNULL:3} of {QTY:4} P-Values)"):
        """Return string which succinctly describes this experiment set."""
        return fmt.format(
            PERCNULL=self.params['perc_null'],
            EXP_ALPHA=float(self.params['perc_null'])/100.0*self.pobj.objbase.alpha,
            TOTNULL=self.num_null,
            QTY=self.params['num_items'])

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

    def _init_experiments(self, prt=sys.stdout):
        """Run a set of experiments."""
        expset = []
        prt.write("\n{DESC} HMS={HMS}\n".format(DESC=self.get_strhdr(), HMS=get_hms(self.pobj.tic)))
        shared_param_keys = ['num_sims', 'num_items', 'perc_null']
        for idx in range(self.params['num_experiments']):
            prt.write("{IDX:4} {DESC} HMS={HMS} {STYLE}\n".format(
                IDX=idx, DESC=self.get_strhdr(), HMS=get_hms(self.pobj.tic),
                STYLE=self.pobj.params['randomize_truenull_assc']))
            experiment_params = {k:self.params[k] for k in shared_param_keys}
            experiment_params['num_null'] = self.num_null
            # One ManyGoeaSims is one experiment which can return one simulated FDR value
            expset.append(ManyGoeaSims(experiment_params, self.pobj))
        return expset

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
