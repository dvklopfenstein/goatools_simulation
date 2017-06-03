# Simulations to Verify GOEA Results
Stochastic simulations are used to investigate the results of
**Gene Ontology Enrichment Analyses** (**GOEAs**).

All simulations use [**Benjamini/Hochberg multiple test correction**](
http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)
with **alpha=0.05**.

**There are two categories of simulations**:
  1. [**Preparatory**: Hypotheses and multiple-test simulations](
     #preparatory-hypotheses-and-multiple-test-simulations) (No gene ontology)
  2. [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations](
     #consequent-gene-ontology-enrichment-results-goea-simulations)

## Two categories of simulations (details):
### [**Preparatory**: Hypotheses and multiple-test simulations]()
Demonstrates that the mean False Discovery Rates (FDRs),
determined by simulations that generate random hypotheses test results,
center around the alpha-level set by the user (0.05) when all hypotheses are true,
but is smaller otherwise.

In fact, as larger percentages of the hypotheses are "Non-true null hypotheses"
(i.e. Null should be rejected; there is a difference between the study items and the population items),
the simulated FDR drops dramatically below alpha(0.05).

![pval tiled FDR values](doc/md/images/suppl_hypoth_fdr_100to025_01to05_004to128_N00500_500.png)
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
If all "non-true null hypotheses" have a randomly generated P-value between 0.0 and 0.01,
all hypotheses will be discovered.
If all "non-true null hypotheses" have a randomly generated P-value between 0.0 and 0.05,
only 10% of the hypotheses will be discovered.


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

  * 1995 Benjamini & Hochberg
    [**Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing](
    http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)
  * [SciPy](https://docs.scipy.org/doc/scipy/reference/)'s
    [stats](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html) package:    
    * [Fishers exact test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.htm)
    * [multipletests](http://www.statsmodels.org/stable/generated/statsmodels.sandbox.stats.multicomp.multipletests.html)
  * [Stomp on Step One](http://www.stomponstep1.com/) Sensitivity, Specificity, and more    


Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
