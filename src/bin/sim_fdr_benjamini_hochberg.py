#!/usr/bin/env python
"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
from pkgsim.report_results import report_results_all
from pkgsim.plot_results import plot_results_all
from pkgsim.pval_mtcorr_sims import PvalMtCorrSimsMany

def main(prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    # Both "Not Significant"/"Significant" P-values are randomly generated w/uniform distribution.
    #   1. "Not significant" vals are randomly chosen between 0.0 to 1.0
    #       Some "not significant" results will be show as "significant"
    #   2. "Significant" vals are randomly chosen between 0.0 and fnc_maxsig
    fnc_maxsig_pNNN.max_sig_pval = 0.05
    fnc_maxsig = fnc_maxsig_pNNN

    # The percentage of "Significant" results in a single simulation is set by perc_sigs.
    # The number of items in perc_sigs indicate the number of sets
    perc_sigs = [0, 15, 20, 40, 80]
    #perc_sigs = range(0, 40, 2)
    #perc_sigs = range(10, 11) # Simulations of P-vals with 10% significance
    #perc_sigs = range(0, 1) # Simulations of P-vals with NO SIGNIFICANCE only
    pval_qtys = [20, 100, 500]
    # Used for all simulations
    num_sims = 1000
    multi_params = {'alpha' : 0.05, 'method' : 'fdr_bh'}
    global_params = {
        'title':"P-values: {PERC_SIG} Expected Significant (<{MAX_SIG})",
        'title_None':"P-values: No Significance Expected",
        'base_img' : "pvalues_sig{SIG:03}_numsims{SIMS:05}.png",
        'max_sig': 0.05,
        'repo' : os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."),
        'dir_img' : "doc/images",
        'num_sims' : num_sims, # 100
        'multi_params' : multi_params}
    # objsim: PvalMtCorrSimsMany
    objsim = PvalMtCorrSimsMany(pval_qtys, num_sims, perc_sigs, multi_params, fnc_maxsig)
    objsim.prt_num_sims_w_errs(prt)
    report_results_all(objsim, global_params, prt)
    lst = sorted(objsim.get_attr_percentile_vals(attrname="perc_Type_I_II", percentile=78.0))
    print "LLLLLL", len(lst), lst
    if lst:
        print "LLLLLL", max(lst)
    plot_results_all(objsim, global_params)

# ----------------------------------------------------------------------------
# Functions for creating randomly-generated "Significant" P-values
#   1. fnc_maxsig_alpha_numpval generates extremely small P-values and varies by sim params
#   2. fnc_maxsig_pNNN generates small P-values and is constant across all sims
def fnc_maxsig_alpha_numpval(**kws):
    """P-values expected to be 'significant' are randomly generated and under alpha/num_pvals."""
    return kws['alpha']/kws['num_pvals']

# pylint: disable=unused-argument
def fnc_maxsig_pNNN(**kws):
    """P-values expected to be 'significant' are randomly generated and under value, N."""
    return fnc_maxsig_pNNN.max_sig_pval

if __name__:
    main()

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
