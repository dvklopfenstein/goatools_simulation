"""Read simulation data. Plot in a two-tiled plot."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import importlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from pkggosim.goea.plot_results import savefig


class FigTiled(object):
    """Read simulation data. Plot in a two-tiled plot."""

    def __init__(self, modulestrs):
        # key2val(alpha, perc_nulls, num_genes_list, propagate_counts), percnull2expsets
        self.mods = [importlib.import_module(m) for m in modulestrs]

    def plt_twotiled(self, fout_img, dpi, show):
        """Plot two simulation images in one figure."""
        fig = plt.figure(dpi=dpi)
        gspec = gridspec.GridSpec(2, 1)
        axes_top = plt.subplot(gspec[0])
        axes_bot = plt.subplot(gspec[1])
        savefig(fout_img, dpi, show)
        sys.stdout.write("      WROTE: {IMG}\n".format(IMG=fout_img))


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
