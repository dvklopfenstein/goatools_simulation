"""Plot GOEA simulation results."""

from __future__ import print_function

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas as pd
from pkggosim.common.plot_results import PlotInfo, get_dftbl_boxplot
from pkggosim.common.plot_results import fill_axes


def plt_box_tiled(fout_img, key2exps, attrs, genes_goids, **args_kws):
    """Plot all detailed boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    # pylint: disable=too-many-locals
    pltobjs = [PlotInfo(a, args_kws) for a in attrs]
    num_rows = len(key2exps)
    num_cols = len(attrs)
    plt.close('all')
    sns.set(style="ticks")
    fig = plt.figure()
    axes_all = _get_tiled_axes(fig, get_gridspecs(num_rows, num_cols), num_rows, num_cols)
    sorted_dat = sorted(key2exps.items(), key=lambda t: -1*t[0]) # sort by perc_null
    for row_idx in range(num_rows):
        perc_null, exps = sorted_dat[row_idx]
        for col_idx, pltobj in enumerate(pltobjs):
            _plt_tile(pltobj, {
                'axes':axes_all[row_idx*num_cols + col_idx],
                'perc_null':perc_null,
                'exps':exps,
                'letter':"{C}{R}".format(R=row_idx+1, C=chr(65+col_idx)),
                'is_bottom_row':row_idx == num_rows-1,
                'is_left_column':col_idx%num_cols == 0}, genes_goids)
            plt.subplots_adjust(hspace=.10, wspace=.15, left=.18, bottom=.19, top=.92)
    _tiled_xyticklabels_off(axes_all, num_cols)
    _set_tiled_txt(fig, pltobjs[0])
    #plt.tight_layout()
    plt.savefig(fout_img, dpi=args_kws.get('dpi', 300))
    sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))
    if args_kws.get('show', False):
        plt.show()

def _get_tiled_axes(fig, gspecs, n_rows, n_cols):
    """Create empty axes to be filled and used in tiled boxplot image."""
    gs_c0 = gspecs[0]
    gs_cn = gspecs[1]
    ax_c0 = fig.add_subplot(gs_c0[0, 0])  # Row 0, col 0 of GridSpec(4, 1)
    ax_cn = fig.add_subplot(gs_cn[0, 0])  # Row 0, col 0 of GridSpec(4, 3)
    axes = [ax_c0, ax_cn]
    for idx in range(2, n_rows*n_cols):
        colidx = idx%n_cols
        if colidx == 0: # Append SubplotSpec object
            axes.append(fig.add_subplot(gs_c0[idx/n_cols, 0], sharex=ax_c0, sharey=ax_c0))
        else:
            axes.append(fig.add_subplot(gs_cn[idx/n_cols, colidx-1], sharex=ax_cn, sharey=ax_cn))
    return axes

def _tiled_xyticklabels_off(axes, num_cols):
    """Turn off xticklabels and yticklabels on the inside plot edges of the tiled boxplots."""
    for xaxis in axes[:-1*num_cols]:
        for label in xaxis.get_xticklabels():
            label.set_visible(False)
    for idx, yaxis in enumerate(axes):
        col_idx = idx%num_cols
        if col_idx > 1:
            for label in yaxis.get_yticklabels():
                label.set_visible(False)

def _plt_tile(pltobj, pvars, genes_goids):
    """Plot one tile of a multi-tiled plot."""
    axes = pvars['axes']
    exps = pvars['exps']
    # qty = len(exps) # Number of gene sets in each tile. Ex: [4, 8, 16, 64] -> 4 sets
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
    print("PVARS EXPS({})".format(exps))
    # Add value text above plot bars to make plot easier to read
    siz = 12   # BAR HEIGHT TEXT.  if qty<=4 else 12.0*4.0/qty
    for ntval in pltobj.get_str_mean(exps, genes_goids):
        axes.text(ntval.x, ntval.y, ntval.valstr, ha='center', va='bottom', size=siz)
    if pvars['is_bottom_row']:
        axes.set_xlabel("{COLHDR}".format(COLHDR=pltobj.grpname), size=17)
    if pvars['is_left_column']:
        axes.set_ylabel("{PERCNULL}% Null".format(
            PERCNULL=pvars['perc_null']), size=kws['txtsz_tile'])

def get_gridspecs(num_rows, num_cols):
    """Get gridspecs, adjusted to fit well into figure."""
    left = .14
    bottom = .16
    margin = 0.07
    wspc = .08
    cn_r = 0.99
    col_wid = (cn_r - left - margin)/num_cols
    c0_r = left + col_wid
    cn_l = c0_r + margin
    gspecs = [gridspec.GridSpec(num_rows, 1), gridspec.GridSpec(num_rows, num_cols-1)]
    gspecs[0].update(hspace=.10, wspace=wspc, left=left, right=c0_r, bottom=bottom, top=.92)
    gspecs[1].update(hspace=.10, wspace=wspc, left=cn_l, right=cn_r, bottom=bottom, top=.92)
    return gspecs

def _set_tiled_txt(fig, pltobj):
    """Add text around edges of plot."""
    kws = pltobj.kws
    xysz = kws['txtsz_xy']
    fig.text(0.5, 0.97, kws['title'], size=kws['txtsz_title'], ha='center', va='center')
    fig.text(0.5, 0.02, kws['xlabel'], size=xysz, ha='center', va='center')
    fig.text(0.02, 0.5, kws['ylabel'], size=xysz, ha='center', va='center', rotation='vertical')

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
