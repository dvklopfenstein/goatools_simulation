"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"


import timeit
import datetime
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
        _maskout = params['genes_popnullmaskout'].union(params['genes_study_bg'])
        self.genes = {
            "population" : self.objassc.pop_genes,
            "study_bg" : params['genes_study_bg'].intersection(self.objassc.pop_genes),
            "null_bg" : self.objassc.pop_genes.difference(_maskout)}
        self._chk_genes(params, self.genes)

    @staticmethod
    def _chk_genes(params, genes):
        """Check the gene counts."""
        assert len(genes['population']) <= len(params['genes_population'])
        assert len(genes['study_bg']) <= len(params['genes_study_bg'])
        assert genes['population'].intersection(genes['study_bg']) == genes['study_bg']
        assert not genes['null_bg'].intersection(genes['study_bg'])

    def get_objgoea(self, study_genes):
        """Return population genes, including study genes. But minus closely related genes."""
        genes_pop_masked = self.genes['null_bg'].union(study_genes)
        return self.objbase.get_goeaobj(genes_pop_masked, self.objassc.assc)

    def prt_summary(self, prt):
        """Print summary of simulation parameters and background data."""
        prt.write("\nWRITTEN: {DATE}:\n\n".format(DATE=datetime.date.today()))
        # Print Random seed
        self.objrnd.prt(prt)
        # Print Info: GO-DAG, Associations, Population
        self.objbase.prt_summary(prt)
        self.objassc.prt_summary(prt)
        prms = self.params
        num_pop_tot = len(prms['genes_population'])
        num_pop_assc = len(self.genes['population'])
        perc_pop = 100.0*num_pop_assc/num_pop_tot
        prt.write("{N:6,} population genes (user)\n".format(N=num_pop_tot))
        prt.write("{N:6,} population genes in assc.\n".format(N=num_pop_assc))
        prt.write("{N:5.0f}% population genes coverage in assc.\n".format(N=perc_pop))
        prt.write("{N:6,} study genes (user)\n".format(N=len(prms['genes_study_bg'])))
        prt.write("{N:6,} study genes in assc.\n".format(N=len(self.genes['study_bg'])))
        prt.write("{N:6,} population genes - study buffer\n".format(N=len(self.genes['null_bg'])))
        prt.write("\n")
        prt.write("SIMULATION PARAMETERS:\n")
        for key in ['perc_nulls', 'num_genes_list', 'num_experiments', 'num_sims']:
            prt.write("    {KEY:15} {VAL}\n".format(KEY=key, VAL=prms[key]))
        prt.write("\n")

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
