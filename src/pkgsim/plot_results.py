"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pkgsim.utils import get_perc_sig

def wrpng_boxplot_sigs(params, numpvals_results, **kws):
    """Plot pvalues showing as significant."""
    dfrm = pd.DataFrame(get_percsig_dicts(params, numpvals_results))
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
    plt.ylim(0, 300.0*params['alpha'])
    plt.tight_layout()
    plt.savefig(fout_img, dpi=kws.get('dpi', 200))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    plt.show()

def get_percsig_dicts(params, numpvals_results):
    """Get pvalue dictionary suitable for a pandas dataframe."""
    tbl = []
    for num_pvals, simsets in numpvals_results:
        for simset in simsets:
            alpha = params['alpha']
            perc_sig_orig = get_perc_sig(simset['pvals'], alpha)
            perc_sig_corr = get_perc_sig(simset['pvals_corr'], alpha)
            tbl.append({'numpvals':num_pvals, 'P-values':'Uncorrected', 'perc_sig':perc_sig_orig})
            tbl.append({'numpvals':num_pvals, 'P-values':'Corrected', 'perc_sig':perc_sig_corr})
    return tbl

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
