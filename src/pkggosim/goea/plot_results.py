"""Plot GOEA simulation results."""

from __future__ import print_function

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import collections as cx
import seaborn as sns
import numpy as np
# import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas as pd
#### from pkggosim.common.plot_results import get_dftbl_boxplot
from pkggosim.common.plot_results import PlotInfo
from pkggosim.common.plot_results import BarText
from pkggosim.common.plot_results import fill_axes
from pkggosim.common.plot_results import fill_axes_data


def plt_box_tiled(base_img, key2exps, attrs, genes_goids, **kws):
    """Plot all detailed boxplots for all experiments. X->'# study genes', Y->FDR or %"""
    # KEYS:  [100, 75, 50, 25, 0]
    # ATTRS: ['fdr_actual', 'sensitivity', 'specificity']
    # pylint: disable=too-many-locals
    plt.close('all')
    sns.set(style="ticks")
    dpi = kws.get('dpi', 600)
    # fig = plt.figure(figsize=(8.0, 5.5), dpi=dpi)
    fig = plt.figure(dpi=dpi)
    outergrid = gridspec.GridSpec(1, 1)
    percnull2expsets = _get_percnull2expsets(key2exps, genes_goids)
    # kws -> 'title': 'GOEAs recovering Humoral Response (HR) genes'
    # kws -> 'xlabel': 'Number of Genes in a Study Group'
    # kws -> 'ylabel': 'Percentage of General Population Genes'
    # kws -> 'dotsize': {'sensitivity': 3.0, 'specificity': 3.0, 'fdr_actual': 4.0}
    pltobjs = [PlotInfo(a, kws) for a in attrs]
    # kws -> 'img': 'all'
    # kws -> 'dpi': 600
    runparams = next(iter(key2exps.items()))[1][0].pobj.params  # ExperimentSet's RunParams params
    _plt_box_tiled(fig, outergrid[0], percnull2expsets, pltobjs, genes_goids, runparams)
    #plt.tight_layout()
    base_img = "{BASE}_dpi{DPI}".format(BASE=base_img, DPI=dpi)
    _savefig(base_img, kws['img'], dpi, kws.get('show', False))

def _get_percnull2expsets(key2exps, genes_goids):
    """Convert key2exps containing classes to percnull2expsets containing namedtuples."""
    percnull_expsets = []
    for percnull, experimentsets in key2exps.items():
        for experimentset in experimentsets:
            num_items = experimentset.params['num_items']
            # mgs => ManyGoeaSims
            nts_tfpn_list = [mgs.nts_tfpn[genes_goids] for mgs in experimentset.expset]
            key_nts = ((percnull, num_items), nts_tfpn_list)
            percnull_expsets.append(key_nts)
    return cx.OrderedDict(percnull_expsets)

def _plt_box_tiled(fig, outergrid, percnull2expsets, pltobjs, genes_goids, runparams):
    """Plot all detailed boxplots for all experiments. X->(maxsigval, #pvals), Y->%sig"""
    num_rows = len(runparams['perc_nulls'])  # 100% Null, 75% Null, 50% Null, 25% Null, 0% Null
    num_cols = len(pltobjs)     # FDR Sensitivity Specificity
    num_genes_list = runparams['num_genes_list']
    rot_xtick = num_genes_list > 8
    # GridSpec for a single figure
    figgrid = _get_gridspecs(outergrid, num_rows, num_cols, rot_xtick)
    # axes returned in 'reading order': left-to-right and top-to-bottom
    # R0/C0 R0/C1 R0/C2 R1/C0 R1/C1 R1/C2 R2/C0 R2/C1 R2/C2 R3/C0 R3/C1 R3/C2 R4/C0 R4/C1 R4/C2
    axes_all = _get_tiled_axes(fig, figgrid, num_rows, num_cols)
    #### sorted_dat = sorted(key2exps.items(), key=lambda t: -1*t[0]) # sort by perc_null
    #### print("SSSSS", sorted_dat)
    #### for row_idx in range(num_rows):
    for row_idx, perc_null in enumerate(sorted(runparams['perc_nulls'], reverse=True)):
        #### perc_null, exps = sorted_dat[row_idx]
        for col_idx, pltobj in enumerate(pltobjs):
            #### exps = [percnull2expsets[(perc_null, ng)] for ng in num_genes_list]
            _plt_tile_barorboxplot(pltobj, {
                'axes':axes_all[row_idx*num_cols + col_idx],
                'alpha':runparams['alpha'],
                'perc_null':perc_null,
                'num_genes_list':num_genes_list,
                #### 'exps':exps,
                'percnull2expsets':percnull2expsets,
                'letter':"{C}{R}".format(R=row_idx+1, C=chr(65+col_idx)),
                'is_bottom_row':row_idx == num_rows-1,
                'is_left_column':col_idx%num_cols == 0,
                'genes_goids':genes_goids})
            plt.subplots_adjust(hspace=.10, wspace=.15, left=.18, bottom=.19, top=.92)
    _tiled_xyticklabels_off(axes_all, num_cols, rot_xtick)
    _set_tiled_txt(fig, pltobjs[0], genes_goids)

