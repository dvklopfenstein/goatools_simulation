# Preparatory: P-value and multiple-test simulations

## Simulation List
 1. [All P-values chosen randomly; None are significant](README_prep.md#1-all-p-values-chosen-randomly-none-are-significant-1)
 2. [95% P-values chosen randomly; 5% are significant ](README_prep.md#2-95-p-values-chosen-randomly-5-are-significant)
 3. [90% P-values chosen randomly; 10% are significant ](README_prep.md#3-90-p-values-chosen-randomly-10-are-significant)
 4. [50% P-values chosen randomly; 50% are significant ](README_prep.md#4-50-p-values-chosen-randomly-50-are-significant)


## Simulation Results
The **alpha-level** is set to **0.05** for all simulations on this page.   

### 1. All P-values chosen randomly (None are significant)
#### Conclusion
When no P-values are in fact significant,
multiple testing correctly reduces the P-values found to be significant to 0.0 or almost 0.0

#### Details
All P-values are randomly chosen from values ranging between 0.0 and 1.0 using the uniform distribution.
As expected, this results in five percent of the uncorrected P-values
to be found as significant (a.k.a < alpha), even though they are randomly generated
and in fact, are not significant (**shown in rose**).

Upon doing multiple-test correction, almost no corrected P-values are found to be significant.
These are shown in green, but appear to be a horizontal lines located at or close to zero.
This shows that multiple-test correction works when
all P-values are randomly generated resulting in no P-values that are actually significant.

Also notice that as the size of P-values in a single simulation increases,
the median value of the uncorrected P-values more closely approaches the 
0.05 alpha-level and the variation of the random P-values becomes much smaller,
centering around the 0.05 alpha-level.

**Conclusion**: Multiple testing correctly reduces the P-values found to be significant to be 0.0 or almost 0.0

![Random pvals w/no significance](doc/images/pvalues_sig00.png)

### 2. 95% P-values chosen randomly; 5% are significant 
TBD

### 3. 90% P-values chosen randomly; 10% are significant 
TBD

### 4. 50% P-values chosen randomly; 50% are significant 
TBD

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
