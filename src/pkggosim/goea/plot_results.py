"""Plot GOEA simulation results."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pkggosim.common.plot_results import PlotInfo, get_dftbl_boxplot
from pkggosim.common.plot_results import fill_axes


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

def plt_box_all(fimg_pat, key2exps, attrname, **args_kws):
    """Plot all boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    objplt = PlotInfo(attrname, args_kws)
    kws = objplt.kws
    title_pat = "{P:}% True Null"
    for perc_null, expsets in key2exps.items():
        assert expsets
        kws['fout_img'] = fimg_pat.format(PERCNULL=perc_null)
        kws['title'] = title_pat.format(P=perc_null)
        dfrm = pd.DataFrame(get_dftbl_boxplot(expsets, attrname, objplt.grpname))
        _wrpng_boxplot_sigs_each(dfrm, expsets[0].pobj.objbase.alpha, **kws)

def plt_box_tiled(fout_img, key2exps, attrs, **args_kws):
    """Plot all detailed boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    pltobjs = [PlotInfo(a, args_kws) for a in attrs]
    num_rows = len(key2exps)
    num_cols = len(attrs)
    plt.close('all')
    sns.set(style="ticks")
    fig = plt.figure()
    axes_2d = _get_tiled_axes(fig, num_rows, num_cols)
    sorted_dat = sorted(key2exps.items(), key=lambda t: -1*t[0]) # sort by perc_null
    for row_idx in range(num_rows):
        perc_null, exps = sorted_dat[row_idx]
        for col_idx, pltobj in enumerate(pltobjs):
            _plt_tile(pltobj, {
                'axes':axes_2d[row_idx*num_cols + col_idx],
                'perc_null':perc_null,
                'exps':exps,
                'letter':"{C}{R}".format(R=row_idx+1, C=chr(65+col_idx)),
                'is_bottom_row':row_idx == num_rows-1,
                'is_left_column':col_idx%num_cols == 0})
            #plt.subplots_adjust(hspace=.1, wspace=.1, left=.18, bottom=.2, top=.92)
            #plt.subplots_adjust(hspace=.17, wspace=.1, left=.15, bottom=.15, top=.87)
            #plt.subplots_adjust(hspace=.17, wspace=.1, left=.15, bottom=.15, top=.87)
            plt.subplots_adjust(hspace=.10, wspace=.15, left=.18, bottom=.19, top=.92)
    _tiled_xyticklabels_off(axes_2d, num_cols)
    set_tiled_txt(fig, pltobjs[0])
    plt.savefig(fout_img, dpi=args_kws.get('dpi', 200))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    if args_kws.get('show', False):
        plt.show()

def _tiled_xyticklabels_off(axes, num_cols):
    """Turn off xticklabels and yticklabels on the inside plot edges of the tiled boxplots."""
    for xaxis in axes[:-1*num_cols]:
        for label in xaxis.get_xticklabels():
            label.set_visible(False)
    # for idx, yaxis in enumerate(axes):
    #     if idx%num_cols != 0:
    #         for label in yaxis.get_yticklabels():
    #             label.set_visible(False)

def _get_tiled_axes(fig, n_rows, n_cols):
    """Create empty axes to be filled and used in tiled boxplot image."""
    ax1 = fig.add_subplot(n_rows, n_cols, 1)
    rng = range(2, n_rows*n_cols+1)
    return [ax1] + [fig.add_subplot(n_rows, n_cols, i, sharex=ax1, sharey=ax1) for i in rng]

def set_tiled_txt(fig, pltobj):
    """Add text around edges of plot."""
    kws = pltobj.kws
    xysz = kws['txtsz_xy']
    fig.text(0.5, 0.96, kws['title'], size=kws['txtsz_title'], ha='center', va='center')
    fig.text(0.5, 0.06, kws['xlabel'], size=xysz, ha='center', va='center')
    fig.text(0.06, 0.5, kws['ylabel'], size=xysz, ha='center', va='center', rotation='vertical')

def _plt_tile(pltobj, pvars):
    """Plot one tile of a multi-tiled plot."""
    axes = pvars['axes']
    exps = pvars['exps']
    kws = pltobj.kws
    dfrm = pd.DataFrame(get_dftbl_boxplot(exps, pltobj.attrname, pltobj.grpname))
    alpha = exps[0].pobj.objbase.alpha if kws['alphaline'] else None
    fill_axes(axes, dfrm, alpha, dotsize=kws['dotsize'],
              plottype=kws['plottype'], letter=pvars['letter'], ylim=kws['ylim'])
    axes.set_xticklabels([e.params['num_items'] for e in exps], size=kws['txtsz_ticks'])
    axes.set_yticks(kws['yticks'])
    axes.set_yticklabels(kws['yticklabels'])
    axes.set_ylim(kws['ylim'])
    axes.tick_params('both', length=3, width=1) # Shorten both x and y axes tick length
    # Add value text above plot bars to make plot easier to read
    for ntval in pltobj.get_str_mean(exps):
        axes.text(ntval.x, ntval.y, ntval.valstr, ha='center', va='bottom')
    if pvars['is_bottom_row']:
        axes.set_xlabel("{COLHDR}".format(COLHDR=pltobj.grpname), size=kws['txtsz_tile'])
    if pvars['is_left_column']:
        axes.set_ylabel("{PERCNULL}% Null".format(
            PERCNULL=pvars['perc_null']), size=kws['txtsz_tile'])

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
