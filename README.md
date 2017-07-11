# Stochastic GOEA Simulations
Stochastic simulations of multitudes of **Gene Ontology Enrichment Analyses** (GOEAs)
are used to generate simulated values of **FDR**, **sensitivity**, and **specificity**
for **GOEAs** run using [GOATOOLS](https://github.com/tanghaibao/goatools).

**Two categories of simulations are contained herein**:
  1. [**Preparatory**: Hypotheses and multiple-test simulations](doc/md/README_bhfdr.md); elements include:    
       * FDR or FWER simulations only
  2. [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations](doc/md/README_goea.md); elements include:
       * Fisher's exact test
       * [Benjamini/Hochberg FDR multiple test corrections](http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)
       * Gene ontology associations    

All simulations shown use **alpha=0.05**.


## Figure List
  * [**Stochastic GOEA simulations:**](#stochastic-goea-simulations-1)
    * [Figure 1) GOEA Simulations with extremely significant P-values for enriched genes](
      #figure-1-goea-simulations-with-true-null-genes-associations-randomized)
    * [Figure 2) GOEA Simulations with some truly enriched genes (_Non-True Nulls_) left unmarked](
      #figure-2-goea-simulations-with-original-associations)
  * [**Stochastic Benjamini/Hochberg-Only Simulations:**](#benjaminihochberg-only-simulations)
    * [Figure 3) Benjamini/Hochberg-Only Simulated FDRs](
      #figure-3-benjaminihochberg-only-simulated-fdrs)
    * [Figure 4) Benjamini/Hochberg-Only Simulated Sensitivities](
      #figure-4-benjaminihochberg-only-simulated-sensitivity)

## Stochastic GOEA simulations

### Table of Contents

* [Abstract](#abstract)
* [Introduction](#introduction)    
  * [GOEA simulation Inputs](goea-simulation-inputs)     
    * Randomly Generated Gene lists
    * Associations with True-Null Genes
    * Associations with None-True-Null Genes
* [GOEA Simulations](#goea-simulation-inputs):    
  * Simulations with randomly-generated gene lists    
    * Simulations viewing only Enriched GOEA results    
  * Simulations with randomly-generated gene lists and randomly-generated associations    

### Abstract
First, we ran simulations using randomly generated gene lists containing varying
percentages of True Null genes. The simulation results contained unacceptably high
FDRs for some gene groups containing 64 or 124 genes.
![FAIL_orig_pruneN_all](doc/md/images/fig1b_FAIL_goea_orig_noprune_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)

Upon investigation, it was found the high numbers of false positives were often from:
  * GO IDs had an unusually high number of gene associations
  * Purified, rather than enriched

If the simulations were re-run, but only the enriched results were used in reports and figures,
the simulations PASSED resulting in FDRs that were very close to zero.
![PASS_orig_pruneN_enr](doc/md/images/fig3b_PASS_goea_orig_noprune_enriched_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)

If the simulations were re-run, but with ~30 GO IDs out of 17,000+ GO IDs in the
association stripped out of the association, the simulations also PASSED.
The 30 GO IDs were chosen to be purged because they were associated with more than 1000 genes.
![PASS_orig_pruneY_pru](doc/md/images/fig2b_PASS_goea_orig_pruned_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)

#### Stress tests
Upon doing a stress test by randomizing the associations for True-Null genes
prior to simulation, the "enriched-gene" simulations FAILed, but the
"30-GOs-Purged" simulations PASSed.

#### Randomize Association and View Enriched Genes Only
![FAIL_rand_pruneN_enr](doc/md/images/fig4b_FAIL_goea_rand_noprune_enriched_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)
#### Purge 30 GOs from Association, then Randomize
![PASS_rand_pruneY_pru](doc/md/images/fig5b_PASS_goea_rand_pruned_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)


### Introduction
Stochastic simulations of multitudes of **Gene Ontology Enrichment Analyses**
(GOEAs) are run on sets of randomly generated gene lists. The study gene lists
in the simulations shown range in sizes of 4 to 124 genes and contain
percentages of genes enriched in a particular set of biological processes
ranging from _no genes are enriched_ (100% Null) to _all genes are enriched_ (0%
Null).  In the simulations shown, the gene enrichment under study is _Humoral
response_ (HR).

The results are analyzed to determine the percentages of study genes which are enriched in
_Humoral response_ and are correctly discovered by the GOEAs.

#### GOEA simulation Inputs

##### Inputs: Randomly Generated Gene lists
The simulation inputs are groups of genes tagged as either **False nulls** and **True nulls**:
  * _**False Null**_ (a.k.a. _**Non-True Null**_) study genes are enriched in _Humoral response_
    by randomly chosing the study genes from any of the
    [124 _Humoral Response_ genes](/src/pkggosim/goea_data/genes_humoral_rsp.py).    
  * _**True Null**_ genes are randomly chosen from the large general population
    genes not enriched in _Humoral Response_.

##### Inputs: Associations with True-Null Genes
For each gene, there is a list of GO IDs that are associated with the gene.
Genes can be True-Null (general population) genes or Non-True-Null 
(Humoral Response) genes.

In the first simulations, we use the associations for Non-True Nulls that are
read from the association file downloaded from the Gene Ontology Consortium.

In the second stress-test simulations, we randomly shuffle the associations for the
True-Null genes.

The nominal case of randomly shuffling all associations for both True-Null
genes and Non-True Null genes yeilds simulations that correctly report no discoveries.

##### Inputs: Associations with None-True-Null Genes
We run three simulations for every simulation set.

### GOEA Simulations
#### Simulations with randomly-generated gene lists
The original GOEA simulations using randomly generated gene lists showed
unacceptably high simulated FDR values that are above the alpha of 0.05 (Panels
A3 and A4 in the Figure).

Upon investigation, the simulation details showed that most _False Positives_ are significant GO terms that are:
  * Purified rather than Enriched and/or
  * Associated with over 1,000 genes    

![fig1b_FAIL_goea_orig_noprune_ntn2](doc/md/images/fig1b_FAIL_goea_orig_noprune_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)

#### Simulations viewing only Enriched GOEA results
Resimulating while only viewing enriched GOEA results still showed elevated FDRs (A2, A3, A4).

EXPLANATION: Genes enriched in the area of interest, **Humoral Response** (HR) can also be legitimately enriched in other biological functions.
If the non-HR genes are not properly marked as **Non-True-Nulls**, they will appear on the plots as elevated FDRs as seen below.
![fig3a_fail_goea_orig_noprune_enriched_ntn1](doc/md/images/fig3a_okay_goea_orig_noprune_enriched_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)

SIMULATION PASSes: Resimulating the GOEAs, but only viewing the enriched results yielded passing simulations
if the associations of the **Non-True-Null** (Humoral Response) genes are purged of GO terms significant for other biological functions.
![fig3b_PASS_goea_orig_noprune_enriched_ntn2](doc/md/images/fig3b_PASS_goea_orig_noprune_enriched_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)

#### Randomly-generated True-Null Associations
The next step is testing the robustness of GOEA simulations using
randomly-generated associations for genes which are _True-Nulls_ (aka HR genes).

The associations for _Non-True-Nulls_ (aka Humoral Response genes) are not 
randomized to test that the GOEAs successfully discover the randomly chosen
Humoral Response genes in each study group.

ADJUSTMENT:
GO terms associated with large numbers of genes, when randomized in an association,
can cause the simulated FDRs to appear to be too high. Because a real association is not mixed
to the extent as seen in randoms, randomizing GO associations with large numbers of genes
yields GOEA results which are unrealistically pessimistic.

The GOEA simulation results using random associations are more realistic if the top ~30 GO IDs out of 17,000+
GO IDs that are associated with > 1,000 mouse protein-coding genes are removed.

The trend of rising FDR values as the study size increases is an artifact of GOEA results
appearing to be significant due to randomization.
![fig5b_goea_rand_pruned_ntn2](images/fig5b_PASS_goea_rand_pruned_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)

## Stochastic GOEA simulations
### Figure 1) GOEA Simulations with _true null genes'_ associations randomized
To ensure that all **True Null** genes are real true nulls, the associations 
not associated with the _Humoral Response_ (i.e. non-true nulls) are randomly shuffled.

![figure](doc/logs/fig_goea_rnd_100to000_004to124_N00100_00030_humoral_rsp.png)
**Observations:**    
* Simulated FDRs are all under alpha (0.50) (A2-A4)     
* Simulated FDRs improve (become smaller) as the study set contains more _Humoral response_ genes (from 
  A2 with 25% _Humoral Response_ genes to A4 with 75% _Humoral Response_ genes)
  meaning there is a smaller percentage of false positives among the discoveries of genes 
  enriched in _Humoral response_.    
* Simulated FDRs are better (smaller) for smaller study groups,
  like groups with 4 genes (A3, left boxplot),
  than for larger study group sizes, like groups with 124 genes (A3, right boxplot).
* **Sensitivity**:
  * Almost all _Humoral response_ genes are found when the difference between alpha and the 
    P-values for _Humoral response_ is extreme. The difference is extreme in this example because the 
    associations are all randomized, so there is a large difference between Humoral gene enrichment and
    other enrichments; which in this case there are none due to randomization.    
  * The sensitivity is poor (B2 left bar, mean value 2%) when the study size is 4 genes
    and 3 of the 4 genes do not differ from the population (True Nulls).
  * The mean sensitivity is about 86% (B3 left bar) when the study gene size is 4 genes and
    half of the genes do not differ from the population (True Nulls).

### Figure 2) GOEA Simulations with original associations
This figure demonstrates the effect of *not* randomizing the genes intended to be _True Nulls_ 
(same as the population).

Simulated FDRs appear higher than alpha (0.05) (A2-A4) because some study genes which are not 
enriched in _Humoral response_ actually have real enrichment in processes other than
_Humoral response_ in the associations, but were not tagged as _False Nulls_.
Compensating for untagged enrichments is shown in Figure 1 above.

![figure](doc/logs/fig_goea_100to000_004to124_N00050_00020_humoral_rsp.png)
**Observations:**    
* Small groups of study genes (e.g. 4 genes and sometimes 16 genes) show low sensitivity
  (blue bars in B2-B5, green bars in B2-B3),
  meaning study genes enriched in _Humoral Response_ in very small study gene groups may not be detected.
* The poor simulated FDR values (A2-A4 for groups of 64 and 124 genes) 
  are an artifact of not properly marking the input genes as enriched when they are
  actually enriched in something other than _Humoral response_.

## Benjamini/Hochberg-Only Simulations
Simulations of the underlying Benjamini/Hochberg multiple test correction are a subset
of the GOEA simulations.
Inputs to these simulations are hypotheses test results (P-values), versus the
inputs in GOEA simulations which are gene lists containing various percentages of enrichments.

### Simulation Inputs
The simulation inputs are groups of hypothesis test results (P-values) tagged as 
either **True nulls** and **Non-True nulls**:
  * **True Null**s are P-values randomly chosen from a uniform distribution of values between **0.0 to 1.0**.    
  * **Non-True Null**s (a.k.a **False Nulls**) are P-values randomly chosen from a uniform distribution of values between:    
    * **0.00 to 0.01** => **Extremely** different from the population.    
    * **0.00 to 0.03** => **Moderately** different from the population.    
    * **0.00 to 0.05** => **Minimally** different from the population.    

### Figure 3) Benjamini/Hochberg-Only Simulated FDRs
![FDR results](doc/logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_fdr_actual.png)
**Results show**:
  * The worst (highest) simulated FDR means are equal to the alpha (0.05)
    for all simulation sets with 100% **True Null** s (A1, B1, and C1).    
  * As the percentage of true nulls drops, the FDR also drops;    
    * row 1, with **100% True Null**, has the highest mean FDR (0.05), while
    * row 4, with   **0% True Null**, has the lowest mean FDR (0.012).
  * The simulated mean FDRs are the same across all study group sizes. For example, in A2    
    * the leftmost boxplot with blue dots showing the groups of 4 tested hypotheses has the same mean FDR as
    * the rightmost boxplot with red dots showing the groups of 128 tested hypotheses.

### Figure 4) Benjamini/Hochberg-Only Simulated Sensitivity
![Sensitivity results](doc/logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_sensitivity.png)
**Observations:**    
* **100%** of **Non-True Nulls** are **discovered** if their **uncorrected P-Value** is **Extreme** (below 0.01 when alpha is 0.05) (A2-A4)
* Moderate non-true null P-values (B2-B3) are discovered less frequently than extreme P-values (A2-A3).
* Minimal non-true null P-values (C2-C4) are discovered even less frequently than moderate P-values (B2-B4).
* Smaller groups of tested hypotheses (B3, blue bar) have more discoveries than larger groups (B3, red bar).

Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
