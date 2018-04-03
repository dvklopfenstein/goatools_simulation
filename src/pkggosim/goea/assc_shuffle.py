"""Holds the function which randomly shuffles a gene-to-ontolgies association."""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from collections import Counter
from numpy.random import shuffle, randint

#pylint: disable=too-few-public-methods

class RandAssc(object):
    """Holds lists for random shuffling."""

    def __init__(self, assc_geneid2gos):
        self.assc_geneid2gos = assc_geneid2gos
        self.genes = assc_geneid2gos.keys()
        self.gos_2d = assc_geneid2gos.values()
        self.golens = [len(gos) for gos in self.gos_2d]
        # Initialize list of all GO IDs and their counts in the association
        self.goids = None  # List of unique GO IDs in an association
        self.gocnts = None # List of the quantity of GO IDs for each GO ID in an association
        self._init_goidcnts()
        self.num_goids = len(self.goids)
        sys.stdout.write("GO({}) CNT({})\n".format(len(self.goids), len(self.gocnts)))

    def _init_goidcnts(self):
        """Initialize list of all GO IDs and their counts in the association."""
        ctr = Counter()
        for gos_gene in self.gos_2d:
            for goid in gos_gene:
                ctr[goid] += 1
        goids, gocnts = zip(*ctr.items())
        self.goids = list(goids)
        self.gocnts = list(gocnts)

    def get_shuffled_associations(self):
        """Randomly shuffle all associations to mimic a list of genes having no significance."""
        assc_rand = {}
        # Create randomly shuffled long list of all GO IDs for random assc.
        shuffle(self.goids)
        goctr_rand = list(Counter({go:cnt for go, cnt in zip(self.goids, self.gocnts)}).elements())
        assert len(goctr_rand) == sum(self.golens) # 275,168
        shuffle(goctr_rand)
        # Use long list of random GO IDs to create new random assc.
        start = 0
        shuffle(self.golens)
        for geneid, golen in zip(self.genes, self.golens):
            stop = start + golen
            goid_set = set(goctr_rand[start:stop])
            # Add more goids if needed
            if len(goid_set) != golen:
                self._get_addtl_goids(goid_set, golen)
            assc_rand[geneid] = goid_set
            assert len(goid_set) == golen
            start = stop
        assert len(assc_rand) == len(self.genes)
        return assc_rand

    def _get_addtl_goids(self, goid_set, golen):
        """Get additional GO IDs."""
        idx = randint(0, self.num_goids)
        while True:
            goid_set.add(self.goids[idx])
            if len(goid_set) == golen:
                return
            idx += 1
            if idx == self.num_goids:
                idx = 0

# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
