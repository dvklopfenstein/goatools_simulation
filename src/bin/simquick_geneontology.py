#!/usr/bin/env python
"""Quick preview of Gene Ontology Simulation Results (GOEAs).

#################################################################
GENE ONTOLOGY SIMULATION
#################################################################

Two GOEA types simulations are run by this script to
simulate 0% 'True Null' and 100% 'True Null':

  1) 0% True Null:
     Uses Current GO-geneid associations.
     Expected result: All study genes are enriched

  2) 100% True Null:
     Randomly shuffles GO-geneid associations.
     Expected result:  No study genes are enriched


*****************************************************************
Discussion
*****************************************************************

Population and study gene sets
------------------------------
The set of population genes for each simulation was the ~22k Ensembl protein-coding mouse genes.
The study gene set for each GOEA simulation ranged in size from 4 genes to over 2,000 genes.
The study gene sets were chosen from various large sets of
genes in broad categories, like immune. The broad immune group
contained over 2,000 genes. The groups viral/bacteria, cytokine response
and humoral response contained 592, 227, and 124 genes respectively.

To simulate no significance, we randomly shuffled the original
association before each simulation. As expected, all simulations
using the randomly shuffled associations showed no significance.

To simulate significance, we used the original association
and randomly chose a set of study genes from one of the broad categories.
100% or nearly 100% of study genes were found significant
until the difference between the size broad category genes
from which the actual study genes were chosen became too great.

For example, if the study genes were chosen from the 124 "humoral response"
genes, all study genes returned as significant until the study size
was reduced to 4 genes.


*****************************************************************
Results log from the run on May, 22, 2017:
*****************************************************************

SIMULATION RESULTS ON 2017-05-22:

  SETTINGS AND GO-DAG VERSION:
    Multitest Params: alpha(0.05) method(fdr_bh)
    GO-DAG version:   go-basic.obo: fmt(1.2) rel(2017-05-20) 48,661 GO Terms

SIMULATION RESULTS:
Sig. GOs Study genes % True Null   assc Max Genes Study Name
-------- ----------- ----------- ------ --------- ----------
     2       4/    4          0% actual  2,122 immune
     0       0/    8          0% actual  2,122 immune
     0       0/   16          0% actual  2,122 immune
    22      24/   32          0% actual  2,122 immune
    33      61/   64          0% actual  2,122 immune
    85     127/  128          0% actual  2,122 immune
   173     254/  256          0% actual  2,122 immune
   579     512/  512          0% actual  2,122 immune
 1,388    1024/ 1024          0% actual  2,122 immune
 3,077    2048/ 2048          0% actual  2,122 immune
 2,667    2122/ 2122          0% actual  2,122 immune
     0       0/    4          0% actual    592 viral/bacteria
     2       5/    8          0% actual    592 viral/bacteria
     0       0/   16          0% actual    592 viral/bacteria
    11      27/   32          0% actual    592 viral/bacteria
    14      57/   64          0% actual    592 viral/bacteria
    90     128/  128          0% actual    592 viral/bacteria
   318     256/  256          0% actual    592 viral/bacteria
   704     512/  512          0% actual    592 viral/bacteria
   783     592/  592          0% actual    592 viral/bacteria
     0       0/    4          0% actual    227 cytokine_rsp
     2       5/    8          0% actual    227 cytokine_rsp
    13      16/   16          0% actual    227 cytokine_rsp
    18      31/   32          0% actual    227 cytokine_rsp
    57      64/   64          0% actual    227 cytokine_rsp
   214     128/  128          0% actual    227 cytokine_rsp
   480     227/  227          0% actual    227 cytokine_rsp
     0       0/    4          0% actual    124 humoral_rsp
    17       8/    8          0% actual    124 humoral_rsp
    19      16/   16          0% actual    124 humoral_rsp
    31      32/   32          0% actual    124 humoral_rsp
    53      64/   64          0% actual    124 humoral_rsp
    97     124/  124          0% actual    124 humoral_rsp
     0       0/    4        100% random  2,122 immune
     0       0/    8        100% random  2,122 immune
     0       0/   16        100% random  2,122 immune
     0       0/   32        100% random  2,122 immune
     0       0/   64        100% random  2,122 immune
     0       0/  128        100% random  2,122 immune
     0       0/  256        100% random  2,122 immune
     0       0/  512        100% random  2,122 immune
     0       0/ 1024        100% random  2,122 immune
     0       0/ 2048        100% random  2,122 immune
     0       0/ 2122        100% random  2,122 immune
     0       0/    4        100% random    592 viral/bacteria
     0       0/    8        100% random    592 viral/bacteria
     0       0/   16        100% random    592 viral/bacteria
     0       0/   32        100% random    592 viral/bacteria
     0       0/   64        100% random    592 viral/bacteria
     0       0/  128        100% random    592 viral/bacteria
     0       0/  256        100% random    592 viral/bacteria
     0       0/  512        100% random    592 viral/bacteria
     0       0/  592        100% random    592 viral/bacteria
     0       0/    4        100% random    227 cytokine_rsp
     0       0/    8        100% random    227 cytokine_rsp
     0       0/   16        100% random    227 cytokine_rsp
     0       0/   32        100% random    227 cytokine_rsp
     0       0/   64        100% random    227 cytokine_rsp
     0       0/  128        100% random    227 cytokine_rsp
     0       0/  227        100% random    227 cytokine_rsp
     0       0/    4        100% random    124 humoral_rsp
     0       0/    8        100% random    124 humoral_rsp
     0       0/   16        100% random    124 humoral_rsp
     0       0/   32        100% random    124 humoral_rsp
     0       0/   64        100% random    124 humoral_rsp
     0       0/  124        100% random    124 humoral_rsp



"""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys

