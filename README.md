# Stochastic GOEA Simulations
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5500663.svg)](https://doi.org/10.5281/zenodo.5500663)

Stochastic simulations of multitudes of **Gene Ontology Enrichment Analyses** (GOEAs)    
are used to generate simulated values of **FDR**, **sensitivity**, and **specificity**
for **GOEAs** run using [GOATOOLS](https://github.com/tanghaibao/goatools).

This repo also contains stochastic simulations showing the FDR, sensitivity, and specificity of
multipletest correction methods including
FDR Benjamini/Hochberg (non-negative) and
Bonferroni one-step correction.
These simulations were used to architect the overall simulation strategy and 
investigate an effective figure to display multiple sets of information including:
  * Study size
  * Percentage of the study that was background (noise).
  * FDR
  * Sensitivity
  * Specificty

### Conclusions from Stochastic GOEA Simulations
  1. GO terms associated with huge numbers (thousands, in human) of genes cause FDR failures
  2. Removing even just 30 of the 17,000+ (human) GOs which are highly annotated causes good passing FDRs
  3. A study size of 4 genes in a GOEA will likely return an unacceptable amount of misses (False Negative)
  4. As study size increases, sensitivity improves (e.g., better sensitivity, fewer False Negatives)
  5. As the percentage of 'actually significant genes' rises in the study set, so does sensitivity
  6. Using a version of propagate counts greatly improves sensitivity    
  7. Remove selected highly annotated GO terms _prior_ to running a GOEA using these criteria:
     * **Highly annotated GO terms** (e.g., top 1%). Example in human: remove GOs assc. w/thousands of genes
     * **low depth** (near the top)
     * **high descendant count**


## Table of Contents

  * [**Recreating the stochastic simulations**](#recreating-the-stochastic-simulations)
  * **Figures** in manuscript:
    * [**Manuscript Figures**](#manuscript-figures)
    * [**Supplemental Figures**](#supplemental-figures)
      * [**Initial failing simulations**](#supplemental-figure-1-initial-failing-simulations)
      * **Exploratory simulations**: Stress tests with associations shuffled stochastically:
         * [**Enriched-only viewed**](#supplemental-figure-2-enriched-only-viewed)
         * [**30 Broad GO terms removed**](#supplemental-figure-3-30-broad-go-terms-removed)

## To Cite
_Please cite the following paper if you mention the stochastic simulations in this repo in your research_

[GOATOOLS: A Python library for Gene Ontology analyses](https://www.nature.com/articles/s41598-018-28948-z)      
Klopfenstein DV, Zhang L, Pedersen BS, ... Tang H    
2018 | _Scientific reports_ | [PMID:30022098](https://pubmed.ncbi.nlm.nih.gov/30022098/) | DOI:10.1038/s41598-018-28948-z


## Details

### Recreating the stochastic simulations
To recreate all five of our stochastic GOEA simulation plots
(for a total of 100,000 total stochastic simulations) 
featured in the GOATOOLS manuscript and supplemental data, clone the repository, 
https://github.com/dvklopfenstein/goatools_simulation,
and run this make target from the command line:

```
  $ make run_ms
```

### Manuscript Figures

**Results for 40,000 GOATOOLS GOEA stochastic simulations (20,000 simulations
for each panel) with varying sensitivity and consistently high specificity.**
GOEAs performed well on study groups of 8+ genes if the
GOATOOLS GOEA option propagate\_counts set to True.

![fig3](/doc/images/ms/fig3_genes.png)

### Supplemental Figures

#### Supplemental Figure 1) Initial failing simulations
**The first GOATOOLS GOEA simulations fail in panels A3 and A4
with FDR values exceeding the alpha of 0.05 set by the researcher.**
The values of failing FDRs are shown using red text.
The source of the failures were false positives for
GO terms annotated with large numbers of gene products.
For mouse annotations in the _biological_process_ branch,
GO terms annotated with 1,000 or more genes were the source of failures.

![suppfig1](/doc/images/ms/fig_goea_orig_noprune_ntn2_p0_100to000_004to124_N00020_00020_humoral_rsp_dpi600.png)

#### Supplemental Figure 2) Enriched-only viewed
**GOATOOLS GOEAs stress tests with randomly shuffled associations
nearly pass if only enriched GO terms are viewed.**
The associations are randomly shuffled while still maintaining the distribution
number of GO terms per gene. The failing FDRs (above 0.05) are seen in panels A2
and A3 for gene groups having 96, 112, or 124 genes.

![suppfig2](/doc/images/ms/fig_goea_rand_noprune_enriched_ntn2_p0_100to000_004to124_N00020_00020_humoral_rsp_dpi600.png)

#### Supplemental Figure 3) 30 Broad GO terms removed
**GOATOOLS GOEAs stress tests with randomly shuffled associations pass for all
cases if only 30 out of over 17k+ GO terms associated with more than 1000 genes
are removed.**
The median number of genes per GO term in the mouse associations is 3 genes/GO.
Genes per GO term ranges from 1 gene to ~7k genes per GO term. (mean=16
genes/GO, SD=128).

![suppfig3](/doc/images/ms/fig_goea_rand_pruned_ntn2_p0_100to000_004to124_N00020_00020_humoral_rsp_dpi600.png)


Copyright (C) 2016-present, DV Klopfenstein, Haibao Tang. All rights reserved.
