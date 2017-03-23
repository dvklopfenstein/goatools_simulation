"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import numpy as np
#from goatools.statsdescribe import StatsDescribe
#from pkgsim.utils import get_perc_sig, _get_perc_sig
from PyBiocode.Utils.stats import prt_percentiles

def report_results_all(percsigs_simsets, global_params, prt=sys.stdout):
    """Report simulation results for many sets of p-values."""
    pfmt = "[({perc_sig:4}=%sig {num_pvalues:6,}=#pvals) -> " \
           "(EXP:{EXP_SIG:5}=#sig {EXP_RND:5}=#rnd)]"
    #dfmt = "{PVAL:8.6f} {PCORR:8.6f} ({ERRTYPE:1}=errtype: {EXPSIG}=expsig {REJECT:1}=rej) {MSG}"
    #objrpt = StatsDescribe("percs", "{:6.2f}")
    alpha = global_params['multi_params']['alpha']
    method = global_params['multi_params']['method']
    #prt.write("%sig #pvals #sims alpha method\n")
    #prt.write("---- ------ ----- ----- ------\n")
    #objrpt.prt_hdr(prt)
    percs = [25.0, 50.0, 75.0]
    attrs = [
      "perc_correct",
      "act_sig",
      "num_Type_II",
      "num_Type_I",
      "num_correct",
      "perc_Type_I"
    ]
    prt.write("num_sims={N} alpha={A:4.2f} method={M} {ATTRS}\n".format(
        N=global_params['num_sims'], A=alpha, M=method, ATTRS=attrs))
    for perc_sig, numpvals_objsims in percsigs_simsets:
        prt.write("\n")
        # objsims: pkgsim.pval_mtcorr_sims.PvalSimMany
        for num_pvalues, objsims in numpvals_objsims:
            # nterrs: cnts perc_Type_I perc_Type_II perc_TypesI_II
            nterrs = objsims.get_nterrs()
            msg = pfmt.format(
                perc_sig=perc_sig,
                num_pvalues=num_pvalues,
                EXP_SIG=objsims.get_num_mksig(),
                EXP_RND=objsims.get_num_mkrnd())
            prt.write(msg)
            #prt_percentiles("Type I", vals_t1, "{:8.6f}", prt)
            #vals_t1 = [nt.cnts[1] for nt in nterrs]
            for attr in attrs:
                prt.write("{}".format(get_percentile_vals(attr, nterrs, percs)))
            prt.write("\n")
            #prt_percentiles("Type I", vals_t1, "{:5}", prt)
            #for obj1sim in objsims.obj1sim_list:
            #    # Report one simulation
            #    for nt1sim in obj1sim.get_zipped_data(): # nt1sim: pval pval_corr reject expsig
            #        err_type = obj1sim.get_type(nt1sim)
            #        if err_type != 0: # Type I or II error
            #            prt.write(dfmt.format(
            #                PVAL=nt1sim.pval, PCORR=nt1sim.pval_corr,
            #                ERRTYPE=err_type, EXPSIG=int(nt1sim.expsig), REJECT=nt1sim.reject, MSG=msg))
            #sigs = [(get_perc_sig(r['pvals'], alpha), get_perc_sig(r['pvals_corr'], alpha)) for r in objsims]
            #sigs = [(get_perc_sig(r['pvals'], alpha), get_perc_sig(r['pvals_corr'], alpha)) for r in objsims]
            #sig_cnt_orig, sig_cnt_corr = zip(*sigs)
            #objrpt.prt_data("orig sig", sig_cnt_orig)
            #objrpt.prt_data("corr sig", sig_cnt_corr)

def get_percentile_vals(attr, nterrs, percs):
    """Return percentile values for 'attr' list."""
    return [np.percentile([getattr(nt, attr) for nt in nterrs], p) for p in percs] 

# def report_results_each(params, results_allsets, prt):
#     """Report one line for each set of p-values."""
#     for results_one in results_allsets:
#         report_results_one(params, results_one, prt)
#
# def report_results_one(params, data, prt):
#     """Report simulation results for one set of p-values."""
#     msg = "{N} of {M} ({P:6.2f}%) {DESC:9} p-values are significant"
#     num_pval_sig, num_pval_tot, perc_pval_sig = _get_perc_sig(data['pvals'], params['alpha'])
#     num_corr_sig, num_corr_tot, perc_corr_sig = _get_perc_sig(data['pvals_corr'], params['alpha'])
#     prtmsg = [
#         msg.format(N=num_pval_sig, M=num_pval_tot, P=perc_pval_sig, DESC="original"),
#         msg.format(N=num_corr_sig, M=num_corr_tot, P=perc_corr_sig, DESC="corrected")]
#     prt.write("{MSG}\n".format(MSG=" ".join(prtmsg)))

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
