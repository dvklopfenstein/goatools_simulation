"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
import timeit
import numpy as np
from pkgsim.randseed import RandomSeed32
from pkgsim.pval_experiments import ExperimentSet
from pkgsim.utils import get_hms
from pkgsim.pval_plot_results import get_dataframe, wrpng_boxplot_sigs
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

    def get_desc(self):
        """Return str describing params used in all simulations."""
        # Ex: Alpha(0.05) Method(fdr_bh) 10=Experiments/Set 100=P-Value simulations/Experiment
        prms = self.params['multi_params']
        return " ".join([
            "Alpha({A}) Method({M})".format(A=prms['alpha'], M=prms['method']),
            "{E}=Experiments/Set".format(E=self.params['num_experiments']),
            "{P}=P-Value simulations/Experiment".format(P=self.params['num_pvalsims'])])

    def _init_experiment_sets(self):
        """Run all variations of Experiments."""
        expsets = []
        tic = timeit.default_timer()
        # Alpha(0.05) Method(fdr_bh) 10=Experiments 100=P-Value simulations/Experiment
        sys.stdout.write("{TITLE}\n".format(TITLE=self.get_desc()))
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

    def plt_box_all(self, attrname='fdr_actual', grpname='FDR'):
        """Plot all boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
        fout_pat = "sim_{A}_{P:03}_{M:02}.png"
        title_pat100 = "{P:}% True Null"
        title_patN = "{P:}% True Null. MaxSig={M:4.2f}"
        key2exps = self._get_key2expsets('perc_sig', 'max_sigpval')
        kws = {
            'fout_img': None,
            'title': None,
            'xlabel': '# P-values per set',
            'ylim_a':0, 'ylim_b':0.10}
        for (perc_sig, max_sigpval), expsets in key2exps.items():
            kws['fout_img'] = fout_pat.format(A=attrname, P=perc_sig, M=int(100*max_sigpval))
            perc_true_null = 100-perc_sig
            title_pat = title_pat100 if perc_true_null == 100 else title_patN
            kws['title'] = title_pat.format(P=perc_true_null, M=max_sigpval)
            dfrm = get_dataframe(expsets, attrname, grpname)
            wrpng_boxplot_sigs(dfrm, **kws)

    def prt_experiments_stats(self, prt=sys.stdout, attrs=None):
        """Print stats for user-specified data in experiment sets."""
        if attrs is None:
            attrs = ["fdr_actual", "frr_actual", "num_Type_I", "num_Type_II", "num_correct"]
        hdrexps = "Sig(% max) #pval" # Header for col0, the description of the statistic
        namefmt = "{SIGPERC:3}% {SIGMAX:5.3f} {EXP_ALPHA:5.3f} {PVALQTY:5}"
        for attrname in attrs:
            prt.write("\n{ATTR} statistics:\n".format(ATTR=attrname))
            objstat = StatsDescribe("exps", "{:10.2f}" if attrname[:3] == "num" else "{:6.4f}")
            objstat.prt_hdr(prt, hdrexps)
            for experiment in self.expsets:
                expname = experiment.get_desc(namefmt)
                means = experiment.get_means(attrname)
                objstat.prt_data(expname, means, prt)

    def prt_experiments_means(self, prt=sys.stdout, attrs=None):
        """Print stats for user-specified data in experiment sets."""
        if attrs is None:
            attrs = ["fdr_actual", "frr_actual", "num_Type_I", "num_Type_II", "num_correct"]
        sys.stdout.write("\n{TITLE}\n".format(TITLE=self.get_desc()))
        num_attrs = len(attrs)
        prt.write("sig% maxSig #pvals {ATTRS}\n".format(ATTRS=" ".join(attrs)))
        prt.write("---- ------ ------ {ATTRS}\n".format(ATTRS=" ".join(["-"*10]*num_attrs)))
        namefmt = "{SIGPERC:3}%  {SIGMAX:5.3f}  {PVALQTY:5}"
        for experiment in self.expsets:
            expname = experiment.get_desc(namefmt)
            means = [np.mean(experiment.get_means(a)) for a in attrs]
            mean_strs = ["{:10.4f}".format(m) for m in means]
            prt.write("{HDR} {ATTRS}\n".format(HDR=expname, ATTRS=" ".join(mean_strs)))

    def prt_num_pvalsims_w_errs(self, prt=sys.stdout):
        """Print if errors were seen in sims."""
        for experiment_set in self.expsets:
            experiment_set.prt_num_pvalsims_w_errs(prt)

    def _get_key2expsets(self, key1='perc_sig', key2='max_sigpval'):
        """Separate experiment sets into sub-lists for plotting."""
        # Get experimentset data
        key2exps = cx.defaultdict(list)
        for expset in self.expsets:
            key2exps[(expset.params[key1], expset.params[key2])].append(expset)
        return key2exps

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
