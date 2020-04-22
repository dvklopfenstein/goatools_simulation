"""Assigns: true positive, true negative, false positive, or false negative."""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

from numpy.random import shuffle

def get_tfpn(reject, expsig):
    """Assigns: true positive, true negative, false positive, or false negative."""
    # pylint: disable=multiple-statements
    #
    # TABLE 1) Number of errors committed when testing m null hypotheses
    # 1995; Yoav Benjamini and Yosef Hochberg:
    #
    #                           reject ->| False         | True
    #
    #                                    |Declared       | Declared      |
    #                                    |non-significant| significant   | Total
    #          --------------------------+---------------+---------------+--------
    # actually True  null hypotheses (N) | U TN          | V FP (Type I) |   m(0)
    # actually False null hypotheses (P) | T FN (Type II)| S TP          | m - m(0)
    #                                    |      m - R    |       R       |   m
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

def mk_stochastic_goeasim_source(num_study_genes, num_null, genes_study_bg, genes_pop_bg):
    """Generate 2 sets of genes: Not intended significant & intended to be significant."""
    # Calculate the number of "Non-true null hypotheses":
    #   Study genes found to be different than the population genes likely not by chance
    num_ntnull = num_study_genes - num_null
    # 1. Generate random genes: Significant and Random
    #   True  -> gene is intended to be significant(different from the population)
    #   False -> If gene is determined significant, it occured by chance
    shuffle(genes_pop_bg)
    shuffle(genes_study_bg)
    genes_ntn = [(g, True) for g in genes_study_bg[:num_ntnull]]
    genes_tn = [(g, False) for g in genes_pop_bg[:num_null]]
    assert len(genes_ntn) == num_ntnull
    assert len(genes_tn) == num_null
    return genes_ntn + genes_tn # gene_expsig_list


# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
