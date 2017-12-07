"""Runs all experiments for all sets of experiments."""

from __future__ import print_function

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import re
import importlib
from pkggosim.goea.plot_results import plt_box_tiled
# import sys

class Basename(object):
    """Runs all experiments for all sets of experiments."""

    # pylint: disable=bad-whitespace
    n2dotsize = {
        (500, 1000): {'fdr_actual':0.70, 'sensitivity':0.50, 'specificity':0.50},
        (100, 1000): {'fdr_actual':0.95, 'sensitivity':0.60, 'specificity':0.60},
        (100,   30): {'fdr_actual':1.30, 'sensitivity':0.60, 'specificity':0.60},
        ( 50,   50): {'fdr_actual':2.00, 'sensitivity':0.70, 'specificity':0.70},
        ( 50,   20): {'fdr_actual':2.00, 'sensitivity':1.00, 'specificity':1.00}, # 4:56
        ( 20,   20): {'fdr_actual':2.00, 'sensitivity':2.00, 'specificity':2.00}, # 1:25
        (  4,    4): {'fdr_actual':4.00, 'sensitivity':3.00, 'specificity':3.00}, # 0:04 0:05
        (  2,    2): {'fdr_actual':4.00, 'sensitivity':3.00, 'specificity':3.00}, # 0:01 0:02
    }

    repo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..")
    desc_pat = 'p{PCNT}_{P0:03}to{PN:03}_{Q0:03}to{QN:03}_N{NEXP:05}_{NSIM:05}'

    def __init__(self):
        pass

    def plt_mod(self, dirloc, modulestr, plt_items, pltargs):
        """Plot one set of experiments."""
        genes_goids = modulestr[-5:]
        assert genes_goids in set(['genes', 'goids'])
        assert modulestr[:14] == 'pkggosim.data.'
        base_img_rel = "{DIRLOC}/{BASE}.img".format(DIRLOC=dirloc, BASE=modulestr[14:])
        base_img_abs = os.path.join(self.repo, base_img_rel)
        kws = pltargs.copy()
        kws['dotsize'] = self._get_dotsize(modulestr)
        key2exps = importlib.import_module(modulestr).percnull2expsets
        plt_box_tiled(base_img_abs, key2exps, plt_items, genes_goids, **kws)

    def _get_dotsize(self, modulestr):
        """Return tuple containing NEXP and NSIM."""
        mtch = re.search(r'_N(\d{5})_(\d{5})', modulestr)
        return self.n2dotsize[(int(mtch.group(1)), int(mtch.group(2)))]

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
