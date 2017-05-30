#!/usr/bin/env python
"""Create GOATOOLS supplemental figure: simulated FDR tiled plot."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
from pkggosim.hypotheses_run_all import ExperimentsAll
from pkggosim.utils import get_fout_img

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

def main(randomseed, log_pat="plt_fdr_benjamini_hochberg_{EXP}.log"):
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
    fout_log = log_pat.format(EXP=exp_params['num_experiments'])
    # Run Hypotheses Simulation
    obj = ExperimentsAll(exp_params)
    img_pat = 'suppl_hypoth_fdr_{P0:03}to{PN:03}_{MAX0:02}to{MAXN:02}_{Q0:03}to{QN:03}_N{NEXP:05}.png'
    # Report and plot simulation results
    with open(fout_log, 'w') as prt:
        obj.prt_params(prt)
        obj.seed.prt(prt)
        obj.prt_experiments_stats(prt, rpt_items)
        obj.prt_experiments_means(prt, rpt_items)
        fout_img = os.path.join(REPO, "doc/md/images", get_fout_img(exp_params, img_pat))
        obj.plt_box_tiled(fout_img, 'fdr_actual', 'FDR')
        sys.stdout.write("  WROTE: {LOG}\n".format(LOG=fout_log))

if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
