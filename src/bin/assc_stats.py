#!/usr/bin/env python
"""Statistics for the protein-coding mouse gene association."""

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
    """Statistics for the protein-coding mouse gene association."""
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
    # Percentage of Ensembl mouse genes covered by GO annotations
    num_pc = len(params['genes_population'])
    num_assc = len(objassc.objassc_all.assc_geneid2gos)
    prt.write("{PERC:2.0f}% of {A} of {P} Mouse protein-coding genes are annotated by GO IDs.\n".format(
        PERC=100.0*num_assc/num_pc, P=num_pc, A=num_assc))


if __name__ == '__main__':
    main()

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
