#!/usr/bin/env python
"""Simulate Gene Ontology Enrichment Analyses."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import collections as cx
from pkggosim.goea.run_all_params import RunParams
from pkggosim.goea.run_all import ExperimentsAll
from pkggosim.goea.utils import get_genes, get_genes_all
from goatools_suppl.data.ensmusg2sym import ensm2sym

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

def main(randomseed, num_experiments, num_sims, dotsize):
    """Simulate Gene Ontology Enrichment Analyses."""
    study_bg = "humoral_rsp"
    popnullmaskout = ['immune', 'viral_bacteria']
    # Gene Ontology Data
    genes_mus = ensm2sym.keys()  # Population genes
    params = {
        'seed' : randomseed,
        'alpha' : 0.05,
        'method' : 'fdr_bh',
        'genes_population':genes_mus,
        'genes_study_bg':get_genes(study_bg),
        'genes_popnullmaskout':get_genes_all(popnullmaskout),
        'association_file':'gene_association.mgi',
        'perc_nulls' : [100, 75, 50, 25],
        'num_genes_list' : [4, 16, 64],
        'num_experiments' : num_experiments, # Number of simulated FDR ratios in an experiment set
        'num_sims' : num_sims}   # Number of sims per experiment; used to create one FDR ratio
    rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    objparams = RunParams(params)
    obj = ExperimentsAll(objparams)
    obj.run_all(rpt_items, dotsize)


if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    NTOBJ = cx.namedtuple("NtRunParams", "num_experiments num_sims dotsize")
    #pylint: disable=bad-whitespace, no-member
    PARAMS = [
        # NTOBJ._make([500, 1000, {'fdr_actual':0.70, 'sensitivity':0.50}]),
        # NTOBJ._make([100, 1000, {'fdr_actual':0.95, 'sensitivity':0.60}]),
        # NTOBJ._make([ 20,   20, {'fdr_actual':2.00, 'sensitivity':1.00}]),
        NTOBJ._make([  2,    2, {'fdr_actual':2.00, 'sensitivity':1.00}]),
    ]
    for ntd in PARAMS:
        main(SEED, ntd.num_experiments, ntd.num_sims, ntd.dotsize)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
