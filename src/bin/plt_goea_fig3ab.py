#!/usr/bin/env python
"""Simulate Gene Ontology Enrichment Analyses."""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkggosim.goea.fig_tiled import FigTiled


def main(show):
    """Two-tiled simulation plot show typical user-experienve w/propagate_counts=T/F."""
    _run('genes', show)
    _run('goids', show)

def _run(desc, show):
    """Two-tiled simulation plot show typical user-experienve w/propagate_counts=T/F."""
    dpi = 600
    data = [
        "pkggosim.data.orig_noprune_enriched_ntn2_p0_100to000_004to124_N00020_00020_{G}".format(G=desc),
        "pkggosim.data.orig_noprune_enriched_ntn2_p1_100to000_004to124_N00020_00020_{G}".format(G=desc),
    ]
    kws_plt = {
        'titles': [
            'A. GOEAs recovering Humoral Response (HR) {G}'.format(G=desc),
            'B. GOEAs recovering HR {G}; propagate_counts=True'.format(G=desc)],
        'xlabel': 'Number of Genes in a Study Group',
        'ylabel': 'Percentage of General Population Genes',
        'dotsize': {'sensitivity': 2.0, 'specificity': 2.0, 'fdr_actual': 2.0}}
    figobj = FigTiled(data, kws_plt)
    figobj.plt_twotiled("log/plt_goea_fig3ab/fig3_{G}.all".format(G=desc), dpi, show)
    kws_plt['title'] = "GOEAs recovering Humoral Response (HR) {G}".format(G=desc)
    figobj.plt_one("log/plt_goea_fig3ab/fig3a_{G}.all".format(G=desc), 0, dpi, show, **kws_plt)
    kws_plt['title'] = "GOEAs recovering HR {G}; propagate_counts=True".format(G=desc)
    figobj.plt_one("log/plt_goea_fig3ab/fig3b_{G}.all".format(G=desc), 1, dpi, show, **kws_plt)


if __name__:
    main(len(sys.argv) != 1)

# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
