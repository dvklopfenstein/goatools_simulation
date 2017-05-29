# Simulation modules

  * [**Simulations of P-Value w/Multipletest Correction**](#simulations-of-p-value-wmultipletest-correction)    
  * [**Utilities & Plotting**](#utilities--plotting)    


## Hypotheses Simulations w/Multipletest Correction

  * [**hypotheses_run_all.py**](hypotheses_run_all.py)    
    Runs the complete set of all hypotheses experiments.
    * [**hypotheses_experiments.py**](hypotheses_experiments.py)    
      This produces **many randomly generated FDR ratios**.    
      This contains one set of experiments that all have common parameters, like:
        1) _Maximum significant value_ for a randomly generated test result having a non-true hypothesis,
        2) _Percent of True Null Hypotheses_ in a single simulation, and
        3) _The number of tested hypotheses_
      * [**hypotheses_sims.py**](hypotheses_sims.py)    
        This is one experiment, which produces **one randomly generated FDR ratio**.    
        One experiment is N (hypotheses_qty) hypotheses simulations.    
        * [**hypotheses_sim.py**](hypotheses_sim.py)    
        This is one P-Value simulation.    
        Multiple P-values are randomly generated to have significance (or not) as specified by the user.
        A multiple-test correction is run on the set of newly generated P-Values.

## Utilities & Plotting
  * [**randseed.py**](randseed.py)    
  * [**utils.py**](utils.py)    
  * [**hypotheses_plot_results.py**](hypotheses_plot_results.py)    

Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved
