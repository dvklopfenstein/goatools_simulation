"""Simulate a Gene Ontology Enrichment Analysis (GOEA) on a set of random study genes."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from collections import namedtuple, Counter
from numpy.random import shuffle
from goatools.go_enrichment import get_study_items
from goatools.associations import get_b2aset
from pkggosim.common.true_positive import get_tfpn, calc_ratio

class GoeaSim(object):
    """Simulate a Gene Ontology Enrichment Analysis (GOEA) on a set of random study genes."""

    ntobj = namedtuple(
        "NtMtAll", "num_items num_sig_actual ctr fdr_actual frr_actual "
        "sensitivity specificity pos_pred_val neg_pred_val")

    def __init__(self, num_study_genes, num_null, pobj):
        self.pobj = pobj
        iniobj = _Init(num_study_genes, num_null, pobj)
        # List of info for each study gene: geneid reject expected_significance tfpn
        self.assc = iniobj.assc_geneid2gos
        self.goea_results = iniobj.goea_results
        self.nts_goea_res = iniobj.get_nts_stugenes()  # study_gene reject expsig tfpn
        self.nts_goid_res = iniobj.get_nts_stugoids()  # GO         reject expsig tfpn GOIDS
        # One namedtuple summarizing results of this GOEA simulation
        self.nt_tfpn_genes = self.get_nt_tfpn(self.nts_goea_res)
        self.nt_tfpn_goids = self.get_nt_tfpn(self.nts_goid_res) # GOIDS
        if pobj.params['log'] is not None:
            if self.nt_tfpn_genes.fdr_actual > pobj.objbase.alpha:
                self.rpt_details(pobj.params['log'])

    def wrpy_genes(self, fout_local):
        """Write randomly generated study study group into a Python module."""
        fout_py = "{REPO}/{PY}".format(REPO=self.pobj.params['repo'], PY=fout_local)
        with open(fout_py, 'w') as prt:
            prt.write("genes = [ \n")
            for ntd in self.nts_goea_res:
                prt.write("    {NT},\n".format(NT=ntd))
            prt.write("]\n")
        sys.stdout.write("  WROTE: {PY}\n".format(PY=fout_local))

    def get_nt_tfpn(self, nts_goea_res):
        """Calculate various statistical quantities of interest, including simulated FDR."""
        ctr = Counter([nt.tfpn for nt in nts_goea_res]) # Counts of TP TN FP FN
        #pylint: disable=invalid-name, bad-whitespace
        #              reject ->| False         | True
        #
        #                       |Declared       | Declared      |
        #                       |non-significant| significant   | Total
        # ----------------------+---------------+---------------+--------
        # True  null hypotheses | U TN          | V FP (Type I) |   m(0)
        # False null hypotheses | T FN (Type II)| S TP          | m - m(0)
        TP, TN, FP, FN = [ctr[name] for name in ["TP", "TN", "FP", "FN"]]
        # Significant(Correct) or Type I Error (Not significant)
        tot_sig_y = sum(nt.reject for nt in nts_goea_res)
        assert tot_sig_y == TP + FP
        # Not Significant(Correct) or Type II Error (significant)
        tot_sig_n = sum(not nt.reject for nt in nts_goea_res)
        assert tot_sig_n == TN + FN
        num_items = len(nts_goea_res)
        assert tot_sig_y + tot_sig_n == num_items
        return self.ntobj(
            num_items      = len(nts_goea_res),
            num_sig_actual = tot_sig_y,
            ctr            = ctr,
            # FDR: expected proportion of false discoveries (FP or Type I errors) among discoveries
            fdr_actual     = calc_ratio(FP, (TP, FP)), # typI(FP)/sig_y(FP+TP)
            frr_actual     = calc_ratio(FN, (TN, FN)), # typII(FN)/sig_n(TN+FN)
            # SENSITIVITY & SPECIFICITY are not affected by prevalence
            # SENSITIVITY: "true positive rate", recall, "probability of detection"
            sensitivity    = calc_ratio(TP, (TP, FN)), # TP/(TP+FN) screening
            # SPECIFICITY: "true negative rate"
            specificity    = calc_ratio(TN, (TN, FP)), # TN/(TN+FP) confirmation
            # "Positive predictive value" and "Negative predictive value" are affected by prevalence
            pos_pred_val   = calc_ratio(TP, (TP, FP)), # TP/(TP+FP)
            neg_pred_val   = calc_ratio(TN, (TN, FN))) # TN/(TN+FN)

    def rpt_details(self, prt=sys.stdout):
        """Report genes and GO IDs found in GOEA results."""
        prt.write("\n")
        self.rpt_details_goids(prt)
        self.rpt_details_genes(prt)

    def rpt_details_goids(self, prt):
        """Report GO IDs found in GOEA results."""
        objprt = _PrtGoIds(self)
        objprt.wr_goids(prt)

    def rpt_details_genes(self, prt):
        """Report genes found in GOEA results."""
        ntr = self.nt_tfpn_genes
        prt.write("{N} = TP({TP}) + FP({FP}) + TN({TN}) + FN({FN}); FDR={FDR:6.4f}\n".format(
            N=len(self.nts_goea_res),
            TP=ntr.ctr['TP'], TN=ntr.ctr['TN'], FP=ntr.ctr['FP'], FN=ntr.ctr['FN'],
            FDR=ntr.fdr_actual))
        prt.write(" Res Reject Signific. Gene     is_sig_gene stu pop GO count\n")
        prt.write(" --- ------ --------- ------------------ - --- ------------\n")
        pat = ("{fp_mrk:1} {tfpn} REJ({reject:1}) EXPSIG({expsig:1}) "
               "{study_gene} {BG:1} {num_gos:3} {assc_gos:3}\n")
        genes_bg = self.pobj.params['genes_study_bg']
        assc = self.pobj.objassc.objassc_all.assc_geneid2gos
        for nti in sorted(self.nts_goea_res, key=lambda nt: [-1*nt.reject, -1*nt.expsig]):
            dct = nti._asdict()
            dct['fp_mrk'] = "X" if nti.tfpn == "FP" else ""
            dct['BG'] = "*" if nti.study_gene in genes_bg else ""
            dct['assc_gos'] = len(assc[nti.study_gene])
            prt.write(pat.format(**dct))


class _PrtGoIds(object):
    """For printing GO IDs found significant in one simulation."""

    def __init__(self, objsim):
        self.go2genes = get_b2aset(objsim.assc)
        self.gos_bg = objsim.pobj.params['goids_study_bg']
        self.gos_sig_all = set([r.GO for r in objsim.goea_results])
        self.go2obj = objsim.pobj.params['gosubdag'].go2obj
        self.go2res = {r.GO:r for r in objsim.goea_results}
        self.attr_pval = "p_{METHOD}".format(METHOD=objsim.pobj.objbase.method)
        self.get_go2desc = objsim.pobj.objassc.get_go2desc

    def wr_goids(self, prt):
        """Print significant GO IDs."""
        gos_sig_bgy = self.gos_sig_all.intersection(self.gos_bg)
        gos_sig_bgn = self.gos_sig_all.difference(self.gos_bg)
        self.wr_goids_tot(gos_sig_bgy, gos_sig_bgn, prt)
        self.wr_goids_details(gos_sig_bgy, "", prt)
        self.wr_goids_details(gos_sig_bgn, "X", prt)

    def wr_goids_tot(self, gos_sig_bgy, gos_sig_bgn, prt):
        """Print summary for significant GO IDs."""
        prt.write("{A} Sig. GO IDs = bgY({Y}) + bgN({N})\n".format(
            A=len(self.gos_sig_all), Y=len(gos_sig_bgy), N=len(gos_sig_bgn)))

    def wr_goids_details(self, gos_sig_bg, pre, prt):
        """Print a details line for each GO ID."""
        pat = "{PRE:1} {EP} {PVAL:8.2e} {DESC}\n"
        for goid, desc in self.get_go2desc(gos_sig_bg, self.go2obj, self.go2genes).items():
            res = self.go2res[goid]
            pval = getattr(res, self.attr_pval)
            prt.write(pat.format(PRE=pre, EP=res.enrichment, PVAL=pval, DESC=desc))


class _Init(object):
    """Run GOEA on randomly-created "True Null" gene sets and "Non-true Null" gene sets."""

    ntobj = namedtuple("NtGoeaRes", "study_gene reject expsig GOs num_gos tfpn")

    def __init__(self, num_study_genes, num_null, pobj):
        self.pobj = pobj # RunParams object
        # I. Genes in two groups: Different than population AND no different than population
        self.gene_expsig_list = self._init_study_genes(num_study_genes, num_null) # [(gene, expsig),
        self.assc_geneid2gos = self._init_assc()
        self.goea_results = self._init_goea_results()
        # for g in self.goea_results:
        #     print "HHHH", g
        self.genes_sig = get_study_items(self.goea_results)
        if self.pobj.params['log'] is not None:
            self._wrlog_summary(num_study_genes, num_null)

    def get_nts_stugenes(self):
        """Combine data to return nts w/fields: pvals, pvals_corr, reject, expsig."""
        goeasim_results = []
        for study_gene, expsig in self.gene_expsig_list:
            reject = study_gene in self.genes_sig
            goids = self.assc_geneid2gos[study_gene]
            #pylint: disable=bad-whitespace
            goeasim_results.append(self.ntobj(
                study_gene = study_gene,
                reject     = reject,
                expsig     = expsig, # False->True Null; True->Non-true null
                GOs        = goids,
                num_gos    = len(goids),
                tfpn       = get_tfpn(reject, expsig))) # Ex: TP, TN, FP, or FN
        return goeasim_results

    def get_nts_stugoids(self):
        """Combine data to return nts w/fields: pvals, pvals_corr, reject, expsig."""
        goeasim_results = []
        ntobj = namedtuple("NtGoeaGos", "GO reject expsig tfpn")
        go2res = {r.GO:r for r in self.goea_results}
        goids_sig = set(go2res.keys())
        for study_goid, expsig in self._get_goids_expsig_list():
            reject = study_goid in goids_sig
            #pylint: disable=bad-whitespace
            goeasim_results.append(ntobj(
                GO     = study_goid,
                reject = reject,
                expsig = expsig, # False->True Null; True->Non-true null
                tfpn   = get_tfpn(reject, expsig))) # Ex: TP, TN, FP, or FN
        return goeasim_results

    def _get_goids_expsig_list(self):
        """Get a list of GO IDs related to study genes and their expected discovery status."""
        goids_all = set()
        goids_sig_all = set()
        goids_sigbg_all = self.pobj.params['goids_study_bg']
        goids_sigtgt_all = self.pobj.objassc.goids_tgtd
        for gene, expsig in self.gene_expsig_list:
            goids_gene = self.assc_geneid2gos[gene]
            goids_all |= goids_gene
            if expsig:
                # Humoral Response GO IDs associated with this gene:
                goids_sigbg = goids_gene.intersection(goids_sigbg_all)
                # GO IDs seen in large quantities for this gene:
                goids_sigtgt = goids_gene.intersection(goids_sigtgt_all)
                goids_sig_all |= goids_sigbg.union(goids_sigtgt)
        return [(go, go in goids_sig_all) for go in goids_all]

    def _init_goea_results(self):
        """Run Gene Ontology Analysis."""
        objgoea = self.pobj.objbase.get_goeaobj(self.pobj.genes['population'], self.assc_geneid2gos)
        attrname = "p_{METHOD}".format(METHOD=self.pobj.objbase.method)
        keep_if = lambda nt: getattr(nt, attrname) < self.pobj.objbase.alpha
        genes_stu = [g for g, _ in self.gene_expsig_list]
        goea_results = objgoea.run_study(genes_stu, keep_if=keep_if)
        if self.pobj.params['enriched_only']:
            goea_results = [r for r in goea_results if r.enrichment == 'e']
        return goea_results

    def _init_assc(self):
        """Association."""
        randomize_truenull_assc = self.pobj.params['randomize_truenull_assc']
        ntn = self.pobj.params['ntn']
        # print "AAAAAAAAAAAAAAAAAAAAAAAAA", randomize_truenull_assc
        assc = None

        # Random or Original Associations
        if randomize_truenull_assc[:5] == "rand_":
            # print "RRRRRRRRRRRRRRRRRRRRRRRRR",
            assc = self.pobj.objassc.objassc_all.get_shuffled_associations() # ret a copy
        #### elif randomize_truenull_assc == "rm_tgtd":
        ####     raise Exception("rm_tgtd") # TBD rm
        ####     assc = self.pobj.objassc.objassc_pruned.assc_geneid2gos

        #### if self.pobj.params['assc_rm_if_genecnt'] is not None:
        ####     raise Exception("assc_rm_if_genecnt") # TBD rm
        ####     #### print "VVVV", self.pobj.params['assc_rm_if_genecnt'], len(assc)
        ####     assc = self.pobj.get_assc_rmgenes(assc if assc is not None else assc_full)
        ####     #### print "vvvv", self.pobj.params['assc_rm_if_genecnt'], len(assc)

        if ntn is not None:
            if assc is None:
                assc = {g:gos for g, gos in self.pobj.objassc.objassc_all.assc_geneid2gos.items()}
            assc = self._fill_assc_ntn(assc, ntn)

        return assc


    def _fill_assc_ntn(self, assc_bg, ntn_num):
        """Given non-true null study genes (ie HR or TARGET): Possibly edit genes' associations."""
        #genes_nontrunull = set([g for g, e in zip(self.genes_stu, self.expsig) if e])
        # Study genes expected to be significant (nontruenull OR target OR truly-significant)
        genes_nontrunull = set([gene for gene, expsig in self.gene_expsig_list if expsig])
        # genes_nontrunullt = set([g for g, e in zip(self.genes_stu, self.expsig) if not e])
        # assert not genes_nontrunull.intersection(genes_nontrunullt)
        # print len(genes_nontrunull), len(genes_nontrunullt)
        # genes_trunull = self.pobj.genes['population'].difference(genes_nontrunull)
        # if genes_nontrunullt:
        #     tn = next(iter(genes_nontrunullt))
        #     assert assc[tn] != self.pobj.objassc.objassc_all.assc_geneid2gos[tn]
        assc_all_orig = self.pobj.objassc.objassc_all.assc_geneid2gos
        # NTN1: Original association remains untouched
        if ntn_num == 1:
            for gene in genes_nontrunull:
                assc_bg[gene] = assc_all_orig[gene]
            return assc_bg
        # NTN2: Remove 'other' truly significant GO IDs from study gene's GO associations
        elif ntn_num == 2:
            goids_tgtd = self.pobj.objassc.goids_tgtd
            for gene in genes_nontrunull:
                assc_bg[gene] = assc_all_orig[gene].difference(goids_tgtd)
            return assc_bg
        # NTN3: Rm all GOs from stu gene's GO assc EXCEPT specific GO IDs used to define ntn genes
        elif ntn_num == 3:
            goids_study_bg = self.pobj.params['goids_study_bg']
            for gene in genes_nontrunull:
                assc_bg[gene] = assc_all_orig[gene].intersection(goids_study_bg)
            return assc_bg
        raise RuntimeError("UNEXPECTED ntn({})".format(ntn_num))

    def _init_study_genes(self, num_study_genes, num_null):
        """Generate 2 sets of genes: Not intended significant & intended to be significant."""
        # Calculate the number of "Non-true null hypotheses":
        #   Study genes found to be different than the population genes likely not by chance
        num_ntnull = num_study_genes - num_null
        # 1. Generate random genes: Significant and Random
        #   True  -> gene is intended to be significant(different from the population)
        #   False -> If gene is determined significant, it occured by chance
        genes_pop_bg = self.pobj.gene_lists['null_bg']
        genes_study_bg = self.pobj.gene_lists['study_bg']
        shuffle(genes_pop_bg)
        shuffle(genes_study_bg)
        genes_ntn = [(g, True) for g in genes_study_bg[:num_ntnull]]
        genes_tn = [(g, False) for g in genes_pop_bg[:num_null]]
        assert len(genes_ntn) == num_ntnull
        assert len(genes_tn) == num_null
        return genes_ntn + genes_tn # gene_expsig_list

    def _wrlog_summary(self, num_study_genes, num_null):
        """Write GOEA summary."""
        num_sig = len(self.genes_sig)
        num_exp = num_study_genes-num_null
        mrk = ""
        if num_exp != num_sig:
            mrk = "-" if num_sig < num_exp else "+"
        txt = "{MRK:1} NULL({NULL:3}) STUDY({STU:3}) EXP_SIG({EXP:3}) ACT_SIG({SIG:3})\n"
        log = self.pobj.params['log']
        log.write(txt.format(STU=num_study_genes, SIG=num_sig, EXP=num_exp, NULL=num_null, MRK=mrk))

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
