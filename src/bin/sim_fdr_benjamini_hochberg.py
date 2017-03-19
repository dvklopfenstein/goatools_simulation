#!/usr/bin/env python
"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

# Controlling the False Discovery Rate: a Practical and Powerful Approach to Multiple Testing
# http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf

#pylint: disable=no-member

import os
import sys
import collections as cx
import numpy as np
from statsmodels.sandbox.stats.multicomp import multipletests
#from pkgsim.report_results import report_results_each
from pkgsim.report_results import report_results_all
from pkgsim.plot_results import plot_results_all

def main(prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    perc_sig_list = [0, 20, 40, 80]
    num_sims = 100
    global_params = {
        'title':"P-values: {PERC_SIG} Expected Significant (<{MAX_SIG})",
        'title_None':"P-values: No Significance Expected",
        'base_img' : "pvalues_sig{SIG:03}_numsims{SIMS:04}.png",
        'max_sig': 0.05,
        'repo' : os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."),
        'dir_img' : "doc/images",
        'alpha' : 0.05,
        'method' : 'fdr_bh'}
    #num_pvalues_list = [10, 20, 50, 100, 500, 1000, 10000]
    num_pvalues_list = [10, 20]
    results_all = _get_data(perc_sig_list, num_sims, num_pvalues_list, global_params)
    report_results_all(results_all, global_params, prt)
    plot_results_all(results_all, global_params)

def _get_data(perc_sig_list, num_sims, num_pvalues_list, global_params):
    """Do P-value and multiple test simulations. Return results."""
    results_all = []
    ntobj = cx.namedtuple("Nt", "perc_sig num_pvalues num_sims params")
    for perc_sig in perc_sig_list:
        results_set = []
        for num_pvalues in num_pvalues_list:
            params = ntobj._make([perc_sig, num_pvalues, num_sims, global_params])
            results = _run_all_simulations(params)
            results_set.append((num_pvalues, results))
        results_all.append((perc_sig, num_sims, results_set))
    return results_all

def _run_all_simulations(pars):
    """Generate many sets of random pvalues and do multipletest correction for each set."""
    results_tot = []
    for _ in range(pars.num_sims):
        results_one = _run_one_simulation(pars.num_pvalues, pars.perc_sig, pars.params)
        results_tot.append(results_one)
    return results_tot

def _run_one_simulation(num_pvalues, perc_sig, params):
    """Generate one set of random pvalues and do multipletest correction."""
    alpha = params['alpha']
    # 1. Get number of P-values which will be random and which will be set
    num_sig = int(round(float(perc_sig)*num_pvalues/100.0))
    num_rand = num_pvalues - num_sig
    #print "NNNNNNNNN", num_pvalues, "{}%".format(perc_sig), num_sig, num_rand, alpha
    # 2. Get random P-values and explicitly set P-values
    pvals_rand = np.random.uniform(0, 1, size=num_rand)
    max_sig = 0.05/num_pvalues
    pvals_sig = np.random.uniform(0, max_sig, size=num_sig)
    # 3. Add rand/set info to P-values
    pvals_rand = [(p, True) for p in pvals_rand]
    pvals_sig = [(p, False) for p in pvals_sig]
    # 4. Combine random P-values and explictly set P-values
    pvals_all = list(pvals_rand) + list(pvals_sig)
    pval_vals = np.array([pval for pval, desc in pvals_all])
    # reject, pvals_corrected, alpha_sidak, alpha_bonf
    reject, pvals_corrected, _, _ = multipletests(pval_vals, alpha, params['method'])
    return {'pvals':pvals_all, 'reject':reject, 'pvals_corr':pvals_corrected}

if __name__:
    main()

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
