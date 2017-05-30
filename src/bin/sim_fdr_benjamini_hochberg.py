#!/usr/bin/env python
"""Explore False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import timeit
from pkggosim.hypotheses_run_all import ExperimentsAll
from pkggosim.utils import get_fout_img, get_hms

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

def main(randomseed):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    fout_log = "sim_fdr_benjamini_hochberg.log"
    num_reps = 100
    exp_params = {
        'seed' : randomseed,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals' : [0.01, 0.03, 0.05],
        'perc_nulls' : [100, 75, 50, 25],
        'num_hypoths_list' : None,
        'num_experiments' : num_reps, # 20, # aka Number of simulated FDR ratios in an experiment set
        'num_pvalsims' : num_reps} # 100}   # Number of sims used to create one FDR ratio
    rpt_items = ['fdr_actual', 'frr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    with open(fout_log, 'w') as prt:
        tic = timeit.default_timer()
        for num_hypoths_list in [[32, 128, 512], [4, 8, 16]]:
            for key, val in exp_params.items():
                prt.write("{KEY:16} {VAL}\n".format(KEY=key, VAL=val))
            exp_params['num_hypoths_list'] = num_hypoths_list
            obj = ExperimentsAll(exp_params)
            obj.prt_experiments_stats(prt, ['fdr_actual'])
            obj.prt_experiments_means(prt, rpt_items)
            obj.plt_box_all("sim_{PSIMATTR}_{PERCNULL:03}_{SIGMAX:02}.png", 'fdr_actual', 'FDR')
            # sim_fdr_LgHypoth__100to025_01to05.png
            fout_img = os.path.join(REPO, "doc/md/images", _get_fout_img('sim_fdr_LgHypoth_', exp_params))
            obj.plt_box_tiled(fout_img, 'fdr_actual', 'FDR')
        obj.seed.prt(prt)
        prt.write("HMS: {HMS}\n".format(HMS=get_hms(tic)))
        sys.stdout.write("  WROTE: {LOG}\n".format(LOG=fout_log))

def _get_fout_img(prefix, exp_params):
    """Get the name of the png file for the tiled plot."""
    img_pat = "_".join(["{PRE}_".format(PRE=prefix), "{P0:03}to{PN:03}_{MAX0:02}to{MAXN:02}.png"])
    return get_fout_img(exp_params, img_pat)

if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
