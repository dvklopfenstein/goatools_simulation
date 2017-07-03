"""Runs GOEA Simulations. Holds background data/params, like GO-DAG & alpha."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

from goatools.base import get_godag
from goatools.go_enrichment import GOEnrichmentStudy

class DataBase(object):
    """Holds paramaters and data used in every GOEA Simulation."""

    def __init__(self, alpha, method):
        self.alpha = alpha
        self.method = method
        self.go_dag = get_godag() # GODag go-basic.obo: fmt(1.2) rel(2017-06-30) 48,928 GO Terms

    def get_goeaobj(self, pop_genes, assoc_geneid2gos):
        """Return a GOEnrichmentStudy specific for user-provided pop_genes and associations."""
        return GOEnrichmentStudy(
            pop_genes,
            assoc_geneid2gos,
            self.go_dag,
            propagate_counts=False,
            alpha=self.alpha,
            methods=[self.method],
            log=None)

    def prt_summary(self, prt):
        """Print summary of base information."""
        prt.write("{MULTI}\n".format(MULTI=self.get_str_mcorr()))
        self.prt_versions(prt)

    def get_str_mcorr(self):
        """Print parameters and versions of GO-DAG used in this simulation."""
        return "alpha({A}) method({M})".format(A=self.alpha, M=self.method)

    def prt_versions(self, prt):
        """Report results GOEAs on actual associations and randon associations."""
        prt.write("SETTINGS AND GO-DAG VERSION:\n")
        prt.write("    Multitest Params: {INFO}\n".format(INFO=self.get_str_mcorr()))
        prt.write("    GO-DAG version:   {INFO}\n".format(INFO=self.go_dag.version))

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
