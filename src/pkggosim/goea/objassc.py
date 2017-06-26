"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
from random import shuffle
from pkggosim.goea.utils import get_assoc_data, get_assoc_hdr

class DataAssc(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntdesc = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, assc_file, pop_genes, randomize_truenull_assc):
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

    def split_assc(self, goids_tgtd_all):
        """Remove targeted GO IDs from all gene associations. Place in new sub-assc."""
        assc_pruned = {}
        assc_tgtd = {}
        for geneid, goids_gene in self.assc.items():
            goids_tgtd_cur = goids_gene.intersection(goids_tgtd_all)
            if goids_tgtd_cur:
                assc_pruned[geneid] = goids_gene.difference(goids_tgtd_cur)
                assc_tgtd[geneid] = goids_tgtd_cur
            else:
                assc_pruned[geneid] = goids_gene
        return assc_pruned, assc_tgtd

    def get_randomized_assc(self, genes_truenull, genes_nontruenull):
        """Randomize assc. for only all "True Null" genes."""
        # If there are no "True Nulls", return original assc wo/randomizing
        assert not genes_truenull.intersection(genes_nontruenull), "TRUE NULL ISEC w/NON-TRUE NULL"
        if not genes_truenull:
            return self.assc
        # Get the subset of the assc to randomize
        assc_subset = {g:self.assc[g] for g in genes_truenull} if genes_nontruenull else self.assc
        assc_rand = self.shuffle_associations(assc_subset)
        # Add back non-randomized parts of the assc.
        for gene in genes_nontruenull:
            assc_rand[gene] = self.assc[gene]
        return assc_rand

    def shuffle_associations(self, assc_geneid2gos):
        """Randomly shuffle all associations to mimic a list of genes having no significance."""
        # Get a list of GO-list length of all genes
        gos_2d = assc_geneid2gos.values()
        # Build new randomly shuffled association
        genes = assc_geneid2gos.keys()
        golens = [len(gos) for gos in gos_2d]
        shuffle(golens)
        # Get Random assc #1
        goctr_rand = self._mk_rand_gocnts(gos_2d)
        assc_rand = {g:self._get_rand_goids(n, goctr_rand) for g, n in zip(genes, golens)}
        # assc_rand = {g:assc_geneid2gos[g] for g, n in zip(genes, golens)}
        # assc_rand = self._simple_assc_rand(genes, golens, gos_2d)
        return assc_rand

####    def _simple_assc_rand(genes, golens, gos_2d):
####        """Long sim times."""
####        goids = self._get_goids_assc(gos_2d)
####        assc_rand = {}
####        for geneid, num in zip(genes, golens):
####            shuffle(goids)
####            assc_rand[geneid] = goids[:num]
####        return assc_rand

####    def _get_goids_assc(self, gos_2d):
####        """Get list of all GO IDs."""
####        goids = set()
####        for gos in gos_2d:
####            goids |= gos
####        return list(goids)

    @staticmethod
    def _mk_rand_gocnts(gos_2d):
        """Use GO IDs in current asscs to create randomized list of GO IDs for new rand assc."""
        # Get current counts of GO IDs in an association
        ctr_orig = cx.Counter()
        for gos_gene in gos_2d:
            for goid in gos_gene:
                ctr_orig[goid] += 1
        # Create new randomized counts of GO IDs in an association
        goids, cnts = zip(*ctr_orig.items())
        goids = list(goids)
        cnts = list(cnts)
        shuffle(goids)
        shuffle(cnts)
        ctr_rand = cx.Counter({g:c for g, c in zip(goids, cnts)})
        assert sum(ctr_orig.values()) == sum(ctr_rand.values())
        assert len(ctr_orig) == len(ctr_rand)
        return ctr_rand

    @staticmethod
    def _get_rand_goids(num_goids, goctr):
        """Return N randomly selected GO IDs. Adjust counts."""
        goids_all = list(goctr)
        assert goids_all
        shuffle(goids_all)
        # Choose a subset
        goids_cur = set(goids_all[:num_goids])
        if num_goids > len(goids_all):
            assert len(goids_all) < 1000, "RQ({}) OF {}".format(num_goids, len(goids_all))
        # Adjust counter values
        for goid in goids_cur:
            if goctr[goid] != 1:
                goctr[goid] -= 1
            else:
                del goctr[goid]
        return goids_cur

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
