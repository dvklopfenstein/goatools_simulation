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

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys

from pkggosim.randseed import RandomSeed32
from pkggosim.genes_immune import GENES as GENES_IMMUNE
from pkggosim.genes_cytokine_rsp import GENES as GENES_CYTOKINE
from pkggosim.genes_humoral_rsp import GENES as GENES_HUMORAL
from pkggosim.genes_viral_bacteria import GENES as GENES_VIRAL
from pkggosim.goea_objrun import RunGoeas

from goatools_suppl.data.ensmusg2sym import ensm2sym
from goatools_suppl.proj_data import GoatoolsDataMaker


def main(seed, prt=sys.stdout):
    """Return a list of all GO IDs associated with protein-coding mouse genes."""
    seed = RandomSeed32(seed)
    # 1. Get objects needed for a gene-ontology simulation: pop_genes, assc, GO-DAG
    genes_mus = ensm2sym.keys()  # Population genes
    objrun = RunGoeas(
        {'alpha':0.05, 'method':'fdr_bh'},
        genes_mus,  # Population genes
        GoatoolsDataMaker.get_assoc_data("gene_association.mgi", genes_mus)) # Associations: ens2gos
    # 2. GET STUDY GENE LENGTHES (Study genes will be chosen randomly, but user specifies length)
    study_lens = [pow(2, exp) for exp in reversed(range(2, 13))]  # 4, 8, ... 1024, 2048, 4096
    results_list = []
    study_list = [
        ('immune', list(GENES_IMMUNE)),
        ('viral/bacteria', list(GENES_VIRAL)),
        ('cytokine_rsp', list(GENES_CYTOKINE)),
        ('humoral_rsp', list(GENES_HUMORAL))]
    # 3. SIMULATE 100% SIGNIFICANCE
    for study_desc, study_genes in study_list:
        results_list.extend(objrun.run_goeas(study_lens, study_genes, study_desc, perc_null=0))
    # 4. SIMULATE NO SIGNIFICANCE (Associations are random)
    for study_desc, study_genes in study_list:
        results_list.extend(objrun.run_goeas(study_lens, study_genes, study_desc, perc_null=100))
    # 5. REPORT RESULTS:
    objrun.prt_results(results_list)
    seed.prt(prt)


if __name__ == '__main__':
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
