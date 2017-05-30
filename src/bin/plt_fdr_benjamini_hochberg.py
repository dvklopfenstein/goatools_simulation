#!/usr/bin/env python
"""Create GOATOOLS supplemental figure: simulated FDR tiled plot."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
from pkggosim.hypotheses_run_all import ExperimentsAll
from pkggosim.utils import get_fout_img

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

def main(randomseed, prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    # User-configurable parameters
    exp_params = {
        'seed' : randomseed,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals' : [0.01, 0.03, 0.05],
        'perc_nulls' : [100, 75, 50, 25],
        'num_hypoths_list' : [4, 16, 128],
        'num_experiments' : 20, # aka Number of simulated FDR ratios in an experiment set
        'num_pvalsims' : 100}   # Number of sims used to create one FDR ratio
    rpt_items = ['fdr_actual', 'frr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    # Run Hypotheses Simulation
    obj = ExperimentsAll(exp_params)
    # Report and plot results
    obj.prt_experiments_stats(prt, ['fdr_actual'])
    obj.prt_experiments_means(prt, rpt_items)
    img_pat = 'suppl_hypoth_fdr_{P0:03}to{PN:03}_{MAX0:02}to{MAXN:02}.png'
    fout_img = os.path.join(REPO, "doc/md/images", get_fout_img(exp_params, img_pat))
    obj.plt_box_tiled(fout_img, 'fdr_actual', 'FDR')
    obj.seed.prt(prt)


if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
