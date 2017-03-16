"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from goatools.statsdescribe import StatsDescribe
from pkgsim.utils import get_perc_sig, _get_perc_sig

def report_results_tot(num_pvalues, params, results, prt=sys.stdout):
    """Report simulation results for many sets of p-values."""
    prt.write("\nCounts of sets of {N} pvalues seen as significant".format(N=num_pvalues))
    objrpt = StatsDescribe("percs", "{:6.2f}")
    aph = params['alpha']
    objrpt.prt_hdr(prt)
    sigs = [(get_perc_sig(r['pvals'], aph), get_perc_sig(r['pvals_corr'], aph)) for r in results]
    sig_cnt_orig, sig_cnt_corr = zip(*sigs)
    objrpt.prt_data("orig sig", sig_cnt_orig)
    objrpt.prt_data("corr sig", sig_cnt_corr)

def report_results_each(params, results_allsets, prt):
    """Report one line for each set of p-values."""
    for results_one in results_allsets:
        report_results_one(params, results_one, prt)

def report_results_one(params, data, prt):
    """Report simulation results for one set of p-values."""
    msg = "{N} of {M} ({P:6.2f}%) {DESC:9} p-values are significant"
    num_pval_sig, num_pval_tot, perc_pval_sig = _get_perc_sig(data['pvals'], params['alpha'])
    num_corr_sig, num_corr_tot, perc_corr_sig = _get_perc_sig(data['pvals_corr'], params['alpha'])
    prtmsg = [
        msg.format(N=num_pval_sig, M=num_pval_tot, P=perc_pval_sig, DESC="original"),
        msg.format(N=num_corr_sig, M=num_corr_tot, P=perc_corr_sig, DESC="corrected")]
    prt.write("{MSG}\n".format(MSG=" ".join(prtmsg)))

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
