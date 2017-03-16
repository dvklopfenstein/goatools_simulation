#!/usr/bin/env python
"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

# Controlling the False Discovery Rate: a Practical and Powerful Approach to Multiple Testing
# http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf

#pylint: disable=no-member

import sys
import numpy as np
from statsmodels.sandbox.stats.multicomp import multipletests
#from pkgsim.report_results import report_results_each
from pkgsim.report_results import report_results_tot

def main(num_samples=100, prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    params = {'num_pvalues':None, 'alpha':0.05, 'method':'fdr_bh'}
    num_pvalues_list = [10, 20, 50, 100]
    for num_pvalues in num_pvalues_list:
        params['num_pvalues'] = num_pvalues
        results = _run_all_simulations(num_samples, params)
        #report_results_each(params, results, prt)
        report_results_tot(params, results, prt)

def _run_all_simulations(num_samples, params):
    """Generate many sets of random pvalues and do multipletest correction for each set."""
    results_tot = []
    for _ in range(num_samples):
        results_one = _run_one_simulation(**params)
        results_tot.append(results_one)
    return results_tot

def _run_one_simulation(num_pvalues, alpha, method):
    """Generate one set of random pvalues and do multipletest correction."""
    pvals = np.random.uniform(0, 1, size=num_pvalues)
    # reject, pvals_corrected, alpha_sidak, alpha_bonf
    reject, pvals_corrected, _, _ = multipletests(pvals, alpha, method)
    return {'pvals':pvals, 'reject':reject, 'pvals_corr':pvals_corrected}


if __name__:
    main(10000)

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
