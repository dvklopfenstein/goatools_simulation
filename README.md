# Simulations to Verify GOEA Results
Simulations in this repository are used to investigate the results of **Gene Ontology Enrichment Analyses** (**GOEAs**).    

## For all simulations in this repository:    
  * The **alpha level** is set to **0.05**
  * The **multiple-test correction** used is [**Benjamini/Hochberg False Discovery Rate**](http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)

## Two main levels of simulations:
  1. [**Preparatory**: Hypotheses and multiple-test simulations]()
  2. [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations]()

### [**Preparatory**: Hypotheses and multiple-test simulations](
     doc/md/README_prep.md#preparatory-p-value-and-multiple-test-simulations):    

     Demonstrates that mean FDR's resulting from simulations using randomly generated 
     hypotheses stay below the alpha-level set by the user.

     Configurable Simulation paramaters include:
       * **Numbers of tested hypotheses**, starting from groups as small as 4 tested hypotheses.
       * **Configurable percentages of "True Null Hypotheses"** varying from "No True Null" to "All True Null" hypotheses.

### [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations](
     doc/md/README_main.md#consequent-goea-simulations)
      * **TBD**

## Simulation Results
**TBD**: Concluding image and text

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
