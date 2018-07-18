# Stochastic GOEA Simulations

Stochastic simulations of multitudes of **Gene Ontology Enrichment Analyses** (GOEAs)
are used to generate simulated values of **FDR**, **sensitivity**, and **specificity**
for **GOEAs** run using [GOATOOLS](https://github.com/tanghaibao/goatools).

  * [Re-Creating the stochastic simulations](#re-creating-the-stochastic-simulations)
  * **Figures** in manuscript:
    * [Initial failing simulations](initial-failing-simulations)
    * [Typical simulations]()
    * Exploratory simulations: Stress tests with stochastically associations shuffled stochastically:
       * 

## Details

### Re-Creating the stochastic simulations
To recreate all five of our stochastic GOEA simulation plots
(for a total of 100,000 total stochastic simulations) 
featured in the GOATOOLS manuscript and supplemental data, clone the repository, 
https://github.com/dvklopfenstein/goatools_simulation,
and run this make target from the command line:

```
  $ make run\_ms
```

### Figures

#### Initial failing simulations
**Results for 20,000 GOATOOLS GOEA stochastic simulations with
varying sensitivity and consistently high specificity.**
GOEAs performed well on study groups of 8+ genes if the
GOATOOLS GOEA option propagate\_counts set to True.
![fig3](/doc/images/ms/fig3_genes.png)

#### Typical simulations

Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