from pkggosim.common.randseed import RandomSeed32
from pkggosim.goea.objrun_prelim import RunPrelim
from pkggosim.goea.utils import get_study2genes
from pkggosim.goea.objbase import DataBase
from pkggosim.goea.objassc import DataAssc
from goatools_suppl.data.ensm2nt_mus import ensm2nt
# from goatools.base import get_godag

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

def main(seed, prt=sys.stdout):
    """Return a list of all GO IDs associated with protein-coding mouse genes."""
    objrnd = RandomSeed32(seed)
    # 1. Get objects needed for a gene-ontology simulation: pop_genes, assc, GO-DAG
    objrun = get_objrun(alpha=0.05, method='fdr_bh', propagate_counts=False)
    study2genes = get_study2genes()
    objrun.set_maskout(study2genes['immune'].union(study2genes['viral_bacteria']))
    # 2. GET STUDY GENE LENGTHES (Study genes will be chosen randomly, but user specifies length)
    study_lens = [pow(2, exp) for exp in reversed(range(2, 13))]  # 4, 8, ... 1024, 2048, 4096
    results_list = []
    # Gene quantities:  2,092        592             227             124              15
    # Studies include: immune viral_bacteria cytokine_rsp humoral_rsp gamma_delta_t
    # 3. SIMULATE 100% SIGNIFICANCE
    for study_desc, study_genes in study2genes.items():
        results_list.extend(objrun.run_goeas(study_lens, study_genes, study_desc, perc_null=0))
    # 4. SIMULATE NO SIGNIFICANCE (Associations are random)
    for study_desc, study_genes in study2genes.items():
        results_list.extend(objrun.run_goeas(study_lens, study_genes, study_desc, perc_null=100))
    # 5. REPORT RESULTS:
    objrun.prt_summary(prt)
    objrun.prt_results(results_list)
    objrnd.prt(prt)

def get_objrun(alpha=0.05, method='fdr_bh', propagate_counts=False):
    """Get run object."""
    params = {
        'title': "Quick Simunation",
        'association_file': os.path.join(REPO, 'gene_association.mgi'),
        'genes_population': ensm2nt.keys()}   # Population genes
    objbase = DataBase(alpha, method, propagate_counts)
    return RunPrelim(objbase, DataAssc(params, objbase.go_dag))


if __name__ == '__main__':
    SEED = int(sys.argv[1], 0) if len(sys.argv) != 1 else None
    main(SEED)

# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
