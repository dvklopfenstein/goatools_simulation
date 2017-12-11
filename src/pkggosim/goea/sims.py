"""Objain one simulated FDR value by running many P-Value sims w/multiple-test correction."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import numpy as np
from pkggosim.goea.sim import GoeaSim
from pkggosim.common.utils import get_hms


class ManyGoeaSims(object):
    """Run many simulations of a multiple-test correction run on a set of P-values."""

    expected_params = set(['num_sims', 'num_items', 'perc_null', 'num_null'])

    def __init__(self, params, pobj):
        self.params = params # num_sims num_items perc_null num_null
        self.pobj = pobj # RunParams object
        assert set(params.keys()) == self.expected_params
        simobjs = self._init_simobjs() # List of N=num_sims GoeaSim objects
        self.nts_tfpn = {
            'genes' : [o.nt_tfpn_genes for o in simobjs],
            'goids' : [o.nt_tfpn_goids for o in simobjs], # GOIDs
        }
        if self.pobj.params['py_dir_genes'] is not None:
            self.wrpy_genes(simobjs)

    def wrpy_genes(self, simobjs):
        """Write randomly generated study study group into a Python module."""
        # prt = sys.stdout
        # seedstr = "0x{S:08x}".format(S=self.pobj.objrnd.seed)
        fpat = "{DIR}/genes_{NM}_pn{PERCNULL:03}_g{G:05}"
        base = fpat.format(
            DIR=self.pobj.params['py_dir_genes'],
            PERCNULL=self.params['perc_null'], G=self.params['num_items'],
            NM=self.pobj.params['randomize_truenull_assc'])
        #### prt.write("NNNNNNNNNNNNNNNNNNNNN {SEED} {P} {NM}\n".format(
        ####     SEED=seedstr, P=self.pobj.params['prefix'],
        ####     NM=self.pobj.params['randomize_truenull_assc']))
        #### for k, v in self.params.items():
        ####     prt.write("NNNNNNNNNNNNNNNNNNNNN {K} {V}\n".format(K=k, V=v))
        for simnum, simobj in enumerate(simobjs):
            fout_py = "{BASE}_sim{N:05}.py".format(BASE=base, N=simnum)
            simobj.wrpy_genes(fout_py)

    def get_mean(self, key, genes_goids='genes'):
        """Returns the actual mean value for the set of P-Value simulations run in this class."""
        return np.mean([getattr(nt, key) for nt in self.nts_tfpn[genes_goids]])

    #### def get_median(self, key, genes_goids='genes'):
    ####     """Returns the actual median value for the set of P-Value simulations run in this class."""
    ####     return np.median([getattr(nt, key) for nt in self.nts_tfpn[genes_goids]])

    def get_summary_str(self):
        """Print summary. Ex: ManyGoeaSims: 10 sims,  16 pvals/sim SET( 50% null)."""
        return " ".join([
            "    ManyGoeaSims:",
            "{SIMS} sims,".format(SIMS=self.params['num_sims']),
            "{HYPOTHS:3} study_genes/sim".format(HYPOTHS=self.params['num_items']),
            "SET({P:3.0f}% null)".format(P=self.params['perc_null'])])

    def prt_summary(self, prt=sys.stdout):
        """Print summary. Ex: ManyGoeaSims: 10 sims,  16 pvals/sim SET( 50% null)."""
        prt.write("{MSG}\n".format(MSG=self.get_summary_str()))

    def get_percentile_vals(self, attr, percentiles, genes_goids='genes'):
        """Return percentile values for 'attr' list."""
        nts_tfpn = self.nts_tfpn[genes_goids]
        return [np.percentile([getattr(nt, attr) for nt in nts_tfpn], p) for p in percentiles]

    def prt_num_sims_w_errs(self, prt=sys.stdout, desc="", genes_goids='genes'):
        """Return the number of simulations that have errors."""
        msgpat = "{N} sims ({P:3} pvals/sim, {PERCNULL:3.0f}% True Null.) " \
                 "{E:5} had errs ({ERR_CNTS}) {DESC}\n"
        nts_tfpn = self.nts_tfpn[genes_goids]
        errpat = "{I:5} I, {II:5} II"
        num_errsims, num_errsimst1, num_errsimst2 = self._get_num_errsims(nts_tfpn)
        prt.write(msgpat.format(
            N=len(nts_tfpn), P=self.params['num_items'],
            PERCNULL=self.params['perc_null'],
            E=num_errsims, ERR_CNTS=errpat.format(I=num_errsimst1, II=num_errsimst2), DESC=desc))

    @staticmethod
    def _get_num_errsims(nts_tfpn):
        """Get error counts for Type I, Type II, and both."""
        err_cnts = [(nt.num_Type_I, nt.num_Type_II, nt.num_Type_I_II) for nt in nts_tfpn]
        t1s, t2s, t12s = zip(*err_cnts)
        return [
            sum([n != 0 for n in t12s]), # num_errsims
            sum([n != 0 for n in t1s]), # num_errsimst1
            sum([n != 0 for n in t2s])] # num_errsimst2

    def get_percentile_strs(self, attr, percentiles, genes_goids='genes'):
        """Return percentile strings suitable for printing for 'attr' list."""
        vals = self.get_percentile_vals(attr, percentiles, genes_goids)
        fmt = "{:6.2f}" if attr[:3] == "per" else "{:4}"
        return [fmt.format(v) for v in vals]

    def _init_simobjs(self, prt=None):
        """Simulate MANY multiple-test correction of P-values."""
        num_sims = self.params['num_sims']
        num_genes = self.params['num_items']
        num_null = self.params['num_null']
        sims = []
        for sim_num in range(num_sims):
            sims.append(GoeaSim(num_genes, num_null, self.pobj))
            if sim_num%100 == 0:
                if prt is not None:
                    prt.write("{I:4} {MSG} {HMS}\n".format(
                        I=sim_num, MSG=self.get_summary_str(), HMS=get_hms(self.pobj.tic)))
        return sims

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
