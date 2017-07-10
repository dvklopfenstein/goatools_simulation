# Hypotheses Simulation Results

## Multiple-test methods
3,600,000 simulations per multiple-test simulation method were run to create each figure:    
* FDR vs FWER    
  Contrast the simulation results **False Discovery Rate** (FDR) vs **Family-wise Error Rate**
  * 0:25:03 [FDR Benjamini/Hochberg (non-negative)](#fdr-benjaminihochberg-non-negative)
  * 0:22:19 [Bonferroni one-step correction](#bonferroni-one-step-correction)
* Other FDR Simulation Results
    * 0:26:00 [FDR Benjamini/Yekutieli (negative)](#fdr-benjaminiyekutieli-negative)
    * 0:24:17 [FDR adaptive Gavrilov-Benjamini-Sarkar](#fdr-adaptive-gavrilov-benjamini-sarkar)
    * 0:26:59 [FDR 2-stage Benjamini-Hochberg (non-negative)](#fdr-2-stage-benjamini-hochberg-non-negative)
    * 0:27:00 [FDR 2-stage Benjamini-Krieger-Yekutieli (non-negative)](#fdr-2-stage-benjamini-krieger-yekutieli-non-negative)
* FWER Simulation Results
    * 0:25:50 [Holm-Sidak step-down method using Sidak adjustments](#holm-sidak-step-down-method-using-sidak-adjustments)
    * 1:18:43 [Hommel closed method based on Simes tests (non-negative)](#hommel-closed-method-based-on-simes-tests-non-negative)
    * 0:23:38 [Sidak one-step correction](#sidak-one-step-correction)
    * 0:23:36 [Simes-Hochberg step-up method (independent)](#simes-hochberg-step-up-method-independent)
    * N:NN:NN Holm step-down method using Bonferroni adjustments

## FDR vs FWER
### FDR Benjamini/Hochberg (non-negative)
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_specificity.png)    

### Bonferroni one-step correction
![fig_hypoth_100to025_01to05_004to128_N00100_01000_bonferroni_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_bonferroni_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_bonferroni_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_bonferroni_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_bonferroni_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_bonferroni_specificity.png)    

## FDR Simulation Results
### FDR Benjamini/Yekutieli (negative)
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_by_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_by_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_by_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_by_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_by_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_by_specificity.png)    

### FDR adaptive Gavrilov-Benjamini-Sarkar
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_gbs_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_gbs_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_gbs_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_gbs_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_gbs_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_gbs_specificity.png)    

### FDR 2-stage Benjamini-Hochberg (non-negative)
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbh_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbh_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbh_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbh_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbh_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbh_specificity.png)    

### FDR 2-stage Benjamini-Krieger-Yekutieli (non-negative)
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbky_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbky_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbky_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbky_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbky_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_tsbky_specificity.png)    

## FWER Simulation Results
### Holm-Sidak step-down method using Sidak adjustments
![fig_hypoth_100to025_01to05_004to128_N00100_01000_holm-sidak_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_holm-sidak_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_holm-sidak_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_holm-sidak_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_holm-sidak_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_holm-sidak_specificity.png)    

### Hommel closed method based on Simes tests (non-negative)
![fig_hypoth_100to025_01to05_004to128_N00100_01000_hommel_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_hommel_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_hommel_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_hommel_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_hommel_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_hommel_specificity.png)    

### Sidak one-step correction
![fig_hypoth_100to025_01to05_004to128_N00100_01000_sidak_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_sidak_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_sidak_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_sidak_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_sidak_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_sidak_specificity.png)    

### Simes-Hochberg step-up method (independent)
![fig_hypoth_100to025_01to05_004to128_N00100_01000_simes-hochberg_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_simes-hochberg_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_simes-hochberg_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_simes-hochberg_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_simes-hochberg_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_simes-hochberg_specificity.png)    

## Misc
### 19)   20.   1 of   1 ./fig_hypoth_100to025_01to05_004to128_N00020_00200_sensitivity.png    
![fig_hypoth_100to025_01to05_004to128_N00020_00200_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00020_00200_sensitivity.png)    
### 23)   24.   1 of   2 ./fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png)    
### 45)   46.   1 of   2 ./fig_hypoth_100to025_01to05_004to128_N00100_01000_sensitivity.png    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_sensitivity.png)    
### 52)   53.   1 of   1 ./fig_hypoth_100to025_01to05_004to128_N00500_01000_fdr_actual.png    
![fig_hypoth_100to025_01to05_004to128_N00500_01000_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00500_01000_fdr_actual.png)    
### 53)   54.   1 of   1 ./fig_hypoth_100to025_01to05_004to128_N00500_01000_sensitivity.png    
![fig_hypoth_100to025_01to05_004to128_N00500_01000_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00500_01000_sensitivity.png)    
### 56)   57.   2 of   2 ./tmpdir/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png](./tmpdir/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png)    
### 57)   58.   2 of   2 ./tmpdir/fig_hypoth_100to025_01to05_004to128_N00100_01000_sensitivity.png    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_sensitivity.png](./tmpdir/fig_hypoth_100to025_01to05_004to128_N00100_01000_sensitivity.png)    

Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved
