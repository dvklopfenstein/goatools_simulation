#!/usr/bin/env python
"""Simulate small set of GOEAs to see full TP/FP/FN/TN gene GO counts."""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
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
NTO = cx.namedtuple("NtRunParams", "num_experiments num_sims dotsize")

def main(run_all, prt=sys.stdout):
    """Simulate small set of GOEAs to see full TP/FP/FN/TN gene GO counts."""
    args = get_args()
    #pylint: disable=no-member
    #ntd = nto._make([1, 2, {'fdr_actual':4.00, 'sensitivity':3.00, 'specificity':3.00}]) # 0:01
    ntd = NTO._make([4, 4, {'fdr_actual':4.00, 'sensitivity':3.00, 'specificity':3.00}])
    randomize_truenull_assc = args.get('randomize_truenull_assc', 'orig')
    fout_log = "log/plt_goea_small/plt_goea_small_{NAME}.log".format(NAME=randomize_truenull_assc)

    study_bg = "humoral_rsp"
    popnullmaskout = ['immune', 'viral_bacteria']
    # Gene Ontology Data
    with open(os.path.join(REPO, fout_log), 'w') as log:
        params = {
            'img' : 'pdf',  # png or pdf
            'title': args['title'],
            'log' : log,
            'prefix' : 'fig_goea_{RND}'.format(RND=randomize_truenull_assc),
            'randomize_truenull_assc' : randomize_truenull_assc,
            'seed' : args.get('randomseed', None),
            'alpha' : 0.05,
            'method' : 'fdr_bh',
            'propagate_counts' : args['propagate_counts'],
            'genes_population':ensm2nt.keys(), # Mouse protein-coding genes
            'genes_study_bg':import_genes(study_bg),
            'goids_study_bg':import_goids(study_bg),
            'genes_popnullmaskout':import_genes_all(popnullmaskout),
            'association_file':'gene_association.mgi',

            'perc_nulls' : [100, 75, 50, 25, 0] if run_all else [25],
            'num_genes_list' : args['genes'], # [4, 16, 64, 128] if run_all else [128],

            'num_experiments' : ntd.num_experiments, # Num. simulated FDR ratios per experiment set
            'num_sims' : ntd.num_sims}   # Number sims per experiment; used to create one FDR ratio
        obj = ExperimentsAll(RunParams(params)) # RunParams
        sys.stdout.write("  propagate_counts={P}\n".format(P=obj.pobj.params['propagate_counts']))

        title_cur = obj.pobj.get_title()
        prt.write("TITLE: {S}\n".format(S=title_cur))
        prt.write("GENES: {S}\n".format(S=params['num_genes_list']))
        prt.write("randomize_truenull_assc: {S}\n".format(S=randomize_truenull_assc))
        prt.write("{NT}\n".format(NT=ntd))

        rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
        plt_items = ['fdr_actual', 'sensitivity', 'specificity']
        pltargs = {'dotsize':ntd.dotsize, 'title':title_cur,
                   'xlabel':'Number of Genes in a Study Group',
                   'ylabel':'Percentage of General Population Genes',
                   #'ylim':{'fdr_actual':[-0.005, 0.50]}
                  }
        obj.run_all(study_bg, rpt_items, plt_items, **pltargs)
        obj.pobj.prt_summary(log)
        obj.pobj.prt_summary(sys.stdout)
        sys.stdout.write("  propagate_counts={P}\n".format(P=obj.pobj.params['propagate_counts']))
        sys.stdout.write("  WROTE: {LOG}\n".format(LOG=fout_log))
    sys.stdout.write("ARGS: {ARGS}\n".format(ARGS=args))


if __name__:
    # Either run full set of sims or reduced sims where false positive genes appear
    RUN_ALL = False if len(sys.argv) != 1 and sys.argv[1] == 'False' else True
    main(RUN_ALL)

# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
