# Hypotheses Simulation Results

## Multiple-test methods
3,600,000 simulations per multiple-test simulation method were run to create each figure:    
* [**FDR vs FWER**](#benjaminihochberg-non-negative-vs-bonferroni-one-step-correction)
  Contrast the simulation results **False Discovery Rate** (FDR) vs **Family-wise Error Rate**
  * 0:25:03 FDR Benjamini/Hochberg (non-negative)
  * 0:22:19 Bonferroni one-step correction
* [**Other FDR Simulation Results**](#fdr-simulation-results)
    * 0:26:00 [FDR Benjamini/Yekutieli (negative)](#fdr-benjaminiyekutieli-negative)
    * 0:24:17 [FDR adaptive Gavrilov-Benjamini-Sarkar](#fdr-adaptive-gavrilov-benjamini-sarkar)
    * 0:26:59 [FDR 2-stage Benjamini-Hochberg (non-negative)](#fdr-2-stage-benjamini-hochberg-non-negative)
    * 0:27:00 [FDR 2-stage Benjamini-Krieger-Yekutieli (non-negative)](#fdr-2-stage-benjamini-krieger-yekutieli-non-negative)
* [**Other FWER Simulation Results**](#fwer-simulation-results)
    * 0:25:50 [Holm-Sidak step-down method using Sidak adjustments](#holm-sidak-step-down-method-using-sidak-adjustments)
    * 1:18:43 [Hommel closed method based on Simes tests (non-negative)](#hommel-closed-method-based-on-simes-tests-non-negative)
    * 0:23:38 [Sidak one-step correction](#sidak-one-step-correction)
    * 0:23:36 [Simes-Hochberg step-up method (independent)](#simes-hochberg-step-up-method-independent)
    * N:NN:NN Holm step-down method using Bonferroni adjustments

## Benjamini/Hochberg (non-negative) vs Bonferroni one-step correction
  * [**FDR vs FWER: Corrected P-Values**](#fdr-vs-fwer-corrected-p-values)
  * [**FDR vs FWER: Sensitivity**](#fdr-vs-fwer-sensitivity)
  * [**FDR vs FWER: Specificity**](#fdr-vs-fwer-specificity)
### FDR vs FWER: Corrected P-Values
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_fdr_actual.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_bonferroni_fdr_actual.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_bonferroni_fdr_actual.png)    
### FDR vs FWER: Sensitivity
The x-axis shows two simulation parameters. The first parameter is the number of tested hypotheses in each simulation, which are 4, 16, and 128. The second x-axis parameter, labeled on the figure as Sig.<=, is the maximum P-value of randomly generated non-true null hypotheses test results. The y-axis shows the percentage of "True nulls". The simulated FDR values, as seen in the right-most text, drop dramatically from FDR=0.05 (SE=0.007) (row 1) to FDR=0.012 (SE=0.001) (row 4) as the percentage of "True nulls" drops.
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_sensitivity.png)    
![fig_hypoth_100to025_01to05_004to128_N00100_01000_bonferroni_sensitivity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_bonferroni_sensitivity.png)    
### FDR vs FWER: Specificity
The x-axis and y-axis parameters are the same as in Figure 3. The values shown in the panels are sensitivity ratios. Sensitivity is defined as the probability of detection of all non-true nulls. This figure shows that as the maximum P-values of non-true nulls gets closer to the user-specified alpha of 0.05, the sensitivity decreases. For example, 100% of all non-true nulls are discovered for all simulations that contain non-true nulls if they are 0.01 are less when the alpha is set to 0.05 (column A). As the maximum P-values of non-true nulls approaches alpha, fewer non-true nulls are detected (column B and C).
![fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_specificity.png](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_bh_specificity.png)    
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

Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved
