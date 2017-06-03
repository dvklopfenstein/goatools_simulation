"""Holds parameters used to create one set of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import timeit
import datetime

def get_result_desc(reject, expsig):
    """Return description of the result of one simulation."""
    # pylint: disable=multiple-statements
    #
    # TABLE 1) Number of errors committed when testing m null hypotheses
    # 1995; Yoav Benjamini and Yosef Hochberg:
    #
    #                 reject ->| False         | True
    #
    #                          |Declared       | Declared      |
    #                          |non-significant| significant   | Total
    # -------------------------+---------------+---------------+--------
    # True null hypotheses     | U TN          | V FP (Type I) |   m(0)
    # Non-true null hypotheses | T FN (Type II)| S TP          | m - m(0)
    #                          |      m - R    |       R       |   m
    if     expsig and     reject: return "TP" # Correct:     Significant
    if not expsig and not reject: return "TN" # Correct: Not Significant
    if not expsig and     reject: return "FP" # Type  I Error (False Positive)
    if     expsig and not reject: return "FN" # Type II Error (False Negative)
    assert True, "UNEXPECTED ERROR TYPE"
    # Random variable, Q = V/(V+S); Q = 0 when V+S = 0, is the proportion of errors committed by
    # falsely rejecting null hypotheses.
    # Power = 1 - beta; Beta < 20% good
    # average power: the proportion of the false hypotheses which are correctly rejected
    # TP/(FN + TP)

def calc_ratio(top, bot_ab):
    """Calc ratios: FDR, sensitivity, specificity, positive/negative predictive value."""
    bottom = sum(bot_ab)
    if bottom == 0:
        # 1995 BH: "Return Q=0 if V+S=0 because no error of false rejection can be commited."
        # True for other ratios as well
        assert top == 0
        return 0.0
    return float(top)/bottom

def get_hms(tic):
    """Print elapsed time as simulations run."""
    return str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))

# TBD: Put in hypotheses_utils
def get_fout_img(params, img_pat="sim_{P0:03}to{PN:03}_{MAX0:02}to{MAXN:02}.png"):
    """Get the name of the png file for the tiled plot."""
    return img_pat.format(
        P0=params['perc_nulls'][0],   # True Null %
        PN=params['perc_nulls'][-1],  # True Null %
        MAX0=int(params['max_sigpvals'][0]*100),  # 0.01 ->"01"
        MAXN=int(params['max_sigpvals'][-1]*100),
        Q0=params['num_hypoths_list'][0],
        QN=params['num_hypoths_list'][-1],
        NEXP=params['num_experiments'],
        NSIM=params['num_sims'])


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
