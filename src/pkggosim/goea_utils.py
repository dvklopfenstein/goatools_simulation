"""Utilities for the GOEA Simulations."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
import pkgutil
import importlib
from random import shuffle
from goatools_suppl.proj_data import GoatoolsDataMaker


def get_study2genes():
    """Return study2genes."""
    studies = ['immune', 'viral_bacteria', 'cytokine_rsp', 'humoral_rsp', 'gamma_delta_t']
    study_genes = [(s, import_var('pkggosim.genes_{S}'.format(S=s), 'GENES')) for s in studies]
    return cx.OrderedDict(study_genes)

def get_assoc_data(fin_assc, genes_pop):
    """Return associations as ens2gos."""
    return GoatoolsDataMaker.get_assoc_data(fin_assc, genes_pop)

def import_var(modulestr, varname, log=None, rpterr=False):
    """Return variable inside module."""
    mod = import_mod(modulestr, log)
    if mod is not None:
        var = getattr(mod, varname, None)
        if var is not None:
            return var
    if rpterr:
        raise Exception("VAR({V}) NOT FOUND IN MOD({M})".format(V=varname, M=modulestr))

def import_mod(modulestr, log=None):
    """Import Python module"""
    if pkgutil.find_loader(modulestr) is not None:
        if log is not None:
            log.write("  IMPORT {MOD}\n".format(MOD=modulestr))
        return importlib.import_module(modulestr)
    if log is not None:
        log.write("  None   {MOD}\n".format(MOD=modulestr))
    return None

def shuffle_associations(assoc_ens2gos):
    """Randomly shuffle associations to mimic a list of genes having no significance."""
    # Get a list of GO-list length of all genes
    goset_lens = [len(gos) for gos in assoc_ens2gos.values()]
    gos_all_set = set()
    for gos_gene in assoc_ens2gos.values():
        gos_all_set |= gos_gene
    gos_all_lst = list(gos_all_set)
    # Randomly shuffle GOs
    shuffle(goset_lens)
    shuffle(gos_all_lst)
    # Build new randomly shuffled association
    assc_rand = {}
    idx_start = 0
    for geneid, golen in zip(assoc_ens2gos.keys(), goset_lens):
        idx_stop = idx_start + golen
        assc_rand[geneid] = gos_all_lst[idx_start:idx_stop]
        idx_start = idx_stop
    return assc_rand

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
