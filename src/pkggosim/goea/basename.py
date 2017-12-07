"""Runs all experiments for all sets of experiments."""

from __future__ import print_function

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
# import sys

class Basename(object):
    """Runs all experiments for all sets of experiments."""

    # expected_params = set([
    #     'title',                   # Title to print on Figure w/FDR/Sensitivity/Specificty
    #     'repo',                    # directory of repository where script is run
    #     'py_dir_genes',            # src/pkgdavid/input/
    #     'log',                     # None sys.stdout
    #     'seed',                    # randomseed
    #     'prefix',                  # fig_goea_rnd
    #     'randomize_truenull_assc', # orig_noprune_ntn2
    #     'alpha',                 # 0.05
    #     'method',                # 'fdr_bh'
    #     'propagate_counts',      # False
    #     'association_file',      # 'gene_association.mgi'
    #     'genes_population',      # genes_mus
    #     'genes_study_bg',        # 'humoral_rsp'
    #     'goids_study_bg',        # 'humoral_rsp'
    #     'genes_popnullmaskout',  # ['immune', 'viral_bacteria']
    #     'perc_nulls',            # [100, 75, 50, 25]
    #     'num_genes_list',        # [4, 16, 128]
    #     'num_experiments',       # Number of simulated FDR ratios in an experiment set
    #     'num_sims',              # Number of sims per experiment; used to create one FDR ratio
    # ])

    desc_pat = 'p{PCNT}_{P0:03}to{PN:03}_{Q0:03}to{QN:03}_N{NEXP:05}_{NSIM:05}'

    def __init__(self):
        pass

    # def plt_box_tiled(self, base_img, plt_items, genes_goids, **kws):
    #     """Plot all boxplots for all experiments. X->(maxsigval, #tests), Y->%sig"""
    #     #key2exps = self._get_key2expsets('perc_null') # Keys are '% True Null'
    #     fout_log, base_img_genes, base_img_goids = self.get_fouts(simname)
    #     base_img_full = os.path.join(self.pobj.params['repo'], base_img)
    #     #plt_box_tiled(base_img_full, key2exps, plt_items, genes_goids, **kws)

    # def _plt_box_tiled(self, base_img, plt_items, genes_goids, **kws):
    #     """Plot all boxplots for all experiments. X->(maxsigval, #tests), Y->%sig"""
    #     #key2exps = self._get_key2expsets('perc_null') # Keys are '% True Null'
    #     fout_log, base_img_genes, base_img_goids = self.get_fouts(simname)
    #     base_img_full = os.path.join(self.pobj.params['repo'], base_img)
    #     #plt_box_tiled(base_img_full, key2exps, plt_items, genes_goids, **kws)

    def get_fouts(self, simname, params):
        """Return output filenames for the logfile and two plot files."""
        pre = params['prefix']
        dir_loc = 'doc/logs' if params['num_experiments'] >= 20 else 'doc/work'
        desc_str = self.get_desc_str(params)
        fout_log = os.path.join(dir_loc, '{PRE}_{DESC}.log'.format(PRE=pre, DESC=desc_str))
        base_img_genes = os.path.join(dir_loc, '{B}'.format(
            B='{PRE}_{DESC}_{NAME}'.format(PRE=pre, DESC=desc_str, NAME=simname)))
        base_img_goids = base_img_genes.replace('goea', 'goids')          # GOIDS
        return fout_log, base_img_genes, base_img_goids

    def get_desc_str(self, params):
        """Get the name of the plot file for the tiled plot."""
        return self.desc_pat.format(
            PCNT=int(params['propagate_counts']),
            P0=params['perc_nulls'][0],   # True Null %
            PN=params['perc_nulls'][-1],  # True Null %
            Q0=params['num_genes_list'][0],
            QN=params['num_genes_list'][-1],
            NEXP=params['num_experiments'],
            NSIM=params['num_sims'])


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
