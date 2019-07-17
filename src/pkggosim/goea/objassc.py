"""Holds population genes and associations."""

from __future__ import print_function

__copyright__ = "Copyright (C) 2016-2019, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import collections as cx
import numpy as np
# from pkggosim.goea.utils import get_assoc_data, get_assoc_hdr
from pkggosim.goea.utils import get_assoc_data
from pkggosim.goea.assc_shuffle import RandAssc
from goatools.associations import get_gaf_hdr
from goatools.associations import get_b2aset
from goatools.associations import get_assc_pruned
from PyBiocode.Utils.stats import prt_percentiles
from goatools.gosubdag.gosubdag import GoSubDag
from goatools.gosubdag.go_tasks import update_association

#pylint: disable=too-many-instance-attributes
class DataAssc(object):
    """Holds GOEA information. Runs sets of GOEAs."""

    ntdesc = cx.namedtuple("results", "name perc_null tot_study")

    def __init__(self, params, godag):
        # Associations: rm obsolete GO IDs
        _assc_file = params['association_file']
        _pop_genes = params['genes_population']
        self.assc_hdr = get_gaf_hdr(_assc_file)
        # Remove obsolete GO IDs from association if needed
        _assc_geneid2gos_orig = self._init_assc(_assc_file, _pop_genes, godag)
        # Associations: Add parent all GO IDs if propagate_counts is True
        # DO propagate_counts before pruning because this step adds created higly associated GO IDs
        _assc_geneid2gos = _assc_geneid2gos_orig
        sys.stdout.write("PROPAGATE_COUNTS({VAL})\n".format(
            VAL=params.get('propagate_counts', False)))
        if params.get('propagate_counts', False):
            _assc_geneid2gos = {g:set(gos) for g, gos in _assc_geneid2gos.items()}
            update_association(_assc_geneid2gos, godag)
            # _go2genes = get_b2aset(_assc_geneid2gos)
            # vals = [len(genes) for genes in _go2genes.values()]
            # # Associations MUST be pruned if using propagate counts
            # max_genes = int(round(np.percentile(vals, 97.5)))
            # _assc_geneid2gos = self._prune_assc(_assc_geneid2gos, max_genes, godag)
        # Associations: rm GOs with lots of genes if specified by user
        # DO prune before getting population gene list so all pop genes have associations
        _assc_geneid2gos = self._possibly_prune_assc(_assc_geneid2gos, 1000, godag, params)
        ##### Associations: rm GOs with lots of genes if specified by user
        ####_assc_geneid2gos = _possibly_prune_assc(_assc_geneid2gos, 1000, godag)
        #### _randomize_truenull_assc = params.get('randomize_truenull_assc', None)
        #### if _randomize_truenull_assc is not None and '_pruned_' in _randomize_truenull_assc:
        ####     _assc_geneid2gos = self._prune_assc(_assc_geneid2gos, 1000, godag)
        ####     print "PRUNE"
        #### else:
        ####     print "NO PRUNE"
        #### For sim analysis: Use population genes found in association for GOEA Sim eval
        self.pop_genes = set(_pop_genes).intersection(set(_assc_geneid2gos.keys()))
        # Speed sims: Use the association subset actually in the population
        _assc_all = {g:gos for g, gos in _assc_geneid2gos.items() if g in self.pop_genes}
        # Get all GO IDs in association
        self.pop_gos = self._init_assc_pop(_assc_all)
        self.go2genes = get_b2aset(_assc_all)
        self.objassc_all = RandAssc(_assc_all)  # Holds assc as well as providing shuffled version
        # Set by local set_targeted() when RunParams is initialized
        self.goids_tgtd = None     # Artifact GO IDs found to be also truly significant
        self.objassc_pruned = None
        self.objassc_tgtd = None

    def _possibly_prune_assc(self, assc_geneid2gos, max_genes, godag, params):
        """Prune association of GOs that are associated with many genes if specified by the user."""
        _randomize_truenull_assc = params.get('randomize_truenull_assc', None)
        if _randomize_truenull_assc is not None and '_pruned_' in _randomize_truenull_assc:
            print("PRUNE")
            return self._prune_assc(assc_geneid2gos, max_genes, godag)
        else:
            print("NO PRUNE")
            return assc_geneid2gos

    @staticmethod
    def _init_assc_pop(assc_geneid2gos):
        """Keep GO IDs that are associated with the population genes."""
        gos_pop = set()
        for gos_cur in assc_geneid2gos.values():
            gos_pop |= gos_cur
        return gos_pop

    def get_assc(self):
        """Return full association."""
        return self.objassc_all.assc_geneid2gos

    def _prune_assc(self, assc_geneid2gos, max_genecnt, godag, prt=sys.stdout):
        """Remove GO IDs which are associated with large numbers of genes."""
        #### # DEPRECATED: Now in GOATOOLS
        #### go2genes_orig = get_b2aset(assc_geneid2gos)
        #### go2genes_prun = {go:gs for go, gs in go2genes_orig.items() if len(gs) <= max_genecnt}
        #### num_was = len(go2genes_orig)
        #### num_now = len(go2genes_prun)
        #### gos_rm = set(go2genes_orig.keys()).difference(set(go2genes_prun.keys()))
        #### assert num_was-num_now == len(gos_rm)
        #### prt.write("{N} GO IDs removed assc. w/>{G} genes = {A} - {B}\n".format(
        ####     N=num_was-num_now, G=max_genecnt, A=num_was, B=num_now))
        assc_geneid2gos_pruned, goids_rm = get_assc_pruned(assc_geneid2gos, None, max_genecnt, prt=prt)
        go2genes_orig = get_b2aset(assc_geneid2gos)

        for desc in self.get_go2desc(goids_rm, godag, go2genes_orig).values():
            prt.write("    {DESC}\n".format(DESC=desc))
        cnts_genes = [len(gs) for gs in go2genes_orig.values()]
        # print sorted(cnts_genes)
        prt_percentiles("Number of genes associated with GO IDs.", cnts_genes, "{:6.0f}", prt)

        #### self.prt_goids_assc(goids_rm, godag, go2genes_orig, "    ", prt)
        #### return get_b2aset(go2genes_prun)
        return assc_geneid2gos_pruned

    @staticmethod
    def get_go2desc(goids, go2obj, go2genes):
        """Print GO terms and the number of genes associated with the GO ID."""
        go_desc = []
        gosubdag = GoSubDag(goids, go2obj)
        go2nt = gosubdag.get_go2nt(goids)
        pat = "{G:6,} genes {DESC}"
        pat_go = gosubdag.prt_attr['fmt']
        for goid, ntgo in sorted(go2nt.items(), key=lambda t: [t[1].NS, t[1].depth, -1*t[1].dcnt]):
            desc = pat_go.format(**ntgo._asdict())
            go_desc.append((goid, pat.format(G=len(go2genes[goid]), DESC=desc)))
        return cx.OrderedDict(go_desc)

    def set_targeted(self, goids_tgtd):
        """Set targeted GO IDs: Significant, but not tracked."""
        self.goids_tgtd = goids_tgtd
        # go:self.go2genes contains only GO IDs related to the population genes
        go2genes = {go:self.go2genes[go] for go in goids_tgtd}
        genes = get_b2aset(go2genes)
        print("TARGETED GENES({Gs})".format(Gs=len(genes)))
        assc_pruned, assc_tgtd = self._split_assc(goids_tgtd)
        print("AASSSSCC LENS PRUNED({}) TGTD({})".format(len(assc_pruned), len(assc_tgtd))) # TBD rm
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

    #### @staticmethod
    #### def get_go2genes(assc, geneids=None):
    ####     """Return association (gene2gos) as go2genes."""
    ####     go2genes = cx.defaultdict(set)
    ####     for gene, goids in assc.items():
    ####         if geneids is None or gene in geneids:
    ####             for goid in goids:
    ####                 go2genes[goid].add(gene)
    ####     return go2genes

    def _split_assc(self, goids_tgtd_all):
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
        gos_active = set([go for go, o in godag.items() if not o.is_obsolete]) # ~2,000 obsolete GOs
        return {g:gos.intersection(gos_active) for g, gos in assc.items()}

# Copyright (C) 2016-2019, DV Klopfenstein, Haibao Tang. All rights reserved.
