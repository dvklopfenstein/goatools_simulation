"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
import timeit
import numpy as np
from pkggosim.randseed import RandomSeed32
from pkggosim.hypotheses_experiments import ExperimentSet
from pkggosim.hypotheses_plot_results import plt_box_all, plt_box_tiled
from pkggosim.utils import get_hms
from goatools.statsdescribe import StatsDescribe


class ExperimentsAll(object):
    """Run all experiments having various: max_sigvals, perc_nulls, num_hypoths_list."""

    expected_params = set(['seed', 'multi_params', 'perc_nulls', 'max_sigpvals', 'num_hypoths_list',
                           'num_experiments', 'num_sims'])

    def __init__(self, params):
        self.seed = RandomSeed32(params.get('seed', None))
        self.params = params
        assert set(params.keys()) == self.expected_params
        self.expsets = self._init_experiment_sets()

    def get_fout_img(self, img_pat="sim_{P0:03}to{PN:03}_{MAX0:02}to{MAXN:02}.png"):
        """Get the name of the png file for the tiled plot."""
        return img_pat.format(
            P0=self.params['perc_nulls'][0],   # True Null %
            PN=self.params['perc_nulls'][-1],  # True Null %
            MAX0=int(self.params['max_sigpvals'][0]*100),  # 0.01 ->"01"
            MAXN=int(self.params['max_sigpvals'][-1]*100),
            Q0=self.params['num_hypoths_list'][0],
            QN=self.params['num_hypoths_list'][-1],
            NEXP=self.params['num_experiments'],
            NSIM=self.params['num_sims'])

    def get_desc(self):
        """Return str describing params used in all simulations."""
        # Ex: Alpha(0.05) Method(fdr_bh) 10=Experiments/Set 100=P-Value simulations/Experiment
        prms = self.params['multi_params']
        return " ".join([
            "Alpha({A}) Method({M})".format(A=prms['alpha'], M=prms['method']),
            "{E}=Experiments/Set".format(E=self.params['num_experiments']),
            "{P}=P-Value simulations/Experiment".format(P=self.params['num_sims'])])

    def prt_params(self, prt=sys.stdout):
        """Print user-specified input parameters."""
        for key, val in self.params.items():
            prt.write("{KEY:16} {VAL}\n".format(KEY=key, VAL=val))

    def _init_experiment_sets(self):
        """Run all variations of Experiments."""
        expsets = []
        tic = timeit.default_timer()
        # Alpha(0.05) Method(fdr_bh) 10=Experiments 100=P-Value simulations/Experiment
        sys.stdout.write("{TITLE}\n".format(TITLE=self.get_desc()))
        # Run all experiment sets
        for perc_null in self.params['perc_nulls']:   # Ex: [0, 5, 10, 20, 60, 80, 90, 95, 98, 100]
            for max_sigpval in self.params['max_sigpvals']:  # Ex: [0.01, 0.02, 0.03, 0.04, 0.05]
                for hypoth_qty in self.params['num_hypoths_list']:   # Ex: [20, 100, 500]
                    exp_parms = {
                        'multi_params' : self.params['multi_params'],
                        'max_sigpval' : max_sigpval,
                        'perc_null' : perc_null,
                        'hypoth_qty' : hypoth_qty,
                        'num_experiments' : self.params['num_experiments'],
                        'num_sims' : self.params['num_sims']}
                    expsets.append(ExperimentSet(exp_parms, tic))
        sys.stdout.write("  ELAPSED TIME: {HMS}\n".format(HMS=get_hms(tic)))
        return expsets

    def plt_box_all(self, fimg_pat, attrname='fdr_actual', grpname='FDR'):
        """Plot all boxplots for all experiments. X->(maxsigval, #tests), Y->%sig"""
        key2exps = self._get_key2expsets('perc_null', 'max_sigpval')
        plt_box_all(fimg_pat, key2exps, attrname, grpname)

    def plt_box_tiled(self, fout_img, attrname='fdr_actual', grpname='FDR', **kws):
        """Plot all boxplots for all experiments. X->(maxsigval, #tests), Y->%sig"""
        key2exps = self._get_key2expsets('perc_null', 'max_sigpval')
        plt_box_tiled(fout_img, key2exps, attrname=attrname, grpname=grpname, **kws)

    def prt_experiments_stats(self, prt=sys.stdout, attrs=None):
        """Print stats for user-specified data in experiment sets."""
        if attrs is None:
            attrs = ["fdr_actual", "frr_actual", "num_Type_I", "num_Type_II", "num_correct"]
        hdrexps = "Nul(% max) #pval #tests" # Header for col0, the description of the statistic
        namefmt = "{PERCNULL:3}% {SIGMAX:5.3f} {EXP_ALPHA:5.3f} {PVALQTY:5}"
        for attrname in attrs:
            prt.write("\n{ATTR} statistics:\n".format(ATTR=attrname))
            objstat = StatsDescribe("exps", "{:10.2f}" if attrname[:3] == "num" else "{:6.4f}")
            objstat.prt_hdr(prt, hdrexps)
            for experiment_set in self.expsets:
                expname = experiment_set.get_desc(namefmt)
                means = experiment_set.get_means(attrname)
                objstat.prt_data(expname, means, prt)

    def prt_experiments_means(self, prt=sys.stdout, attrs=None):
        """Print means and stderrs for user-specified data in experiment sets."""
        if attrs is None:
            attrs = ["fdr_actual", "frr_actual", "num_Type_I", "num_Type_II", "num_correct"]
        sys.stdout.write("\n{TITLE}\n".format(TITLE=self.get_desc()))
        num_attrs = len(attrs)
        attrstrs = ["{:>19}".format(a) for a in attrs]
        prt.write("\nSummary of mean values and standard errors:\n\n")
        prt.write("nul% maxSig #tests {ATTRS}\n".format(ATTRS=" ".join(attrstrs)))
        prt.write("---- ------ ------ {ATTRS}\n".format(ATTRS=" ".join(["-"*19]*num_attrs)))
        namefmt = "{PERCNULL:3}%  {SIGMAX:5.3f}  {PVALQTY:5}"
        for experiment_set in self.expsets:
            # expname = experiment_set.get_desc(namefmt)
            means = [np.mean(experiment_set.get_means(a)) for a in attrs]
            # mean_strs = ["{:10.4f}".format(m) for m in means]
            stderrs = [np.std(experiment_set.get_stderrs(a)) for a in attrs]
            # stderr_strs = ["{:10.4f}".format(m) for m in stderrs]
            prt.write("{EXP_DESC} ".format(EXP_DESC=experiment_set.get_desc(namefmt)))
            for mean, stderr in zip(means, stderrs):
                prt.write("{AVG:10.4f} +/-{SE:5.3f} ".format(AVG=mean, SE=stderr))
            prt.write("\n")
            # prt.write("{HDR} {ATTRS}\n".format(HDR=expname, ATTRS=" ".join(mean_strs)))
        prt.write("\n")

    def prt_num_sims_w_errs(self, prt=sys.stdout):
        """Print if errors were seen in sims."""
        for experiment_set in self.expsets:
            experiment_set.prt_num_sims_w_errs(prt)

    def _get_key2expsets(self, key1='perc_null', key2='max_sigpval'):
        """Separate experiment sets into sub-lists for plotting."""
        # Get experimentset data
        key2exps = cx.defaultdict(list)
        for expset in self.expsets:
            key2exps[(expset.params[key1], expset.params[key2])].append(expset)
        return key2exps

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
