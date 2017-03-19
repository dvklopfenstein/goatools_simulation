"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from goatools.statsdescribe import StatsDescribe
from pkgsim.utils import get_perc_sig, _get_perc_sig

def report_results_all(results_all, global_params, prt=sys.stdout):
    """Report simulation results for many sets of p-values."""
    pfmt = "{perc_sig:4}=%sig {num_pvalues:6,}=#pvals {num_sims:5}=#sims " \
           "{alpha:5.2f} {method} {EXP_SIG:5}=#expsig {EXP_RND:5}=#exprnd\n"
    objrpt = StatsDescribe("percs", "{:6.2f}")
    prt.write("%sig #pvals #sims alpha method\n")
    prt.write("---- ------ ----- ----- ------\n")
    #objrpt.prt_hdr(prt)
    aph = global_params['alpha']
    method = global_params['method']
    for perc_sig, num_sims, results_set in results_all:
        print
        for num_pvalues, results in results_set:
            # results: list of {'pvals':[(pval0, desc0), (pval1, desc1), ..., 'pvals_corr':..., 'reject':...}
            num_pvals_sig = int(round(float(num_pvalues)*perc_sig/100))
            num_pvals_rnd = num_pvalues - num_pvals_sig
            #exp_num_pass = 
            msg = pfmt.format(
                perc_sig=perc_sig,
                num_pvalues=num_pvalues,
                num_sims=num_sims,
                EXP_SIG=num_pvals_sig,
                EXP_RND=num_pvals_rnd,
                alpha=aph,
                method=method)
            prt.write(msg)
            for k2v in results:
                for (pval, isrand), pval_corr, reject in zip(k2v['pvals'], k2v['pvals_corr'], k2v['reject']):
                    err_type = get_err_type(reject, isrand)
                    if err_type[0:1] == "T": # Type I or II error
                    #if desc == "set" and not reject:
                        prt.write("{ERRTYPE:7} {PVAL:8.6f} {ISRAND}=is_Rand {PCORR:8.6f} {REJECT:5} {MSG}".format(
                            ERRTYPE=err_type, PVAL=pval, ISRAND=int(isrand), PCORR=pval_corr, REJECT=reject, MSG=msg))
            #sigs = [(get_perc_sig(r['pvals'], aph), get_perc_sig(r['pvals_corr'], aph)) for r in results]
            #sigs = [(get_perc_sig(r['pvals'], aph), get_perc_sig(r['pvals_corr'], aph)) for r in results]
            #sig_cnt_orig, sig_cnt_corr = zip(*sigs)
            #objrpt.prt_data("orig sig", sig_cnt_orig)
            #objrpt.prt_data("corr sig", sig_cnt_corr)

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

def get_err_type(reject, isrand):
    if not isrand and reject:
        return ""
    if isrand and not reject:
        return ""
    if isrand and reject:
        return "Type I"
    if not isrand and not reject:
        return "Type II"

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
