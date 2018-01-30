#!/usr/bin/env python
"""Create GOATOOLS supplemental figure: simulated FDR tiled plot."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
from pkggosim.common.cli import get_args
from pkggosim.hypotheses.run_all import ExperimentsAll


def run(args, ntd, method, max_sigpvals):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    sim_params = {
        'seed' : args['randomseed'],
        'multi_params' : {'alpha' : 0.05, 'method' : method},
        'max_sigpvals' : max_sigpvals,
        'perc_nulls' : [100, 75, 50, 25],
        'num_hypoths_list' : [4, 16, 128],
        'num_experiments' : ntd.num_experiments, # Num. of simulated FDR ratios in an experiment set
        'num_sims' : ntd.num_sims}   # Number of sims per experiment; used to create one FDR ratio
    obj = ExperimentsAll(sim_params)
    rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    #obj.prt_params(sys.stdout)
    #obj.prt_num_sims(sys.stdout)
    obj.run_all(rpt_items, ntd.dotsize)


def main():
    """Run all sets of hypotheses experiments."""
    args = get_args()
    ntobj = cx.namedtuple("NtRunParams", "num_experiments num_sims dotsize")
    #pylint: disable=bad-whitespace, no-member
    lst_experiment_cnts = [
        ntobj._make([500, 2500, {'fdr_actual':0.70, 'sensitivity':0.40}]), # 00:NN:NN
        ntobj._make([500, 1000, {'fdr_actual':0.90, 'sensitivity':0.50}]), # 02:37:NN
        ntobj._make([100, 1000, {'fdr_actual':1.20, 'sensitivity':0.65}]), # 00:24:31
        ntobj._make([ 20,  200, {'fdr_actual':2.00, 'sensitivity':2.00}]), # 00:01:00
        ntobj._make([ 10,   10, {'fdr_actual':2.00, 'sensitivity':2.00}]), # 00:00:02
    ]
    ntd = lst_experiment_cnts[args['idx_experiment_cnts']]

    lst_max_sigpvals = [
        [0.01, 0.03, 0.05],
        [0.0001, 0.001, 0.01],
    ]
    max_sigpvals = lst_max_sigpvals[args['idx_max_sigpvals']]

    methods = [               # Time for one ExperimentSet (100, 1000)                  H:MM:SS
        #'bonferroni',     #  0) Bonferroni one-step correction                      0:00:09
        #'sidak',          #  1) Sidak one-step correction                           0:00:09
        #'holm-sidak',     #  2) Holm-Sidak step-down method using Sidak adjustments 0:00:12
        ##holm',           #  3) Holm step-down method using Bonferroni adjustments  2:29:59
        #'simes-hochberg', #  4) Simes-Hochberg step-up method  (independent)        0:00:11
        'hommel',         #  5) Hommel closed method based on Simes tests (non-negative)
        'fdr_by',         #  7) FDR Benjamini/Yekutieli (negative)
        'fdr_tsbh',       #  8) FDR 2-stage Benjamini-Hochberg (non-negative)
        'fdr_tsbky',      #  9) FDR 2-stage Benjamini-Krieger-Yekutieli (non-negative)
        'fdr_gbs',        # 10) FDR adaptive Gavrilov-Benjamini-Sarkar
        'fdr_bh',         #  6) FDR Benjamini/Hochberg  (non-negative)
    ]
    #main(args, ntd.num_experiments, ntd.num_sims, ntd.dotsize)
    for method in methods:
        run(args, ntd, method, max_sigpvals)


if __name__ == '__main__':
    main()

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
