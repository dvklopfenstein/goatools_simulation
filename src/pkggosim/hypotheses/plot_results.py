"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pkggosim.common.plot_results import PlotInfo
from pkggosim.common.plot_results import BarText
from pkggosim.common.plot_results import get_dftbl_boxplot
from pkggosim.common.plot_results import get_num_rows_cols
from pkggosim.common.plot_results import fill_axes_data


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
    dpi = kws.get('dpi', 600)
    plt.savefig(fout_img, dpi=dpi)
    sys.stdout.write("  DPI={DPI} WROTE: {IMG}\n".format(DPI=dpi, IMG=fout_img))
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
        stderr = np.std(means)/np.sqrt(len(means))
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
    fill_axes_data(axes, dfrm, alpha=alpha, dotsize=kws['dotsize'],
              plottype=kws['plottype'], letter=letter, ylim=kws['ylim'])
    axes.set_xticklabels([e.params['num_items'] for e in exps], size=kws['txtsz_ticks'])
    axes.set_yticks(kws['yticks'])
    axes.set_yticklabels(kws['yticklabels'])
    if idx >= num_cols*(num_rows-1): # bottom_row
        _set_xlabels(axes, maxsig, exps[0].alpha)
    if idx%num_cols == 0:
        axes.set_ylabel("{PERCNULL}% Null".format(PERCNULL=perc_null), size=kws['txtsz_tile'])
    axes.set_ylim(kws['ylim'])
    axes.tick_params('both', length=3, width=1) # Shorten both x and y axes tick length
    # Add value text above plot bars to make plot easier to read
    #### for ntval in objplt.get_str_mean(exps):
    if kws['plottype'] == 'barplot':
        means = [np.mean(exp.get_means(objplt.attrname)) for exp in exps]
        for ntval in BarText(means).get_bar_text():
            axes.text(ntval.x, ntval.y, ntval.valstr, ha='center', va='bottom')

def _set_xlabels(axes, maxsig, alpha):
    """Set xlabels with max P-value and description."""
    desc = "Minimal"
    if maxsig <= alpha/5:
        desc = 'Extreme'
    elif maxsig <= alpha*3/5:
        desc = 'Moderate'
    xlabel = "{DESC}(P{LT}{MAXSIG})".format(LT=r'$\leq$', MAXSIG=maxsig, DESC=desc)
    axes.set_xlabel(xlabel, size=15)


# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.154
