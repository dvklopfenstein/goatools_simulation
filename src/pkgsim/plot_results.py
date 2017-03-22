"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_results_all(percsigs_simsets, params):
    """Plot simulation results for many sets of p-values."""
    num_sims = params['num_sims']
    alpha = params['multi_params']['alpha']
    for perc_sig, numpvals_sims in percsigs_simsets:
        # params: perc_sig num_pvalues num_sims params
        #### pars = params.params  # repo dir_img alpha method
        base_img = params['base_img'].format(SIG=perc_sig, SIMS=num_sims)
        fout_img = os.path.join(params['dir_img'], base_img)
        #print fout_img
        # Plot results in boxplots
        perc_sig = "None" if perc_sig == 0 else "{N}{P}".format(N=perc_sig, P='%')
        title = params['title_None']
        if perc_sig is not None:
            title = params['title'].format(PERC_SIG=perc_sig, MAX_SIG=params['max_sig'])
        pltargs = {
            'show':False,
            'title':title,
            'xlabel':"# of P-values per set; {N} sets".format(N=num_sims),
            'fout_img':fout_img,
        }
        wrpng_boxplot_sigs(alpha, numpvals_sims, **pltargs)

def wrpng_boxplot_sigs(alpha, numpvals_sims, **kws):
    """Plot pvalues showing as significant."""
    plt.clf()
    dfrm = pd.DataFrame(get_percsig_dicts(numpvals_sims))
    sns.set(style="ticks")
    sns.boxplot(x="numpvals", y="perc_sig", hue="P-values", data=dfrm, palette="PRGn")
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
    plt.xlabel(kws.get('xlabel', '# P-values per set'), size=20)
    plt.ylabel("% of P-values found significant", size=20)
    #plt.ylim(0, 300.0*params.params['alpha'])
    plt.tight_layout()
    plt.savefig(fout_img, dpi=kws.get('dpi', 200))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    show = kws.get('show', 'False')
    if show:
        plt.show()

def get_percsig_dicts(numpvals_sims):
    """Get pvalue dictionary suitable for a pandas dataframe."""
    tbl = []
    for num_pvals, objsims in numpvals_sims: # objsims is an PvalSimMany obj
        # objsims: pkgsim.pval_mtcorr_sims.PvalSimMany
        for obj1sim in objsims.obj1sim_list:
            perc_sig_orig = obj1sim.get_perc_sig("pvals")
            perc_sig_corr = obj1sim.get_perc_sig("pvals_corr")
            tbl.append({'numpvals':num_pvals, 'P-values':'Uncorrected', 'perc_sig':perc_sig_orig})
            tbl.append({'numpvals':num_pvals, 'P-values':'Corrected', 'perc_sig':perc_sig_corr})
    #for e in tbl: print "EEEE", e
#EEEE {
#'perc_sig': 0.0,
#'numpvals': Nt(
#   perc_sig=50,
#   num_pvalues=10000,
#   num_sims=100,
#   params={
#     'repo': '/cygdrive/c/Users/note2/Data/git/goatools_simulation/src/bin/../..',
#     'alpha': 0.05,
#     'dir_img': 'doc/images',
#     'method': 'fdr_bh'}),
#'P-values': 'Corrected'}
    return tbl

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
