# [**Preparatory**: Hypotheses and multiple-test simulations]()
These preparatory Benjamini/Hochberg FDR (False Discovery Rate) simulations
are used to establish proof of concept for the architecture and implementation
for the simulation methodology used in both levels of simulations listed below:
  1. **Benjamini/Hochberg FDR simulation only** (described here)     
  2. **Gene Ontology Enrichment Results (GOEA) simulations**    


## Table of Contents
  * [**Figures** for all multiple-test corrections](README_figs_hypoth.md)
  * [Abstract](#abstract)
  * [Introduction](#introduction)
  * [Methods](#methods)
  * [Discussion](#discussion)
  * [Results](#results)
  * [Conclusion](#conclusion)


## Abstract
Simulations of various sizes of study groups containing tested hypotheses with
various percentages of true nulls are run. The results are analyzed to
determine the percentages the false null hypotheses recovered from thousands of
simulations.

The observations are:
  * Simulated FDRs stay below the guaranted alpha value.    
  * Simulated FDRs fall below the alpha as the percentage of true nulls in the study group fall    
  * All non-true null (actually significant hypotheses tests) are discovered if 
    their uncorrected P-Value is below 0.01 when the alpha is 0.50    
  * The non-true null discovery rate (sensitivity) drops as the 
    their uncorrected P-Value rises and becomes close to the alpha (0.50)    


## Methods

### 1. Data is randomly generated
A hypothesis test result is a P-value.

P-values are generated randomly using a uniform distribution for each simulation:    
  * **True Null** hypothesis tests are randomly chosen from 0.0 to 1.0    
  * **False Null** hypothesis tests are randomly chosen from three sets of values:    
    * **Extreme Probability**: P-values are randomly chosen from 0.00 to 0.01    
    * **Moderate Probability**: P-values are randomly chosen from 0.00 to 0.03    
    * **Minimal Probability**: P-values are randomly chosen from 0.00 to 0.05    

### 2. Multiple test correction is done
A Benjamin/Hochberg multiple test correction is run on a set of P-values.

For each uncorrected P-value in the input set, a multiple test correction returns 
**corrected P-values** and a **reject** value.

### 3. Collect, report, and visualize results

In the table below:
  * The **rows** contain the uncorrected P-values of the tested hypotheses and each corresponding null value (True/False).    
  * The **columns** contain the Benjamini/Hochberg reject value (True/False) for each tested hypothesis.

|                     | **Fail to reject Null**	        | **Reject Null**
|---------------------|---------------------------------|-----------------
| **True Null Genes**	| True Negative	                  | False Positive (Type I Error)
| **False Null Gene**	| False Negative (Type II Error)	| True Positive

Combining the input and output information, the counts of true positives, true negatives,
false positives, and false negatives are obtained according to the table above. Many
simulations are run, resulting in a probability of true positives, true negative, false
positives, and false negatives. Many more simulations are completed, resulting in a
multitiude of probabilities having a distribuition which may be plotted and analyzed.

## Discussion
These simulations demonstrate that the mean False Discovery Rates (FDRs),
center around the alpha-level set by the user (0.05) when all hypotheses are true (row 1 in figure 1),
but is smaller otherwise (rows 2-4 in figure 1).

As larger percentages of the hypotheses are "Non-true null hypotheses"
(i.e. Null should be rejected; there is a difference between the study items and the population items),
the simulated FDR drops dramatically below alpha(0.05).

All simulations use [**Benjamini/Hochberg multiple test correction**](
http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)
with **alpha=0.05**.

## Results
### Simulated FDR Ratios
![FDR results](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png)
The x-axis shows two simulation parameters.
The first parameter is the _number of tested hypotheses_ in each simulation, with group sizes of 4, 16, and 128.
The second parameter, labeled on the figure as _**Sig.<=**_, is the _maximum P-value_,
of randomly generated non-true null hypotheses test results.
The y-axis shows the _percentage of "True nulls"_.
The simulated FDR drops dramatically
As the percentage of "True nulls" drops causing the number of "non-true nulls" to rise.

The maximum P-value for **false null hypotheses** is seen here with values:
  * **0.01**; Extremely significant compared to alpha=0.05 (column A)     
  * **0.03**; Somewhat significant compared to alpha=0.05 (column B)    
  * **0.05**; Significance can be close to the alpha=0.05 (column C)    
Maximum significance for false null hyotheses has no affect on the simulated FDR values.
But it has a large affect on the sensitivity of the test.

### Simulated Sensitivity Ratios
Sensitivity is also known as the _true positive rate_, _recall_, or _probability of detection_.
![Sensitivity results](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_sensitivity.png)
**At an alpha of 0.05, 100% of "non-true null hypotheses" are detected when their P-Values are <= 0.01**
as seen in column A.
The top row shows sensitivity is 0% because all hypotheses are set to null for these simulations,
so there are no "non-true null hypotheses" to detect.

A "non-true null hypotheses" in gene ontology analyses are genes which
are extremely likely to be different from the general population of genes.

**The sensitivity improves as the percentage of "non-true null hypotheses" increases.**    
For example, only 21% of the "non-true nulls" are detected when 25% of the hypotheses are "non-true nulls" as seen in B2.
But the detection rate rises to 62% of the total "non-true nulls" when 50% of the hypotheses are "non-true nulls" as seen in B3.

**The sensitivity decreases as the P-values of the "non-true null hypotheses" approach the alpha value 0.05.**    
When the "non-true nulls" have a maximum P-value of 0.01 and the alpha is 0.05, all "non-true nulls" are detected in all simulations (A2, A3, A4).

The detection is shown to drop to only 1% of all possible "non-true nulls" detected (C2)
when 25% of the 128 hypotheses tested are "non-true nulls" which have P-values between 0 and alpha.

**The sensitivity decreases as the number of total tested hypotheses get larger.**    
Over many simulations the detection rate is 61% for groups of 4 tested hypotheses (C4, blue bar),
but only 10% for groups of 128 hypotheses tested as shown in C4.

## Conclusion

The observations are:
  * Simulated FDRs stay below the guaranted alpha value.    
  * Simulated FDRs fall below the alpha as the percentage of true nulls in the study group fall    
  * All non-true null (actually significant hypotheses tests) are discovered if 
    their uncorrected P-Value is below 0.01 when the alpha is 0.50    
  * The non-true null discovery rate (sensitivity) drops as the 
    their uncorrected P-Value rises and becomes close to the alpha (0.50)    


Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
