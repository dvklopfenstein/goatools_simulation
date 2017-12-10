"""Read simulation data. Plot in a two-tiled plot."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import importlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

from pkggosim.common.plot_results import PlotInfo
from pkggosim.goea.plot_results import savefig
from pkggosim.goea.plot_results import _plt_box_tiled


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
        sns.set(style="ticks")

    def plt_twotiled(self, fout_img, dpi, show, **kws):
        """Plot two simulation images in one figure."""
        fig = plt.figure(dpi=dpi)
        gspec = gridspec.GridSpec(2, 1)
        axes_top = plt.subplot(gspec[0])
        axes_bot = plt.subplot(gspec[1])
        savefig(fout_img, dpi, show)
        sys.stdout.write("      WROTE: {IMG}\n".format(IMG=fout_img))

    def plt_one(self, fout_img, mod_idx, dpi, show, **kws):
        """Plot two simulation images in one figure."""
        plt.close('all')
        fig = plt.figure(dpi=dpi)
        mod = self.mods[mod_idx]
        key2exps = self.get_key2exps(mod)
        pltobjs = [PlotInfo(a, kws) for a in self.attrs]
        runparams = mod.key2val
        _plt_box_tiled(fig, key2exps, pltobjs, 'goids', runparams)
        savefig(fout_img, dpi, show)
        sys.stdout.write("      WROTE: {IMG}\n".format(IMG=fout_img))
        # plt_box_tiled(os.path.basename(fout_img), key2exps, attrs, genes_goids, **kws):

    def get_key2exps(self, mod):
        """Get key2exps for plotting."""
        key2exps = {}
        for perc_null in mod.key2val['perc_nulls']:
            experimentset = []
            for num_genes in mod.key2val['num_genes_list']:
               print "perc_null({}) num_genes({})".format(perc_null, num_genes)
               manygoeasims = mod.percnull2expsets[(perc_null, num_genes)]
               experimentset.append(manygoeasims)
            key2exps[perc_null] = experimentset
        return key2exps

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
