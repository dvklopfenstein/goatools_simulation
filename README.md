# Simulations to Verify GOEA Results
Simulations in this repository are used to investigate the results of **Gene Ontology Enrichment Analyses** (GOEAs).    

#### For all simulations in this repo:    
  * The **alpha level** is set to **0.05**
  * The **multiple-test correction** used is **Benjamini/Hochberg False Discovery Rate**

#### There are two main levels of simulations(Preparatory/Consequent):
  1. [**Preparatory**: P-value and multiple-test simulations](#preparatory-p-value-and-multiple-test-simulations)    
      * [All P-values chosen randomly; None are significant](README_prep.md#all-p-values-chosen-randomly-none-are-significant-1)
      * [95% P-values chosen randomly; 5% are significant ] (README_prep.md#95-p-values-chosen-randomly-5-are-significant)
      * [90% P-values chosen randomly; 10% are significant ](README_prep.md#90-p-values-chosen-randomly-10-are-significant)
      * [50% P-values chosen randomly; 50% are significant ](README_prep.md#50-p-values-chosen-randomly-50-are-significant)
  2. [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations](README_main.md#consequent-goea-simulations)

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
