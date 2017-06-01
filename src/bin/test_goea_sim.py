#!/usr/bin/env python
"""Simulate a Gene Ontology Enrichment Analysis (GOEA) on one set of randomly generated study genes."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
from pkggosim.goea_sim import GoeaSim

def main():
    hypoth_qty = 8
    num_null = 4
    multi_params = {'alpha' : 0.05, 'method' : 'fdr_bh'}
    #import_var(modulestr, varname, log=None, rpterr=False):
    objsim = GoeaSim(hypoth_qty, num_null, multi_params)

if __name__ == '__main__':
    main()

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
