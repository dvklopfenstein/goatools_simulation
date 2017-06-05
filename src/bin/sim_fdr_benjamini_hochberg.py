#!/usr/bin/env python
"""Simulate two sets of FDR values: Small and Large groups of hypotheses."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import timeit
from pkggosim.hypotheses.run_all import ExperimentsAll
from pkggosim.common.utils import get_hms


def main(randomseed):
    """Simulate two sets of FDR values: Small and Large groups of hypotheses."""
    num_reps = 20
    exp_params = {
        'seed' : randomseed,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'max_sigpvals' : [0.01, 0.03, 0.05],
        'perc_nulls' : [100, 75, 50, 25],
        'num_hypoths_list' : None,
        'num_experiments' : num_reps, # Number of simulated FDR ratios in an experiment set
        'num_sims' : num_reps} # Number of sims per experiment; used to create one FDR ratio
    rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    tic = timeit.default_timer()
    for num_hypoths_list in [[32, 128, 512], [4, 8, 16]]:
        exp_params['num_hypoths_list'] = num_hypoths_list
        obj = ExperimentsAll(exp_params)
        obj.run_all(rpt_items)
    sys.stdout.write("HMS: {HMS}\n".format(HMS=get_hms(tic)))


if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
