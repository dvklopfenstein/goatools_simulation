# Stochastic GOEA Simulations
Stochastic simulations of multitudes of **Gene Ontology Enrichment Analyses**
are used to generate simulated values of **FDR**, **sensitivity**, and **specificity**
for GOEAs run using [GOATOOLS](https://github.com/tanghaibao/goatools).

**Two categories of simulations are in this repo**:
  1. [**Preparatory**: Hypotheses and multiple-test simulations](doc/md/README_prep1.md); elements include:    
       * Benjamini/Hochberg FDR simulation only
  2. [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations](
     #consequent-gene-ontology-enrichment-results-goea-simulations); elements include    
       * Fisher's exact test    
       * Benjamini/Hochberg calculations    
       * Gene ontology associations    

All simulations herein use [**Benjamini/Hochberg multiple test correction**](
http://www.stat.purdue.edu/~doerge/BIOINFORM.D/FALL06/Benjamini%20and%20Y%20FDR.pdf)
with **alpha=0.05**.


## [**Consequent**: Gene Ontology Enrichment Results (GOEA) simulations]()

### Table of Contents
  * Figures:    
    * [Simulations using **original** gene-GO associations](#original-associations)    
    * [Simulations using **random** gene-GO associations](#random-associations)    
  * [Abstract](#abstract)
  * [Introduction](#introduction)
  * [Methods](#methods)
  * [Discussion](#discussion)
  * [Results](#results)
  * [Conclusion](#conclusion)
  * [References](#references)   

### Simulation Figures
Figure 1 presents the estimates of simulated FDRs, sensitivity, and specificity.

Sensitivity, also known as "true positive rate", recall, "probability of detection",
is the proportion of false hypotheses (humoral respose genes in our study sets) 
which are correctly detected as being significant.

Specificity, is the proportion of of true hypotheses (general population genes in the study) 
which failed to reject the null (not declared as being significantly different that the population.

#### Original Associations
![figure](doc/logs/fig_goea_100to000_004to124_N00050_00020_humoral_rsp.png)

#### Random Associations
The original associations are randomized for all associations except for the
_Non-True Nulls_ (the humoral genes that are significantly different that the population of all mouse genes)
from a randomly chosen study set of genes.    

![figure](doc/logs/fig_goea_rnd_100to000_004to124_N00100_00030_humoral_rsp.png)

### Abstract
Simulations of various sizes of study gene lists with various percentages of
genes which are enriched in _Humoral response_ are simulated. The results are
analyzed to determine the percentages the _Humoral response_ genes recovered
from thousands of gene ontology analyses.

### Introduction
Using GOATOOLS grouping, we find over 2,000 genes having immune functions. A subset of
the immune genes is the 124 _Humoral Response_ genes, which are used as a background
from which to draw upon for the study groups in the simulations. Study group sizes in
the simulations include 4 genes, 16, 64, and all 124 _Humoral Response_ genes.

The null hypotheses is the study genes are no different that the population genes.
The population genes in the simulations are the set of all protein-coding mouse genes
which have gene ontology associations, which is over 18,600 genes out a total of over 22,000 Ensembl genes.

The study groups are composed of various percentages of both true and false null hypotheses.
True null hypotheses in the study group are selected from the large general group of population genes.
False null hypotheses in the study group are selected from the small group of 124 humoral response genes.


Simulation-based estimates of precentage of humoral response study genes (famse nullrecovered from a GOEA

### Methods
### Discussion
### Results
### Conclusion
### References

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

  * [Statistical power and significance testing in large-scale genetic studies](https://www.nature.com/nrg/journal/v15/n5/full/nrg3706.html)
  * [Stomp on Step One](http://www.stomponstep1.com/) for Sensitivity, Specificity, and more    


Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
