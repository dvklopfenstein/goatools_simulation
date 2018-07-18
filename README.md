# Stochastic GOEA Simulations

Stochastic simulations of multitudes of **Gene Ontology Enrichment Analyses** (GOEAs)
are used to generate simulated values of **FDR**, **sensitivity**, and **specificity**
for **GOEAs** run using [GOATOOLS](https://github.com/tanghaibao/goatools).

## Further Description
These simulations are described in detail in the research paper:

Klopfenstein, D.V. et al. [GOATOOLS: A Python library for Gene Ontology analyses](https://www.nature.com/articles/s41598-018-28948-z)
_Scientific reports_| (2018) 8:10872 | DOI:10.1038/s41598-018-28948-z

_Please cite the preceeding paper if you mention the stochastic GOEA simulations in your research_

## Table of Contents

  * [Re-Creating the stochastic simulations](#re-creating-the-stochastic-simulations)
  * **Figures** in manuscript:
    * [**Manuscript Figures**](#manuscript-figures)
    * [**Supplemental Figures**](#supplemental-figures)
      * [**Initial failing simulations**](#supplemental-figure-1-initial-failing-simulations)
      * **Exploratory simulations**: Stress tests with associations shuffled stochastically:
         * [**Enriched-only viewed**](#supplemental-figure-2-enriched-only-viewed)
         * [**30 Broad GO terms removed**](#supplemental-figure-3-30-broad-go-terms-removed)

## Details

### Re-Creating the stochastic simulations
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


Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
