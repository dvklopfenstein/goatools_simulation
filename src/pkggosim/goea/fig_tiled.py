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

    def __init__(self, modulestrs, kws):
        # key2val(alpha, perc_nulls, num_genes_list, propagate_counts), percnull2expsets
        self.mods = [importlib.import_module(m) for m in modulestrs]
        self.kws = kws
        self.pltobjs = [PlotInfo(a, kws) for a in self.attrs]
        self.genes_goids = [m[-5:] for m in modulestrs]
        self.gs2 = self._init_gs2()
        sns.set(style="ticks")

    def _init_gs2(self):
        rot_xticklabels = len(self.mods[0].key2val['num_genes_list']) > 8
        num_rows = len(self.mods[0].key2val['perc_nulls'])  # 100% Null, 75% Null, 50% Null, 25% Null, 0% Null
        num_cols = len(self.pltobjs)     # FDR Sensitivity Specificity
        return TwoSets(num_rows, num_cols, rot_xticklabels)

    def plt_twotiled(self, fout_img, dpi, show):
        """Plot two simulation images in one figure."""
        plt.close('all')
        fig = plt.figure(figsize=(8.00, 11.00), dpi=dpi)
        print("FIGSIZE({})".format(fig.get_size_inches()))

        # axes = self._get_tiled_axes2(pltobjs, fig)
        axes = self.gs2.get_tiled_axes2(fig)
        for idx, mod in enumerate(self.mods):
            runparams = self.mods[idx].key2val
            plt1_axes_tiled(axes[idx], mod.percnull2expsets, self.pltobjs, self.genes_goids[idx], runparams)
        self.gs2.add_figtext2(fig, self.genes_goids, self.pltobjs[0].kws)

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


class TwoSets(object):
    """Holds layout information for TWO SETs of simululations."""

    def __init__(self, num_rows, num_cols, rot_xticklabels):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.rot_xticklabels = rot_xticklabels
        self.gspecs = self._init_gspecs()
        self.xms = get_left_right(num_cols)
        self.yms = self._init_top_bottom(rot_xticklabels)
        self._update_gspecs()

    def add_figtext2(self, fig, genes_goids_list, kws):
        """Add text around edges of plot."""
        xysz = kws['txtsz_xy']
        # Simulations in this repo were done from the perspective of genes recovered.
        # However, the simulations also contain GO ID recovery in the same simulation.
        # Both gene and GO ID recovery are plotted using the same title.
        # But for the GO ID recovery plots, replace 'gene' in the title with 'GO ID'
        titles = kws['titles']
        for idx, genes_goids in enumerate(genes_goids_list):
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

    def get_tiled_axes2(self, fig):
        """Get TWO SETS of axes for TWO SETS of experiments."""
        return [
            get_tiled_axes1(fig, self.gspecs[:2], self.num_rows, self.num_cols),  # top
            get_tiled_axes1(fig, self.gspecs[2:], self.num_rows, self.num_cols)]  # bottom

    def _update_gspecs(self):
        """Update the position of the TWO SETS of sim plots."""
        xms = self.xms
        yms = self.yms
        # Top plot
        self.gspecs[0].update(hspace=.10, wspace=.08, left=xms[0], right=xms[1], bottom=yms[2], top=yms[3])
        self.gspecs[1].update(hspace=.10, wspace=.08, left=xms[2], right=xms[3], bottom=yms[2], top=yms[3])
        # Bottom plot
        self.gspecs[2].update(hspace=.10, wspace=.08, left=xms[0], right=xms[1], bottom=yms[0], top=yms[1])
        self.gspecs[3].update(hspace=.10, wspace=.08, left=xms[2], right=xms[3], bottom=yms[0], top=yms[1])

    def _init_gspecs(self):
        return [
            # Top plot
            gridspec.GridSpec(self.num_rows, 1),  # FDR
            gridspec.GridSpec(self.num_rows, self.num_cols-1),  # Sensitivity, Specificity
            # Bottom plot
            gridspec.GridSpec(self.num_rows, 1),  # FDR
            gridspec.GridSpec(self.num_rows, self.num_cols-1),  # Sensitivity, Specificity
        ]

    @staticmethod
    def _init_top_bottom(rot_xticklabels):
        """Get the left-right values for two plots."""
        num_sets = 2.00
        bottom = .09 if rot_xticklabels else .08
        ymargin = 0.07 # margin between box/barplots
        y3_r = .04     # right margin
        row_hi = .50 - y3_r - bottom - ymargin/num_sets
        row_hi = (1.00 - num_sets*y3_r - num_sets*bottom - ymargin)/num_sets
        y1_r = bottom + row_hi
        y2_l = y1_r + y3_r + ymargin + bottom
        return [bottom, y1_r, y2_l, 1.00 - y3_r]



# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
