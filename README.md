# Simulations to Verify GOEA Results
The characteristics of **Gene Ontology Enrichment Analyses** (**GOEAs**) using
[GOATOOLS](https://github.com/tanghaibao/goatools)
are examined using stochastic simulations.

All simulations use [**Benjamini/Hochberg multiple test correction**](
http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)
with **alpha=0.05**.

**There are two categories of simulations**:
  1. [**Preparatory**: Hypotheses and multiple-test simulations](
     #preparatory-hypotheses-and-multiple-test-simulations)    
     Benjamini/Hochberg FDR simulation only
  2. [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations](
     #consequent-gene-ontology-enrichment-results-goea-simulations)    
     Simulations encompass the Benjamini/Hochberg functions from step 1, as well as
     gene ontology associations, and Fisher's exact test.

## Two categories of simulations (details):
### [**Preparatory**: Hypotheses and multiple-test simulations]()
These simulations demonstrate that the mean False Discovery Rates (FDRs),
center around the alpha-level set by the user (0.05) when all hypotheses are true,
but is smaller otherwise.

In fact, as larger percentages of the hypotheses are "Non-true null hypotheses"
(i.e. Null should be rejected; there is a difference between the study items and the population items),
the simulated FDR drops dramatically below alpha(0.05).

#### Simulated FDR Ratios
![FDR results](doc/logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_fdr_actual.png)
The x-axis shows two simulation parameters.
The first parameter is the _number of tested hypotheses_ in each simulation, which is 4, 16, and 128.
The second parameter, labeled on the figure as _**Sig.<=**_, is the _maximum P-value_,
of randomly generated non-true null hypotheses test results.
The y-axis shows the _percentage of "True nulls"_.
The simulated FDR drops dramatically
As the percentage of "True nulls" drops and the number of "non-true nulls" rises.

The maximum P-value for "non-true null hypotheses" is seen here with values 0.05, 0.03, & 0.01.
This value has no affect on the simulated FDR values.
But it has a large affect on the sensitivity of the test.

#### Simulated Sensitivity Ratios
Sensitivity is also known as the _true positive rate_, _recall_, or _probability of detection_.
![Sensitivity results](doc/logs/fig_hypoth_100to025_01to05_004to128_N00100_01000_sensitivity.png)
**At an alpha of 0.05, 100% of "non-true null hypotheses" are detected when their P-Values are <= 0.01**
as seen in the leftmost "Sig.<=0.01" column.
The top row shows sensitivity is 0% because all hypotheses are set to null for these simulations,
so there are no "non-true null hypotheses" to detect.

A "non-true null hypotheses"** in gene ontology analyses are genes which
are extremely likely to be different from the general population of genes.

**The sensitivity improves as the percentage of "non-true null hypotheses" increases.**
Increasing sensitivity can be seen in the figure when
comparing the rows in middle "Sig<=0.03" column between one another or
comparing the rows in right-most "Sig<=0.05" column between one another.

**The sensitivity decreases as the P-values of the "non-true null hypotheses" approach the alpha value 0.05.**
For example, in the last two columns of the "50% Null" row, the green bars 

**The sensitivity decreases as the number of total tested hypotheses get larger.**
For example, in the "75% Null" row and "Sig<=0.03" column
when the number of tested hypotheses is 4, 45% (SE 0.2%) of all "non-true null" are found.
But when the number of tested hypotheses is 128, only 4% (SE 0.2%) of all "non-true null" are found.



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
