# Simulation modules

  * [**Simulations of P-Value w/Multipletest Correction**](#simulations-of-p-value-wmultipletest-correction)    
  * [**Plotting and Reporting**](#plotting-and-reporting)    
  * [**Utilities**](#utilities)    


## Simulations of P-Value w/Multipletest Correction

  * [**run_all_experiments.py**](run_all_experiments.py)    
    * [**experiments.py**](experiments.py)    
      This contains one set of experiments that all have common parameters, like:
        1) _maximum significant value for a randomly generated P-Value_,
        2) _percent of pvalues in one P-Value simulation which are significant_, and
        3) _the number of randomly generated P-Values in a single P-Value simulation_.
      * [**pval_sims.py**](pval_sims.py)    
        This is one experiment, which produces one randomly generated FDR ratio.    
        One experiment is N (pval_qty) P-Value simulations.    
        * [**pval_sim.py**](pval_sim.py)    
        This is one P-Value simulation.    
        Multiple P-values are randomly generated to have significance (or not) as specified by the user.
        A multiple-test correction is run on the set of newly generated P-Values.

## Plotting and Reporting
  * [**plot_results.py**](plot_results.py)    
  * [**report_results.py**](report_results.py)    

## Utilities
  * [**randseed.py**](randseed.py)    
  * [**utils.py**](utils.py)    

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved
