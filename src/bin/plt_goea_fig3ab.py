#!/usr/bin/env python
"""Simulate Gene Ontology Enrichment Analyses."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkggosim.goea.fig_tiled import FigTiled


def main(show):
    """Two-tiled simulation plot show typical user-experienve w/propagate_counts=T/F."""
    fout_img = "fig3.all"
    dpi = 600
    data = [
        "pkggosim.data.orig_noprune_enriched_ntn2_p0_100to000_004to124_N00020_00020_genes",
        "pkggosim.data.orig_noprune_enriched_ntn2_p1_100to000_004to124_N00020_00020_genes",
    ]
    kws_plt = {
        'title': 'GOEAs recovering Humoral Response (HR) genes',
        'xlabel': 'Number of Genes in a Study Group',
        'ylabel': 'Percentage of General Population Genes',
        'dotsize': {'sensitivity': 3.0, 'specificity': 3.0, 'fdr_actual': 4.0}}
    fig = FigTiled(data)
    #fig.plt_twotiled(fout_img, dpi, show, **kws_plt)
    fig.plt_one("fig3a.all", dpi, show, **kws_plt)
    fig.plt_one("fig3b.all", dpi, show, **kws_plt)


if __name__:
    main(len(sys.argv) != 1)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.