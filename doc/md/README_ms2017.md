# Stochastic Simulation figures for GOATOOLS manuscript

* [Manuscript Figures](#manuscript-figures)    
  * [**Original annotations** (propagate_counts=False)](#goeas-recovering-humoral-response-hr-genes)    
  * [**Augmented annotations** (propagate_counts=True)](#goeas-recovering-hr-genes-propagate_countstrue)    
* [Supplemental Figures](#supplemental-figures)     
  * [Original Annotations; View over/under-enrichments](#original-annotations-view-overunder-enrichments)
  * [Randomly Shuffled Annotations; View enriched results](#randomly-shuffled-annotations-view-enriched-results-only)
  * [Randomly Shuffled Annotations (Pruned)]()

## Manuscript Figures
**Figure 3**. Results for 20,000 GOATOOLS GOEA stochastic simulations per figure showed **varying sensitivity and consistently high specificity**, performing **better on large gene groups than on small gene groups (e.g., 4 genes)**.

GOEAs performed **well on study groups of 8+ genes** if the GOATOOLS GOEA option, **propagate_counts is set to True**.

The simulation **gene groups** ranged in **size and content**.

The group size ranged from **4 to 124 genes**.

The content ranged in percentage of targeted genes versus background genes (“True Null” or “Null” genes). Targeted genes are randomly chosen from 124 genes associated with Humoral Response (HR). Background genes are randomly chosen from the ~20k protein-coding genes which are not associated with HR. 

### GOEAs recovering Humoral Response (HR) genes
(A) Stochastic GOEAs using downloaded annotations perform well if the **gene groups are large** or if the **percentage of targeted HR genes in a gene group is over 50%**. Study groups containing **8 or less genes** have a **low probability** of revealing genes associated with truly enriched GO terms. 
![propcnts=F](images/fig_goea_orig_noprune_enriched_ntn2_p0_100to000_004to124_N00020_00020_humoral_rsp.png)

### GOEAs recovering HR genes; propagate_counts=True
(B) Setting the GOATOOLS GOEA option, propagate_counts, to True, causing GO term gene annotations to be added to the GO parents up through the GO hierarchy, greatly improves the GOEA sensitivity with no degradation of the specificity, even for small gene groups.
![propcnts=T](images/fig_goea_orig_noprune_enriched_ntn2_p1_100to000_004to124_N00020_00020_humoral_rsp.png)


## Supplemental Figures

### Original Annotations: View over/under-enrichments
**Supplemental Figure 1**. The first GOATOOLS GOEA simulations fail in panels A3 and A4 with FDRs above the alpha cut-off of 0.05. The values of failing FDRs are shown using red text.
![orig](images/fig_goea_orig_noprune_ntn2_p0_100to000_004to124_N00020_00020_humoral_rsp.png)

### Randomly shuffled Annotations: View enriched results only
**Supplemental Figure 2**. GOATOOLS GOEAs stress tests with randomly shuffled associations nearly pass if only enriched GO terms are viewed. The associations are randomly shuffled while still maintaining the distribution number of GO terms per gene. The failing FDRs (above 0.05) are seen in panels A2 and A3 for gene groups having 96, 112, or 124 genes.
![rand enriched](images/fig_goea_rand_noprune_enriched_ntn2_p0_100to000_004to124_N00020_00020_humoral_rsp.png)

### Randomly shuffled Pruned Annotations
**Supplemental Figure 3**. GOATOOLS GOEAs stress tests with randomly shuffled associations pass for all cases if only 30 out of over 17k+ GO terms associated with more than 1000 genes are removed. The median number of genes per GO term in the mouse associations is 3 genes/GO. Genes per GO term range from 1 gene to ~7k genes per GO term. (mean=16 genes/GO, SD=128)
![rand pruner](images/fig_goea_rand_pruned_ntn2_p0_100to000_004to124_N00020_00020_humoral_rsp.png)

Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
