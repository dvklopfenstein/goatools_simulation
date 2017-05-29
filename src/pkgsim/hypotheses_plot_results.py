"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_results_all(objsim, params):
    """Plot simulation results for many sets of p-values."""
    num_sims = objsim.num_sims
    alpha = objsim.multi_params['alpha']
    # repo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."),
    for perc_sig, numpvals_sims in objsim.percsig_simsets:
        # params: perc_sig num_pvalues num_sims params
        #### pars = params.params  # repo dir_img alpha method
        base_img = params['base_img'].format(SIG=perc_sig, SIMS=num_sims)
        fout_img = os.path.join(params['dir_img'], base_img)
        #print fout_img
        # Plot results in boxplots
        perc_sig = "None" if perc_sig == 0 else "{N}{P}".format(N=perc_sig, P='%')
        title = params['title_None']
        if perc_sig is not None:
            title = params['title'].format(PERC_SIG=perc_sig, ALPHA=alpha)
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
    """Return axis for one boxplot of simulated FDRs."""
    dotsz = kws.get('dotsize', 5)
    sns.stripplot(x="xval", y="yval", data=dfrm, jitter=True, size=dotsz, ax=ax_boxplot)
    sns.boxplot(x="xval", y="yval", hue="group", data=dfrm, palette="PRGn", ax=ax_boxplot)
    ax_boxplot.legend_.remove()
    for i, line in enumerate(ax_boxplot.lines):
        is_median = i%6 == 4
        line.set_color('red' if is_median else 'black')
        if is_median:
            line.set_linestyle('--')
    ax_boxplot.plot([-1000, 1000], [alpha, alpha], 'b.-')
    if 'ylim_a' in kws and 'ylim_b' in kws:
        ax_boxplot.set_ylim(kws['ylim_a'], kws['ylim_b'])
    if 'title' in kws:
        ax_boxplot.set_title(kws['title'], size=25)
    if 'xlabel' in kws:
        ax_boxplot.set_xlabel(kws['xlabel'], size=20)
    if 'ylabel' in kws:
        #ax_boxplot.set_ylabel("Simulated FDR Ratios", size=20)
        ax_boxplot.set_ylabel(kws['ylabel'], size=20)
    return ax_boxplot

def get_percsig_dicts(numpvals_sims):
    """Get pvalue dictionary suitable for a pandas dataframe."""
    tbl = []
    for num_pvals, objsims in numpvals_sims: # objsims is an ManyHypothesesSims obj
        # objsims: pkgsim.pval_mtcorr_sims.ManyHypothesesSims
        for obj1sim in objsims.pvalsimobjs:
            perc_sig_orig = obj1sim.get_perc_sig("pvals")
            perc_sig_corr = obj1sim.get_perc_sig("pvals_corr")
            tbl.append({'xval':num_pvals, 'group':'Uncorrected', 'yval':perc_sig_orig})
            tbl.append({'xval':num_pvals, 'group':'Corrected', 'yval':perc_sig_corr})
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
    for (perc_sig, max_sigpval), expsets in key2exps.items():
        assert expsets
        kws['fout_img'] = fimg_pat.format(
            PSIMATTR=attrname, SIGPERC=perc_sig, SIGMAX=int(100*max_sigpval))
        perc_true_null = 100-perc_sig
        title_pat = title_pat100 if perc_true_null == 100 else title_patpnul
        kws['title'] = title_pat.format(P=perc_true_null, M=max_sigpval)
        dfrm = pd.DataFrame(_get_dftbl_boxplot(expsets, attrname, grpname))
        wrpng_boxplot_sigs_each(dfrm, expsets[0].alpha, **kws)

