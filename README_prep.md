# Preparatory: P-value and multiple-test simulations
The P-value and multiple-test correction simulations show how results vary with:
  * Number of P-values in a single P-value set; Ex: 10, 20, 50, 100, 500, 1k, or 10k P-values    
  * Number of sets of P-values in a single sample    
  * Number of P-values which have been set to be significant     

## Simulation List
 1. [All P-values chosen randomly; None are significant](README_prep.md#all-p-values-chosen-randomly-none-are-significant-1)
 2. [95% P-values chosen randomly; 5% are significant ](README_prep.md#95-p-values-chosen-randomly-5-are-significant)
 3. [90% P-values chosen randomly; 10% are significant ](README_prep.md#90-p-values-chosen-randomly-10-are-significant)
 4. [50% P-values chosen randomly; 50% are significant ](README_prep.md#50-p-values-chosen-randomly-50-are-significant)

**Methods for all 4 simulations:**    
Random P-values between 0.0 and 1.0 are generated using a uniform distribution.
It is expected that 5% of the randomly generated P-values will appear to be significant (<0.05) by chance.
We generate P-value sets in set sizes ranging from 10 P-values per set to 10,000 P-values per set.

## All P-values chosen randomly (None are significant)
Five percent of the randomly chosen uncorrected P-values are found to be significant, as expected.
These are shown in rose.
Upon doing multiple-test correction, practically no corrected P-values are found to be significant.
These are shown in green, but are so small that they appear to be a horizontal line around zero.
![Random pvals w/no significance](doc/images/pvalues_sig00.png)

## All P-values chosen randomly; None are significant
TBD

## 95% P-values chosen randomly; 5% are significant 
TBD

## 90% P-values chosen randomly; 10% are significant 
TBD

## 50% P-values chosen randomly; 50% are significant 
TBD

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
