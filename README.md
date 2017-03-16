# Simulations to Verify GOEA Results
Simulations in this repository are used to investigate the results of **Gene Ontology Enrichment Analyses** (GOEAs).    

#### For all simulations in this repo:    
  * The **alpha level** is set to **0.05**
  * The **multiple-test correction** used is **Benjamini/Hochberg False Discovery Rate**

#### There are two-levels of simulations:
  1. [**Preparatory**: P-value and multiple-test simulations](#preparatory-p-value-and-multiple-test-simulations)    
      * All P-values chosen randomly; None are significant
      * 95% P-values chosen randomly; 5% are significant 
      * 90% P-values chosen randomly; 10% are significant 
      * 50% P-values chosen randomly; 50% are significant 
  2. [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations](#goea-simulations)


## Preparatory: P-value and multiple-test simulations
The P-value and multiple-test correction simulations show how results vary with:
  * The number of P-values in one set    
  * The number of sets of P-values in one sample    
  * The number of P-values which have been set to be significant     

Then, we do Gene Ontology Enrichment Analyses simulations    

**Methods:**    
Random P-values between 0.0 and 1.0 are generated using a uniform distribution.
It is expected that 5% of the randomly generated P-values will appear to be significant (<0.05) by chance.
We generate P-value sets in set sizes ranging from 10 P-values per set to 10,000 P-values per set.

### All P-values chosen randomly (None are significant)
Five percent of the randomly chosen uncorrected P-values are found to be significant, as expected.
These are shown in rose.
Upon doing multiple-test correction, practically no corrected P-values are found to be significant.
These are shown in green, but are so small that they appear to be a horizontal line around zero.
![Random pvals w/no significance](doc/images/pvalues_sig00.png)

### All P-values chosen randomly; None are significant
TBD

### 95% P-values chosen randomly; 5% are significant 
TBD

### 90% P-values chosen randomly; 10% are significant 
TBD

### 50% P-values chosen randomly; 50% are significant 
TBD


## Consequent: GOEA simulations    
TBD

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
