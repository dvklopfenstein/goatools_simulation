#!/usr/bin/env python
"""GOEA association stats."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys

from pkggosim.goea.objassc import DataAssc
from goatools_suppl.data.ensm2nt_mus import ensm2nt
from goatools.base import get_godag
from goatools.statsdescribe import StatsDescribe

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

def main(prt=sys.stdout):
    """Return a list of all GO IDs associated with protein-coding mouse genes."""
    godag = get_godag()
    params = {
        'association_file' : os.path.join(REPO, 'gene_association.mgi'),
        'genes_population' : ensm2nt.keys()} # Population genes
    objassc = DataAssc(params, godag)
    # Statistics for number of genes per GO in the mouse association for protein-coding genes
    go2numgenes = {go:len(genes) for go, genes in objassc.go2genes.items()}
    objdesc = StatsDescribe("GOs", "{:>5.0f}")
    objdesc.prt_hdr(prt, name="\nname      ")
    objdesc.prt_data("# genes/GO", go2numgenes.values(), prt)
    # Statistics for number of GOs per gene in the mouse association for protein-coding genes
    gene2numgos = {gene:len(gos) for gene, gos in objassc.objassc_all.assc_geneid2gos.items()}
    objdesc = StatsDescribe("genes", "{:>5.0f}")
    objdesc.prt_hdr(prt, name="\nname      ")
    objdesc.prt_data("# GOs/gene", gene2numgos.values(), prt)


if __name__ == '__main__':
    main()

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
