"""Utilities for the GOEA Simulations."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
import pkgutil
import importlib
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

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
