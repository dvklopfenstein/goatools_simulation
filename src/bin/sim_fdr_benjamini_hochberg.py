#!/usr/bin/env python
"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
#### from pkgsim.report_results import report_results_all
from pkgsim.plot_results import plot_results_all
from pkgsim.pval_mtcorr_sims import PvalMtCorrSimsMany

def main(prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    # Both "Not Significant"/"Significant" P-values are randomly generated w/uniform distribution.
    #   1. "Not significant" vals are randomly chosen between 0.0 to 1.0
    #       Some "not significant" results will be show as "significant"
    #   2. "Significant" vals are randomly chosen between 0.0 and fnc_maxsig
    fnc_maxsig_pnnn.max_sig_pval = 0.05
    fnc_maxsig = fnc_maxsig_pnnn

    # The percentage of "Significant" results in a single simulation is set by perc_sigs.
    # The number of items in perc_sigs indicate the number of sets
    #perc_sigs = range(0, 40, 2)
    #perc_sigs = range(10, 11) # Simulations of P-vals with 10% significance
    #perc_sigs = range(0, 1) # Simulations of P-vals with NO SIGNIFICANCE only
    # Used for all simulations
    sim_params = {
        'num_sims' : 1000,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'perc_sigs' : [0, 15, 20, 40, 80],
        'pval_qtys' : [20, 100, 500],
        'fnc_maxsig' : fnc_maxsig}
    objsim = PvalMtCorrSimsMany(**sim_params)
    objsim.prt_num_sims_w_errs(prt)
    # attrs = ["fdr_actual", "frr_actual", "num_Type_I", "num_Type_II", "num_correct"]
    # objsim.prt_summary(prt, attrs)
    plt_params = {
        'title':"P-values: {PERC_SIG} Expected Significant (<{ALPHA})",
        'title_None':"P-values: No Significance Expected",
        'base_img' : "pvalues_sig{SIG:03}_numsims{SIMS:05}.png",
        'dir_img' : "doc/images"}
    #### report_results_all(objsim, global_params, prt)
    plot_results_all(objsim, plt_params)

def main_stepped_sigset(prt=sys.stdout):
    sim_params = {
        'num_sims' : 1000,
        'multi_params' : {'alpha' : 0.05, 'method' : 'fdr_bh'},
        'perc_sigs' : [0, 15, 20, 40, 80],
        'pval_qtys' : [20, 100, 500],
        'fnc_maxsig' : None}
    attrs = ["fdr_actual", "frr_actual", "num_Type_I", "num_Type_II", "num_correct"]
    for sig_max in [0.005, 0.01, 0.02, 0.03, 0.04, 0.05]:
        prt.write("{SPVAL:5.3f} Maximum P-Value for actual significant results.\n".format(SPVAL=sig_max))
        fnc_maxsig_pnnn.max_sig_pval = sig_max
        sim_params['fnc_maxsig'] = fnc_maxsig_pnnn
        objsim = PvalMtCorrSimsMany(**sim_params)
        objsim.prt_num_sims_w_errs(prt)
        objsim.prt_summary(prt, attrs)

# ----------------------------------------------------------------------------
# Functions for creating randomly-generated "Significant" P-values
#   1. fnc_maxsig_alpha_numpval generates extremely small P-values and varies by sim params
#   2. fnc_maxsig_pnnn generates small P-values and is constant across all sims
def fnc_maxsig_alpha_numpval(**kws):
    """P-values expected to be 'significant' are randomly generated and under alpha/num_pvals."""
    name = "alpha/#pvals"
    return kws['alpha']/kws['num_pvals']

# pylint: disable=unused-argument
def fnc_maxsig_pnnn(**kws):
    """P-values expected to be 'significant' are randomly generated and under value, N."""
    name = fnc_maxsig_pnnn.max_sig_pval
    return fnc_maxsig_pnnn.max_sig_pval

if __name__:
    #main()
    main_stepped_sigset()

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
