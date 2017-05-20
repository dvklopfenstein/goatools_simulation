"""Holds parameters used to create one set of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkgsim.pval_sims import PvalSimMany


class ExperimentSet(object):
    """Run a set of experiments to obtain experimentally obtained frequencies of ratios."""

    expected_params = set(['multi_params', 'perc_sig', 'pval_qty', 'num_experiments',
                           'num_pvalsims', 'max_sigpval', 'fnc_maxsig'])

    def __init__(self, params):
        self.params = params
        self.alpha = params['multi_params']['alpha']
        assert set(params.keys()) == self.expected_params
        # max_sigval<-fnc_maxsig(pval_qty, alpha) AND num_sig<-fnc(perc_sig, pval_qty)
        self.max_sigval = params['fnc_maxsig'](num_pvalues=params['pval_qty'], alpha=self.alpha)
        self.num_sig = int(round(float(params['perc_sig'])*params['pval_qty']/100.0))
        self.expset = self._init_experiments()

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

    def _init_experiments(self):
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
