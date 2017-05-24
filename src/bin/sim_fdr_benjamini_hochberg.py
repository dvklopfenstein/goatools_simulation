#!/usr/bin/env python
"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkgsim.pval_run_all import ExperimentsAll


def main(randomseed, prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    exp_params = {
        'seed' : randomseed,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals' : [0.01, 0.03, 0.05],
        #perc_sigs' : [75, 50, 25, 0], # [25, 50, 75, 100]
        'perc_sigs' : [ 0, 25, 50, 75], # [25, 50, 75, 100]
        'num_hypoths_list' : [20, 100, 500],
        'num_experiments' : 20,
        'num_pvalsims' : 100}
    obj = ExperimentsAll(exp_params)
    obj.prt_experiments_stats(prt, ['fdr_actual'])
    obj.prt_experiments_means(prt, ['fdr_actual', 'frr_actual', 'sensitivity', 'specificity'])
    obj.plt_box_all("sim_{PSIMATTR}_{SIGPERC:03}_{SIGMAX:02}.png", 'fdr_actual', 'FDR')
    fout_img = get_fout_img('sim_fdr_LgHypoth_', exp_params)
    obj.plt_box_tiled(fout_img, 'fdr_actual', 'FDR')
    # Re-run with a smaller number of hypotheses
    exp_params['num_hypoths_list'] = [4, 8, 16]
    obj = ExperimentsAll(exp_params)
    fout_img = get_fout_img('sim_fdr_SmHypoth', exp_params)
    obj.plt_box_tiled(fout_img, 'fdr_actual', 'FDR')
    obj.seed.prt(prt)

def get_fout_img(prefix, exp_params):
    """Get the name of the png file for the tiled plot."""
    return "{PRE}_{P0:03}to{PN:03}_{MAX0:02}to{MAXN:02}.png".format(
        PRE=prefix,
        P0=100-exp_params['perc_sigs'][0],   # True Null %
        PN=100-exp_params['perc_sigs'][-1],  # True Null %
        MAX0=int(exp_params['max_sigpvals'][0]*100),  # 0.01 ->"01"
        MAXN=int(exp_params['max_sigpvals'][-1]*100))

if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
