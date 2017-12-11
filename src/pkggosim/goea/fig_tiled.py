"""Read simulation data. Plot TWO SETS of simulations."""

from __future__ import print_function

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import importlib
# import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

from pkggosim.common.plot_results import PlotInfo
from pkggosim.goea.plot_results import savefig
from pkggosim.goea.plot_results import get_axes_1plot
from pkggosim.goea.plot_results import plt1_axes_tiled
from pkggosim.goea.plot_results import add_figtext1
from pkggosim.goea.plot_results import get_tiled_axes1
from pkggosim.goea.plot_results import get_left_right


class FigTiled(object):
    """Read simulation data. Plot in a two-tiled plot."""

    attrs = ['fdr_actual', 'sensitivity', 'specificity']

    # kws -> 'title': 'GOEAs recovering Humoral Response (HR) genes'
    # kws -> 'xlabel': 'Number of Genes in a Study Group'
    # kws -> 'ylabel': 'Percentage of General Population Genes'
    # kws -> 'dotsize': {'sensitivity': 3.0, 'specificity': 3.0, 'fdr_actual': 4.0}
    # kws -> 'img': 'all'
    # kws -> 'dpi': 600

    def __init__(self, modulestrs):
        # key2val(alpha, perc_nulls, num_genes_list, propagate_counts), percnull2expsets
        self.mods = [importlib.import_module(m) for m in modulestrs]
        self.genes_goids = [m[-5:] for m in modulestrs]
        sns.set(style="ticks")

    def plt_twotiled(self, fout_img, dpi, show, **kws):
        """Plot two simulation images in one figure."""
        plt.close('all')
        fig = plt.figure(figsize=(8.00, 11.00), dpi=dpi)
        print("FIGSIZE({})".format(fig.get_size_inches()))
        pltobjs = [PlotInfo(a, kws) for a in self.attrs]

        axes = self._get_tiled_axes2(pltobjs, fig)
        for idx, mod in enumerate(self.mods):
            runparams = self.mods[idx].key2val
            plt1_axes_tiled(axes[idx], mod.percnull2expsets, pltobjs, self.genes_goids[idx], runparams)
        # plt1_axes_tiled(axes_top, self.mods[0].percnull2expsets, pltobjs, self.genes_goids[0], runparams)
        # plt1_axes_tiled(axes_bot, self.mods[1].percnull2expsets, pltobjs, self.genes_goids[1], runparams)
        self._add_figtext2(fig, pltobjs[0].kws)

        savefig(fout_img, dpi, show)
        sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))


    def plt_one(self, fout_img, mod_idx, dpi, show, **kws):
        """Plot two simulation images in one figure."""
        plt.close('all')
        fig = plt.figure(dpi=dpi)
        print("FIGSIZE({})".format(fig.get_size_inches()))
        mod = self.mods[mod_idx]
        pltobjs = [PlotInfo(a, kws) for a in self.attrs]
        runparams = mod.key2val

        axes_1plot = get_axes_1plot(fig, pltobjs, runparams)
        plt1_axes_tiled(axes_1plot, mod.percnull2expsets, pltobjs, self.genes_goids[mod_idx], runparams)
        add_figtext1(fig, pltobjs[0], self.genes_goids[mod_idx])

        savefig(fout_img, dpi, show)
        sys.stdout.write("  WROTE: {IMG}\n".format(IMG=fout_img))


    def _add_figtext2(self, fig, kws):
        """Add text around edges of plot."""
        xysz = kws['txtsz_xy']
        # Simulations in this repo were done from the perspective of genes recovered.
        # However, the simulations also contain GO ID recovery in the same simulation.
        # Both gene and GO ID recovery are plotted using the same title.
        # But for the GO ID recovery plots, replace 'gene' in the title with 'GO ID'
        titles = kws['titles']
        for idx, genes_goids in enumerate(self.genes_goids):
            if genes_goids == 'goids':
                titles[idx] = titles[idx].replace('genes', 'GO IDs')
        # title:
        fig.text(0.50, 0.97, titles[0], size=kws['txtsz_title'], ha='center', va='bottom')
        fig.text(0.50, 0.47, titles[1], size=kws['txtsz_title'], ha='center', va='bottom')
        # xlabel: Number of Genes in a Study Group
        fig.text(0.50, 0.52, kws['xlabel'], size=xysz, ha='center', va='top')
        fig.text(0.50, 0.02, kws['xlabel'], size=xysz, ha='center', va='top')
        # ylabel: Percentage of General Population Genes
        fig.text(0.02, 0.75, kws['ylabel'], size=xysz, ha='center', va='center', rotation='vertical')
        fig.text(0.02, 0.25, kws['ylabel'], size=xysz, ha='center', va='center', rotation='vertical')

    def _get_tiled_axes2(self, pltobjs, fig):
        """Get TWO SETS of axes for TWO SETS of experiments."""
        rot_xticklabels = len(self.mods[0].key2val['num_genes_list']) > 8
        num_rows = len(self.mods[0].key2val['perc_nulls'])  # 100% Null, 75% Null, 50% Null, 25% Null, 0% Null
        num_cols = len(pltobjs)     # FDR Sensitivity Specificity
        gridspecs = self._get_gridspecs_2(num_rows, num_cols, rot_xticklabels)
        axes_top = get_tiled_axes1(fig, gridspecs[:2], num_rows, num_cols)
        axes_bot = get_tiled_axes1(fig, gridspecs[2:], num_rows, num_cols)
        return axes_top, axes_bot

    @staticmethod
    def _get_gridspecs_2(num_rows, num_cols, rot_xticklabels):
        """Get gridspecs for TWO SETS of experiments, adjusted to fit well into figure."""
        bottom = .09 if rot_xticklabels else .08
        wspc = .08
        xms = get_left_right(num_cols)
        # [GridSpec(Boxplot:FDR),   GridSpec(Barplots:Sensitivity, Specificity, ...)]
        #    gridspec.GridSpec(5, 1),  # FDR
        #    gridspec.GridSpec(5, 2),  # Sensitivity, Specificity
        gspecs = [
            # Top plot
            gridspec.GridSpec(num_rows, 1),  # FDR
            gridspec.GridSpec(num_rows, num_cols-1),  # Sensitivity, Specificity
            # Bottom plot
            gridspec.GridSpec(num_rows, 1),  # FDR
            gridspec.GridSpec(num_rows, num_cols-1),  # Sensitivity, Specificity
        ]
        # Add enough space between Boxplots and barplots to add bar yticklabels
        # Top plot
        gspecs[0].update(hspace=.10, wspace=wspc, left=xms[0], right=xms[1], bottom=bottom+0.50, top=.96)
        gspecs[1].update(hspace=.10, wspace=wspc, left=xms[2], right=xms[3], bottom=bottom+0.50, top=.96)
        # Bottom plot
        gspecs[2].update(hspace=.10, wspace=wspc, left=xms[0], right=xms[1], bottom=bottom, top=.46)
        gspecs[3].update(hspace=.10, wspace=wspc, left=xms[2], right=xms[3], bottom=bottom, top=.46)
        return gspecs


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
