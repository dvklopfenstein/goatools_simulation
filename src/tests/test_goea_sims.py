#!/usr/bin/env python
"""Simulate a Gene Ontology Enrichment Analysis (GOEA) on one set of study genes."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from pkggosim.goea_sims import ManyGoeaSims
from pkggosim.goea_utils import get_study2genes, get_assoc_data
from pkggosim.goea_objbg import DataBackground
from goatools_suppl.data.ensmusg2sym import ensm2sym

def main(prt=sys.stdout):
    """Test ManyGoeaSims in ./src/pkggosim/goea_sims.py"""
    alpha = 0.05
    method = 'fdr_bh'


    study_genes_lens = [4, 8, 16, 32, 64]
    num_study_genes = study_genes_lens[2]
    num_null = num_study_genes/2 # 50% Null
    # Use study genes seen in population
    study_genes_bg = [g for g in study2genes['humoral_rsp'] if g in objbg.pop_genes]

    params = {
        'num_sims':10,
        'num_study_genes':16,
        'perc_null':50,
        'num_null':8,
        'study_genes_bg':study_genes_bg}
    objsim = ManyGoeaSims(params, study_genes_bg, objbg)
    objsim.prt_summary(prt)
    for nt_tfpn in objsim.nts_tfpn:
        print nt_tfpn

def get_objbg():
    """Return object holding all params/data structures used in all sims (eg GO-DAG)."""
    study2genes = get_study2genes()
    genes_mus = ensm2sym.keys()  # Population genes
    assc_geneid2gos = get_assoc_data("gene_association.mgi", genes_mus)
    objbg = DataBackground(alpha, method, genes_mus, assc_geneid2gos)

if __name__ == '__main__':
    main()

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
