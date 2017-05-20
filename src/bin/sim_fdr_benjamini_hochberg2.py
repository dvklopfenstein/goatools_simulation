#!/usr/bin/env python
"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
#### from pkgsim.report_results import report_results_all
#### from pkgsim.plot_results import plot_results_all
from pkgsim.pval_mtcorr_sims import PvalExperiment
from pkgsim.experiments_params import ExperimentsAll

def main(randomseed, prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    exp_params = {
        'seed' : randomseed,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals' : [0.01, 0.03, 0.05],
        'perc_sigs' : [0, 20, 60, 100],
        'pval_qtys' : [20, 100, 500],
        'num_experiments' : 10,
        'fnc_maxsig' : fnc_maxsig_pnnn,
        'num_pvalsims' : 100}
    obj = ExperimentsAll(exp_params)
    obj.seed.prt(prt)

# ----------------------------------------------------------------------------
# Functions for creating randomly-generated "Significant" P-values
#   1. fnc_maxsig_alpha_numpval generates extremely small P-values and varies by sim params
#   2. fnc_maxsig_pnnn generates small P-values and is constant across all sims
def fnc_maxsig_alpha_numpval(**kws):
    """P-values expected to be 'significant' are randomly generated and under alpha/num_pvals."""
    name = "alpha/#pvals"
    return kws['alpha']/kws['num_pvals']

# pylint: disable=unused-argument
def fnc_maxsig_pnnn(**kws):
    """P-values expected to be 'significant' are randomly generated and under value, N."""
    name = fnc_maxsig_pnnn.max_sig_pval
    return fnc_maxsig_pnnn.max_sig_pval

if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
