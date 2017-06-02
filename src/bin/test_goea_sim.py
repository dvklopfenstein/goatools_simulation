#!/usr/bin/env python
"""Simulate a Gene Ontology Enrichment Analysis (GOEA) on one set of study genes."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

from pkggosim.goea_sim import GoeaSim
from pkggosim.goea_utils import get_study2genes, get_assoc_data
from pkggosim.goea_objrun_all import RunGoeas
from goatools_suppl.data.ensmusg2sym import ensm2sym

def main():
    """Test GoeaSim in ./src/pkggosim/goea_sim.py"""
    hypoth_qty = 8
    num_null = 4
    alpha = 0.05
    method = 'fdr_bh'

    study2genes = get_study2genes()

    genes_mus = ensm2sym.keys()  # Population genes
    assc_geneid2gos = get_assoc_data("gene_association.mgi", genes_mus)

    objbg = RunGoeas(alpha, method, genes_mus, assc_geneid2gos)

    #objsim = GoeaSim(hypoth_qty, num_null, multi_params)
    study_genes_lens = [4, 8, 16, 32, 64]
    num_study_genes = study_genes_lens[1]
    study_genes_bg = study2genes['humoral_rsp']
    objsim = GoeaSim(num_study_genes, num_null, study_genes_bg, objbg)

if __name__ == '__main__':
    main()

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
