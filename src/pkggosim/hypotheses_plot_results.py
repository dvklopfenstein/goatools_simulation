"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np

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
    # https://stackoverflow.com/questions/23969619/plotting-with-seaborn-using-the-matplotlib-object-oriented-interface
    plt.clf()
    sns.despine(offset=10, trim=True)
    sns.set(style="ticks")
    fig, ax_boxplot = plt.subplots()
    set_axis_boxplot(ax_boxplot, dfrm, alpha, **kws)
    # # Set the tick labels font
    # # http://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
    # axis = plt.subplot() # Defines variable by creating an empty plot
    # for label in axis.get_xticklabels() + axis.get_yticklabels():
    #     #label.set_fontname('Arial')
    #     label.set_fontsize(15)
    # # Plot text
    fout_img = kws.get("fout_img", "sim_hypotheses.png")
    # #plt.yticks([0.01, 0.03, 0.05, 0.07, 0.09])
    # #plt.tight_layout()
    fig.savefig(fout_img, dpi=kws.get('dpi', 200))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    show = kws.get('show', False)
    if show:
        plt.show()

def set_axis_boxplot(ax_boxplot, dfrm, alpha, **kws):
    """Fills axis ax_boxplot with one set of boxplots of simulated FDRs."""
    lwd = kws.get('linewidth', 0.7)
    dotsz = kws.get('dotsize', 5)
    sns.stripplot(x="xval", y="yval", data=dfrm, jitter=True, size=dotsz, ax=ax_boxplot)
    sns.boxplot(x="xval", y="yval", hue="group", data=dfrm, # palette="PRGn",
                ax=ax_boxplot, linewidth=lwd, color='black', saturation=1)
    ax_boxplot.legend_.remove()
    _set_color_whiskers(ax_boxplot, lwd, 'black', 'red')
    _set_color_boxes(ax_boxplot, 'black')
    ax_boxplot.plot([-1000, 1000], [alpha, alpha], 'k--', alpha=1.0,
                    linewidth=lwd, solid_capstyle="butt")
    if 'ylim_a' in kws and 'ylim_b' in kws:
        ax_boxplot.set_ylim(kws['ylim_a'], kws['ylim_b'])
    if 'title' in kws:
        ax_boxplot.set_title(kws['title'], size=25)
    ax_boxplot.set_xlabel(kws.get('xlabel', ""), size=20)
    ax_boxplot.set_ylabel(kws.get('ylabel', ""), size=20)
    return ax_boxplot

def _set_color_whiskers(axes, lwd, col_end, col_mid):
    """Set boxplot whisker line color and thinkness."""
    for i, line in enumerate(axes.lines):
        line.set_linewidth(lwd)
        is_median = i%6 == 4
        line.set_color(col_mid if is_median else col_end)
        if is_median:
            line.set_linestyle('--')

def _set_color_boxes(axes, color):
    """Set boxplot box line color."""
    for artist in axes.artists:
        artist.set_edgecolor(color)

def get_percsig_dicts(numtests_sims):
    """Get pvalue dictionary suitable for a pandas dataframe."""
    tbl = []
    for num_tests, objsims in numtests_sims: # objsims is an ManyHypothesesSims obj
        # objsims: pkggosim.pval_mtcorr_sims.ManyHypothesesSims
        for obj1sim in objsims.pvalsimobjs:
            perc_null_orig = obj1sim.get_perc_null("pvals")
            perc_null_corr = obj1sim.get_perc_null("pvals_corr")
            tbl.append({'xval':num_tests, 'group':'Uncorrected', 'yval':perc_null_orig})
            tbl.append({'xval':num_tests, 'group':'Corrected', 'yval':perc_null_corr})
    return tbl

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
        dfrm = pd.DataFrame(_get_dftbl_boxplot(expsets, attrname, grpname))
        wrpng_boxplot_sigs_each(dfrm, expsets[0].alpha, **kws)

