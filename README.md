# Simulations to Verify GOEA Results
Simulations in this repository are used to investigate the results of **Gene Ontology Enrichment Analyses** (**GOEAs**).    

## For all simulations in this repository:    
  * The **alpha level** is set to **0.05**
  * The **multiple-test correction** used is [**Benjamini/Hochberg False Discovery Rate**](http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)

## There are two main levels of simulations: [Preparatory](doc/md/README_prep.md#preparatory-p-value-and-multiple-test-simulations) and [Consequent](doc/md/README_main.md#consequent-goea-simulations)
  1. [**Preparatory**: Hypotheses and multiple-test simulations](
     doc/md/README_prep.md#preparatory-p-value-and-multiple-test-simulations):    
     Simulates testing groups of hypotheses using Fishers exact test from [SciPy](
     https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html)
     

     Demonstrates that mean FDR's resulting from simulations using randomly generated 
     hypotheses stay below the alpha-level set by the user.

     Configurable Simulation paramaters include:
       * **Numbers of tested hypotheses**, starting from groups as small as 4 tested hypotheses.
       * **Configurable percentages of "True Null Hypotheses"** including the extremes and all percentages between:
         * All hypotheses are "True Null", meaning there are is no difference between the items in the study and population.
         * All hypotheses are "Non-true Null", meaning all items in the study are extremely different from the population.

  2. [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations](
     doc/md/README_main.md#consequent-goea-simulations)
      * **TBD**

## Simulation Results
**TBD**: Concluding image and text

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
