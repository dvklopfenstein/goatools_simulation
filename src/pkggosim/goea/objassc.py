"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
from pkggosim.goea.utils import get_assoc_data, get_assoc_hdr
from pkggosim.goea.assc_shuffle import RandAssc

class DataAssc(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntdesc = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, assc_file, pop_genes, goids_study_bg):
        # Read the association file. Save GOs related to population genes
        assc_geneid2gos = get_assoc_data(assc_file, pop_genes)
        # Simplify sim analysis: Use population genes found in association for GOEA Sim eval
        self.pop_genes = set(pop_genes).intersection(set(assc_geneid2gos.keys()))
        self.goids_study_bg = goids_study_bg # 9 GO IDs for humoral response
        # Speed sims: Use the association subset actually in the population
        self.assc_hdr = get_assoc_hdr(assc_file)
        self.assc = {g:gos for g, gos in assc_geneid2gos.items() if g in self.pop_genes}
        self.objassc_all = RandAssc(self.assc)
        self._go2genes = self._init_go2genes()
        # Set by set_targeted
        self.goids_tgtd = None
        self.objassc_pruned = None
        self.objassc_tgtd = None

    def set_targeted(self, goids_tgtd):
        """Set targeted GO IDs: Significant, but not tracked."""
        self.goids_tgtd = goids_tgtd
        assc_pruned, assc_tgtd = self.split_assc(goids_tgtd)
        self.objassc_pruned = RandAssc(assc_pruned)
        self.objassc_tgtd = RandAssc(assc_tgtd)

    def prt_summary(self, prt):
        """Print summary of parameters and background data."""
        prt.write("\nASSOCIATION INFORMATION:\n    ")
        prt.write("{ASSC}\n\n".format(ASSC="\n    ".join(self.assc_hdr.split("\n"))))
        prt.write("{N:6,} GENES  IN ASSOCIATION\n".format(N=len(self.objassc_all.assc_geneid2gos)))
        prt.write("{N:6,} GO IDs IN ASSOCIATION\n".format(N=len(self._go2genes.keys())))
        prt.write("{N:6,} GENES  IN POPULATION\n".format(N=len(self.pop_genes)))

    def _init_go2genes(self, geneids=None):
        """Return association (gene2gos) as go2genes."""
        return self.get_go2genes(self.objassc_all.assc_geneid2gos, geneids)

    @staticmethod
    def get_go2genes(assc, geneids=None):
        """Return association (gene2gos) as go2genes."""
        go2genes = cx.defaultdict(set)
        for gene, goids in assc.items():
            if geneids is None or gene in geneids:
                for goid in goids:
                    go2genes[goid].add(gene)
        return go2genes

    def split_assc(self, goids_tgtd_all):
        """Remove targeted GO IDs from all gene associations. Place in new sub-assc."""
        assc_pruned = {}
        assc_tgtd = {}
        for geneid, goids_gene in self.objassc_all.assc_geneid2gos.items():
            goids_tgtd_cur = goids_gene.intersection(goids_tgtd_all)
            if goids_tgtd_cur:
                assc_pruned[geneid] = goids_gene.difference(goids_tgtd_cur)
                assc_tgtd[geneid] = goids_tgtd_cur
            else:
                assc_pruned[geneid] = goids_gene
        return assc_pruned, assc_tgtd

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
