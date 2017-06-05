# Simulations to Verify GOEA Results
The characteristics of **Gene Ontology Enrichment Analyses** (**GOEAs**) using
[GOATOOLS](https://github.com/tanghaibao/goatools)
are examined using stochastic simulations.

**There are two categories of simulations**:
  1. [**Preparatory**: Hypotheses and multiple-test simulations](
     #preparatory-hypotheses-and-multiple-test-simulations)    
     Benjamini/Hochberg FDR simulation only
  2. [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations](
     #consequent-gene-ontology-enrichment-results-goea-simulations)    
     Simulations encompass the Benjamini/Hochberg calculations like those from step 1, as well as
     gene ontology associations, and Fisher's exact test.

## Two categories of simulations (details):
All simulations use [**Benjamini/Hochberg multiple test correction**](
http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)
with **alpha=0.05**.

### [**Preparatory**: Hypotheses and multiple-test simulations]()
These simulations demonstrate that the mean False Discovery Rates (FDRs),
center around the alpha-level set by the user (0.05) when all hypotheses are true (row 1 in figure 1),
but is smaller otherwise (rows 2-4 in figure 1).

In fact, as larger percentages of the hypotheses are "Non-true null hypotheses"
(i.e. Null should be rejected; there is a difference between the study items and the population items),
the simulated FDR drops dramatically below alpha(0.05).

#### Simulated FDR Ratios
![FDR results](doc/logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png)
The x-axis shows two simulation parameters.
The first parameter is the _number of tested hypotheses_ in each simulation, with values of 4, 16, and 128.
The second parameter, labeled on the figure as _**Sig.<=**_, is the _maximum P-value_,
of randomly generated non-true null hypotheses test results.
The y-axis shows the _percentage of "True nulls"_.
The simulated FDR drops dramatically
As the percentage of "True nulls" drops and the number of "non-true nulls" rises.

The maximum P-value for "non-true null hypotheses" is seen here with values 0.01, 0.03, & 0.05
in columns A, B, and C repectively.
This value has no affect on the simulated FDR values.
But it has a large affect on the sensitivity of the test.

#### Simulated Sensitivity Ratios
Sensitivity is also known as the _true positive rate_, _recall_, or _probability of detection_.
![Sensitivity results](doc/logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_sensitivity.png)
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

The detection drops to a worst case of only 1% of all possible "non-true nulls" detected (C2)
when 25% of the 128 hypotheses tested are "non-true nulls" which have P-values between 0 and alpha.

**The sensitivity decreases as the number of total tested hypotheses get larger.**
Over many simulations the detection rate is 61% for groups of 4 tested hypotheses,
but only 10% for groups of 128 hypotheses tested as shown in C4.



### [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations]()
TBD


## Prerequisites

  * numpy
  * statsmodels
  * datetime
  * seaborn
  * pandas
  * goatools
  * goatools_suppl

## Links

  * 1995 Benjamini & Hochberg's [**Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing**](
    http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)
  * [SciPy](https://docs.scipy.org/doc/scipy/reference/)'s
    [stats](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html) package:    
    * [Fishers exact test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.htm)
    * [multipletests](http://www.statsmodels.org/stable/generated/statsmodels.sandbox.stats.multicomp.multipletests.html)
  * [Stomp on Step One](http://www.stomponstep1.com/) for Sensitivity, Specificity, and more    


Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
