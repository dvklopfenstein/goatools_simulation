"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pkggosim.common.plot_results import PlotInfo, plt_tile, get_tiled_axes, get_dftbl_boxplot
from pkggosim.common.plot_results import tiled_xyticklabels_off, get_num_rows_cols, fill_axes


def plot_results_all(objsim, params):
    """Plot simulation results for many sets of p-values."""
    num_sims = objsim.num_sims
    alpha = objsim.multi_params['alpha']
    # repo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."),
    for perc_null, numpvals_sims in objsim.percsig_simsets:
        # params: perc_null num_pvalues num_sims params
        #### pars = params.params  # repo dir_img alpha method
        base_img = params['base_img'].format(PERCNULL=perc_null, SIMS=num_sims)
        fout_img = os.path.join(params['dir_img'], base_img)
        #print fout_img
        # Plot results in boxplots
        perc_null = None if perc_null == 0 else "{N}{P}".format(N=perc_null, P='%')
        title = params['title_None']
        if perc_null is not None:
            title = params['title'].format(PERCNULL=perc_null, ALPHA=alpha)
        pltargs = {
            'show':False,
            'title':title,
            'xlabel':"# of P-values per set; {N} sets".format(N=num_sims),
            'ylabel':'Simulated FDR Ratios',
            'fout_img':fout_img,
        }
        wrpng_boxplot_sigs_each(numpvals_sims, alpha, **pltargs)

def wrpng_boxplot_sigs_each2(dfrm, alpha, **kws):
    """Plot one boxplot of simulated FDRs per experiment set of %true_null & MaxSigVal."""
    # dfrm = pd.DataFrame(get_percsig_dicts(numpvals_sims))
    plt.clf()
    sns.set(style="ticks")
    sns.stripplot(x="xval", y="yval", data=dfrm, jitter=True, size=5)
    ax_boxplot = sns.boxplot(x="xval", y="yval", hue="group", data=dfrm, palette="PRGn")
    ax_boxplot.legend_.remove()
    for i, line in enumerate(ax_boxplot.lines):
        is_median = i%6 == 4
        #color = 'red' if i%6 == 4 else 'black'
        line.set_color('red' if is_median else 'black')
        if is_median:
            line.set_linestyle('--')
    ax_boxplot.plot([0, 1000], [alpha, alpha], 'b.-')
    sns.despine(offset=10, trim=True)
    # Set the tick labels font
    # http://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
    axis = plt.subplot() # Defines variable by creating an empty plot
    for label in axis.get_xticklabels() + axis.get_yticklabels():
        #label.set_fontname('Arial')
        label.set_fontsize(15)
    # Plot text
    fout_img = kws.get("fout_img", "sim_pvals.png")
    plt.title(kws.get('title', 'P-values'), size=25)
    plt.yticks([0.01, 0.03, 0.05, 0.07, 0.09])
    plt.xlabel(kws.get('xlabel', '# P-values/multitest correction'), size=20)
    plt.ylabel("Simulated FDR Ratios", size=20)
    if 'ylim_a' in kws and 'ylim_b' in kws:
        plt.ylim(kws['ylim_a'], kws['ylim_b'])
    plt.tight_layout()
    plt.savefig(fout_img, dpi=kws.get('dpi', 200))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    show = kws.get('show', False)
    if show:
        plt.show()

def wrpng_boxplot_sigs_each(dfrm, alpha, **kws):
    """Plot one boxplot of simulated FDRs per experiment set of %true_null & MaxSigVal."""
    plt.clf()
    sns.despine(offset=10, trim=True)
    sns.set(style="ticks")
    fig, ax_boxplot = plt.subplots()
    fill_axes(ax_boxplot, dfrm, alpha, **kws)
    fout_img = kws.get("fout_img", "sim_hypotheses.png")
    fig.savefig(fout_img, dpi=kws.get('dpi', 200))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    show = kws.get('show', False)
    if show:
        plt.show()

#def get_percsig_dicts(numtests_sims):
#    """Get pvalue dictionary suitable for a pandas dataframe."""
#    tbl = []
#    for num_tests, objsims in numtests_sims: # objsims is an ManyHypothesesSims obj
#        # objsims: pkggosim.pval_mtcorr_sims.ManyHypothesesSims
#        for obj1sim in objsims.pvalsimobjs:
#            perc_null_orig = obj1sim.get_perc_null("pvals")
#            perc_null_corr = obj1sim.get_perc_null("pvals_corr")
#            tbl.append({'xval':num_tests, 'group':'Uncorrected', 'yval':perc_null_orig})
#            tbl.append({'xval':num_tests, 'group':'Corrected', 'yval':perc_null_corr})
#    return tbl

def plt_box_all(fimg_pat, key2exps, attrname='fdr_actual', grpname='FDR'):
    """Plot all boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    title_pat100 = "{P:}% True Null"
    title_patpnul = "{P:}% True Null. MaxSig={M:4.2f}"
    kws = {
        'fout_img': None,
        'title': None,
        'xlabel': 'Number of Tested Hypotheses',
        'ylabel': 'Simulated FDR Ratios',
        'ylim_a':0, 'ylim_b':0.10}
    for (perc_null, max_sigpval), expsets in key2exps.items():
        assert expsets
        kws['fout_img'] = fimg_pat.format(
            PSIMATTR=attrname, PERCNULL=perc_null, SIGMAX=int(100*max_sigpval))
        perc_true_null = 100-perc_null
        title_pat = title_pat100 if perc_true_null == 100 else title_patpnul
        kws['title'] = title_pat.format(P=perc_true_null, M=max_sigpval)
        dfrm = pd.DataFrame(get_dftbl_boxplot(expsets, attrname, grpname))
        wrpng_boxplot_sigs_each(dfrm, expsets[0].alpha, **kws)

def plt_box_tiled(fout_img, key2exps, **args_kws):
    """Plot all detailed boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    objplt = PlotInfo(args_kws)
    kws = objplt.kws
    num_rows, num_cols = get_num_rows_cols(key2exps)
    plt.close('all')
    sns.set(style="ticks")
    fig = plt.figure()
    axes_2d = get_tiled_axes(fig, num_rows, num_cols)
    sorted_dat = sorted(key2exps.items(), key=lambda t: [-1*t[0][0], t[0][1]]) # perc_null, max_sig
    for idx, tile_items in enumerate(zip(axes_2d, sorted_dat)):
        plt.subplots_adjust(hspace=.1, wspace=.1, left=.18, bottom=.2, top=.92)
        plt_tile(idx, num_rows, num_cols, tile_items, objplt)
    tiled_xyticklabels_off(axes_2d, num_cols)
    xysz = kws['txtsz_xy']
    fig.text(0.5, 0.96, kws['title'], size=kws['txtsz_title'], ha='center', va='center')
    fig.text(0.5, 0.06, kws['xlabel'], size=xysz, ha='center', va='center')
    fig.text(0.06, 0.5, kws['ylabel'], size=xysz, ha='center', va='center', rotation='vertical')
    plt.savefig(fout_img, dpi=kws.get('dpi', 200))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    if kws.get('show', False):
        plt.show()

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
