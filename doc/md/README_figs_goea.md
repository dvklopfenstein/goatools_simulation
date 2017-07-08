# GOEA Simulations


## Table of Contents
  1. [**Introduction and Definitions**](#1-introduction-and-definitions)
  2. **First Simulations**:
     * **FAIL**: [First Simulations w/Original Associations unchanged.]()    
     * Simulations with Random True Null Associations look similar to those with Original Associations.    
  3. **PASS: Modification 1**:    
     Upon printing simulation result details, observed that most _False Positives_ are GO terms associated with over 1,000 genes. 
     Therefore, re-run simulation after removing 30 GO terms out of > 17,000 Mouse GO terms that are assc. w/> 1,000 genes.   
     * **PASS**: Original Associations minus the [~30 GO IDs assc w/>1000 genes](#go-terms-removed).
  4. **PASS: Modification 2**:
     Upon printing simulation result details, observed that many _False Positives_ are GO terms associated with over 1,000 genes
     are **enriched**, rather than purified. 
     Therefore, use original associations, but only evaluate **enriched** GOEA results.


## 1) Introduction and Definitions

1. **Simulation Inputs**
   * [**A) Study gene sets**](#a-study-gene-sets)
   * **Associations:**    
     * [**B1) Associations for True Nulls (Population genes)**](#b1-associations-for-true-nulls-population-genes)
     * [**B2) Associations for Non-True Nulls (Humoral Response genes)**](#b2-associations-for-non-true-nulls-humoral-response-genes)
2. **Simulation Results**
   * **PASS**: Simulated FDR means are all **below** alpha (0.05)     
   * **FAIL**: Some simulated FDR means are **above** alpha (0.05)    

### A) Study Gene Sets
Inputs gene sets are randomly chosen from either of two groups:
* **True-Null genes**: Chosen from the population of **Mouse protein-coding genes** having GO associations (~18,000 genes).    
* **Non-True Null genes**: Chosen from any of **124 Humoral Response genes**.

### B1) Associations for True Nulls (Population genes)    
Input gene/GO associations in the simulations are one of:
* **Original Associations** (~17,000)
* **Original Associations minus ~30 GO IDs associated with over 1,000 genes**
* **Randomly shuffled Associations**
* **Randomly shuffled Associations minus ~30 GO IDs associated with over 1,000 genes**

### B2) Associations for Non-True Nulls (Humoral Response genes)
* **Original Associations**    
  Genes enriched in _Humoral Response_ can also be enriched in other processes.
  Therefore, simulations may correctly return significant GO IDs other than _Humoral Response_ GOs.
  The original associations will contain both _Humoral Reponse_ genes properly marked as _Non-True Null_ genes
  and other genes correctly enriched in other functions, but not marked as _Non-True Null_.
* **Original Associations minus signficant GO IDs that are **not** Humoral Response GOs 
* Original Associations minus all GO IDs except Humoral Response GOs    
  These simulations are expected to PASS    




## 2) FAIL: First Simulations using Original Associations
**Simulated FDRs exceed alpha(0.05) in the original simulation.**    
**False Positives are seen in all 3 images** showing various sets of 'Non-True Nulls' (aka Humoral Response genes)    

  * a) [Non-True Nulls use original associations](#2a-fail-non-true-nulls-use-original-associations)
  * b) [Non-True Nulls use original associations stripped of other significant GOs](#2b-fail-false-positives---non-true-nulls-wother-significant-discoveries-marked)
  * c) [Non-True Nulls only contain Humoral Response GO IDs](#2c-fail-false-positives---non-true-nulls-wonly-humoral-response-gos)

### 2a) FAIL: Non-True Nulls use original associations
  * **A2** -> 124 genes, 64 genes
  * **A3** -> 124 genes, 64 genes
  * **A4** -> 124 genes    
![fig1a_FAIL_goea_orig_noprune_ntn1](images/fig1a_FAIL_goea_orig_noprune_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)

### 2b) FAIL: False Positives - Non-True Nulls w/other significant discoveries marked
  * **A3** -> 124 genes, 64 genes
  * **A4** -> 124 genes    
![fig1b_FAIL_goea_orig_noprune_ntn2](images/fig1b_FAIL_goea_orig_noprune_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)

### 2c) FAIL: False Positives - Non-True Nulls w/ONLY Humoral Response GOs
  * **A3** -> 124 genes, 64 genes
  * **A4** -> 124 genes    
![fig1c_FAIL_goea_orig_noprune_ntn3](images/fig1c_FAIL_goea_orig_noprune_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png)


## 2) PASS: Attempt 1 -> Remove [~30 GO IDs assc w/>1000 genes](#go-terms-removed). Otherwise Original Associations unchanged.
**All 3 Simulations PASS**

### 2a) PASS: Non-True Nulls not marked
Cause the appearance of an acceptable level of false positives.    
![fig2a_PASS_goea_orig_pruned_ntn1](images/fig2a_PASS_goea_orig_pruned_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)
### 2b) PASS: Non-True Nulls assc. w/significant discoveries are marked
Very low False Positives marked.
![fig2b_PASS_goea_orig_pruned_ntn2](images/fig2b_PASS_goea_orig_pruned_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)
### 2c) PASS: None-True Nulls w/ONLY Humoral Response GOs
![fig2c_PASS_goea_orig_pruned_ntn3](images/fig2c_PASS_goea_orig_pruned_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png)


## 3) PASS: Attempt 2 -> Original Association. Enriched GOEA results.
No change to Association. Retain enriched GOEA results and do not assess the purified GOEA results.    

### 3a) OKAY: Non-True Nulls not marked
![fig3a_fail_goea_orig_noprune_enriched_ntn1](images/fig3a_okay_goea_orig_noprune_enriched_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)
### 3b) PASS: Non-True Nulls assc. w/significant discoveries are marked
![fig3b_PASS_goea_orig_noprune_enriched_ntn2](images/fig3b_PASS_goea_orig_noprune_enriched_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)
### 3c) PASS: None-True Nulls w/ONLY Humoral Response GOs
![fig3c_PASS_goea_orig_noprune_enriched_ntn3](images/fig3c_PASS_goea_orig_noprune_enriched_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png)


## 4) Okay? Using Enriched GOEAs acceptable? Try Randoms
### 4a) Okay?
![fig4b_goea_rand_noprune_enriched_ntn1](images/fig4a_okay_goea_rand_noprune_enriched_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)
### 4b) Okay? -  Truly enriched not properly marked
![fig4c_goea_rand_noprune_enriched_ntn2](images/fig4b_okay_goea_rand_noprune_enriched_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)
### 4c) PASS
![fig4d_goea_rand_noprune_enriched_ntn3](images/fig4c_PASS_goea_rand_noprune_enriched_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png)


## 5) PASS: Prune GOs w/>1000 genes from Association acceptable? Try Randoms
### 5a) PASS: Non-True Nulls not marked
![fig5a_goea_rand_pruned_ntn1](images/fig5a_PASS_goea_rand_pruned_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)
### 5b) PASS: Non-True Nulls assc. w/significant discoveries are marked
![fig5b_goea_rand_pruned_ntn2](images/fig5b_PASS_goea_rand_pruned_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)
### 5c) PASS: None-True Nulls w/ONLY Humoral Response GOs
![fig5c_goea_rand_pruned_ntn3](images/fig5c_PASS_goea_rand_pruned_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png)

## 1a-rand) FAIL Randomized True Nulls
Same as 'Original Association', but _True Nulls_ are randomized.    
Results are FAIL and similar to [Original Association]
### 1a-rand) FAIL: Non-True Nulls not marked
![fig1a_goea_rand_noprune_ntn1](images/fig1aR_goea_rand_noprune_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)
### 1b-rand) FAIL: Non-True Nulls assc. w/significant discoveries are marked
![fig1b_goea_rand_noprune_ntn2](images/fig1bR_goea_rand_noprune_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)
### 1c-rand) FAIL: None-True Nulls w/ONLY Humoral Response GOs
![fig1c_goea_rand_noprune_ntn3](images/fig1cR_goea_rand_noprune_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png)

# ALL RAND) PASS: Various runs of All Associations Randomized
**PASS**: No change to Association.
![fig_goea_rand_noprune_all](images/fig1R_goea_rand_noprune_all_100to000_004to124_N00020_00020_humoral_rsp.png)
**PASS**: No change to Association. Retain enriched GOEA results and do not assess the purified GOEA results.    
![fig4_goea_rand_noprune_enriched_all](images/fig9a_PASS_goea_rand_noprune_enriched_all_100to000_004to124_N00020_00020_humoral_rsp.png)
**PASS**: GOs with more than 1000 genes pruned
![fig9_goea_rand_pruned_all](images/fig9b_PASS_goea_rand_pruned_all_100to000_004to124_N00020_00020_humoral_rsp.png)


## 2a) Original Association, enriched GOs only 
Includes 'unmarked' Non-True Null genes found to be enriched. Purified GO terms are removed.    
'Non-True Null' gene associations are the untouched original gene associations with GO terms    
![fig_goea_orig_noprune_enriched_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_orig_noprune_enriched_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)
### Original Association, enriched GOs only 
![fig_goea_orig_noprune_enriched_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_orig_noprune_enriched_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)
### Original Association, enriched GOs only 
![fig_goea_orig_noprune_enriched_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_orig_noprune_enriched_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png)

## 2b) Randomized Association, enriched GOs only
![fig_goea_rand_noprune_enriched_all_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_rand_noprune_enriched_all_100to000_004to124_N00020_00020_humoral_rsp.png)
### Randomized Association, enriched GOs only
![fig_goea_rand_noprune_enriched_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_rand_noprune_enriched_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)
### Randomized Association, enriched GOs only
![fig_goea_rand_noprune_enriched_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_rand_noprune_enriched_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)
### Randomized Association, enriched GOs only
![fig_goea_rand_noprune_enriched_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_rand_noprune_enriched_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png)

## 3a) Association w/30 GOs removed
![fig_goea_orig_pruned_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_orig_pruned_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)    
### Association w/30 GOs removed
![fig_goea_orig_pruned_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_orig_pruned_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)    
### Association w/30 GOs removed
![fig_goea_orig_pruned_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_orig_pruned_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png)    

## 3b) Randomized Association w/30 GOs removed
![fig_goea_rand_pruned_all_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_rand_pruned_all_100to000_004to124_N00020_00020_humoral_rsp.png)    
### Randomized Association w/30 GOs removed
![fig_goea_rand_pruned_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_rand_pruned_ntn1_100to000_004to124_N00020_00020_humoral_rsp.png)    
### Randomized Association w/30 GOs removed
![fig_goea_rand_pruned_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_rand_pruned_ntn2_100to000_004to124_N00020_00020_humoral_rsp.png)    
### Randomized Association w/30 GOs removed
![fig_goea_rand_pruned_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png](../logs/fig_goea_rand_pruned_ntn3_100to000_004to124_N00020_00020_humoral_rsp.png)    

## GO terms removed
32 out of 17,276 GO terms are associated with more than 1,000 genes

| # genes | GO ID    |NS| dcnt | Level | Depth | L1 | Description
|---------|----------|--|------|-------|-------|----|---------------
| 1,807 | GO:0006810 |BP|1,648 | L03 | D03 | F   | transport
| 1,027 | GO:0007275 |BP|   22 | L03 | D03 | CEG | multicellular organism development
| 1,242 | GO:0007165 |BP|  724 | L02 | D04 | AB  | signal transduction
| 1,618 | GO:0007186 |BP|  100 | L03 | D05 | AB  | G-protein coupled receptor signaling pathway
| 1,077 | GO:0007608 |BP|    0 | L06 | D06 | G   | sensory perception of smell
| 2,064 | GO:0006355 |BP|  479 | L06 | D09 | A   | regulation of transcription, DNA-templated
| 1,842 | GO:0006351 |BP|   88 | L05 | D09 | BD  | transcription, DNA-templated
| 1,022 | GO:0045944 |BP|  109 | L08 | D11 | A   | positive regulation of transcription from RNA polymerase II promoter
| 6,921 | GO:0016020 |CC|  204 | L01 | D01 | E   | membrane
| 1,660 | GO:0005576 |CC|    4 | L01 | D01 | G   | extracellular region
| 3,704 | GO:0005886 |CC|    3 | L02 | D02 | AE  | plasma membrane
| 1,440 | GO:0005615 |CC|    0 | L02 | D02 | F   | extracellular space
| 5,296 | GO:0016021 |CC|   57 | L03 | D03 | C   | integral component of membrane
| 6,132 | GO:0005737 |CC|   24 | L03 | D03 | A   | cytoplasm
| 1,063 | GO:0005887 |CC|   15 | L04 | D04 | AC  | integral component of plasma membrane
| 2,764 | GO:0005829 |CC|    3 | L04 | D04 | A   | cytosol
| 1,127 | GO:0005856 |CC|   38 | L04 | D05 | AD  | cytoskeleton
| 5,704 | GO:0005634 |CC|   21 | L04 | D05 | AD  | nucleus
| 1,671 | GO:0005739 |CC|    6 | L04 | D05 | AD  | mitochondrion
| 1,349 | GO:0005783 |CC|    5 | L04 | D05 | AD  | endoplasmic reticulum
| 2,586 | GO:0070062 |CC|    0 | L04 | D05 | DF  | extracellular exosome
| 1,811 | GO:0005654 |CC|    0 | L04 | D05 | AB  | nucleoplasm
| 1,179 | GO:0005794 |CC|    0 | L04 | D05 | AD  | Golgi apparatus
| 1,656 | GO:0016740 |MF|2,418 | L02 | D02 | A   | transferase activity
| 1,514 | GO:0016787 |MF|1,618 | L02 | D02 | A   | hydrolase activity
| 4,544 | GO:0005515 |MF|1,005 | L02 | D02 | B   | protein binding
| 1,417 | GO:0003723 |MF|  173 | L04 | D04 | B   | RNA binding
| 1,727 | GO:0003677 |MF|  155 | L04 | D04 | B   | DNA binding
| 1,657 | GO:0000166 |MF|   53 | L03 | D04 | B   | nucleotide binding
| 2,945 | GO:0046872 |MF|   32 | L04 | D04 | B   | metal ion binding
| 1,050 | GO:0004984 |MF|    1 | L04 | D05 | CD  | olfactory receptor activity
| 1,368 | GO:0005524 |MF|    0 | L05 | D08 | B   | ATP binding


Copyright (C) 2016-2017. DV Klopfenstein, Haibao Tang. All rights reserved.
