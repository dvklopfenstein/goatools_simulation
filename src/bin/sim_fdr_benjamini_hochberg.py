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

def main(num_sims, prt=sys.stdout):
    """Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""
    global_params = {
        'repo' : os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."),
        'dir_img' : "doc/images",
        'alpha' : 0.05,
        'method' : 'fdr_bh'}
    perc_sig_list = [0, 5, 10, 50]
    num_pvalues_list = [10, 20, 50, 100, 500, 1000, 10000]
    params_results = _get_data(perc_sig_list, num_pvalues_list, num_sims, global_params)
    report_results_all(params_results, prt)
    plot_results_all(params_results, prt)

def _get_data(perc_sig_list, num_pvalues_list, num_sims, global_params):
    """Do P-value and multiple test simulations. Return results."""
    params_results = []
    ntobj = cx.namedtuple("Nt", "perc_sig num_pvalues num_sims params")
    for perc_sig in perc_sig_list:
        for num_pvalues in num_pvalues_list:
            params = ntobj._make([perc_sig, num_pvalues, num_sims, global_params])
            results = _run_all_simulations(params)

            #params['perc_sig'] = perc_sig
            #params['num_pvalues'] = num_pvalues
            ##results_sets = _run_all_simulations(num_sims, params)
            ##report_results_each(params, results_sets, prt)

            #results_sets = []
            #for _ in range(num_sims):
            #    results_one = _run_one_simulation(**params)
            #    results_sets.append(results_one)

            # report_results_tot(params, results_sets, prt)
            params_results.append((params, results))
    return params_results
    ## Plot results in boxplots
    #fout_img =os.path.join(REPO, "doc/images/pvalues_sig{EXP:02}.png".format(EXP=perc_sig))
    #pltargs = {
    #    'title':"P-values: None are significant",
    #    'xlabel':"# of P-values per set; {N} sets".format(N=num_sims),
    #    'fout_img':os.path.join(REPO, "doc/images/pvalues_sig{EXP:02}.png".format(EXP=perc_sig))
    #}
    #wrpng_boxplot_sigs(params, params_results, **pltargs)


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
    num_sig = int(round(float(perc_sig)*num_pvalues/100.0))
    num_rand = num_pvalues - num_sig
    #print "NNNNNNNNN", num_pvalues, "{}%".format(perc_sig), num_sig, num_rand, alpha
    pvals_rand = np.random.uniform(0, 1, size=num_rand)
    pvals_sig = np.random.uniform(0, alpha, size=num_sig)
    #print pvals_rand
    pvals_all = np.array(list(pvals_rand) + list(pvals_sig))
    # reject, pvals_corrected, alpha_sidak, alpha_bonf
    reject, pvals_corrected, _, _ = multipletests(pvals_all, alpha, params['method'])
    return {'pvals':pvals_all, 'reject':reject, 'pvals_corr':pvals_corrected}

if __name__:
    main(100)

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
