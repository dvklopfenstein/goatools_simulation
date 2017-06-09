"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import collections as cx
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pkggosim.common.plot_results import PlotInfo, get_dftbl_boxplot
from pkggosim.common.plot_results import get_num_rows_cols, fill_axes


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
        _wrpng_boxplot_sigs_each(numpvals_sims, alpha, **pltargs)

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
    plt.title(kws['title'], size=25)
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

def _wrpng_boxplot_sigs_each(dfrm, alpha, **kws):
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
        _wrpng_boxplot_sigs_each(dfrm, expsets[0].alpha, **kws)

def plt_box_tiled(fout_img, key2exps, attrname, **args_kws):
    """Plot all detailed boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    objplt = PlotInfo(attrname, args_kws)
    kws = objplt.kws
    num_rows, num_cols = get_num_rows_cols(key2exps)
    plt.close('all')
    sns.set(style="ticks")
    fig = plt.figure()
    axes_2d = _get_tiled_axes(fig, num_rows, num_cols)
    sorted_dat = sorted(key2exps.items(), key=lambda t: [-1*t[0][0], t[0][1]]) # perc_null, max_sig
    for idx, tile_items in enumerate(zip(axes_2d, sorted_dat)):
        plt.subplots_adjust(hspace=.1, wspace=.1, left=.18, bottom=.2, top=.92)
        _plt_tile(idx, num_rows, num_cols, tile_items, objplt)
    _tiled_xyticklabels_off(axes_2d, num_cols)
    xysz = kws['txtsz_xy']
    if attrname == "fdr_actual":
        _add_means_txt(fig, key2exps, objplt, .92-.2, .2+.1) # top-bottom, bottom+hspace
    fig.text(0.5, 0.96, kws['title'], size=kws['txtsz_title'], ha='center', va='center')
    fig.text(0.5, 0.06, kws['xlabel'], size=xysz, ha='center', va='center')
    fig.text(0.06, 0.5, kws['ylabel'], size=xysz, ha='center', va='center', rotation='vertical')
    plt.savefig(fout_img, dpi=kws.get('dpi', 200))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    if kws.get('show', False):
        plt.show()

def _tiled_xyticklabels_off(axes, num_cols):
    """Turn off xticklabels and yticklabels on the inside plot edges of the tiled boxplots."""
    for xaxis in axes[:-1*num_cols]:
        for label in xaxis.get_xticklabels():
            label.set_visible(False)
    for idx, yaxis in enumerate(axes):
        if idx%num_cols != 0:
            for label in yaxis.get_yticklabels():
                label.set_visible(False)

def _get_tiled_axes(fig, n_rows, n_cols):
    """Create empty axes to be filled and used in tiled boxplot image."""
    ax1 = fig.add_subplot(n_rows, n_cols, 1)
    rng = range(2, n_rows*n_cols+1)
    return [ax1] + [fig.add_subplot(n_rows, n_cols, i, sharex=ax1, sharey=ax1) for i in rng]

def _add_means_txt(fig, key2exps, objplt, y_m, y_b):
    """Add means per row to plot."""
    nullperc_meantxt = sorted(_get_row_means(key2exps, objplt).items())
    num_rows = len(nullperc_meantxt)
    for row, (_, meantxt) in enumerate(nullperc_meantxt):
        yval = y_m*row/num_rows + y_b
        fig.text(0.93, yval, meantxt, ha='center', va='center', rotation='vertical')

def _get_row_means(key2exps, objplt):
    """Get the mean and SE for each row."""
    nullperc2means = cx.defaultdict(list)
    for (nullperc, _), expsets in key2exps.items():
        for expset in expsets:
            means = expset.get_means(objplt.attrname)
            nullperc2means[nullperc].extend(means)
    nullperc2meantxt = {}
    for nullperc, means in nullperc2means.items():
        mean = np.mean(means)
        stderr = np.std(means)
        txt = "{NAME}={MEAN:5.3f}\nSE={SE:5.3f}".format(NAME=objplt.grpname, MEAN=mean, SE=stderr)
        nullperc2meantxt[nullperc] = txt
    return nullperc2meantxt

def _plt_tile(idx, num_rows, num_cols, tile_items, objplt):
    """Plot one tile of a multi-tiled plot."""
    kws = objplt.kws
    (axes, ((perc_null, maxsig), exps)) = tile_items
    letter = "{C}{R}".format(R=idx/num_cols+1, C=chr(65+idx%num_cols))
    dfrm = pd.DataFrame(get_dftbl_boxplot(exps, objplt.attrname, objplt.grpname))
    alpha = exps[0].alpha if kws['alphaline'] else None
    fill_axes(axes, dfrm, alpha, dotsize=kws['dotsize'],
              plottype=kws['plottype'], letter=letter, ylim=kws['ylim'])
    axes.set_xticklabels([e.params['num_items'] for e in exps], size=kws['txtsz_ticks'])
    axes.set_yticks(kws['yticks'])
    axes.set_yticklabels(kws['yticklabels'])
    if idx >= num_cols*(num_rows-1): # bottom_row
        axes.set_xlabel("Sig.<={MAXSIG}".format(MAXSIG=maxsig), size=kws['txtsz_tile'])
    if idx%num_cols == 0:
        axes.set_ylabel("{PERCNULL}% Null".format(PERCNULL=perc_null), size=kws['txtsz_tile'])
    axes.set_ylim(kws['ylim'])
    axes.tick_params('both', length=3, width=1) # Shorten both x and y axes tick length
    # Add value text above plot bars to make plot easier to read
    for ntval in objplt.get_str_mean(exps):
        axes.text(ntval.x, ntval.y, ntval.valstr, ha='center', va='bottom')

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.154
