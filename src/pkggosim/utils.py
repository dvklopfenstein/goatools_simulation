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

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
