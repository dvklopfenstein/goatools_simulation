#!/usr/bin/env python
"""Simulate a Gene Ontology Enrichment Analysis (GOEA) on one set of study genes."""
# TBD: REMOVE THIS TEST?

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkggosim.goea.sims import ManyGoeaSims
from pkggosim.goea.utils import get_assoc_data
from pkggosim.goea.objassc import DataAssc
from goatools_suppl.data.ensm2nt_mus import ensm2nt
from pkggosim.goea.utils import get_genes, get_genes_all

def main(prt=sys.stdout):
    """Test ManyGoeaSims in ./src/pkggosim.goea.sims.py"""
    study_genes_lens = [4, 8, 16, 32, 64]
    num_study_genes = study_genes_lens[2]
    num_null = num_study_genes/2 # 50% Null
    # Use study genes seen in population
    study_genes_bg = get_genes('humoral_rsp')
    genes_mus = ensm2nt.keys()  # Population genes
    assc_geneid2gos = get_assoc_data("gene_association.mgi", genes_mus)
    objbg = DataAssc(0.05, 'fdr_bh', genes_mus, assc_geneid2gos)

    params = {
        'randomize_truenull_assc':False,
        'num_sims':10,
        'num_study_genes':16,
        'perc_null':50,
        'num_null':8,
        'study_genes_bg':study_genes_bg,
        'genes_population':set(genes_mus)}
    objsim = ManyGoeaSims(params, study_genes_bg, objbg)
    objsim.prt_summary(prt)
    for nt_tfpn_genes in objsim.nts_tfpn_genes:
        print nt_tfpn_genes

if __name__ == '__main__':
    main()

# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
