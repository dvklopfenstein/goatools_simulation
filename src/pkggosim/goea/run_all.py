"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
import numpy as np
from pkggosim.goea.experiments import ExperimentSet
from pkggosim.hypotheses.plot_results import plt_box_all, plt_box_tiled
from pkggosim.common.utils import get_hms
from goatools.statsdescribe import StatsDescribe


class ExperimentsAll(object):
    """Run all experiments having various: max_sigvals, perc_nulls, num_genes_list."""

    def __init__(self, pobj):
        self.pobj = pobj
        self.tic = pobj.tic
        self.expsets = []

    def prt_seed(self, prt):
        """Print random seed."""
        self.pobj.objrnd.prt(prt)

    def get_fout_img(self, img_pat="sim_{P0:03}to{PN:03}.png"):
        """Get the name of the png file for the tiled plot."""
        params = self.pobj.params
        return img_pat.format(
            P0=params['perc_nulls'][0],   # True Null %
            PN=params['perc_nulls'][-1],  # True Null %
            Q0=params['num_genes_list'][0],
            QN=params['num_genes_list'][-1],
            NEXP=params['num_experiments'],
            NSIM=params['num_sims'])

    def get_desc(self):
        """Return str describing params used in all simulations."""
        # Ex: Alpha(0.05) Method(fdr_bh) 10=Experiments/Set 100=P-Value simulations/Experiment
        params = self.pobj.params
        return " ".join([
            "Alpha({A}) Method({M})".format(A=params['alpha'], M=params['method']),
            "{E}=Experiments/Set".format(E=params['num_experiments']),
            "{P}=P-Value simulations/Experiment".format(P=params['num_sims'])])

    def prt_summary(self, prt):
        """Print user-specified input parameters."""
        self.pobj.prt_summary(prt)
        # for key, val in self.pobj.params.items():
        #     prt.write("{KEY:16} {VAL}\n".format(KEY=key, VAL=val))

    def run(self, prt):
        """Run all variations of Experiments."""
        expsets = []
        # Alpha(0.05) Method(fdr_bh) 10=Experiments 100=P-Value simulations/Experiment
        sys.stdout.write("{TITLE}\n".format(TITLE=self.get_desc()))
        # Run all experiment sets
        prms = self.pobj.params
        for perc_null in prms['perc_nulls']:   # Ex: [0, 5, 10, 20, 60, 80, 90, 95, 98, 100]
            for num_study_genes in prms['num_genes_list']:   # Ex: [20, 100, 500]
                exp_parms = { # Experiment Set Parameters
                    'perc_null' : perc_null,
                    'num_study_genes' : num_study_genes,
                    'num_experiments' : prms['num_experiments'],
                    'num_sims' : prms['num_sims']}
                eset = ExperimentSet(exp_parms, self.pobj)
                expsets.append(eset)
        self.prt_hms(prt, "Simulations Completed")
        return expsets

    def prt_hms(self, prt, msg):
        """Print the elapsed time."""
        prt.write("  ELAPSED TIME: {HMS} {MSG}\n".format(HMS=get_hms(self.tic), MSG=msg))

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
