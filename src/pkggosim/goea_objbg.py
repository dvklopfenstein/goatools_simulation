"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
from pkggosim.goea_objbase import DataBase
from pkggosim.goea_utils import get_assoc_data

class DataBackground(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntdesc = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, alpha, method, pop_genes, assc_file):
        self.objbase = DataBase(alpha, method)
        # Read the association file. Save GOs related to population genes
        assc_geneid2gos = get_assoc_data(assc_file, pop_genes)
        # Simplify sim analysis: Use population genes found in association for GOEA Sim eval
        self.pop_genes = set(pop_genes).intersection(set(assc_geneid2gos.keys()))
        # Speed sims: Use the association subset actually in the population
        self.assc = {g:gos for g, gos in assc_geneid2gos.items() if g in self.pop_genes}
        self.objgoea = self.objbase.get_goeaobj(self.pop_genes, self.assc) # GOEnrichmentStudy obj


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
