"""Runs all experiments for all sets of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import timeit
import datetime
from pkggosim.goea.objbase import DataBase
from pkggosim.goea.objassc import DataAssc
from pkggosim.common.randseed import RandomSeed32

class RunParams(object):
    """Runs all experiments for all sets of experiments."""

    expected_params = set([
        'seed',                  # randomseed
        'randomize_truenull_assc',
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
        self.objassc = DataAssc(
            params['association_file'],
            params['genes_population'],
            params['randomize_truenull_assc'])
        # These study background genes have associations
        self.genes = {
            "population" : self.objassc.pop_genes,
            "study_bg" : params['genes_study_bg'].intersection(self.objassc.pop_genes),
            "null_bg" : self._init_null_bg()}
        self.gene_lists = {
            "study_bg" : list(params['genes_study_bg'].intersection(self.objassc.pop_genes)),
            "null_bg" : list(self._init_null_bg())}
        self._chk_genes(params, self.genes)
        self._adj_num_genes_list()

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

    def _init_null_bg(self):
        """Initialize null background, the population subset not related to study genes."""
        maskout = self.params['genes_popnullmaskout'].union(self.params['genes_study_bg'])
        return self.objassc.pop_genes.difference(maskout)

    def _adj_num_genes_list(self):
        """If the number of genes in num_genes_list is less than study_bg, update num_genes_list."""
        lst_orig = self.params['num_genes_list']
        lst_curr = []
        num_bg = len(self.gene_lists['study_bg'])
        for num_genes_orig in sorted(lst_orig):
            if num_genes_orig <= num_bg:
                lst_curr.append(num_genes_orig)
            else:
                lst_curr.append(num_bg)
                break
        if lst_orig != lst_curr:
            sys.stdout.write("**NOTE: num_genes_list WAS: {LIST}\n".format(LIST=lst_orig))
            sys.stdout.write("**NOTE: num_genes_list NOW: {LIST}\n".format(LIST=lst_curr))
            self.params['num_genes_list'] = lst_curr
        return lst_curr

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
