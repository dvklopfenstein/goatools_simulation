#!/usr/bin/env python
"""Simulate Gene Ontology Enrichment Analyses."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import collections as cx
from pkggosim.goea_run_all_params import RunParams
from pkggosim.goea_run_all import ExperimentsAll
from pkggosim.goea_utils import import_var
from goatools_suppl.data.ensmusg2sym import ensm2sym

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

def main(randomseed, num_experiments, num_sims, dotsize):
    """Simulate Gene Ontology Enrichment Analyses."""
    # Gene Ontology Data
    genes_mus = ensm2sym.keys()  # Population genes
    params = {
        'seed' : randomseed,
        'alpha' : 0.05,
        'method' : 'fdr_bh',
        'genes_population':genes_mus,
        'genes_study_bg':import_var("pkggosim.genes_b_cell_activation", "GENES"),
        'genes_popnullmaskout':import_var("pkggosim.genes_immune", "GENES"),
        'association_file':'gene_association.mgi',
        'perc_nulls' : [100, 75, 50, 25],
        'num_genes_list' : [4, 16, 128],
        'num_experiments' : num_experiments, # Number of simulated FDR ratios in an experiment set
        'num_sims' : num_sims}   # Number of sims per experiment; used to create one FDR ratio
    rpt_items = ['fdr_actual', 'sensitivity', 'specificity', 'pos_pred_val', 'neg_pred_val']
    objparams = RunParams(params)
    obj = ExperimentsAll(objparams)
    obj.run() # Runs simulations and Loads obj.expsets
    # run_sim(obj, rpt_items, dotsize)
    obj.prt_seed(prt)

def run_sim(obj, rpt_items, dotsize):
    """Run Hypotheses Simulation using Benjamini/Hochberg FDR."""
    desc_pat = '{P0:03}to{PN:03}_{Q0:03}to{QN:03}_N{NEXP:05}_{NSIM}'
    desc_str = obj.get_fout_img(desc_pat)
    fout_log = os.path.join('doc/logs', 'fig_goea_{DESC}.log'.format(DESC=desc_str))
    # Report and plot simulation results
    with open(os.path.join(REPO, fout_log), 'w') as prt:
        obj.prt_summary(prt)
        obj.prt_params(prt)
        obj.prt_seed(prt)
        obj.prt_experiments_means(prt, rpt_items)
        obj.prt_experiments_stats(prt, rpt_items)
        title = "GOEA Simulations"
        plts = [('fdr_actual', 'FDR'),
                ('sensitivity', 'Sensitivity')]
        for attr, name in plts:
            base_img = 'fig_goea_{DESC}_{ATTR}.png'.format(ATTR=attr, DESC=desc_str)
            fout_img = os.path.join(REPO, 'doc/logs', base_img)
            obj.plt_box_tiled(fout_img, attr, name, dotsize=dotsize, title=title)
        sys.stdout.write("  WROTE: {LOG}\n".format(LOG=fout_log))

if __name__:
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    NTOBJ = cx.namedtuple("NtRunParams", "num_experiments num_sims dotsize")
    #pylint: disable=bad-whitespace, no-member
    PARAMS = [
        # NTOBJ._make([500, 1000, {'fdr_actual':0.70, 'sensitivity':0.50}]),
        # NTOBJ._make([100, 1000, {'fdr_actual':0.95, 'sensitivity':0.60}]),
        NTOBJ._make([ 10,   10, {'fdr_actual':2.00, 'sensitivity':1.00}]),
    ]
    for ntd in PARAMS:
        main(SEED, ntd.num_experiments, ntd.num_sims, ntd.dotsize)

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
