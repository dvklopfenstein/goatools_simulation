"""Simulate a Gene Ontology Enrichment Analysis (GOEA) on a set of random study genes."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
from collections import namedtuple, Counter
from random import shuffle
from goatools.go_enrichment import get_study_items
from pkggosim.common.true_positive import get_tfpn, calc_ratio

class GoeaSim(object):
    """Simulate a Gene Ontology Enrichment Analysis (GOEA) on a set of random study genes."""

    ntobj = namedtuple(
        "NtMtAll", "num_genes num_sig_actual ctr fdr_actual frr_actual "
        "sensitivity specificity pos_pred_val neg_pred_val")

    def __init__(self, num_study_genes, num_null, pobj, log=sys.stdout):
        self.pobj = pobj
        iniobj = _Init(num_study_genes, num_null, pobj, log)
        # List of info for each study gene: geneid reject expected_significance tfpn
        self.nts_goea_res = iniobj.get_nts_stugenes()  # study_gene reject expsig tfpn
        # One namedtuple summarizing results of this GOEA simulation
        self.nt_tfpn = self.get_nt_tfpn()
        if self.nt_tfpn.fdr_actual > pobj.objbase.alpha:
            self.rpt_details()

    def get_nt_tfpn(self):
        """Calculate various statistical quantities of interest, including simulated FDR."""
        ctr = Counter([nt.tfpn for nt in self.nts_goea_res]) # Counts of TP TN FP FN
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
        tot_sig_y = sum(nt.reject for nt in self.nts_goea_res)
        assert tot_sig_y == TP + FP
        # Not Significant(Correct) or Type II Error (significant)
        tot_sig_n = sum(not nt.reject for nt in self.nts_goea_res)
        assert tot_sig_n == TN + FN
        num_genes = len(self.nts_goea_res)
        assert tot_sig_y + tot_sig_n == num_genes
        return self.ntobj(
            num_genes      = len(self.nts_goea_res),
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
        """Report each gene's GOEA results."""
        ntr = self.nt_tfpn
        prt.write("\n{N} = TP({TP}) + FP({FP}) + TN({TN}) + FN({FN}); FDR={FDR:6.4f}\n".format(
            N=len(self.nts_goea_res),
            TP=ntr.ctr['TP'], TN=ntr.ctr['TN'], FP=ntr.ctr['FP'], FN=ntr.ctr['FN'],
            FDR=ntr.fdr_actual))
        pat = "{fp_mrk:1} {tfpn} REJ({reject:1}) EXP({expsig:1}) {study_gene} {BG:1} {num_gos:3} {assc_gos:3}\n"
        genes_bg = self.pobj.params['genes_study_bg']
        assc = self.pobj.objassc.objassc_all.assc_geneid2gos
        for nti in sorted(self.nts_goea_res, key=lambda nt: [-1*nt.reject, -1*nt.expsig]):
            dct = nti._asdict()
            dct['fp_mrk'] = "X" if nti.tfpn == "FP" else ""
            dct['BG'] = "*" if nti.study_gene in genes_bg else ""
            dct['assc_gos'] = len(assc[nti.study_gene])
            prt.write(pat.format(**dct))

