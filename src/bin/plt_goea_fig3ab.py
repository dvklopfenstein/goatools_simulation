#!/usr/bin/env python
"""Simulate Gene Ontology Enrichment Analyses."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkggosim.goea.fig_tiled import FigTiled


def main(show):
    """Two-tiled simulation plot show typical user-experienve w/propagate_counts=T/F."""
    fout_img = "fig2.all"
    data = [
        "pkggosim.data.orig_noprune_enriched_ntn2_p0_100to000_004to124_N00020_00020_genes",
        "pkggosim.data.orig_noprune_enriched_ntn2_p1_100to000_004to124_N00020_00020_genes",
    ]
    fig = FigTiled(data)
    fig.plt_twotiled(fout_img, dpi=600, show=show)


if __name__:
    main(len(sys.argv) != 1)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
