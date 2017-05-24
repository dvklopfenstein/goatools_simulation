"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

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
            'fout_img':fout_img,
        }
        wrpng_boxplot_sigs_each(numpvals_sims, **pltargs)

def wrpng_boxplot_sigs_each(dfrm, **kws):
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

def get_percsig_dicts(numpvals_sims):
    """Get pvalue dictionary suitable for a pandas dataframe."""
    tbl = []
    for num_pvals, objsims in numpvals_sims: # objsims is an PvalSimMany obj
        # objsims: pkgsim.pval_mtcorr_sims.PvalSimMany
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
        'ylim_a':0, 'ylim_b':0.10}
    for (perc_sig, max_sigpval), expsets in key2exps.items():
        kws['fout_img'] = fimg_pat.format(
          PSIMATTR=attrname, SIGPERC=perc_sig, SIGMAX=int(100*max_sigpval))
        perc_true_null = 100-perc_sig
        title_pat = title_pat100 if perc_true_null == 100 else title_patpnul
        kws['title'] = title_pat.format(P=perc_true_null, M=max_sigpval)
        dfrm = pd.DataFrame(_get_dftbl_boxplot(expsets, attrname, grpname))
        wrpng_boxplot_sigs_each(dfrm, **kws)

def plt_box_tiled(fout_img, key2exps, attrname='fdr_actual', grpname='FDR'):
    """Plot all boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
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