def _savefig(img_base, img_ext, dpi, show):
    """Save figure in various formats."""
    img_exts = ['tiff', 'jpg', 'png', 'pdf'] if img_ext == 'all' else [img_ext]
    for ext in img_exts:
        fout_img = "{IMG}.{EXT}".format(IMG=img_base, EXT=ext)
        plt.savefig(fout_img, dpi=dpi)
        sys.stdout.write("  DPI={DPI} WROTE: {IMG}\n".format(DPI=dpi, IMG=fout_img))
    if show:
        plt.show()

def savefig(fout_img, dpi, show):
    """Save figure in various formats."""
    base, ext = os.path.splitext(fout_img)
    _savefig(base, ext[1:], dpi, show)

#### def _get_rot_xticklabels(key2exps):
####     """Rotate xticklabels if there are a large number of gene sets."""
####     print("VVVVVV", next(iter(key2exps.items()))[1][0])
####     #num_genes_list = set([nt.num_items for nt in next(iter(key2exps.items()))[1]])
####     runparams = next(iter(key2exps.items()))[1][0].pobj.params  # ExperimentSet's RunParams params
####     num_genes_list = runparams['num_genes_list']
####     return len(num_genes_list) > 8 # Ex: 2 = len([4, 8])

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
    #### ax_c0 = fig.add_subplot(gs_c0[0, 0])  # Row 0, col 0 of GridSpec(4, 1)
    #### ax_cn = fig.add_subplot(gs_cn[0, 0])  # Row 0, col 0 of GridSpec(4, 3)
    ax_c0 = plt.Subplot(fig, (gs_c0[0, 0]))  # Row 0, col 0 of GridSpec(4, 1)
    ax_cn = plt.Subplot(fig, (gs_cn[0, 0]))  # Row 0, col 0 of GridSpec(4, 3)
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

def _plt_tile_barorboxplot(pltobj, pvars):
    """Plot one tile of a multi-tiled plot."""
    axes = pvars['axes']
    #### exps = pvars['exps']
    perc_null = pvars['perc_null']
    num_genes_list = pvars['num_genes_list']
    percnull2expsets = pvars['percnull2expsets']
    genes_goids = pvars['genes_goids']
    # qty = len(exps) # Number of gene sets in each tile. Ex: [4, 8, 16, 64] -> 4 sets
    kws = pltobj.kws
    #### dfrm = pd.DataFrame(get_dftbl_boxplot(exps, pltobj.attrname, pltobj.grpname, genes_goids))
    dfrm = pd.DataFrame(_get_dftbl_boxplot(percnull2expsets, perc_null, num_genes_list, pltobj.attrname, pltobj.grpname))
    # alpha = 0.05  # exps[0].pobj.objbase.alpha if kws['alphaline'] else None
    fill_axes_data(axes, dfrm, dotsize=kws['dotsize'], plottype=kws['plottype'])
    #### fill_axes(axes, alpha, letter=pvars['letter'], ylim=kws['ylim'])
    fill_axes(axes, pvars['alpha'], letter=pvars['letter'], ylim=kws['ylim'])
    #### axes.set_xticklabels([e.params['num_items'] for e in exps], size=kws['txtsz_ticks'])
    axes.set_xticklabels(num_genes_list, size=kws['txtsz_ticks'])
    axes.set_yticks(kws['yticks'])
    axes.set_yticklabels(kws['yticklabels'])
    axes.set_ylim(kws['ylim'])
    axes.tick_params('both', length=3, width=1) # Shorten both x and y axes tick length
    mean_2d = _get_mean_2d(percnull2expsets, perc_null, num_genes_list, pltobj.attrname)
    _add_text(axes, mean_2d, kws['plottype'], (pltobj.attrname, genes_goids))
    if pvars['is_bottom_row']:
        axes.set_xlabel("{COLHDR}".format(COLHDR=pltobj.grpname), size=17)
    if pvars['is_left_column']:
        axes.set_ylabel("{PERCNULL}% Null".format(PERCNULL=perc_null), size=kws['txtsz_tile'])

