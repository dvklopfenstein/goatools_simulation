"""Holds population genes and associations."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import timeit
import collections as cx
from random import shuffle
from pkggosim.common.utils import get_hms
from numpy.random import choice

class RandAssc(object):
    """Holds lists for random shuffling."""

    def __init__(self, assc_geneid2gos):
        self.assc_geneid2gos = assc_geneid2gos
        self.genes = assc_geneid2gos.keys()
        self.gos_2d = assc_geneid2gos.values()
        self.golens = [len(gos) for gos in self.gos_2d]
        # Initialize list of all GO IDs and their counts in the association
        self.goids = None
        self.gocnts = None
        self._init_goidcnts()
        print "GO({}) CNT({})".format(len(self.goids), len(self.gocnts))

    def _init_goidcnts(self):
        """Initialize list of all GO IDs and their counts in the association."""
        ctr = cx.Counter()
        for gos_gene in self.gos_2d:
            for goid in gos_gene:
                ctr[goid] += 1
        goids, gocnts = zip(*ctr.items())
        self.goids = list(goids)
        self.gocnts = list(gocnts)

    def get_shuffled_associations(self, maskout=None):
        return self.shuffle_associations_3(maskout)
        # return self.shuffle_associations_fast(maskout)

    def shuffle_associations_3(self, maskout):
        """Randomly shuffle all associations to mimic a list of genes having no significance."""
        # Create randomly shuffled long list of all GO IDs for random assc.
        num_gos_tot = sum(self.golens) # 275,168
        shuffle(self.gocnts)
        goctr_rand = list(cx.Counter({go:cnt for go, cnt in zip(self.goids, self.gocnts)}).elements())
        assert num_gos_tot == len(goctr_rand)
        shuffle(goctr_rand)
        # Use long list of random GO IDs to create new random assc.
        assc_rand = {}
        shuffle(self.golens)
        start = 0
        for geneid, golen in zip(self.genes, self.golens):
            stop = start + golen
            goid_list = goctr_rand[start:stop]
            goid_set = set(goctr_rand[start:stop])
            # Add more goids if needed
            num_addtl = len(goid_list) - len(goid_set)
            # if num_addtl != 0:
            #     goid_set |= set(choice(self.goids, num_addtl, replace=False))
            assc_rand[geneid] = goid_set
            start = stop
        return assc_rand

    def shuffle_associations_fast(self, maskout):
        """Randomly shuffle all associations to mimic a list of genes having no significance."""
        # Build new randomly shuffled association
        assc_rand = {}
        shuffle(self.golens)
        shuffle(self.goids)
        num_goids = len(self.goids)
        # print "GOIDS({}) GENES({}) GOLENS({})".format(num_goids, len(self.genes), len(self.golens))
        start = 0
        for geneid, go_cnt in zip(self.genes, self.golens):
            stop = start + go_cnt
            if stop >= num_goids:
                shuffle(self.goids)
                start = 0
                stop = go_cnt
            assc_rand[geneid] = self.goids[start:stop]
        return assc_rand

    def shuffle_associations_slow(self, maskout):
        """Randomly shuffle all associations to mimic a list of genes having no significance."""
        print "SHUFFLE"
        tic = timeit.default_timer()
        # Build new randomly shuffled association
        shuffle(self.golens)
        sys.stdout.write("HMS: {HMS} SHUFFLE A-2\n".format(HMS=get_hms(tic)))
        goctr_rand = cx.Counter({go:cnt for go, cnt in zip(self.goids, self.golens)})
        # Get Random assc #1
        shuffle(self.golens)
        sys.stdout.write("HMS: {HMS} SHUFFLE A-1 CTR\n".format(HMS=get_hms(tic)))
        lst = zip(self.genes, self.golens)
        sys.stdout.write("HMS: {HMS} SHUFFLE ZIP\n".format(HMS=get_hms(tic)))
        assc_rand = {g:self._get_rand_goids(n, goctr_rand) for g, n in lst if g not in maskout}
        # assc_rand = {g:assc_geneid2gos[g] for g, n in zip(genes, golens)}
        # assc_rand = self._simple_assc_rand(genes, golens, gos_2d)
        sys.stdout.write("HMS: {HMS} SHUFFLE DONE\n".format(HMS=get_hms(tic)))
        return assc_rand

    @staticmethod
    def _get_rand_goids(num_goids, goctr):
        """Return N randomly selected GO IDs. Adjust counts."""
        #tic = timeit.default_timer()
        # Choose a subset
        goids_cur = list(goctr)
        if num_goids < len(goids_cur):
            goids_cur = set(choice(goids_cur, num_goids, replace=False))
        #sys.stdout.write("HMS: {HMS} ... CHOSEN\n".format(HMS=get_hms(tic)))
        # Adjust counter values
        for goid in goids_cur:
            if goctr[goid] != 1:
                goctr[goid] -= 1
            else:
                del goctr[goid]
        #sys.stdout.write("HMS: {HMS} ... \n".format(HMS=get_hms(tic)))
        return goids_cur

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

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
