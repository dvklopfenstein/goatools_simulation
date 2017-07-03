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

def main(prt=sys.stdout):
    """Simulate Gene Ontology Enrichment Analyses."""
    args = get_args()
    nto = cx.namedtuple("NtRunParams", "num_experiments num_sims dotsize")
    ntd = nto._make([1, 2, {'fdr_actual':4.00, 'sensitivity':3.00, 'specificity':3.00}]) # 0:01 0:02
    randomize_truenull_assc = args.get('randomize_truenull_assc', 'orig')

    study_bg = "humoral_rsp"
    popnullmaskout = ['immune', 'viral_bacteria']
    # Gene Ontology Data
    genes_mus = ensm2nt.keys()  # Population genes
    params = {
        'prefix' : 'fig_goea_{RND}'.format(RND=randomize_truenull_assc),
        'randomize_truenull_assc' : randomize_truenull_assc,
        'seed' : args.get('randomseed', None),
        'alpha' : 0.05,
        'method' : 'fdr_bh',
        'genes_population':genes_mus,
        'genes_study_bg':import_genes(study_bg),
        'goids_study_bg':import_goids(study_bg),
        'genes_popnullmaskout':import_genes_all(popnullmaskout),
        'association_file':'gene_association.mgi',
        #'perc_nulls' : [100, 75, 50, 25, 0],
        'perc_nulls' : [50, 25], 
        #'num_genes_list' : [4, 16, 64, 128],
        'num_genes_list' : [64, 128], 
        'num_experiments' : ntd.num_experiments, # Num. of simulated FDR ratios per experiment set
        'num_sims' : ntd.num_sims}   # Number of sims per experiment; used to create one FDR ratio
    objparams = RunParams(params)
    obj = ExperimentsAll(objparams) # RunParams

    title_cur = objparams.get_title()
    prt.write("Title: {S}\n".format(S=title_cur))
    prt.write("randomize_truenull_assc: {S}\n".format(S=randomize_truenull_assc))
    prt.write("{NT}".format(NT=ntd))

    rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    plt_items = ['fdr_actual', 'sensitivity', 'specificity']
    pltargs = {'dotsize':ntd.dotsize, 'title':title_cur,
               'xlabel':'Number of Genes in a Study Group',
               'ylabel':'Percentage of General Population Genes',
               'ylim':{'fdr_actual':[-0.005, 0.50]}}
    obj.run_all(study_bg, rpt_items, plt_items, **pltargs)
    objparams.prt_summary(sys.stdout)


if __name__:
    main()

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
