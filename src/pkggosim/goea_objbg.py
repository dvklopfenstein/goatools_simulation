"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
from pkggosim.goea_objbase import DataBase
from pkggosim.goea_utils import get_assoc_data, get_assoc_hdr

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
        self.assc_hdr = get_assoc_hdr(assc_file)
        self.assc = {g:gos for g, gos in assc_geneid2gos.items() if g in self.pop_genes}
        self.objgoea = self.objbase.get_goeaobj(self.pop_genes, self.assc) # GOEnrichmentStudy obj

    def prt_summary(self, prt):
        """Print summary of parameters and background data."""
        self.objbase.prt_summary(prt)
        prt.write("\nASSOCIATION INFORMATION:\n    ")
        prt.write("{ASSC}\n\n".format(ASSC="\n    ".join(self.assc_hdr.split("\n"))))
        prt.write("{N:6,} GENES  IN ASSOCIATION\n".format(N=len(self.assc)))
        prt.write("{N:6,} GO IDs IN ASSOCIATION\n".format(N=len(self.get_assc_goids())))
        prt.write("{N:6,} GENES  IN POPULATION\n".format(N=len(self.pop_genes)))

    def get_assc_goids(self):
        """Return the GO IDs used in the simulation."""
        goids_all = set()
        for goids_gene in self.assc.values():
            goids_all |= goids_gene
        return goids_all

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
