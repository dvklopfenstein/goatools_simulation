#!/usr/bin/env python
"""Simulate Gene Ontology Enrichment Analyses."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkggosim.goea.fig_tiled import FigTiled


def main(show):
    """Two-tiled simulation plot show typical user-experienve w/propagate_counts=T/F."""
    dpi = 600
    data = [
        "pkggosim.data.orig_noprune_enriched_ntn2_p0_100to000_004to124_N00020_00020_genes",
        "pkggosim.data.orig_noprune_enriched_ntn2_p1_100to000_004to124_N00020_00020_genes",
    ]
    kws_plt = {
        'titles': [
            'GOEAs recovering Humoral Response (HR) genes',
            'GOEAs recovering HR genes; propagate_counts=True'],
        'xlabel': 'Number of Genes in a Study Group',
        'ylabel': 'Percentage of General Population Genes',
        'dotsize': {'sensitivity': 2.0, 'specificity': 2.0, 'fdr_actual': 2.0}}
    figobj = FigTiled(data)
    figobj.plt_twotiled("fig3.all", dpi, show, **kws_plt)
    kws_plt['title'] = "GOEAs recovering Humoral Response (HR) genes"
    figobj.plt_one("fig3a.all", 0, dpi, show, **kws_plt)
    kws_plt['title'] = "GOEAs recovering HR genes; propagate_counts=True"
    figobj.plt_one("fig3b.all", 1, dpi, show, **kws_plt)


if __name__:
    main(len(sys.argv) != 1)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
