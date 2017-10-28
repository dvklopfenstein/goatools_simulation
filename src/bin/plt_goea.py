#!/usr/bin/env python
"""Simulate Gene Ontology Enrichment Analyses."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import collections as cx
from pkggosim.common.cli import get_args
from pkggosim.goea.run_all_params import RunParams
from pkggosim.goea.run_all import ExperimentsAll
from pkggosim.goea.utils import import_genes, import_goids, import_genes_all
from goatools_suppl.data.ensm2nt_mus import ensm2nt

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

def run(args, ntd, prt=sys.stdout):
    """Simulate Gene Ontology Enrichment Analyses."""
    randomize_truenull_assc = args.get('randomize_truenull_assc', 'orig')

    study_bg = "humoral_rsp"
    popnullmaskout = ['immune', 'viral_bacteria']
    # Gene Ontology Data
    genes_mus = ensm2nt.keys()  # Population genes
    params = {
        'log' : None if ntd.num_experiments > 4 else sys.stdout,
        'prefix' : 'fig_goea_{RND}'.format(RND=randomize_truenull_assc),
        'randomize_truenull_assc' : randomize_truenull_assc,
        'seed' : args.get('randomseed', None),
        'alpha' : 0.05,
        'method' : 'fdr_bh',
        'propagate_counts' : args.get('propagate_counts', False),
        'genes_population':genes_mus,
        'genes_study_bg':import_genes(study_bg),
        'goids_study_bg':import_goids(study_bg),
        'genes_popnullmaskout':import_genes_all(popnullmaskout),
        'association_file':'gene_association.mgi',
        'perc_nulls' : [100, 75, 50, 25, 0],
        'num_genes_list' : [4, 16, 64, 128],
        'num_experiments' : ntd.num_experiments, # Num. of simulated FDR ratios per experiment set
        'num_sims' : ntd.num_sims}   # Number of sims per experiment; used to create one FDR ratio
    objparams = RunParams(params)
    obj = ExperimentsAll(objparams) # RunParams

    title_cur = objparams.get_title()
    prt.write("Title: {S}\n".format(S=title_cur))
    prt.write("randomize_truenull_assc: {S}\n".format(S=randomize_truenull_assc))
    prt.write("{NT}\n".format(NT=ntd))

    rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    plt_items = ['fdr_actual', 'sensitivity', 'specificity']
    pltargs = {'dotsize':ntd.dotsize, 'title':title_cur,
               'xlabel':'Number of Genes in a Study Group',
               'ylabel':'Percentage of General Population Genes'}
    obj.run_all(study_bg, rpt_items, plt_items, **pltargs)
    objparams.prt_summary(sys.stdout)

def main():
    """Arguments for running all experiments."""
    args = get_args()
    nto = cx.namedtuple("NtRunParams", "num_experiments num_sims dotsize")
    #pylint: disable=bad-whitespace, no-member, line-too-long
    experiment_cnts = [
        nto._make([500, 1000, {'fdr_actual':0.70, 'sensitivity':0.50, 'specificity':0.50}]),
        nto._make([100, 1000, {'fdr_actual':0.95, 'sensitivity':0.60, 'specificity':0.60}]),
        nto._make([100,   30, {'fdr_actual':1.30, 'sensitivity':0.60, 'specificity':0.60}]),
        nto._make([ 50,   50, {'fdr_actual':2.00, 'sensitivity':0.70, 'specificity':0.70}]),
        nto._make([ 50,   20, {'fdr_actual':2.00, 'sensitivity':1.00, 'specificity':1.00}]), # 4:56
        nto._make([ 20,   20, {'fdr_actual':2.00, 'sensitivity':2.00, 'specificity':2.00}]), # 1:25
        nto._make([  4,    4, {'fdr_actual':4.00, 'sensitivity':3.00, 'specificity':3.00}]), # 0:04 0:05
        nto._make([  2,    2, {'fdr_actual':4.00, 'sensitivity':3.00, 'specificity':3.00}]), # 0:01 0:02
    ]
    ntd = experiment_cnts[args['idx_experiment_cnts']]
    run(args, ntd)

if __name__:
    main()

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
