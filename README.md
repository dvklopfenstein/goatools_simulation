# Stochastic GOEA Simulations
Stochastic simulations of multitudes of **Gene Ontology Enrichment Analyses** (GOEAs)
are used to generate simulated values of **FDR**, **sensitivity**, and **specificity**
for **GOEAs** run using [GOATOOLS](https://github.com/tanghaibao/goatools).

**Two categories of simulations are contained herein**:
  1. [**Preparatory**: Hypotheses and multiple-test simulations](doc/md/README_bhfdr.md); elements include:    
       * Benjamini/Hochberg FDR simulation only
  2. [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations](doc/md/README_goea.md); elements include:
       * Fisher's exact test    
       * Benjamini/Hochberg multiple test corrections
       * Gene ontology associations    

All simulations shown use [**Benjamini/Hochberg multiple test correction**](
http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)
with **alpha=0.05**.


## Figure List
  * [**Stochastic GOEA simulations:**](#stochastic-goea-simulations-1)
    * [Figure 1) GOEA Simulations with extremely significant P-values for enriched genes](
      #figure-1-goea-simulations-with-true-null-genes-associations-randomized)
    * [Figure 2) GOEA Simulations with some _Non-True Nulls_ unmarked](
      #figure-2-goea-simulations-with-original-associations)
  * [**Stochastic Benjamini/Hochberg-Only Simulations:**](#benjaminihochberg-only-simulations)
    * [Figure 3) Benjamini/Hochberg-Only Simulated FDRs](
      #figure-3-benjaminihochberg-only-simulated-fdrs)
    * [Figure 4) Benjamini/Hochberg-Only Simulated Sensitivities](
      #figure-4-benjaminihochberg-only-simulated-sensitivity)


## Stochastic GOEA simulations
Stochastic simulations of multitudes of **Gene Ontology Enrichment Analyses** (GOEAs) are
run on sets of randomly generated gene lists. The study gene lists in the simulations shown
range in sizes of 4 to 124 genes
and contain percentages of genes enriched in a particular set of biological processes
ranging from _no genes are enriched_ (100% Null) to _all genes are enriched_ (0% Null).
In the simulations shown, the enrichment is _Humoral response_.

The results are analyzed to determine the percentages of study genes which are enriched in
_Humoral response_ and are correctly discovered by the GOEAs.

### GOEA simulation Inputs
The simulation inputs are groups of genes tagged as either **False nulls** and **True nulls**:
  * _**False Null**_ (or _**Non-True Null**_) study genes are enriched in _Humoral response_
    by randomly chosing the study genes from any of the
    [124 _Humoral Response_ genes](/src/pkggosim/goea_data/genes_humoral_rsp.py).    
  * _**True Null**_ genes are randomly chosen from the large general population
    genes not enriched in _Humoral Response_.

### Figure 1) GOEA Simulations with _true null genes'_ associations randomized
To ensure that all **True Null** genes are real true nulls, the associations 
not associated with the _Humoral Response_ (i.e. non-true nulls) are randomly shuffled.

This simulates 
![figure](doc/logs/fig_goea_rnd_100to000_004to124_N00100_00030_humoral_rsp.png)
**Observations:**    
* Simulated FDRs are all under alpha (0.50) (A2-A4)     
* Simulated FDRs improve (become smaller) as the study set contains more _Humoral response_ genes (from A2 to A4)
  meaning there is a smaller percentage of false positives among the discoveries of genes 
  enriched in _Humoral response_.    
* Simulated FDRs are smaller for smaller study groups, like groups with 4 genes (A3, left boxplot),
  than for larger study group sizes, like groups with 124 genes (A3, right boxplot).
* **Sensitivity**: Almost all _Humoral response_ genes are found when the difference between alpha and the 
  P-values for _Humoral response_ is extreme. The difference is extreme in this example because the 
  associations are all randomized, so there is a large difference between Humoral gene enrichment and
  other enrichments; which in this case there are none due to randomization.    

### Figure 2) GOEA Simulations with original associations
Simulated FDRs appear higher than alpha (0.05) (A2-A4) because some study genes which are not 
enriched in _Humoral response_ actually have real enrichment in processes other than
_Humoral response_ in the associations, but were not tagged as _False Nulls_.
Compensating for untagged enrichments is shown in Figure 2.
![figure](doc/logs/fig_goea_100to000_004to124_N00050_00020_humoral_rsp.png)
**Observations:**    
* Small groups of study genes (e.g. 4 genes and sometimes 16 genes) show low sensitivity
  (blue bars in B2-B5, green bars in B2-B3),
  meaning study genes enriched in _Humoral Response_ in very small study gene groups may not be detected.

## Benjamini/Hochberg-Only Simulations
Simulations of the underlying Benjamini/Hochberg multiple test correction are a subset
of the GOEA simulations.
Study sets in these simulations contain hypotheses test results (P-values), versus
study sets in GOEA simulations which contain genes with various levels of enrichments.

### Simulation Inputs
The simulation inputs are groups of hypothesis test results (P-values) tagged as 
either **True nulls** and **Non-True nulls**:
  * **True Null**s are P-values randomly chosen from a uniform distribution of values between **0.0 to 1.0**.    
  * **Non-True Null**s (a.k.a **False Nulls**) are P-values randomly chosen from a uniform distribution of values between:    
    * **0.00 to 0.01** => **Extremely** different from the population.    
    * **0.00 to 0.03** => **Moderately** different from the population.    
    * **0.00 to 0.05** => **Minimally** different from the population.    

### Figure 3) Benjamini/Hochberg-Only Simulated FDRs
![FDR results](doc/logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png)
**Results show**:
  * The worst (highest) simulated FDR means are equal to the alpha (0.05)
    for all simulation sets with no **False null** s (A1, B1, and C1).    
  * As the percentage of true nulls drops, the FDR also drops;
    row 1, with 100% Null, has the highest mean FDR (0.05), while
    row 4, with 0% Null, has the lowest mean FDR (0.012).
  * The simulated mean FDRs are the same across all study group sizes. For example, in A2
    the leftmost column with the group of 4 tested hypotheses has the same mean FDR as
    the rightmost column in A2 with the group of 128 tested hypotheses.

### Figure 4) Benjamini/Hochberg-Only Simulated Sensitivity
![Sensitivity results](doc/logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_sensitivity.png)
**Observations:**    
* When non-true null P-values have extreme values, like below 0.01 when alpha is 0.05, 100% of _Non-true nulls_
  are discovered (A2-A4).
* Moderate non-true null P-values (B2-B3) are discovered less frequently than extreme P-values (A2-A3).
* Minimal non-true null P-values (C2-C4) are discovered even less frequently than moderate P-values (B2-B4).
* Smaller groups of tested hypotheses (B3, blue bar) have more discoveries than larger groups (B3, red bar).

Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
