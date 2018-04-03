#!/usr/bin/env python
"""Simulate a Gene Ontology Enrichment Analysis (GOEA) on one set of study genes."""
# TBD: REMOVE THIS TEST?

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkggosim.common.plot_results import BarText


def test_text_barheight(prt=sys.stdout):
    """Test ManyGoeaSims in ./src/pkggosim.goea.sims.py"""
    #pylint: disable=bad-whitespace
    means_lst = [
        ([.26, .30, .42, .42, .46, .50, .60, .67, .70],
         [     .30,      .42,      .50,      .67     ]),

        ([.72, .76, .80, .84, .87, .89, .90, .91, .92],
         [     .76,      .84,      .89,      .91,    ]),

        ([.88, .89, .90, .92, .93, .94, .94, .95, .95],
         [     .89,      .92,      .94,      .95,    ]),

        ([.94, .94, .95, .95, .96, .96, .97, .97, .99],
         [     .94,      .95,      .96,      .97,    ]),
    ]
    for means_orig, means_exp in means_lst:
        means_act = [nt.val for nt in BarText(means_orig).get_bar_text()]
        _prt(prt, "INI", means_orig)
        _prt(prt, "ACT", means_act)
        _prt(prt, "EXP", means_exp)
        prt.write("\n")
        assert means_act == means_exp, "ACTUAL DID NOT MATCH EXPECTED"

def _prt(prt, name, means):
    """Print means list."""
    txt = ["{NAME}({N}):".format(NAME=name, N=len(means))]
    txt.extend(["{:2.0f}".format(m*100) for m in means])
    prt.write("{TXT}\n".format(TXT="  ".join(txt)))


if __name__ == '__main__':
    test_text_barheight()

# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
