"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"


import timeit
import datetime
from pkggosim.goea.utils import import_var
from pkggosim.goea.objbase import DataBase
from pkggosim.goea.objassc import DataAssc
from pkggosim.common.randseed import RandomSeed32

class RunParams(object):
    """Runs all experiments for all sets of experiments."""

    expected_params = set([
        'seed',                  # randomseed
        'alpha',                 # 0.05
        'method',                # 'fdr_bh'
        'association_file',      # 'gene_association.mgi'
        'genes_population',      # genes_mus
        'genes_study_bg',        # 'humoral_rsp'
        'genes_popnullmaskout',  # ['immune', 'viral_bacteria']
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
        self.objbase = DataBase(params['alpha'], params['method'])
        self.objassc = DataAssc(params['association_file'], params['genes_population'])
        # These study background genes have associations
        self.genes_population = self.objassc.pop_genes
        self.genes_study_bg = self._init_genes_study_bg()
        self.genes_null_bg = self._init_genes_null_bg()

    def _init_genes_study_bg(self):
        """Read genes in user-provided module. Limit study genes to those in assc."""
        study_genes = self.get_genes(self.params['genes_study_bg'])
        return study_genes.intersection(self.genes_population)

    def _init_genes_null_bg(self):
        """Read genes in user-provided module. Limit study genes to those in assc."""
        null_bg = set(self.genes_population)
        for genedesc in self.params['genes_popnullmaskout']:
            genes_rm = self.get_genes(genedesc)
            null_bg = null_bg.difference(genes_rm)
        return null_bg

    def get_objgoea(self, study_genes):
        """Return population genes, including study genes. But minus closely related genes."""
        genes_pop_masked = self.genes_null_bg.union(study_genes)
        return self.objbase.get_goeaobj(genes_pop_masked, self.objassc.assc)

    def get_genes(self, moddesc):
        """Return gene list using description."""
        modstr = 'pkggosim.gene_data.genes_{DESC}'.format(DESC=moddesc)
        genes = import_var(modstr, "GENES")
        assert genes, "NO GENES FOUND FOR MODULE({})".format(modstr)
        return genes

    def prt_summary(self, prt):
        """Print summary of simulation parameters and background data."""
        prt.write("\nWRITTEN: {DATE}:\n\n".format(DATE=datetime.date.today()))
        # Print Random seed
        self.objrnd.prt(prt)
        # Print Info: GO-DAG, Associations, Population
        self.objbase.prt_summary(prt)
        self.objassc.prt_summary(prt)
        prt.write("{N:6,} GENES  IN STUDY BACKGROUND\n".format(N=len(self.genes_study_bg)))
        prt.write("{N:6,} GENES  IN NULL  BACKGROUND\n".format(N=len(self.genes_null_bg)))
        prt.write("\n")
        prt.write("SIMULATION PARAMETERS:\n")
        for key in ['perc_nulls', 'num_genes_list', 'num_experiments', 'num_sims']:
            prt.write("    {KEY:15} {VAL}\n".format(KEY=key, VAL=self.params[key]))
        prt.write("\n")

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
