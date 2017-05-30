#!/usr/bin/env python
"""Explore False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
from pkggosim.hypotheses_run_all import ExperimentsAll
from pkggosim.utils import get_fout_img

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

def main(randomseed, prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    exp_params = {
        'seed' : randomseed,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals' : [0.01, 0.03, 0.05],
        #perc_sigs' : [75, 50, 25, 0], # [25, 50, 75, 100]
        'perc_sigs' : [0, 25, 50, 75], # [25, 50, 75, 100]
        'num_hypoths_list' : [32, 128, 512],
        'num_experiments' : 20,
        'num_pvalsims' : 100}
    obj = ExperimentsAll(exp_params)
    obj.prt_experiments_stats(prt, ['fdr_actual'])
    obj.prt_experiments_means(prt, ['fdr_actual', 'frr_actual', 'sensitivity', 'specificity'])
    obj.plt_box_all("sim_{PSIMATTR}_{SIGPERC:03}_{SIGMAX:02}.png", 'fdr_actual', 'FDR')
    # sim_fdr_LgHypoth__100to025_01to05.png
    fout_img = os.path.join(REPO, "doc/md/images", _get_fout_img('sim_fdr_LgHypoth_', exp_params))
    obj.plt_box_tiled(fout_img, 'fdr_actual', 'FDR')
    # Re-run with a smaller number of hypotheses: [32, 128, 512] -> [4, 8, 16]
    exp_params['num_hypoths_list'] = [4, 8, 16]
    obj = ExperimentsAll(exp_params)
    # sim_fdr_SmHypoth_100to025_01to05.png
    fout_img = os.path.join(REPO, "doc/md/images", _get_fout_img('sim_fdr_SmHypoth', exp_params))
    obj.plt_box_tiled(fout_img, 'fdr_actual', 'FDR')
    obj.seed.prt(prt)

def _get_fout_img(prefix, exp_params):
    """Get the name of the png file for the tiled plot."""
    img_pat = "_".join(["{PRE}_".format(PRE=prefix), "{P0:03}to{PN:03}_{MAX0:02}to{MAXN:02}.png"])
    return get_fout_img(exp_params, img_pat)

if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
