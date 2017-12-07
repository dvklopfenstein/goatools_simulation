#!/usr/bin/env python
"""Simulate Gene Ontology Enrichment Analyses."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

# import os
# import sys
from pkggosim.common.cli import get_args
from pkggosim.goea.basename import Basename


def main():
    """Simulate Gene Ontology Enrichment Analyses."""
    args = get_args()
    obj = Basename()

    modules = [
        'pkggosim.data.orig_noprune_enriched_ntn2_p0_100to000_004to124_N00002_00002_genes',
        'pkggosim.data.orig_noprune_enriched_ntn2_p0_100to000_004to124_N00002_00002_goids',
    ]
    # randomize_truenull_assc = args.get('randomize_truenull_assc', 'orig')

    # study_bg = "humoral_rsp"
    # popnullmaskout = ['immune', 'viral_bacteria']
    # # Gene Ontology Data
    # genes_mus = ensm2nt.keys()  # Population genes
    # params = {
    #     'log' : None if ntd.num_experiments > 4 else sys.stdout,
    #     'prefix' : 'fig_goea_{RND}'.format(RND=randomize_truenull_assc),
    #     'randomize_truenull_assc' : randomize_truenull_assc,
    #     'seed' : args.get('randomseed', None),
    #     'alpha' : 0.05,
    #     'method' : 'fdr_bh',
    #     'propagate_counts' : args.get('propagate_counts', False),
    #     'genes_population':genes_mus,
    #     'genes_study_bg':import_genes(study_bg),
    #     'goids_study_bg':import_goids(study_bg),
    #     'genes_popnullmaskout':import_genes_all(popnullmaskout),
    #     'association_file':'gene_association.mgi',
    #     'perc_nulls' : [100, 75, 50, 25, 0],
    #     #'num_genes_list' : [4, 16, 64, 128],
    #     #'num_genes_list' : [4, 8, 16, 24, 32, 40, 48, 56, 64],
    num_genes_list = args['genes']
    #     'num_experiments' : ntd.num_experiments, # Num. of simulated FDR ratios per experiment set
    #     'num_sims' : ntd.num_sims}   # Number of sims per experiment; used to create one FDR ratio
    # objparams = RunParams(params)
    # #### obj = ExperimentsAll(objparams) # RunParams

    # title_cur = objparams.get_title()
    # prt.write("TITLE: {S}\n".format(S=title_cur))
    # prt.write("GENES: {S}\n".format(S=params['num_genes_list']))
    # prt.write("randomize_truenull_assc: {S}\n".format(S=randomize_truenull_assc))
    # prt.write("{NT}\n".format(NT=ntd))

    #### rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    plt_items = ['fdr_actual', 'sensitivity', 'specificity']
    pltargs = {'dotsize':None, 'title':args['title'],
               'dpi':600, 'img':'all',
               'xlabel':'Number of Genes in a Study Group',
               'ylabel':'Percentage of General Population Genes'}
    for mod in modules: 
        obj.plt_mod('log/dat_goea_plot', mod, plt_items, pltargs)
    #### plt_box_tiled(base_img_genes, plt_items, 'genes', **pltargs)
    #### plt_box_tiled(base_img_goids, plt_items, 'goids', **pltargs) # GOIDS
    #### obj.run_all(study_bg, rpt_items, plt_items, **pltargs)
    #### objparams.prt_summary(sys.stdout)

if __name__:
    main()


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
