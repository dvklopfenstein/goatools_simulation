"""Holds population genes and associations."""

__cright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
import numpy as np
from pkggosim.goea.utils import get_assoc_data, get_assoc_hdr
from pkggosim.goea.assc_shuffle import RandAssc
from goatools_alpha.gosubdag import GoSubDag

class DataAssc(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntdesc = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, params, godag):
        # Associations: rm obsolete GO IDs
        _assc_file = params['association_file']
        _pop_genes = params['genes_population']
        _assc_geneid2gos = self._init_assc(_assc_file, _pop_genes, godag)
        # Associations: rm GOs with lots of genes
        if '_pruned_' in params['randomize_truenull_assc']:
            _assc_geneid2gos = self._prune_assc(_assc_geneid2gos, 1000, godag)
            print "PRUNE"
        else:
            print "NO PRUNE"
        # Simplify sim analysis: Use population genes found in association for GOEA Sim eval
        self.pop_genes = set(_pop_genes).intersection(set(_assc_geneid2gos.keys()))
        # Speed sims: Use the association subset actually in the population
        self.assc_hdr = get_assoc_hdr(_assc_file)
        _assc_all = {g:gos for g, gos in _assc_geneid2gos.items() if g in self.pop_genes}
        self.go2genes = self.get_go2genes(_assc_all)
        self.objassc_all = RandAssc(_assc_all)
        # Set by local set_targeted() when RunParams is initialized
        self.goids_tgtd = None
        self.objassc_pruned = None
        self.objassc_tgtd = None

    def _prune_assc(self, assc_geneid2gos, max_genecnt, godag, prt=sys.stdout):
        """Remove GO IDs which are associated with large numbers of genes."""
        go2genes_orig = self.get_go2genes(assc_geneid2gos)
        go2genes_prun = {go:gs for go, gs in go2genes_orig.items() if len(gs) <= max_genecnt}
        num_was = len(go2genes_orig)
        num_now = len(go2genes_prun)
        gos_rm = set(go2genes_orig.keys()).difference(set(go2genes_prun.keys()))
        assert num_was-num_now == len(gos_rm)
        prt.write("{N} GO IDs removed assc. w/>{G} genes = {A} - {B}\n".format(
            N=num_was-num_now, G=max_genecnt, A=num_was, B=num_now))
        self.prt_goids_assc(gos_rm, godag, go2genes_orig, "    ", prt)
        return self.get_go2genes(go2genes_prun)

    def prt_goids_assc(self, goids, go2obj, go2genes, pre="", prt=sys.stdout):
        """Print GO terms and the number of genes associated with the GO ID."""
        go2desc = self.get_go2desc(goids, go2obj, go2genes)
        pat = "{PRE}{DESC}\n"
        for goid, desc in go2desc.items():
            prt.write(pat.format(PRE=pre, DESC=desc))

    @staticmethod
    def get_go2desc(goids, go2obj, go2genes):
        """Print GO terms and the number of genes associated with the GO ID."""
        go_desc = []
        gosubdag = GoSubDag(goids, go2obj)
        go2nt = gosubdag.get_go2nt(goids)
        pat = "{G:5,} genes {DESC}"
        pat_go = gosubdag.get_prt_fmt()
        sortby = gosubdag.get_sortby()
        for goid, ntgo in sorted(go2nt.items(), key=lambda t: sortby(t[1])):
            desc = pat_go.format(**ntgo._asdict())
            go_desc.append((goid, pat.format(G=len(go2genes[goid]), DESC=desc)))
        return cx.OrderedDict(go_desc)

    def set_targeted(self, goids_tgtd):
        """Set targeted GO IDs: Significant, but not tracked."""
        self.goids_tgtd = goids_tgtd
        assc_pruned, assc_tgtd = self.split_assc(goids_tgtd)
        print "AASSSSCC LENS PRUNED({}) TGTD({})".format(len(assc_pruned), len(assc_tgtd)) # TBD rm
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

    @staticmethod
    def _init_assc(assc_file, pop_genes, godag):
        """Read the association file. Save GOs related to population genes that are not obsolete."""
        assc = get_assoc_data(assc_file, pop_genes) # ~18,600
        gos_obsolete = set([o.id for o in godag.values() if o.is_obsolete]) # ~2,000
        return {g:gos.difference(gos_obsolete) for g, gos in assc.items()}

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
