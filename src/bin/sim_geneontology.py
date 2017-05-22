#!/usr/bin/env python
"""Runs a gene ontology analyses on gene rich in immune functions."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from goatools_suppl.data.gosimdata import GoSimData
from goatools_suppl.data.ensmusg2sym import ensm2sym
from goatools_suppl.proj_data import GoatoolsDataMaker
from goatools_suppl.proj_sections import SECTIONS


def main(prt=sys.stdout):
    """Return a list of all GO IDs associated with protein-coding mouse genes."""
    # Population is all protein-coding mouse genes
    mus_genes = set(ensm2sym.keys())
    assoc_ens2gos = GoatoolsDataMaker.get_assoc("gene_association.mgi", mus_genes)


if __name__ == '__main__':
    main()

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
