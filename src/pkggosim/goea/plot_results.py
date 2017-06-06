"""Plot GOEA simulation results."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pkggosim.common.plot_results import PlotInfo, get_tiled_axes, get_dftbl_boxplot
from pkggosim.common.plot_results import tiled_xyticklabels_off, fill_axes


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

def plt_box_all(fimg_pat, key2exps, **args_kws):
    """Plot all boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    objplt = PlotInfo(args_kws)
    kws = objplt.kws
    title_pat = "{P:}% True Null"
    for perc_null, expsets in key2exps.items():
        assert expsets
        kws['fout_img'] = fimg_pat.format(PERCNULL=perc_null)
        kws['title'] = title_pat.format(P=perc_null)
        dfrm = pd.DataFrame(get_dftbl_boxplot(expsets, objplt.attrname, objplt.grpname))
        _wrpng_boxplot_sigs_each(dfrm, expsets[0].pobj.objbase.alpha, **kws)

def plt_box_tiled(fout_img, key2exps, **args_kws):
    """Plot all detailed boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    objplt = PlotInfo(args_kws)
    kws = objplt.kws
    num_rows, num_cols = len(key2exps)/2, 2
    plt.close('all')
    sns.set(style="ticks")
    fig = plt.figure()
    axes_2d = get_tiled_axes(fig, num_rows, num_cols)
    #### sorted_dat = sorted(key2exps.items(), key=lambda t: [-1*t[0][0], t[0][1]]) # perc_null, max_sig
    sorted_dat = sorted(key2exps.items(), key=lambda t: -1*t[0]) # perc_null
    for idx, tile_items in enumerate(zip(axes_2d, sorted_dat)):
        #plt.subplots_adjust(hspace=.1, wspace=.1, left=.18, bottom=.2, top=.92)
        #plt.subplots_adjust(hspace=.17, wspace=.1, left=.15, bottom=.15, top=.87)
        plt.subplots_adjust(hspace=.17, wspace=.1, left=.15, bottom=.15, top=.87)
        _plt_tile(idx, num_rows, num_cols, tile_items, objplt)
    tiled_xyticklabels_off(axes_2d, num_cols)
    xysz = kws['txtsz_xy']
    fig.text(0.5, 0.96, kws['title'], size=kws['txtsz_title'], ha='center', va='center')
    fig.text(0.5, 0.06, kws['xlabel'], size=xysz, ha='center', va='center')
    fig.text(0.06, 0.5, kws['ylabel'], size=xysz, ha='center', va='center', rotation='vertical')
    plt.savefig(fout_img, dpi=kws.get('dpi', 200))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    if kws.get('show', False):
        plt.show()

def _plt_tile(idx, num_rows, num_cols, tile_items, objplt):
    """Plot one tile of a multi-tiled plot."""
    kws = objplt.kws
    #### (axes, ((perc_null, maxsig), exps)) = tile_items
    (axes, (perc_null, exps)) = tile_items
    letter = "{C}{R}".format(R=idx/num_cols+1, C=chr(65+idx%num_cols))
    dfrm = pd.DataFrame(get_dftbl_boxplot(exps, kws['attrname'], objplt.grpname))
    alpha = exps[0].pobj.objbase.alpha if objplt.get_val('alphaline') else None
    fill_axes(axes, dfrm, alpha, dotsize=kws['dotsize'],
              plottype=objplt.get_val('plottype'), letter=letter, ylim=objplt.get_val('ylim'))
    axes.set_xticklabels([e.params['num_items'] for e in exps], size=kws['txtsz_ticks'])
    axes.set_yticks(objplt.get_val('yticks'))
    axes.set_yticklabels(objplt.get_val('yticklabels'))
    #### if idx >= num_cols*(num_rows-1): # bottom_row
    ####     axes.set_xlabel("Sig.<={MAXSIG}".format(MAXSIG=maxsig), size=kws['txtsz_tile'])
    axes.set_title("{PERCNULL}% Null".format(PERCNULL=perc_null), size=kws['txtsz_tile'])
    axes.set_ylim(objplt.get_val('ylim'))
    axes.tick_params('both', length=3, width=1) # Shorten both x and y axes tick length
    # Add value text above plot bars to make plot easier to read
    for ntval in objplt.get_str_mean(exps):
        axes.text(ntval.x, ntval.y, ntval.valstr, ha='center', va='bottom')


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
