"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
from random import shuffle
from pkggosim.goea.utils import get_assoc_data, get_assoc_hdr

class DataAssc(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntdesc = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, assc_file, pop_genes, randomize_truenull_assc=False):
        # Read the association file. Save GOs related to population genes
        assc_geneid2gos = get_assoc_data(assc_file, pop_genes)
        # Simplify sim analysis: Use population genes found in association for GOEA Sim eval
        self.pop_genes = set(pop_genes).intersection(set(assc_geneid2gos.keys()))
        # Speed sims: Use the association subset actually in the population
        self.assc_hdr = get_assoc_hdr(assc_file)
        self.assc = {g:gos for g, gos in assc_geneid2gos.items() if g in self.pop_genes}
        self.go2genes = self.get_go2genes()
        self.randomize_truenull_assc = randomize_truenull_assc

    def prt_summary(self, prt):
        """Print summary of parameters and background data."""
        prt.write("\nASSOCIATION INFORMATION:\n    ")
        prt.write("{ASSC}\n\n".format(ASSC="\n    ".join(self.assc_hdr.split("\n"))))
        prt.write("{N:6,} GENES  IN ASSOCIATION\n".format(N=len(self.assc)))
        prt.write("{N:6,} GO IDs IN ASSOCIATION\n".format(N=len(self.go2genes.keys())))
        prt.write("{N:6,} GENES  IN POPULATION\n".format(N=len(self.pop_genes)))

    def get_go2genes(self, geneids=None):
        """Return association (gene2gos) as go2genes."""
        go2genes = cx.defaultdict(set)
        for gene, goids in self.assc.items():
            if geneids is None or gene in geneids:
                for goid in goids:
                    go2genes[goid].add(gene)
        return go2genes

    def get_randomized_assc(self, genes_nontruenull):
        """Randomize assc. with all "True Null" genes."""
        assc_rand = self.assc
        raise RuntimeError("TIME TO IMPLEMENT get_randomized_assc")
        return assc_rand

    @staticmethod
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