# TBD: rm
def plt_box_tiled1(fout_img, key2exps, attrname='fdr_actual', grpname='FDR'):
    """Plot all detailed boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    kws = {
        'fout_img': None,
        'xlabel': 'Number of Tested Hypotheses',
        'ylabel': 'Simulated FDR Ratios',
        'ylim_a':0, 'ylim_b':0.10}
    perc_sigs, max_sigpvals = _get_num_rows_cols(key2exps)
    num_rows = len(perc_sigs)
    num_cols = len(max_sigpvals)
    plt.close('all')
    fig, axes_2d = plt.subplots(num_rows, num_cols, sharex='col', sharey='row')
    for row, perc_sig in enumerate(perc_sigs):
        for col, max_sigpval in enumerate(max_sigpvals):
            expsets = key2exps[(perc_sig, max_sigpval)]
            dfrm = pd.DataFrame(_get_dftbl_boxplot(expsets, attrname, grpname))
            set_axis_boxplot(axes_2d[row][col], dfrm, expsets[0].alpha, **kws)
    plt.show()

def plt_box_tiled(fout_img, key2exps, attrname='fdr_actual', grpname='FDR'):
    """Plot all detailed boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    kws = {
        'fout_img': None,
        #'xlabel': 'Number of Tested Hypotheses',
        #'ylabel': 'Simulated FDR Ratios',
        'ylim_a':0, 'ylim_b':0.09}
    perc_sigs, max_sigpvals = _get_num_rows_cols(key2exps)
    num_plts = len(key2exps)
    rows = len(perc_sigs)
    cols = len(max_sigpvals)
    plt.close('all')
    # https://stackoverflow.com/questions/6963035/pyplot-axes-labels-for-subplots
    fig = plt.figure()
    axall = fig.add_subplot(1, 1, 1)
    ax1 = fig.add_subplot(rows, cols, 1)
    #fig, axes_2d = plt.add_subplots(num_rows, num_cols, sharex='col', sharey='row')
    axes_2d = [ax1] + [fig.add_subplot(rows, cols, i, sharex=ax1, sharey=ax1) for i in range(2, num_plts+1)]
    #axes_2d = fig.add_subplot(rows, cols, 1, sharex='col', sharey='row')
    idx = 0
    for row, perc_sig in enumerate(perc_sigs):
        for col, max_sigpval in enumerate(max_sigpvals):
            expsets = key2exps[(perc_sig, max_sigpval)]
            dfrm = pd.DataFrame(_get_dftbl_boxplot(expsets, attrname, grpname))
            #set_axis_boxplot(axes_2d[row][col], dfrm, expsets[0].alpha, **kws)
            set_axis_boxplot(axes_2d[idx], dfrm, expsets[0].alpha, **kws)
            idx += 1
    # https://stackoverflow.com/questions/3584805/in-matplotlib-what-does-the-argument-mean-in-fig-add-subplot111
    # https://matplotlib.org/examples/pylab_examples/shared_axis_demo.html
    # https://stackoverflow.com/questions/1358977/how-to-make-several-plots-on-a-single-page-using-matplotlib
    # https://stackoverflow.com/questions/6963035/pyplot-axes-labels-for-subplots
    axall.set_xlabel('Number of Tested Hypotheses')
    axall.set_ylabel('Simulated {GRP} Ratios'.format(GRP=grpname))
    plt.show()

def _get_num_rows_cols(key2exps):
    """Given the list of experiment sets, return the number of rows and columns for plotting."""
    perc_sigs, max_sigpval = zip(*key2exps.keys())
    return sorted(set(perc_sigs)), sorted(set(max_sigpval))

# TBD: rm
def plt_box_tiled_plain(fout_img, key2exps, attrname='fdr_actual', grpname='FDR'):
    """Plot all plain boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    dpi = 200
    dfrm = pd.DataFrame(_get_dftbl_boxplots(key2exps, attrname, grpname))
    grd = sns.FacetGrid(dfrm, col='max_sigpval', row='perc_true_null')
    grd = grd.map(sns.boxplot, "xval", "yval")
    plt.title('{GRP} Simulations'.format(GRP=grpname))
    plt.xlabel('Number of Tested Hypotheses')
    plt.ylabel('Simulated {GRP}s'.format(GRP=grpname))
    #plt.show()
    plt.savefig(fout_img, dpi=dpi)
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))

# TBD: rm
def _get_dftbl_boxplots(key2exps, attrname='fdr_actual', grpname='FDR'):
    """Get data for dataframe for multiple boxplot tiles."""
    tbl_full = []
    for (perc_sig, max_sigpval), expsets in key2exps.items():
        perc_true_null = 100 - perc_sig
        for dct in _get_dftbl_boxplot(expsets, attrname, grpname):
            dct['max_sigpval'] = max_sigpval
            dct['perc_true_null'] = perc_true_null
            tbl_full.append(dct)
    return tbl_full

def _get_dftbl_boxplot(experimentsets, attr='fdr_actual', grp='FDR'):
    """Get plotting data suitable for a single plot of boxplots."""
    tbl = []
    for exps in experimentsets: # Each expset has the same (X)max_sigpval and (Y)perc_sig
        tot_h = exps.params['hypoth_qty'] # Number of hypotheses
        # Make one dictionary line for each value of fdr_actual
        dcts = [{'xval':tot_h, 'yval':y, 'group':grp} for y in exps.get_means(attr)]
        tbl.extend(dcts)
    return tbl

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
