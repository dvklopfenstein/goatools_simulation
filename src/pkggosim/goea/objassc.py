"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
import numpy as np
from pkggosim.goea.utils import get_assoc_data, get_assoc_hdr
from pkggosim.goea.assc_shuffle import RandAssc

class DataAssc(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntdesc = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, assc_file, pop_genes, goids_study_bg, godag):
        assc_all = self._init_assc(assc_file, pop_genes, godag) # rm obsolete GO IDs
        assc_geneid2gos = self._prune_assc(assc_all, 1000) # rm GOs with lots of genes
        # Simplify sim analysis: Use population genes found in association for GOEA Sim eval
        self.pop_genes = set(pop_genes).intersection(set(assc_geneid2gos.keys()))
        self.goids_study_bg = goids_study_bg # 9 GO IDs for humoral response
        # Speed sims: Use the association subset actually in the population
        self.assc_hdr = get_assoc_hdr(assc_file)
        self.assc = {g:gos for g, gos in assc_geneid2gos.items() if g in self.pop_genes}
        self.go2genes = self.get_go2genes(self.assc)
        self.objassc_all = RandAssc(self.assc)
        # Set by set_targeted
        self.goids_tgtd = None
        self.objassc_pruned = None
        self.objassc_tgtd = None

    def _prune_assc(self, assc_geneid2gos, max_genecnt):
        """Remove GO IDs which are associated with large numbers of genes."""
        go2genes_orig = self.get_go2genes(assc_geneid2gos)
        print "GOs WAS", len(go2genes_orig)
        go2genes_prun = {go:gs for go, gs in go2genes_orig.items() if len(gs) <= max_genecnt}
        print "GOs NOW", len(go2genes_prun)
        return self.get_go2genes(go2genes_prun)

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
        prt.write("{N:6,} GO IDs IN ASSOCIATION\n".format(N=len(self.go2genes.keys())))
        prt.write("{N:6,} GENES  IN POPULATION\n".format(N=len(self.pop_genes)))

    def prt_go2genes_freq(self, prt=sys.stdout):
        """Print gene count frequency among GOs in association."""
        # Of ~17,278 GOs in mouse association for Ensembl genes:
        #      ~5,200 GOs are assc. w/1 gene
        #     ~17,200 GOs are assc. w/ <= 350 genes
        go_genecnts = [len(gs) for gs in self.go2genes.values()]
        hist, bin_edges = np.histogram(go_genecnts, 20)
        for aval, bval in zip(hist, bin_edges):
            prt.write("EEEEEEEEEEE {A:6,} GOs {B:6.0f}\n".format(A=aval, B=bval))
        # print "CCCCC", sum(1 for c in go_genecnts if c <= 350)
        sys.exit()

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

    def _init_assc(self, assc_file, pop_genes, godag):
        """Read the association file. Save GOs related to population genes that are not obsolete."""
        assc = get_assoc_data(assc_file, pop_genes) # ~18,600
        gos_obsolete = set([o.id for o in godag.values() if o.is_obsolete]) # ~2,000
        return {g:gos.difference(gos_obsolete) for g, gos in assc.items()}

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