def _get_dftbl_boxplot(percnull2expsets, perc_null, num_genes_list, attr='fdr_actual', label='FDR'):
    """Get plotting data suitable for a single plot of boxplots."""
    # attr        |label
    # ------------|------------
    # fdr_actual  |FDR
    # sensitivity |Sensitivity
    # specificity |Specificity
    tbl = []
    for num_genes in num_genes_list:
        nts_tfpn_list = percnull2expsets[(perc_null, num_genes)]
        for nts_tfpn in nts_tfpn_list:
            mean = np.mean([getattr(nt, attr) for nt in nts_tfpn])
            tbl.append({'xval':num_genes, 'yval':mean, 'group':label})
    return tbl

def _add_text(axes, mean_2d, plottype, attrs):
    """Add value text above plot bars and in failing boxplots to make plot easier to read."""
    siz = 12   # BAR HEIGHT TEXT.  if qty<=4 else 12.0*4.0/qty
    # exps: ManyHypothesesSims or ManyGoeaSims
    # attrs: [attrname(sensitivity|specificity), genes_goids]
    if plottype == 'barplot':
        #### means = [np.mean(exp.get_means(*attrs)) for exp in exps]
        means = [np.mean(means) for means in mean_2d]
        for ntval in BarText(means).get_bar_text():
            axes.text(ntval.x, ntval.y, ntval.valstr, ha='center', va='bottom', size=siz)
    # Print BOXPLOT MEDIAN VALUES for failing FDRs
    elif plottype == 'boxplot':
        #### medians = [np.median(exp.get_medians(*attrs)) for exp in exps]
        medians = [np.median(means) for means in mean_2d]
        for xval, fdr_median in enumerate(medians):
            if fdr_median > 0.080:
                axes.text(xval, 0.037, "{V:5.03f}".format(V=fdr_median),
                          ha='center', va='center', size=siz, rotation=90, color='red')

#### def _get_mean_or_median(mean_or_median, percnull2expsets, perc_null, num_genes_list, attr):
def _get_mean_2d(percnull2expsets, perc_null, num_genes_list, attr):
    """Get plotting data suitable for a single plot of boxplots."""
    vals = []
    for num_genes in num_genes_list:
        mean_2d = []
        for nts_tfpn in percnull2expsets[(perc_null, num_genes)]:
            mean_vals = np.mean([getattr(nt, attr) for nt in nts_tfpn])
            mean_2d.append(mean_vals)
        vals.append(mean_2d)
    return vals

def _get_gridspecs(outergrid, num_rows, num_cols, rot_xticklabels):
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
    gspecs = [
        # FDR
        gridspec.GridSpecFromSubplotSpec(
            num_rows, 1,
            subplot_spec=outergrid,
            hspace=.10, wspace=wspc),  # , left=left, right=c0_r, bottom=bottom, top=.92),
        # Sensitivity, Specificity
        gridspec.GridSpecFromSubplotSpec(
            num_rows, num_cols-1,
            subplot_spec=outergrid,
            hspace=.10, wspace=wspc),  # , left=cn_l, right=cn_r, bottom=bottom, top=.92),
    ]
    #### Add enough space between Boxplots and barplots to add bar yticklabels
    #### gspecs[0].update(hspace=.10, wspace=wspc, left=left, right=c0_r, bottom=bottom, top=.92)
    #### gspecs[1].update(hspace=.10, wspace=wspc, left=cn_l, right=cn_r, bottom=bottom, top=.92)
    return gspecs

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
