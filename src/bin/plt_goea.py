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

def run(randomseed, ntd):
    """Simulate Gene Ontology Enrichment Analyses."""
    study_bg = "humoral_rsp"
    title = 'GOEA Simulations; Humoral Response Genes'
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
        'num_experiments' : ntd.num_experiments, # Num. of simulated FDR ratios per experiment set
        'num_sims' : ntd.num_sims}   # Number of sims per experiment; used to create one FDR ratio
    rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    plt_items = ['fdr_actual', 'sensitivity', 'specificity']
    pltargs = {'dotsize':ntd.dotsize, 'ylim':ntd.ylim, 'yticklabels':ntd.yticklabels, 'title':title}
    objparams = RunParams(params)
    obj = ExperimentsAll(objparams)
    obj.run_all(study_bg, rpt_items, plt_items, **pltargs)
    objparams.prt_summary(sys.stdout)

def main():
    """Arguments for running all experiments."""
    seed = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    nto = cx.namedtuple("NtRunParams", "num_experiments num_sims dotsize ylim yticklabels")
    #pylint: disable=bad-whitespace, no-member, line-too-long
    ylim = {'fdr_actual':[-0.005, 0.10]}
    ylab = {'fdr_actual':['0.00', '0.25', '0.50', '0.75', '1.00']}
    params = [
        # nto._make([500, 1000, {'fdr_actual':0.70, 'sensitivity':0.50}, ylim, ylab]),
        # nto._make([100, 1000, {'fdr_actual':0.95, 'sensitivity':0.60}, ylim, ylab]),
        # nto._make([100,   20, {'fdr_actual':0.95, 'sensitivity':0.60}, ylim, ylab]),
        # nto._make([ 50,   50, {'fdr_actual':2.00, 'sensitivity':0.70}, ylim, ylab]),
        # nto._make([ 50,   20, {'fdr_actual':3.00, 'sensitivity':2.00}, ylim, ylab]), # 2:50
        # nto._make([ 20,   20, {'fdr_actual':2.00, 'sensitivity':2.00}, ylim, ylab]), # 1:25
        nto._make([  4,    4, {'fdr_actual':4.00, 'sensitivity':3.00, 'specificity':3.00}, ylim, ylab]), # 0:04
    ]
    for ntd in params:
        run(seed, ntd)

if __name__:
    main()

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
