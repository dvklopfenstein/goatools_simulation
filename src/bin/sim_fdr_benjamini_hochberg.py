#!/usr/bin/env python
"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
from pkgsim.report_results import report_results_all
from pkgsim.plot_results import plot_results_all
from pkgsim.pval_mtcorr_sims import PvalMtCorrSimsMany

def main(prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    perc_sig_list = [0, 10, 20, 40, 80]
    num_pvalues_list = [10, 20, 50, 100, 500, 1000, 10000]
    #num_pvalues_list = [10, 20]
    # Used for all simulations
    num_sims = 100
    multi_params = {'alpha' : 0.05, 'method' : 'fdr_bh'}
    global_params = {
        'title':"P-values: {PERC_SIG} Expected Significant (<{MAX_SIG})",
        'title_None':"P-values: No Significance Expected",
        'base_img' : "pvalues_sig{SIG:03}_numsims{SIMS:05}.png",
        'max_sig': 0.05,
        'repo' : os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."),
        'dir_img' : "doc/images",
        'num_sims' : num_sims, # 100
        'multi_params' : multi_params} # alpha=0.05, method='fdr_bh'
    # objsim: PvalMtCorrSimsMany
    objsim = PvalMtCorrSimsMany(num_pvalues_list, num_sims, perc_sig_list, multi_params)
    report_results_all(objsim, global_params, prt)
    lst = sorted(objsim.get_attr_percentile_vals(attrname="perc_Type_I_II", percentile=78.0))
    print lst
    print max(lst)
    plot_results_all(objsim, global_params)

if __name__:
    main()

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
