"""Plot GOEA simulation results."""

from __future__ import print_function

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas as pd
from pkggosim.common.plot_results import get_dftbl_boxplot
from pkggosim.common.plot_results import PlotInfo
from pkggosim.common.plot_results import BarText
from pkggosim.common.plot_results import fill_axes
from pkggosim.common.plot_results import fill_axes_data


#pylint: disable=line-too-long
def plt_box_tiled(base_img, key2exps, attrs, genes_goids, **args_kws):
    """Plot all detailed boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    # pylint: disable=too-many-locals
    pltobjs = [PlotInfo(a, args_kws) for a in attrs]
    num_rows = len(key2exps)  # 100% Null, 75% Null, 50% Null, 25% Null, 0% Null
    num_cols = len(attrs)     # FDR Sensitivity Specificity
    plt.close('all')
    sns.set(style="ticks")
    fig = plt.figure()
    rot_xtick = _get_rot_xticklabels(key2exps)
    axes_all = _get_tiled_axes(fig, get_gridspecs(num_rows, num_cols, rot_xtick), num_rows, num_cols)
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
    _tiled_xyticklabels_off(axes_all, num_cols, rot_xtick)
    _set_tiled_txt(fig, pltobjs[0], genes_goids)
    #plt.tight_layout()
    dpi = args_kws.get('dpi', 600)
    base_img = "{BASE}_dpi{DPI}".format(BASE=base_img, DPI=dpi)
    img_ext = args_kws['img']
    img_exts = ['tiff', 'jpg', 'png', 'pdf'] if img_ext == 'all' else [img_ext]
    for ext in img_exts:
        fout_img = "{IMG}.{EXT}".format(IMG=base_img, EXT=ext)
        plt.savefig(fout_img, dpi=dpi)
        sys.stdout.write("  DPI={DPI} WROTE: {IMG}\n".format(DPI=dpi, IMG=fout_img))
    if args_kws.get('show', False):
        plt.show()

def _get_rot_xticklabels(key2exps):
    """Rotate xticklabels if there are a large number of gene sets."""
    print("VVVVVV", next(iter(key2exps.items()))[1][0])
    #num_genes_list = set([nt.num_items for nt in next(iter(key2exps.items()))[1]])
    runparams = next(iter(key2exps.items()))[1][0].pobj.params  # ExperimentSet's RunParams params
    num_genes_list = runparams['num_genes_list']
    return len(num_genes_list) > 8 # Ex: 2 = len([4, 8])

def _set_tiled_txt(fig, pltobj, genes_goids):
    """Add text around edges of plot."""
    kws = pltobj.kws
    xysz = kws['txtsz_xy']
    # Simulations in this repo were done from the perspective of genes recovered.
    # However, the simulations also contain GO ID recovery in the same simulation.
    # Both gene and GO ID recovery are plotted using the same title.
    # But for the GO ID recovery plots, replace 'gene' in the title with 'GO ID'
    title = kws['title']
    if genes_goids == 'goids':
        title = title.replace('genes', 'GO IDs')
    fig.text(0.5, 0.97, title, size=kws['txtsz_title'], ha='center', va='center')
    fig.text(0.5, 0.02, kws['xlabel'], size=xysz, ha='center', va='center')
    fig.text(0.02, 0.5, kws['ylabel'], size=xysz, ha='center', va='center', rotation='vertical')

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

def _tiled_xyticklabels_off(axes, num_cols, rot_xtick):
    """Turn off xticklabels and yticklabels on the inside plot edges of the tiled boxplots."""
    # If there are many gene sets, rotate the gene size xtick labels
    for xaxis in axes:
        if rot_xtick:
            for label in xaxis.get_xmajorticklabels():
                label.set_rotation(90)
                # label.set_horizontalalignment("right")
    # Turn most xticklabels off except for bottom row
    for xaxis in axes[:-1*num_cols]:
        xticklabels = xaxis.get_xticklabels()
        for label in xticklabels:
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
    dfrm = pd.DataFrame(get_dftbl_boxplot(exps, pltobj.attrname, pltobj.grpname, genes_goids))
    alpha = exps[0].pobj.objbase.alpha if kws['alphaline'] else None
    fill_axes_data(axes, dfrm, dotsize=kws['dotsize'], plottype=kws['plottype'])
    fill_axes(axes, alpha, letter=pvars['letter'], ylim=kws['ylim'])
    axes.set_xticklabels([e.params['num_items'] for e in exps], size=kws['txtsz_ticks'])
    axes.set_yticks(kws['yticks'])
    axes.set_yticklabels(kws['yticklabels'])
    axes.set_ylim(kws['ylim'])
    axes.tick_params('both', length=3, width=1) # Shorten both x and y axes tick length
    _add_text(axes, exps, kws['plottype'], (pltobj.attrname, genes_goids))
    if pvars['is_bottom_row']:
        axes.set_xlabel("{COLHDR}".format(COLHDR=pltobj.grpname), size=17)
    if pvars['is_left_column']:
        axes.set_ylabel("{PERCNULL}% Null".format(
            PERCNULL=pvars['perc_null']), size=kws['txtsz_tile'])

def _add_text(axes, exps, plottype, attrs):
    """Add value text above plot bars and in failing boxplots to make plot easier to read."""
    siz = 12   # BAR HEIGHT TEXT.  if qty<=4 else 12.0*4.0/qty
    # exps: ManyHypothesesSims or ManyGoeaSims
    # attrs: [attrname(sensitivity|specificity), genes_goids]
    if plottype == 'barplot':
        means = [np.mean(exp.get_means(*attrs)) for exp in exps]
        for ntval in BarText(means).get_bar_text():
            axes.text(ntval.x, ntval.y, ntval.valstr, ha='center', va='bottom', size=siz)
    # Print BOXPLOT MEDIAN VALUES for failing FDRs
    elif plottype == 'boxplot':
        medians = [np.median(exp.get_medians(*attrs)) for exp in exps]
        for xval, fdr_median in enumerate(medians):
            if fdr_median > 0.080:
                axes.text(xval, 0.037, "{V:5.03f}".format(V=fdr_median),
                          ha='center', va='center', size=siz, rotation=90, color='red')

def get_gridspecs(num_rows, num_cols, rot_xticklabels):
    """Get gridspecs, adjusted to fit well into figure."""
    left = .14
    bottom = .18 if rot_xticklabels else .16
    margin = 0.07
    wspc = .08
    cn_r = 0.99
    col_wid = (cn_r - left - margin)/num_cols
    c0_r = left + col_wid
    cn_l = c0_r + margin
    # [GridSpec(Boxplot:FDR),   GridSpec(Barplots:Sensitivity, Specificity, ...)]
    gspecs = [gridspec.GridSpec(num_rows, 1), gridspec.GridSpec(num_rows, num_cols-1)]
    # Add enough space between Boxplots and barplots to add bar yticklabels
    gspecs[0].update(hspace=.10, wspace=wspc, left=left, right=c0_r, bottom=bottom, top=.92)
    gspecs[1].update(hspace=.10, wspace=wspc, left=cn_l, right=cn_r, bottom=bottom, top=.92)
    return gspecs

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