def plt_box_tiled(fout_img, key2exps, attrname='fdr_actual', grpname='FDR'):
    """Plot all detailed boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    kws = {
        'dpi':400,
        'title':'Hypotheses Simulations',
        'xlabel':'Number of Tested Hypotheses',
        'ylabel':'Simulated {GRP} Ratios'.format(GRP=grpname),
        'txtsz_title':20,
        'txtsz_xy'   :15,
        'txtsz_tile' :None,
        'txtsz_ticks':None,
    }
    #ax_kws = {
    #    'fout_img': None,
    #    #'xlabel': 'Number of Tested Hypotheses',
    #    #'ylabel': 'Simulated FDR Ratios',
    #    'ylim_a':0, 'ylim_b':0.09}
    num_rows, num_cols = _get_num_rows_cols(key2exps)
    plt.close('all')
    sns.set(style="ticks")
    # https://stackoverflow.com/questions/6963035/pyplot-axes-labels-for-subplots
    fig = plt.figure()
    #axall = fig.add_subplot(1, 1, 1)
    axes_2d = _get_tiled_axes(fig, num_rows, num_cols)
    # http://matplotlib.org/users/recipes.html
    sorted_dat = sorted(key2exps.items(), key=lambda t: [-1*t[0][0], t[0][1]]) # perc_null, max_sig
    bottom_row = num_cols*(num_rows-1)
    for idx, (axes, ((perc_null, maxsig), exps)) in enumerate(zip(axes_2d, sorted_dat)):
        plt.subplots_adjust(hspace=.1, wspace=.1, left=.18, bottom=.2, top=.92)
        dfrm = pd.DataFrame(_get_dftbl_boxplot(exps, attrname, grpname))
        set_axis_boxplot(axes, dfrm, exps[0].alpha, dotsize=2)
        axes.set_xticklabels([e.params['hypoth_qty'] for e in exps], size=kws['txtsz_ticks'])
        axes.set_yticks([0.00, 0.025, 0.05, 0.075])
        axes.set_yticklabels(["", "0.025", "0.050", "0.075"])
        if idx >= bottom_row:
            axes.set_xlabel("Sig.<={MAXSIG}".format(MAXSIG=maxsig), size=kws['txtsz_tile'])
        if idx%num_cols == 0:
            axes.set_ylabel("{PERCNULL}% Null".format(PERCNULL=perc_null), size=kws['txtsz_tile'])
        axes.set_ylim(0.0, 0.09)
        axes.tick_params('both', length=3, width=1) # Shorten both x and y axes tick length

    _tiled_xyticklabels_off(axes_2d, num_cols)
    # https://stackoverflow.com/questions/3584805/in-matplotlib-what-does-the-argument-mean-in-fig-add-subplot111
    # https://matplotlib.org/examples/pylab_examples/shared_axis_demo.html
    # https://stackoverflow.com/questions/1358977/how-to-make-several-plots-on-a-single-page-using-matplotlib
    # https://stackoverflow.com/questions/6963035/pyplot-axes-labels-for-subplots
    #axall.set_xticks([])
    #axall.set_yticks([])
    #axall.set_xlabel(kws['xlabel'], size=30)
    #axall.set_ylabel(kws['ylabel'], size=30)
    #plt.subplots_adjust(bottom=.25, left=.25)
    fig.text(0.5, 0.96, kws['title'], size=kws['txtsz_title'], ha='center', va='center')
    fig.text(0.5, 0.06, kws['xlabel'], size=kws['txtsz_xy'], ha='center', va='center')
    fig.text(0.06, 0.5, kws['ylabel'], size=kws['txtsz_xy'], ha='center', va='center', rotation='vertical')
    #plt.tight_layout()
    plt.savefig(fout_img, dpi=kws.get('dpi', 200))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    if kws.get('show', False):
        plt.show()

def _get_tiled_axes(fig, n_rows, n_cols):
    """Create empty axes to be filled and used in tiled boxplot image."""
    ax1 = fig.add_subplot(n_rows, n_cols, 1)
    rng = range(2, n_rows*n_cols+1)
    return [ax1] + [fig.add_subplot(n_rows, n_cols, i, sharex=ax1, sharey=ax1) for i in rng]

def _tiled_xyticklabels_off(axes, num_cols):
    """Turn off xticklabels and yticklabels on the inside plot edges of the tiled boxplots."""
    for xaxis in axes[:-1*num_cols]:
        for label in xaxis.get_xticklabels():
            label.set_visible(False)
    for idx, yaxis in enumerate(axes):
        if idx%num_cols != 0:
            for label in yaxis.get_yticklabels():
                label.set_visible(False)

def _get_num_rows_cols(key2exps):
    """Return the number of rows and columns for a matrix of tiled boxplots."""
    perc_nulls, max_sigpval = zip(*key2exps.keys())
    return len(set(perc_nulls)), len(set(max_sigpval))

def _get_dftbl_boxplot(experimentsets, attr='fdr_actual', grp='FDR'):
    """Get plotting data suitable for a single plot of boxplots."""
    tbl = []
    for exps in experimentsets: # Each expset has the same (X)max_sigpval and (Y)perc_null
        tot_h = exps.params['hypoth_qty'] # Number of hypotheses
        # Make one dictionary line for each value of fdr_actual
        dcts = [{'xval':tot_h, 'yval':y, 'group':grp} for y in exps.get_means(attr)]
        tbl.extend(dcts)
    return tbl

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
