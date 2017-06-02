"""Holds parameters used to create one set of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import timeit
import datetime
from random import shuffle

def get_hms(tic):
    """Print elapsed time as simulations run."""
    return str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))


def get_fout_img(exp_params, img_pat="sim_{P0:03}to{PN:03}_{MAX0:02}to{MAXN:02}.png"):
    """Get the name of the png file for the tiled plot."""
    return img_pat.format(
        P0=exp_params['perc_nulls'][0],   # True Null %
        PN=exp_params['perc_nulls'][-1],  # True Null %
        MAX0=int(exp_params['max_sigpvals'][0]*100),  # 0.01 ->"01"
        MAXN=int(exp_params['max_sigpvals'][-1]*100),
        Q0=exp_params['num_hypoths_list'][0],
        QN=exp_params['num_hypoths_list'][-1],
        NEXP=exp_params['num_experiments'])


def shuffle_associations(assoc_ens2gos):
    """Randomly shuffle associations to mimic a list of genes having no significance."""
    # Get a list of GO-list length of all genes
    goset_lens = [len(gos) for gos in assoc_ens2gos.values()]
    gos_all = set()
    for gos_gene in assoc_ens2gos.values():
        gos_all |= gos_gene
    gos_all = list(gos_all)
    # Randomly shuffle GOs
    shuffle(goset_lens)
    shuffle(gos_all)
    # Build new randomly shuffled association
    assc_rand = {}
    idx_start = 0
    for geneid, golen in zip(assoc_ens2gos.keys(), goset_lens):
        idx_stop = idx_start + golen
        assc_rand[geneid] = gos_all[idx_start:idx_stop]
        idx_start = idx_stop
    return assc_rand
        


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
