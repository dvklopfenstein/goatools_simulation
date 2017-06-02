# Simulations to Verify GOEA Results
Simulations in this repository are used to investigate the results of
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
Demonstrates that mean FDR's resulting from simulations using randomly generated 
hypotheses stay below the alpha-level set by the user.

Configurable Simulation paramaters include:
  * **Numbers of tested hypotheses**, starting from groups as small as 4 tested hypotheses.
  * **Configurable percentages of "True Null Hypotheses"** varying from "No True Null" to "All True Null" hypotheses.

### [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations]()


## Prerequisites
  * numpy
  * statsmodels
  * datetime
  * seaborn
  * pandas
  
  * goatools
  * goatools_suppl


Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
