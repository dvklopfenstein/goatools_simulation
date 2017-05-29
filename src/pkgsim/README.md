# Simulation modules

  * [**Simulations of P-Value w/Multipletest Correction**](#simulations-of-p-value-wmultipletest-correction)    
  * [**Plotting and Reporting**](#plotting-and-reporting)    
  * [**Utilities**](#utilities)    


## Simulations of P-Value w/Multipletest Correction

  * [**hypotheses_run_all.py**](hypotheses_run_all.py)    
    * [**hypotheses_experiments.py**](hypotheses_experiments.py)    
      This contains one set of experiments that all have common parameters, like:
        1) _Maximum significant value for a randomly generated P-Value which has a non-true hypothesis_,
        2) _Percent of P-Values in one P-Value simulation which are significant_, and
        3) _The number of randomly generated P-Values in a single P-Value simulation_.
      * [**hypotheses_sims.py**](hypotheses_sims.py)    
        This is one experiment, which produces one randomly generated FDR ratio.    
        One experiment is N (pval_qty) P-Value simulations.    
        * [**hypotheses_sim.py**](hypotheses_sim.py)    
        This is one P-Value simulation.    
        Multiple P-values are randomly generated to have significance (or not) as specified by the user.
        A multiple-test correction is run on the set of newly generated P-Values.

## Utilities & Plotting
  * [**randseed.py**](randseed.py)    
  * [**utils.py**](utils.py)    
  * [**hypotheses_plot_results.py**](hypotheses_plot_results.py)    

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved
