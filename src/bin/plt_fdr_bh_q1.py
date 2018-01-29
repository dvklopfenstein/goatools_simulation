#!/usr/bin/env python
"""What is the effect of a subset of P having uncor-pvals several orders of mag smaller?"""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
from pkggosim.common.cli import get_args
from pkggosim.hypotheses.run_all import ExperimentsAll


def run(args, ntd, max_sigpvals_super, perc_super):
    """What is the effect of a subset of P having uncor-pvals several orders of mag smaller?"""
    # What happens if POS group has a subset of uncorrected P-values several orders of
    # magnitude above the remaining POS group?
    sim_params = {
        'seed' : args['randomseed'],
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals' : [0.01, 0.03, 0.05],  # [0.0001,  0.001,  0.01]
        'max_sigpvals_super' : max_sigpvals_super, # Magnitudes smaller than max_sigpvals
        'perc_super': perc_super,
        'perc_nulls' : [100, 75, 50, 25],
        'num_hypoths_list' : [8, 16, 32, 64, 128, 256],
        #'num_hypoths_list' : [8, 16, 128],
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

    #                     0.01,  0.03,  0.05
    max_sigpvals_super = [0.001, 0.003, 0.005]
    perc_super = 50

    run(args, ntd, max_sigpvals_super, perc_super)


if __name__ == '__main__':
    main()

# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
