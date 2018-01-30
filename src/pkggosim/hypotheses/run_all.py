"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import re
import sys
import collections as cx
import timeit
import numpy as np
from pkggosim.common.randseed import RandomSeed32
from pkggosim.hypotheses.experiments import ExperimentSet
#### from pkggosim.hypotheses.plot_results import plt_box_all
from pkggosim.hypotheses.plot_results import plt_box_tiled
from pkggosim.common.utils import get_hms
from goatools.statsdescribe import StatsDescribe


class ExperimentsAll(object):
    """Run all experiments having various: max_sigvals, perc_nulls, num_hypoths_list."""

    desc_pat = '{P0:03}to{PN:03}_{MAX0}to{MAXN}_{Q0:03}to{QN:03}_N{NEXP:05}_{NSIM:05}_{M}'

    expected_params = set(['seed', 'multi_params', 'perc_nulls', 'num_hypoths_list',
                           'max_sigpvals', 'max_sigpvals_super', 'perc_super',
                           'num_experiments', 'num_sims', 'repo'])

    method2name = {
        'bonferroni':     "Bonferroni one-step correction",
        'sidak':          "Sidak one-step correction",
        'holm-sidak':     "Holm-Sidak step-down method using Sidak adjustments",
        'holm':           "Holm step-down method using Bonferroni adjustments",
        'simes-hochberg': "Simes-Hochberg step-up method (independent)",
        'hommel':         "Hommel closed method based on Simes tests (non-negative)",
        'fdr_bh':         "FDR Benjamini/Hochberg (non-negative)",
        'fdr_by':         "FDR Benjamini/Yekutieli (negative)",
        'fdr_tsbh':       "FDR 2-stage Benjamini-Hochberg (non-negative)",
        'fdr_tsbky':      "FDR 2-stage Benjamini-Krieger-Yekutieli (non-negative)",
        'fdr_gbs':        "FDR adaptive Gavrilov-Benjamini-Sarkar",
    }

    def __init__(self, params):
        self.tic = timeit.default_timer()
        self.seed = RandomSeed32(params.get('seed', None))
        self.params = self._init_params(params)
        self.method = self.params['multi_params']['method']
        # assert set(self.params.keys()) == self.expected_params, \
        #     set(params.keys()).symmetric_difference(self.expected_params)
        self.expsets = []
        # print "IIIIIIIIIIIIIIII ExperimentsAll", self.params

    @staticmethod
    def _init_params(params):
        """Initialize params."""
        if 'repo' not in params:
            params['repo'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..")
        return params

    def run_all(self, rpt_items, plts, dotsize=None):
        """Run Hypotheses Simulation using Benjamini/Hochberg FDR."""
        self._run_experiments()
        desc_str = self._get_fout_img()
        dir_loc = 'doc/logs' if self.params['num_experiments'] > 20 else 'doc/work'
        fout_log = os.path.join(dir_loc, 'fig_hypoth_{DESC}.log'.format(DESC=desc_str))
        # Report and plot simulation results
        with open(os.path.join(self.params['repo'], fout_log), 'w') as prt:
            self.prt_hms(prt, "Simulations Completed\n")
            self.prt_params(prt)
            self.prt_num_sims(prt)
            self.seed.prt(prt)
            self.prt_experiments_means(prt, rpt_items)
            self.prt_experiments_stats(prt, rpt_items)
            self.prt_hms(prt, "Simulations Completed\n")
            #title = "{M} Hypotheses Simulations".format(M=self.method2name[self.method])
            title = "{M}".format(M=self.method2name[self.method])
            for attrname in plts:  # ['fdr_actual', 'sensitivity', 'specificity']:
                base_img = 'fig_hypoth_{DESC}_{ATTR}.png'.format(ATTR=attrname, DESC=desc_str)
                fout_img = os.path.join(self.params['repo'], dir_loc, base_img)
                self.plt_box_tiled(fout_img, attrname, dotsize=dotsize, title=title)
            self.prt_num_sims(sys.stdout)
            self.prt_hms(prt, "Reports and Plots Completed")
            sys.stdout.write("  WROTE: {LOG}\n".format(LOG=fout_log))

    def prt_num_sims(self, prt):
        """Returns the number of simulations run."""
        lens = [len(self.params[k]) for k in ['perc_nulls', 'max_sigpvals', 'num_hypoths_list']]
        tot_sets = np.prod(lens)
        tot_fdrs = self.params['num_experiments']*tot_sets
        prt.write("{N:12,} Total sets\n".format(N=tot_sets))
        prt.write("{F:12,} Total FDRs; {f:7,} FDRs/set\n".format(
            F=tot_fdrs, f=self.params['num_experiments']))
        prt.write("{F:12,} Total sims; {f:7,} sims/FDR\n".format(
            F=self.params['num_sims']*tot_fdrs, f=self.params['num_sims']))
        prt.write("\n")

    def _get_fout_img(self, img_pat=None):
        """Get the name of the png file for the tiled plot."""
        if img_pat is None:
            img_pat = self.desc_pat
        # print "PPPPPPPPPPP", self.params
        return img_pat.format(
            P0=self.params['perc_nulls'][0],   # True Null %
            PN=self.params['perc_nulls'][-1],  # True Null %
            MAX0=get_floatstr(self.params['max_sigpvals'][0]),  # 0.01 ->"01"
            MAXN=get_floatstr(self.params['max_sigpvals'][-1]),
            Q0=self.params['num_hypoths_list'][0],
            QN=self.params['num_hypoths_list'][-1],
            NEXP=self.params['num_experiments'],
            NSIM=self.params['num_sims'],
            M=self.method)

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
        prt.write("\n")

    def _run_experiments(self):
        """Run all variations of Experiments."""
        # Alpha(0.05) Method(fdr_bh) 10=Experiments 100=P-Value simulations/Experiment
        assert not self.expsets
        sys.stdout.write("{TITLE}\n".format(TITLE=self.get_desc()))
        # Run all experiment sets
        # print "iiiiiiiiiiiiiiii ExperimentsAll::_run_experiments", self.params
        for perc_null in self.params['perc_nulls']:   # Ex: [0, 5, 10, 20, 60, 80, 90, 95, 98, 100]
            for idx1, max_sigpval in enumerate(self.params['max_sigpvals']):  # Ex: [0.01, 0.03, 0.05]
                for num_items in self.params['num_hypoths_list']:   # Ex: [20, 100, 500]
                    max_sup = self.params['max_sigpvals_super'][idx1] if 'max_sigpvals_super' in self.params else None
                    # print "iiiiiiiiiiiiiiii ExperimentsAll::_run_experiments max_sup", max_sup
                    # print "iiiiiiiiiiiiiiii ExperimentsAll::_run_experiments perc_super", self.params.get('perc_super', None)
                    exp_parms = {
                        'multi_params' : self.params['multi_params'],
                        'max_sigpval' : max_sigpval,
                        'max_sigpval_super' : max_sup,
                        'perc_super' : self.params.get('perc_super', None),
                        'perc_null' : perc_null,
                        'num_items' : num_items,
                        'num_experiments' : self.params['num_experiments'],
                        'num_sims' : self.params['num_sims']}
                    self.expsets.append(ExperimentSet(exp_parms, self.tic))
        self.prt_hms(sys.stdout, "Simulations Completed")

    def prt_hms(self, prt, msg):
        """Print the elapsed time."""
        prt.write("  ELAPSED TIME: {HMS} {MSG}\n".format(HMS=get_hms(self.tic), MSG=msg))

####    def plt_box_all(self, fimg_pat, attrname='fdr_actual', grpname='FDR'):
####        """Plot all boxplots for all experiments. X->(maxsigval, #tests), Y->%sig"""
####        key2exps = self._get_key2expsets('perc_null', 'max_sigpval')
####        plt_box_all(fimg_pat, key2exps, attrname, grpname)

    def plt_box_tiled(self, fout_img, attrname, **kws):
        """Plot all boxplots for all experiments. X->(maxsigval, #tests), Y->%sig"""
        key2exps = self._get_key2expsets('perc_null', 'max_sigpval')
        plt_box_tiled(fout_img, key2exps, attrname, **kws)

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
            se_denom = np.sqrt(len(means))
            # mean_strs = ["{:10.4f}".format(m) for m in means]
            stderrs = [np.std(m)/se_denom for m in means]
            # stderr_strs = ["{:10.4f}".format(m) for m in stderrs]
            prt.write("{EXP_DESC} ".format(EXP_DESC=experiment_set.get_desc(namefmt)))
            for mean, stderr in zip(means, stderrs):
                prt.write("{AVG:6.4f} +/-{SE:8.6f} ".format(AVG=mean, SE=stderr))
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

def get_floatstr(val):
    """Convert floating point to a string: 0.0001 -> '0001'."""
    valstr = "{V:f}".format(V=val)
    mtch = re.search(r'0\.(0+[1-9]+)0*$', valstr)
    if mtch:
        return mtch.group(1)
    raise RuntimeError("COULD NOT CONVERT float({F:f}) TO str".format(F=val))

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
