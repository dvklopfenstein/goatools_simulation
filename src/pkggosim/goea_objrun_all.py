"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
from random import shuffle
from pkggosim.goea_objbg import GoeaSimObj


class RunGoeas(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntdesc = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, alpha, method, pop_genes, assc_geneid2gos):
        self.objbg = GoeaSimObj(alpha, method)
        self.pop_genes = pop_genes
        self.assc = assc_geneid2gos
        self.objgoea = objbg.get_goeaobj(genes_mus, assoc_geneid2gos) # GOEnrichmentStudy obj


# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
