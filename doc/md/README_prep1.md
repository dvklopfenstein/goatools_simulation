# [**Preparatory**: Hypotheses and multiple-test simulations]()

## Introduction


## Discussion
These simulations demonstrate that the mean False Discovery Rates (FDRs),
center around the alpha-level set by the user (0.05) when all hypotheses are true (row 1 in figure 1),
but is smaller otherwise (rows 2-4 in figure 1).

In fact, as larger percentages of the hypotheses are "Non-true null hypotheses"
(i.e. Null should be rejected; there is a difference between the study items and the population items),
the simulated FDR drops dramatically below alpha(0.05).

All simulations use [**Benjamini/Hochberg multiple test correction**](
http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)
with **alpha=0.05**.

## Results
### Simulated FDR Ratios
![FDR results](../logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png)
The x-axis shows two simulation parameters.
The first parameter is the _number of tested hypotheses_ in each simulation, with values of 4, 16, and 128.
The second parameter, labeled on the figure as _**Sig.<=**_, is the _maximum P-value_,
of randomly generated non-true null hypotheses test results.
The y-axis shows the _percentage of "True nulls"_.
The simulated FDR drops dramatically
As the percentage of "True nulls" drops causing the number of "non-true nulls" to rise.

The maximum P-value for "non-true null hypotheses" is seen here with values 0.01, 0.03, & 0.05
in columns A, B, and C repectively.
This value has no affect on the simulated FDR values.
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


Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.