class _Init(object):
    """Run GOEA on randomly-created "True Null" gene sets and "Non-true Null" gene sets."""

    ntobj = namedtuple("NtGoeaRes", "study_gene reject expsig GOs num_gos tfpn")

    def get_nts_stugenes(self):
        """Combine data to return nts w/fields: pvals, pvals_corr, reject, expsig."""
        goeasim_results = []
        for study_gene, expsig in zip(self.genes_stu, self.expsig):
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

    def __init__(self, num_study_genes, num_null, pobj, log=None):
        self.pobj = pobj # RunParams object
        # I. Genes in two groups: Different than population AND no different than population
        self.genes_stu = None  # List of randomly-generated gene lists
        self.expsig = None # List of bool/gene. True:gene is intended to be signif.(Non-true null)
        self._init_study_genes(num_study_genes, num_null)
        num_study = len(self.genes_stu)
        assert num_study == num_study_genes, "{} {}".format(num_study, num_study_genes)
        assert num_study_genes - sum(self.expsig) == num_null
        self.assc_geneid2gos = self._init_assc()
        goea_results = self._init_goea_results()
        # for g in goea_results:
        #     print "HHHH", g
        self.genes_sig = get_study_items(goea_results)
        num_sig = len(self.genes_sig)
        if log is not None:
            num_exp = num_study-num_null
            mrk = ""
            if num_exp != num_sig:
                mrk = "-" if num_sig < num_exp else "+"
            txt = "{MRK:1} NULL({NULL:3}) STUDY({STU:3}) EXP_SIG({EXP:3}) ACT_SIG({SIG:3})\n"
            log.write(txt.format(STU=num_study, SIG=num_sig, EXP=num_exp, NULL=num_null, MRK=mrk))

    def _init_goea_results(self):
        """Run GOEA."""
        objgoea = self.pobj.objbase.get_goeaobj(self.pobj.genes['population'], self.assc_geneid2gos)
        attrname = "p_{METHOD}".format(METHOD=self.pobj.objbase.method)
        keep_if = lambda nt: getattr(nt, attrname) < self.pobj.objbase.alpha
        return objgoea.run_study(self.genes_stu, keep_if=keep_if)

    def _init_assc(self):
        """Run Gene Ontology Analysis."""
        randomize_truenull_assc = self.pobj.params['randomize_truenull_assc']
        assc = {g:gos for g, gos in self.pobj.objassc.objassc_all.assc_geneid2gos.items()}

        if randomize_truenull_assc[:4] == "rand_tgtd":
            assc = self._get_assc_rndtgtd()
        elif randomize_truenull_assc[:4] == "rand_":
            assc = self.pobj.objassc.objassc_all.get_shuffled_associations()
        elif randomize_truenull_assc == "rm_tgtd":
            assc = self.pobj.objassc.objassc_pruned.assc_geneid2gos

        if self.pobj.params['assc_rm_if_genecnt'] is not None:
            #### print "VVVV", self.pobj.params['assc_rm_if_genecnt'], len(assc)
            assc = self.pobj.get_assc_rmgenes(assc)
            #### print "vvvv", self.pobj.params['assc_rm_if_genecnt'], len(assc)

        if randomize_truenull_assc[-4:-1] == "ntn" and randomize_truenull_assc[-1].isdigit():
            assc = self._fill_assc_ntn(assc, randomize_truenull_assc)
        return assc


    def _fill_assc_ntn(self, assc_bg, randomize_truenull_assc):
        """Return one of many flavors of randomly shuffled associations."""
        genes_nontrunull = set([g for g, e in zip(self.genes_stu, self.expsig) if e])
        # genes_nontrunullt = set([g for g, e in zip(self.genes_stu, self.expsig) if not e])
        # assert not genes_nontrunull.intersection(genes_nontrunullt)
        # print len(genes_nontrunull), len(genes_nontrunullt)
        # genes_trunull = self.pobj.genes['population'].difference(genes_nontrunull)
        # if genes_nontrunullt:
        #     tn = next(iter(genes_nontrunullt))
        #     assert assc[tn] != self.pobj.objassc.objassc_all.assc_geneid2gos[tn]
        assc_all_orig = self.pobj.objassc.objassc_all.assc_geneid2gos
        if randomize_truenull_assc[-4:] == "ntn1":
            for gene in genes_nontrunull:
                assc_bg[gene] = assc_all_orig[gene]
            return assc_bg
        elif randomize_truenull_assc[-4:] == "ntn2":
            goids_tgtd = self.pobj.objassc.goids_tgtd
            for gene in genes_nontrunull:
                assc_bg[gene] = assc_all_orig[gene].difference(goids_tgtd)
            return assc_bg
        elif randomize_truenull_assc[-4:] == "ntn3":
            goids_study_bg = self.pobj.objassc.goids_study_bg
            for gene in genes_nontrunull:
                assc_bg[gene] = assc_all_orig[gene].intersection(goids_study_bg)
            return assc_bg
        raise RuntimeError("UNEXPECTED randomize_truenull_assc({})".format(randomize_truenull_assc))


    def _get_assc_rndtgtd(self):
        """rnd_tgtd: Concatenate pruned assc and targeted randomized assc."""
        assc = {g:gos for g, gos in self.pobj.assc_pruned.items()} # copy pruned assc
        assc_tgtd_rnd = self.pobj.objassc.shuffle_associations(self.pobj.assc_tgtd)
        for geneid, goids_rnd in assc_tgtd_rnd.items():
            if geneid in assc:
                assc[geneid] |= goids_rnd
            else:
                assc[geneid] = goids_rnd
        return assc

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
        genes_expsig = \
            [(g, True) for g in genes_study_bg[:num_ntnull]] + \
            [(g, False) for g in genes_pop_bg[:num_null]]         # True Null
        # 2. Extract "genes" and "intended significance" by transposing data
        self.genes_stu, self.expsig = zip(*genes_expsig)


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
