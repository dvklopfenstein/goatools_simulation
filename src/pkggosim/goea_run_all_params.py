"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"


import timeit
import datetime
from pkggosim.goea_objbg import DataBackground
from pkggosim.randseed import RandomSeed32

class RunParams(object):
    """Runs all experiments for all sets of experiments."""

    expected_params = set([
        'seed',                  # randomseed
        'alpha',                 # 0.05
        'method',                # 'fdr_bh'
        'association_file',      # 'gene_association.mgi'
        'genes_population',      # genes_mus
        'genes_study_bg',        # import_var("pkggosim.genes_b_cell_activation", "GENES")
        'genes_popnullmaskout',  # import_var("pkggosim.genes_immune", "GENES")
        'perc_nulls',            # [100, 75, 50, 25]
        'num_genes_list',        # [4, 16, 128]
        'num_experiments',       # Number of simulated FDR ratios in an experiment set
        'num_sims',              # Number of sims per experiment; used to create one FDR ratio
    ])

    def __init__(self, params):
        assert set(params.keys()) == self.expected_params
        self.tic = timeit.default_timer()
        self.params = params
        self.objrnd = RandomSeed32(params['seed'])
        self.objbg = DataBackground(
            params['alpha'],
            params['method'],
            params['genes_population'], # Population genes
            params['association_file']) # Associations: ens2gos
        # These study background genes have associations
        self.genes_population = self.objbg.pop_genes
        self.genes_study_bg = params['genes_study_bg'].intersection(self.genes_population)
        self.genes_null_bg = self.genes_population.difference(params['genes_popnullmaskout'])

    def prt_summary(self, prt):
        """Print summary of simulation parameters and background data."""
        prt.write("\nWRITTEN: {DATE}:\n\n".format(DATE=datetime.date.today()))
        # Print Random seed
        self.objrnd.prt(prt)
        # Print Info: GO-DAG, Associations, Population
        self.objbg.prt_summary(prt)
        prt.write("{N:6,} GENES  IN STUDY BACKGROUND\n".format(N=len(self.genes_study_bg)))
        prt.write("{N:6,} GENES  IN NULL  BACKGROUND\n".format(N=len(self.genes_null_bg)))
        prt.write("\n")
        prt.write("SIMULATION PARAMETERS:\n")
        for key in ['perc_nulls', 'num_genes_list', 'num_experiments', 'num_sims']:
            prt.write("    {KEY:15} {VAL}\n".format(KEY=key, VAL=self.params[key]))
        prt.write("\n")

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
