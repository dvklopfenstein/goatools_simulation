#!/usr/bin/env python
"""Create GOATOOLS supplemental figure: simulated FDR tiled plot."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
from pkggosim.hypotheses_run_all import ExperimentsAll
from pkggosim.utils import get_fout_img

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

# def main(randomseed, num_experiments=500, num_sims=1000, dotsize=0.80):
def main(randomseed, num_experiments=100, num_sims=1000, dotsize=0.70):
# def main(randomseed, num_experiments=20, num_sims=20, dotsize=2):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    # User-configurable parameters
    sim_params = {
        'seed' : randomseed,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals' : [0.01, 0.03, 0.05],
        'perc_nulls' : [100, 75, 50, 25],
        'num_hypoths_list' : [4, 16, 128],
        'num_experiments' : num_experiments, # Number of simulated FDR ratios in an experiment set
        'num_sims' : num_sims}   # Number of sims per experiment; used to create one FDR ratio
    rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    run_sim(sim_params, rpt_items, dotsize)

def run_sim(sim_params, rpt_items, dotsize):
    """Run Hypotheses Simulation using Benjamini/Hochberg FDR."""
    obj = ExperimentsAll(sim_params)
    desc_pat = '{P0:03}to{PN:03}_{MAX0:02}to{MAXN:02}_{Q0:03}to{QN:03}_N{NEXP:05}_{NSIM:05}'
    desc_str = get_fout_img(sim_params, desc_pat)
    fout_log = os.path.join('doc/logs', 'suppl_hypoth_{DESC}.log'.format(DESC=desc_str))
    # Report and plot simulation results
    with open(os.path.join(REPO, fout_log), 'w') as prt:
        obj.prt_params(prt)
        obj.seed.prt(prt)
        obj.prt_experiments_means(prt, rpt_items)
        obj.prt_experiments_stats(prt, rpt_items)
        title = "Benjamini/Hochberg FDR Hypotheses Simulations"
        plts = [('fdr_actual', 'FDR'), 
                ('sensitivity', 'Sensitivity')]
        for attr, name in plts:
            base_img = 'suppl_hypoth_{DESC}_{ATTR}.png'.format(ATTR=attr, DESC=desc_str)
            fout_img = os.path.join(REPO, 'doc/logs', base_img)
            obj.plt_box_tiled(fout_img, attr, name, dotsize=dotsize, title=title)
        sys.stdout.write("  WROTE: {LOG}\n".format(LOG=fout_log))

if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
