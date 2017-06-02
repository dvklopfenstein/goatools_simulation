#!/usr/bin/env python
"""Simulate a Gene Ontology Enrichment Analysis (GOEA) on one set of randomly generated study genes."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
from pkggosim.goea_objbg import GoeaSimObj
from pkggosim.goea_sim import GoeaSim
from pkggosim.goea_objrun_prelim import RunGoeas
from goatools_suppl.data.ensmusg2sym import ensm2sym

def main():
    hypoth_qty = 8
    num_null = 4
    alpha = 0.05
    method = 'fdr_bh'

    genes_mus = ensm2sym.keys()  # Population genes
    assoc_geneid2gos = get_assoc_data("gene_association.mgi", genes_mus)

    objbg = RunGoeas(alpha, method, genes_mus, assc_geneid2gos)

    #objsim = GoeaSim(hypoth_qty, num_null, multi_params)
    objsim = RunGoeas(num_study_genes, num_null, study_genes_bg, objbg)

if __name__ == '__main__':
    main()

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
