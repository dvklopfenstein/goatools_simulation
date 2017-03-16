"""Simulate False discovery rate multiple test correction with Benjamini and Hochberg."""

__copyright__ = "Copyright (C) 2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

def get_perc_sig(pvals, alpha):
    """Calculate the percentage of p-values which are significant."""
    return _get_perc_sig(pvals, alpha)[2]

def _get_perc_sig(pvals, alpha):
    """Calculate the percentage of p-values which are significant."""
    num_pvals_sig = sum(pvals < alpha)
    num_pvals_tot = len(pvals)
    return num_pvals_sig, num_pvals_tot, 100.0*num_pvals_sig/num_pvals_tot

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
