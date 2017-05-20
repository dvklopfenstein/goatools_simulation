# Simulation modules

  * [Simulations of P-Value w/Multipletest Correction]()
  * [Plotting and Reporting]()
  * [Utilities]()


## Simulations of P-Value w/Multipletest Correction

  * [**run_all_experiments.py**](run_all_experiments.py)    
    * [**experiments.py**](experiments.py)    
      * [**pval_sims.py**](pval_sims.py)    
        This is one experiment, which produces one randomly generated FDR ratio.    
        One experiment is N(pval_qty) P-Value simulations.    
        * [**pval_sim.py**](pval_sim.py)    
        This is one P-Value simulation.    
        Multiple P-values are randomly generated to have significance (or not)
          and a multiple-test correction is run on the set of newly generated P-Values.

## Plotting and Reporting
  * [**plot_results.py**](plot_results.py)    
  * [**report_results.py**](report_results.py)    

## Utilities
  * [**randseed.py**](randseed.py)    
  * [**utils.py**](utils.py)    

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved
