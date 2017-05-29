# Simulation modules

  * [**Simulations of P-Value w/Multipletest Correction**](#hypotheses-simulations-wmultipletest-correction)
  * [**Utilities & Plotting**](#utilities--plotting)    


## Hypotheses Simulations w/Multipletest Correction

  * [**hypotheses_run_all.py**](hypotheses_run_all.py)    
    Runs all hypotheses experiments in a user-specified set.
    * [**hypotheses_experiments.py**](hypotheses_experiments.py)    
      Runs numerous experiments, producing **a slew of simulated FDR ratios** on sets of randomly generated hypotheses results.    
      Experimental results grouped together in a single boxplot tile have common parameters, like:
        1) _Maximum significant value_ for a randomly generated tests having a non-true hypotheses,
        2) _Percent of True Null Hypotheses_ in a single simulation set, and
        3) _The number of tested hypotheses_
      * [**hypotheses_sims.py**](hypotheses_sims.py)    
        This is one experiment, which produces **one simulated FDR ratio** using randomly generated hypotheses results.    
        One experiment is N (hypotheses_qty) hypotheses simulations.    
        * [**hypotheses_sim.py**](hypotheses_sim.py)    
        This is one simulation for testing one set of hypotheses.    
        Multiple hypotheses results (P-Values) are randomly generated to be either:    
          * True Null: There is no difference between the study group and population group    
          * Non-true Null: There is a difference between the study group and population group    
        A multiple-test correction is run on the set of newly generated P-Values.

## Utilities & Plotting
  * [**randseed.py**](randseed.py)    
  * [**utils.py**](utils.py)    
  * [**hypotheses_plot_results.py**](hypotheses_plot_results.py)    

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved
