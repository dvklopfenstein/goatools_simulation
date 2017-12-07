"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import collections as cx
import numpy as np
from pkggosim.goea.basename import Basename
from pkggosim.goea.experiments import ExperimentSet
from pkggosim.goea.plot_results import plt_box_tiled
from pkggosim.goea.sim import GoeaSim
from pkggosim.common.utils import get_hms
from goatools.statsdescribe import StatsDescribe



class ExperimentsAll(object):
    """Run all experiments having various: max_sigvals, perc_nulls, num_genes_list."""

    def __init__(self, pobj):
        self.pobj = pobj    # RunParams object
        self.bname = Basename()
        self.tic = pobj.tic
        self.expsets = []   # ExperimentSet contains (expset: list of ManyGoeaSims)

    def run_all(self, simname, rpt_items, plt_items, **pltargs):
        """Run Hypotheses Simulation using Benjamini/Hochberg FDR."""
        # Report and plot simulation results
        fout_log, base_img_genes, base_img_goids = self.bname.get_fouts(simname, self.pobj.params)
        log = self.pobj.params['log']
        with open(os.path.join(self.pobj.params['repo'], fout_log), 'w') as prt:
            self.prt_hms(sys.stdout, "Simulations initialized.")
            self.run(prt) # Runs simulations and loads self.expsets (Lists of Experiment Sets)
            self.prt_hms(sys.stdout, "Simulations complete.")
            self.prt_summary(prt)
            self.prt_experiments_means(sys.stdout, rpt_items, 'genes')
            if log is not None:
                self.prt_experiments_means(log, rpt_items, 'genes')
            self.prt_experiments_means(prt, rpt_items, 'genes')
            self.prt_experiments_means(prt, rpt_items, 'goids')
            self.prt_experiments_stats(prt, rpt_items)
            self.plt_box_tiled(base_img_genes, plt_items, 'genes', **pltargs)
            self.plt_box_tiled(base_img_goids, plt_items, 'goids', **pltargs) # GOIDS
            self.prt_seed(sys.stdout)
            self.prt_hms(prt, "Simulations complete. Reports and plots generated.")
            self.prt_hms(sys.stdout, "Simulations complete. Reports and plots generated.")
            if log is not None:
                self.prt_hms(log, "Simulations complete. Reports and plots generated.")
            sys.stdout.write("  WROTE: {LOG}\n".format(LOG=fout_log))
            self.wrpy_expsets('genes')
            self.wrpy_expsets('goids')

    def plt_box_tiled(self, base_img, plt_items, genes_goids, **kws):
        """Plot all boxplots for all experiments. X->(maxsigval, #tests), Y->%sig"""
        key2exps = self._get_key2expsets('perc_null') # Keys are '% True Null'
        base_img_full = os.path.join(self.pobj.params['repo'], base_img)
        plt_box_tiled(base_img_full, key2exps, plt_items, genes_goids, **kws)

    def _get_key2expsets(self, key1='perc_null'):
        """Separate experiment sets into sub-lists for plotting."""
        # Get ordered perc_null values from experimentset data
        keys = []
        for expset in self.expsets:
            key = expset.params[key1]
            if key not in keys:
                keys.append(key)
        # Get experimentset data
        key2exps = cx.OrderedDict([(k, []) for k in keys])
        for expset in self.expsets:
            print('EEEEE', expset)
            key2exps[expset.params[key1]].append(expset)
        return key2exps

    def wrpy_expsets(self, genes_goids='genes'):
        """Save data to Python file."""
        fout_py = 'src/pkggosim/data/{A}_{B}_{G}.py'.format(
            A=self.pobj.params['randomize_truenull_assc'],
            B=self.bname.get_desc_str(self.pobj.params), G=genes_goids)
        with open(os.path.join(self.pobj.params['repo'], fout_py), 'w') as prt:
            prt.write('"""Simulation data."""\n\n')
            prt.write('__copyright__ = "{C}"\n\n'.format(C=__copyright__))
            prt.write('from collections import namedtuple\n')
            prt.write('from collections import Counter\n')
            prt.write('from collections import OrderedDict\n\n')
            prt.write('ntobj = namedtuple("Nt", "{F}")\n\n'.format(F=" ".join(GoeaSim.ntobj._fields)))
            prt.write('num_expsets = {N}\n'.format(N=len(self.expsets)))
            prt.write('num_simsets = {N}\n\n'.format(N=len(self.expsets[0].expset)))
            prt.write('percnull2expsets = OrderedDict([\n')
            for percnull, expsets in self._get_key2expsets('perc_null').items():
                prt.write('    ({PNULL}, [\n'.format(PNULL=percnull))
                for expset in expsets:
                    for simset in expset.expset:  # simset = ManyGoeaSims
                        name_tfpn = 'nt_tfpn_{G}'.format(G=genes_goids)
                        for nt_tfpn in simset.nts_tfpn[genes_goids]:
                            prt.write('        ntobj._make({NT}),\n'.format(NT=list(nt_tfpn)))
                prt.write('    ]),\n')
            prt.write('])\n')
            prt.write('\n# {C}\n'.format(C=__copyright__))
        sys.stdout.write("  WROTE: {PY}\n".format(PY=fout_py))

    def prt_seed(self, prt):
        """Print random seed."""
        self.pobj.objrnd.prt(prt)

    def get_desc(self):
        """Return str describing params used in all simulations."""
        # Ex: Alpha(0.05) Method(fdr_bh) 10=Experiments/Set 100=P-Value simulations/Experiment
        params = self.pobj.params
        return " ".join([
            "Alpha({A}) Method({M})".format(A=params['alpha'], M=params['method']),
            "PropagateCounts({P})".format(P=params['propagate_counts']),
            "{E}=Experiments/Set".format(E=params['num_experiments']),
            "{P}=P-Value simulations/Experiment".format(P=params['num_sims'])])

    def prt_summary(self, prt):
        """Print user-specified input parameters."""
        self.pobj.prt_summary(prt)
        # for key, val in self.pobj.params.items():
        #     prt.write("{KEY:16} {VAL}\n".format(KEY=key, VAL=val))

    def run(self, prt):
        """Run all variations of Experiments. Save in self.expsets."""
        # Alpha(0.05) Method(fdr_bh) 10=Experiments 100=P-Value simulations/Experiment
        sys.stdout.write("{TITLE}\n".format(TITLE=self.get_desc()))
        # Run all experiment sets
        prms = self.pobj.params
        for perc_null in prms['perc_nulls']:   # Ex: [0, 5, 10, 20, 60, 80, 90, 95, 98, 100]
            for num_items in prms['num_genes_list']:   # Ex: [20, 100, 500]
                exp_parms = { # Experiment Set Parameters
                    'perc_null' : perc_null,
                    'num_items' : num_items,
                    'num_experiments' : prms['num_experiments'],
                    'num_sims' : prms['num_sims']}
                eset = ExperimentSet(exp_parms, self.pobj)
                self.expsets.append(eset)
        self.prt_hms(prt, "Simulations Completed")

    def prt_hms(self, prt, msg):
        """Print the elapsed time."""
        prt.write("  ELAPSED TIME: {HMS} {MSG}\n".format(HMS=get_hms(self.tic), MSG=msg))

    def prt_experiments_stats(self, prt=sys.stdout, attrs=None, genes_goids='genes'):
        """Print stats for user-specified data in experiment sets."""
        if attrs is None:
            attrs = ["fdr_actual", "frr_actual", "num_Type_I", "num_Type_II", "num_correct"]
        hdrexps = "Nul(% max) #pval #tests" # Header for col0, the description of the statistic
        namefmt = "{PERCNULL:3}% {EXP_ALPHA:5.3f} {QTY:5}"
        for attrname in attrs:
            prt.write("\n{ATTR} statistics:\n".format(ATTR=attrname))
            objstat = StatsDescribe("exps", "{:10.2f}" if attrname[:3] == "num" else "{:6.4f}")
            objstat.prt_hdr(prt, hdrexps)
            for experiment_set in self.expsets: # ExperimentSet
                expname = experiment_set.get_desc(namefmt)
                means = experiment_set.get_means(attrname, genes_goids)
                objstat.prt_data(expname, means, prt)

    def prt_experiments_means(self, prt=sys.stdout, attrs=None, genes_goids='genes'):
        """Print means and stderrs for user-specified data in experiment sets."""
        if attrs is None:
            attrs = ["fdr_actual", "frr_actual", "num_Type_I", "num_Type_II", "num_correct"]
        sys.stdout.write("\n{TITLE}\n".format(TITLE=self.get_desc()))
        num_attrs = len(attrs)
        attrstrs = ["{:>19}".format(a) for a in attrs]
        prt.write("\nSummary of {DESC} mean values and standard errors ".format(DESC=genes_goids))
        prt.write("for {N} sets of experiments\n\n".format(N=len(self.expsets)))
        prt.write("nul% #tests {ATTRS}\n".format(ATTRS=" ".join(attrstrs)))
        prt.write("---- ------ {ATTRS}\n".format(ATTRS=" ".join(["-"*19]*num_attrs)))
        namefmt = "{PERCNULL:3}% {QTY:6}"
        for experiment_set in self.expsets:
            means = [np.mean(experiment_set.get_means(a, genes_goids)) for a in attrs]
            se_denom = np.sqrt(len(means))
            stderrs = [np.std(m)/se_denom for m in means]
            prt.write("{EXP_DESC}".format(EXP_DESC=experiment_set.get_desc(namefmt)))
            for mean, stderr in zip(means, stderrs):
                prt.write("  {AVG:6.4f} +/-{SE:8.6f}".format(AVG=mean, SE=stderr))
            prt.write("\n")
        prt.write("\n")

    def prt_num_sims_w_errs(self, prt=sys.stdout):
        """Print if errors were seen in sims."""
        for experiment_set in self.expsets:
            experiment_set.prt_num_sims_w_errs(prt)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
