"""Utilities for the GOEA Simulations."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import pkgutil
import importlib
from goatools_suppl.proj_data import GoatoolsDataMaker


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

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
