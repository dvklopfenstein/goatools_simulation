#!/usr/bin/env python
"""Simulate Gene Ontology Enrichment Analyses."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import collections as cx
from pkggosim.goea.run_all_params import RunParams
from pkggosim.goea.run_all import ExperimentsAll
from pkggosim.goea.utils import import_genes, import_goids, import_genes_all
from goatools_suppl.data.ensm2nt_mus import ensm2nt

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

def run(randomseed, ntd):
    """Simulate Gene Ontology Enrichment Analyses."""
    # User parameters
    # randomize_truenull_assc = "orig" # orig  rnd_all  rm_tgtd  rnd_tgtd
    randomize_truenull_assc = "rnd_all" # orig  rnd_all  rm_tgtd  rnd_tgtd
    # randomize_truenull_assc = "rm_tgtd" # orig  rnd_all  rm_tgtd  rnd_tgtd
    # randomize_truenull_assc = "rnd_tgtd" # orig  rnd_all  rm_tgtd  rnd_tgtd
    study_bg = "humoral_rsp"
    title = 'GOEA Simulations; Humoral Response Genes'
    popnullmaskout = ['immune', 'viral_bacteria']
    # Gene Ontology Data
    genes_mus = ensm2nt.keys()  # Population genes
    params = {
        'prefix' : 'fig_goea_{RND}'.format(RND=randomize_truenull_assc),
        'randomize_truenull_assc' : randomize_truenull_assc,
        'seed' : randomseed,
        'alpha' : 0.05,
        'method' : 'fdr_bh',
        'genes_population':genes_mus,
        'genes_study_bg':import_genes(study_bg),
        'goids_study_bg':import_goids(study_bg),
        'genes_popnullmaskout':import_genes_all(popnullmaskout),
        'association_file':'gene_association.mgi',
        'perc_nulls' : [100, 75, 50, 25, 0],
        'num_genes_list' : [4, 16, 64, 128],
        'num_experiments' : ntd.num_experiments, # Num. of simulated FDR ratios per experiment set
        'num_sims' : ntd.num_sims}   # Number of sims per experiment; used to create one FDR ratio
    rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    plt_items = ['fdr_actual', 'sensitivity', 'specificity']
    pltargs = {'dotsize':ntd.dotsize, 'title':title,
               'xlabel':'Number of Genes in a Study Group',
               'ylabel':'Percentage of General Population Genes'}
    objparams = RunParams(params)
    obj = ExperimentsAll(objparams) # RunParams
    obj.run_all(study_bg, rpt_items, plt_items, **pltargs)
    objparams.prt_summary(sys.stdout)

def main():
    """Arguments for running all experiments."""
    seed = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    nto = cx.namedtuple("NtRunParams", "num_experiments num_sims dotsize")
    #pylint: disable=bad-whitespace, no-member, line-too-long
    params = [
        # nto._make([500, 1000, {'fdr_actual':0.70, 'sensitivity':0.50, 'specificity':0.50}]),
        # nto._make([100, 1000, {'fdr_actual':0.95, 'sensitivity':0.60, 'specificity':0.60}]),
        # nto._make([100,   30, {'fdr_actual':1.30, 'sensitivity':0.60, 'specificity':0.60}]),
        # nto._make([ 50,   50, {'fdr_actual':2.00, 'sensitivity':0.70, 'specificity':0.70}]),
        # nto._make([ 50,   20, {'fdr_actual':2.00, 'sensitivity':1.00, 'specificity':1.00}]), # 4:56
        nto._make([ 20,   20, {'fdr_actual':2.00, 'sensitivity':2.00, 'specificity':2.00}]), # 1:25
        # nto._make([  4,    4, {'fdr_actual':4.00, 'sensitivity':3.00, 'specificity':3.00}]), # 0:04 0:05
        # nto._make([  2,    2, {'fdr_actual':4.00, 'sensitivity':3.00, 'specificity':3.00}]), # 0:01 0:02
    ]
    for ntd in params:
        run(seed, ntd)

if __name__:
    main()

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
