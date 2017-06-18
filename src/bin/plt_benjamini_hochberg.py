#!/usr/bin/env python
"""Create GOATOOLS supplemental figure: simulated FDR tiled plot."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
from pkggosim.hypotheses.run_all import ExperimentsAll


def main(randomseed, num_experiments, num_sims, dotsize):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    sim_params = {
        'seed' : randomseed,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals' : [0.01, 0.03, 0.05],
        'perc_nulls' : [100, 75, 50, 25],
        'num_hypoths_list' : [4, 16, 128],
        'num_experiments' : num_experiments, # Number of simulated FDR ratios in an experiment set
        'num_sims' : num_sims}   # Number of sims per experiment; used to create one FDR ratio
    obj = ExperimentsAll(sim_params)
    rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    #obj.prt_params(sys.stdout)
    #obj.prt_num_sims(sys.stdout)
    obj.run_all(rpt_items, dotsize)


if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    NTOBJ = cx.namedtuple("NtRunParams", "num_experiments num_sims dotsize")
    #pylint: disable=bad-whitespace, no-member
    PARAMS = [
        # NTOBJ._make([500, 2500, {'fdr_actual':0.70, 'sensitivity':0.40}]), # 00:NN:NN
        NTOBJ._make([500, 1000, {'fdr_actual':0.90, 'sensitivity':0.50}]), # 02:37:NN
        # NTOBJ._make([100, 1000, {'fdr_actual':1.20, 'sensitivity':0.65}]), # 00:24:31
        # NTOBJ._make([ 20,  200, {'fdr_actual':2.00, 'sensitivity':2.00}]), # 00:01:00
        # NTOBJ._make([ 10,   10, {'fdr_actual':2.00, 'sensitivity':2.00}]), # 00:00:02
    ]
    for ntd in PARAMS:
        main(SEED, ntd.num_experiments, ntd.num_sims, ntd.dotsize)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
