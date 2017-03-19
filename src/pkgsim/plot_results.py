"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pkgsim.utils import get_perc_sig

def plot_results_all(results_all, global_params):
    """Plot simulation results for many sets of p-values."""
    for perc_sig, num_sims, results_set in results_all:
        # params: perc_sig num_pvalues num_sims params
        #### pars = params.params  # repo dir_img alpha method
        base_img = "pvalues_sig{SIG:02}_numsims{SIMS:04}.png".format(SIG=perc_sig, SIMS=num_sims)
        fout_img = os.path.join(global_params['dir_img'], base_img)
        #print fout_img
        # Plot results in boxplots
        perc_sig = "None" if perc_sig == 0 else "{N}{P}".format(N=perc_sig, P='%')
        pltargs = {
            'show':False,
            'title':"P-values: {PERC_SIG}".format(PERC_SIG=perc_sig),
            'xlabel':"# of P-values per set; {N} sets".format(N=num_sims),
            'fout_img':fout_img,
        }
        wrpng_boxplot_sigs(global_params['alpha'], results_set, **pltargs)

def wrpng_boxplot_sigs(alpha, numpvals_results, **kws):
    """Plot pvalues showing as significant."""
    dfrm = pd.DataFrame(get_percsig_dicts(alpha, numpvals_results))
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

def get_percsig_dicts(alpha, numpvals_results):
    """Get pvalue dictionary suitable for a pandas dataframe."""
    tbl = []
    for num_pvals, results_lst in numpvals_results:
        for results in results_lst:
            perc_sig_orig = get_perc_sig(results['pvals'], alpha)
            perc_sig_corr = get_perc_sig(results['pvals_corr'], alpha)
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
