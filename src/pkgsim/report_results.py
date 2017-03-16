"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from goatools.statsdescribe import StatsDescribe

def report_results_tot(params, results_tot, prt=sys.stdout):
    """Report simulation results for many sets of p-values."""
    prt.write("\nCounts of sets of {N} pvalues seen as significant".format(N=params['num_pvalues']))
    objrpt = StatsDescribe("counts", "{:6,}")
    alpha = params['alpha']
    objrpt.prt_hdr(prt)
    sig_cnts = [(sum(r['pvals'] < alpha), sum(r['pvals_corr'] < alpha)) for r in results_tot]
    sig_orig, sig_corr = zip(*sig_cnts)
    objrpt.prt_data("orig sig", sig_orig)
    objrpt.prt_data("corr sig", sig_corr)

def report_results_each(params, results_allsets, prt):
    """Report one line for each set of p-values."""
    for results_one in results_allsets:
        report_results_one(params, results_one, prt)

def report_results_one(params, data, prt):
    """Report simulation results for one set of p-values."""
    msg = "{N} of {M} ({P:3.1f}%) {DESC:9} p-values are significant"
    num_pval_sig, num_pval_tot, perc_pval_sig = get_perc_sig(data['pvals'], params['alpha'])
    num_corr_sig, num_corr_tot, perc_corr_sig = get_perc_sig(data['pvals_corr'], params['alpha'])
    prtmsg = [
        msg.format(N=num_pval_sig, M=num_pval_tot, P=perc_pval_sig, DESC="original"),
        msg.format(N=num_corr_sig, M=num_corr_tot, P=perc_corr_sig, DESC="corrected")]
    prt.write("{MSG}\n".format(MSG=" ".join(prtmsg)))

def get_perc_sig(pvals, alpha):
    """Calculate the percentage of p-values which are significant."""
    num_pvals_sig = sum(pvals < alpha)
    num_pvals_tot = len(pvals)
    return num_pvals_sig, num_pvals_tot, 100.0*num_pvals_sig/num_pvals_tot


# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
