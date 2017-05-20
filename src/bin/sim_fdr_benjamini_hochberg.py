#!/usr/bin/env python
"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
#### from pkgsim.report_results import report_results_all
#### from pkgsim.plot_results import plot_results_all
from pkgsim.run_all_experiments import ExperimentsAll


def main(randomseed, prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    exp_params = {
        'seed' : randomseed,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals' : [0.01, 0.03, 0.05],
        'perc_sigs' : [0, 20, 60, 100],
        'pval_qtys' : [20, 100, 500],
        'num_experiments' : 10,
        'num_pvalsims' : 100}
    obj = ExperimentsAll(exp_params)
    attrs = ['fdr_actual']
    attrs = ["fdr_actual", "frr_actual"]
    attrs = ["fdr_actual", "frr_actual", "sensitivity"]
    #attrs = ["fdr_actual", "frr_actual", "num_Type_II"]
    obj.prt_summary(prt, attrs)
    obj.seed.prt(prt)


if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
