"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
from pkggosim.goea_objbg import GoeaSimObj


class RunGoeas(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntdesc = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, alpha, method, pop_genes, assc_geneid2gos):
        self.objbg = GoeaSimObj(alpha, method)
        self.pop_genes = pop_genes
        self.assc = assc_geneid2gos
        self.objgoea = self.objbg.get_goeaobj(pop_genes, assc_geneid2gos) # GOEnrichmentStudy obj


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
