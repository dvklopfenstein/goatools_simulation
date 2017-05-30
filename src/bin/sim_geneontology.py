#!/usr/bin/env python
"""Runs a gene ontology analyses on gene rich in immune functions.

#################################################################
GENE ONTOLOGY SIMULATION
#################################################################

Two GOEA simulations are run with a set of study genes that are rich in immune functions:

  1) Input: Current GO-geneid associations.
     Expected result: All study genes are enriched

  2) Input: Randomly shuffled GO-geneid associations
     Expected result:  No study genes are enriched


*****************************************************************
Results log from the run on May, 22, 2017:
*****************************************************************

SIMULATION RESULTS ON 2017-05-22:

  SETTINGS AND GO-DAG VERSION:
    Multitest Params: alpha(0.05) method(fdr_bh)
    GO-DAG version:   go-basic.obo: fmt(1.2) rel(2017-05-20) 48,661 GO Terms

  SIMULATION RESULTS:
      2,545 significant GO terms found for 2157 immune genes in actual association
          0 significant GO terms found for 2157 immune genes in random association

*****************************************************************
Discussion
*****************************************************************
Both gene ontology simulations produced the expected results:

The first simulation indicated that all study genes were enriched, as expected.

The second simulation indicated that no study genes were enriched, as expected.


"""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from random import shuffle

#from pkggosim.data_geneids_rich_immune import geneids as genes_immune
from pkggosim.genes_immune import GENES
from pkggosim.randseed import RandomSeed32
from pkggosim.goeasim_obj import GoeaSimObj

from goatools_suppl.data.ensmusg2sym import ensm2sym
from goatools_suppl.proj_data import GoatoolsDataMaker


def main(seed, prt=sys.stdout):
    """Return a list of all GO IDs associated with protein-coding mouse genes."""
    seed = RandomSeed32(seed)
    # 1. Get objects needed for a gene-ontology simulation: pop_genes, assc, GO-DAG
    obj = GoeaSimObj(alpha=0.05, method='fdr_bh')
    genes_mus = ensm2sym.keys()  # Population genes
    genes_immune = list(GENES)   # Study genes
    assoc_ens2gos = GoatoolsDataMaker.get_assoc_data("gene_association.mgi", genes_mus)
    # 2. GET STUDY GENE LENGTHES (Study genes will be chosen randomly, but user specifies length)
    study_lens = [pow(2, exp) for exp in reversed(range(2, 13))]  # 4, 8, ..., 256, 512, 1024, 2048, 4096
    # 2. SIMULATE SIGNIFICANCE TO IMMUNE: Population is all mouse genes
    results_sig = []
    for study_len in study_lens:
        shuffle(genes_immune)
        results_sig.append(obj.run_actual_assc(assoc_ens2gos, genes_mus, genes_immune[:study_len]))
    # 3. SIMULATE NO SIGNIFICANCE:
    results_rnd = []
    for study_len in study_lens:
        shuffle(genes_immune)
        results_rnd.append(obj.run_random_assc(assoc_ens2gos, genes_mus, genes_immune[:study_len]))
    # 4. REPORT RESULTS:
    obj.rpt_results(prt, results_sig, results_rnd)
    seed.prt(prt)


if __name__ == '__main__':
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
