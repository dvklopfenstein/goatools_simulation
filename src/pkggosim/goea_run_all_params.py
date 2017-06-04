"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

#    sim_params = {
#        'seed' : randomseed,
#        'alpha' : 0.05,
#        'method' : 'fdr_bh',
#        'population_genes':genes_mus,
#        'association_file':'gene_association.mgi',
#        'perc_nulls' : [100, 75, 50, 25],
#        'num_genes_list' : [4, 16, 128],
#        'num_experiments' : num_experiments, # Number of simulated FDR ratios in an experiment set
#        'num_sims' : num_sims}   # Number of sims per experiment; used to create one FDR ratio

import timeit
from pkggosim.goea_objbg import DataBackground
from pkggosim.randseed import RandomSeed32

class RunParams(object):
    """Runs all experiments for all sets of experiments."""

    expected_params = set(['seed', 'perc_nulls', 'max_sigpvals',
                           'num_genes_list', 'num_experiments', 'num_sims'])

    def __init__(self, params):
        self.tic = timeit.default_timer()
        self.params = params
        self.objrnd = RandomSeed32(params['seed'])
        self.objbg = DataBackground(
            params['alpha'],
            params['method'],
            params['population_genes'], # Population genes
            params['association_file']) # Associations: ens2gos
#        assert set(params.keys()) == self.expected_params

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
