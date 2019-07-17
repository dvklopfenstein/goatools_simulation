"""Runs all experiments for all sets of experiments."""

from __future__ import print_function

__copyright__ = "Copyright (C) 2016-2019, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import os
import sys
import timeit
import datetime
from pkggosim.common.randseed import RandomSeed32
from pkggosim.goea.basename import Basename
from pkggosim.goea.objbase import DataBase
from pkggosim.goea.objassc import DataAssc
from goatools.rpt.goea_nt_xfrm import get_study_items
from goatools.gosubdag.gosubdag import GoSubDag

class RunParams(object):
    """Runs all experiments for all sets of experiments."""

    expected_params = set([
        'title',                   # Title to print on Figure w/FDR/Sensitivity/Specificty
        'repo',                    # directory of repository where script is run
        'py_dir_genes',            # src/pkgdavid/input/
        'log',                     # None sys.stdout
        'seed',                    # randomseed
        'prefix',                  # fig_goea_rnd
        'randomize_truenull_assc', # orig_noprune_ntn2
        'alpha',                 # 0.05
        'method',                # 'fdr_bh'
        'propagate_counts',      # False
        'association_file',      # 'gene_association.mgi'
        'genes_population',      # genes_mus
        'genes_study_bg',        # 'humoral_rsp'
        'goids_study_bg',        # 'humoral_rsp'
        'genes_popnullmaskout',  # ['immune', 'viral_bacteria']
        'perc_nulls',            # [100, 75, 50, 25]
        'num_genes_list',        # [4, 16, 128]
        'num_experiments',       # Number of simulated FDR ratios in an experiment set
        'num_sims',              # Number of sims per experiment; used to create one FDR ratio
    ])

    def __init__(self, params):
        self.tic = timeit.default_timer()
        self.params = self._init_params(params)
        print("TITLE({T})".format(T=self.params['title']))
        self.objrnd = RandomSeed32(params['seed'])
        self.bname = Basename()
        # PROPAGATE_COUNTS HANDLED IN objassc, NOT REDONE FOR EACH AND EVERY SIMULATION
        # self.objbase = DataBase(params['alpha'], params['method'], params['propagate_counts'])
        self.objbase = DataBase(params['alpha'], params['method'], False)
        self.objassc = DataAssc(params, self.objbase.go_dag)
        self.params['gosubdag'] = GoSubDag(self.objassc.go2genes.keys(), self.objbase.go_dag)
        # self.params['cwd'] = os.getcwd()
        # These study background genes have associations
        self.genes = {
            "population" : self.objassc.pop_genes,
            "study_bg" : params['genes_study_bg'].intersection(self.objassc.pop_genes),
            "null_bg" : self._init_null_bg()}
        self.gene_lists = {
            "study_bg" : list(self.genes['study_bg']),
            "null_bg" : list(self.genes['null_bg'])}
        self.params['gosubdag_bg'] = GoSubDag(params["goids_study_bg"], self.objbase.go_dag)
        self.params['ntn'] = self._init_ntn() # 1, 2, or 3
        self._chk_genes(params, self.genes)
        self._adj_num_genes_list()
        # self.assc_pruned = self._init_get_goids_tgtd()
        # GO IDs targeted for removal or randomization: Sig GOs - background GOs
        # Targeted GOs: Sig. GO IDs minus the GO IDs used to choose our background genes
        _gos_targeted = self._init_get_goids_tgtd()
        self.objassc.set_targeted(_gos_targeted)

    def get_fouts(self, simname):
        """Return output filenames for the logfile and plot file(s)."""
        # fout_log, base_img_genes, base_img_goids = self.bname.get_fouts(simname, self.pobj.params)
        ret = self.bname.get_fouts(simname, self.params)
        for fout in ret:
            print("BBBBBBBBBBBBBBBBBB get_fouts", fout)
        return ret  # fout_log, base_img_genes, base_img_goids

    def get_desc_str(self):
        """Get the name of the plot file for the tiled plot."""
        #### B=self.bname.get_desc_str(self.pobj.params),
        ret = self.bname.get_desc_str(self.params)
        print("BBBBBBBBBBBBBBBBBB get_desc_str", ret)
        return ret

    def _init_ntn(self):
        """Initialize param ntn with a digit or None."""
        randomize_truenull_assc = self.params['randomize_truenull_assc']
        if randomize_truenull_assc[-4:-1] == "ntn":
            digit_str = randomize_truenull_assc[-1]
            assert digit_str.isdigit()
            return int(digit_str)

    @staticmethod
    def get_bgname():
        """Get the Background gene name"""
        return "HR"

    # Randomized Associations
    # Assoc: TN=Rand NTN=Orig
    # Assoc: TN=Rand NTN=Orig - non-HR
    # Assoc: TN=Rand NTN=HR Only
    #
    # Original Associations (Enriched Shown)
    # Assoc: TN=Orig NTN=Orig-nonHR
    # Assoc: TN=Orig NTN=HR Only
    def get_title(self):
        """Return a title to use in plots based on string in 'randomize_truenull_assc'."""
        if self.params['title'] is not None:
            return self.params['title']
        # 'GOEA Simulations'
        key = self.params['randomize_truenull_assc']
        #pylint: disable=multiple-statements
        if key == 'orig_noprune_ntn1': return 'Original Associations'
        if key == 'orig_pruned_ntn1': return 'Original Associations, Pruned'
        if key == 'orig_noprune_enriched_ntn1': return 'Original Associations (View Enriched)'
        lst = []
        if "_pruned_" in key:
            lst.append("Pruned")
        lst.append("Assc:")
        ntn_str = ""
        name = self.get_bgname()
        if   'ntn1' in key: ntn_str = 'Orig'
        # elif 'ntn2' in key: ntn_str = 'Orig-Sig.Non{BG}'.format(BG=name)
        elif 'ntn3' in key: ntn_str = '{BG} Only'.format(BG=name)
        tn_pat = "{TN} True Nulls" if 'ntn2' in key else "TN={TN}"
        lst.append(tn_pat.format(TN=key[:4].capitalize()))
        if ntn_str:
            lst.append("NTN={NTN}".format(NTN=ntn_str))
        if '_enriched_' in key:
            lst.append("(View Enriched)")
        #### if self.params['assc_rm_if_genecnt'] is not None:
        ####     raise Exception("assc_rm_if_genecnt") # TBD rm
        ####     lst.append("(rm GOs<{N} genes)".format(N=self.params['assc_rm_if_genecnt']))
        return " ".join(lst)

    @staticmethod
    def _chk_genes(params, genes):
        """Check the gene counts."""
        assert len(genes['population']) <= len(params['genes_population'])
        assert len(genes['study_bg']) <= len(params['genes_study_bg'])
        assert genes['population'].intersection(genes['study_bg']) == genes['study_bg']
        assert not genes['null_bg'].intersection(genes['study_bg'])

    def get_objgoea(self, study_genes):
        """Return population genes, including study genes. But minus closely related genes."""
        genes_pop_masked = self.genes['null_bg'].union(study_genes)
        return self.objbase.get_goeaobj(genes_pop_masked, self.objassc.objassc_all.assc_geneid2gos)

    def prt_summary(self, prt):
        """Print summary of simulation parameters and background data."""
        prt.write("\nWRITTEN: {DATE}:\n\n".format(DATE=datetime.date.today()))
        # Print Random seed
        self.objrnd.prt(prt)
        # Print Info: GO-DAG, Associations, Population
        self.objbase.prt_summary(prt)
        self.objassc.prt_summary(prt)
        prms = self.params
        num_pop_tot = len(prms['genes_population'])
        num_pop_assc = len(self.genes['population'])
        perc_pop = 100.0*num_pop_assc/num_pop_tot
        prt.write("{N:6,} population genes (user)\n".format(N=num_pop_tot))
        prt.write("{N:6,} population genes in assc.\n".format(N=num_pop_assc))
        prt.write("{N:5.0f}% population genes coverage in assc.\n".format(N=perc_pop))
        prt.write("{N:6,} study genes (user)\n".format(N=len(prms['genes_study_bg'])))
        prt.write("{N:6,} study genes in assc.\n".format(N=len(self.genes['study_bg'])))
        prt.write("{N:6,} population genes - study buffer\n".format(N=len(self.genes['null_bg'])))
        prt.write("\n")
        prt.write("TITLE: {T}\n".format(T=self.get_title()))
        prt.write("SIMULATION PARAMETERS:\n")
        keys = ['randomize_truenull_assc', 'perc_nulls',
                'num_genes_list', 'num_experiments', 'num_sims']
        for key in keys:
            prt.write("    {KEY:15} {VAL}\n".format(KEY=key, VAL=prms[key]))
        prt.write("\n")

    # --- Initialization --------------------------------------------------------------------------
    def _init_null_bg(self):
        """Initialize null background, the population subset not related to study genes."""
        maskout = self.params['genes_popnullmaskout'].union(self.params['genes_study_bg'])
        return self.objassc.pop_genes.difference(maskout)
        # return self.objassc.pop_genes.difference(self.params['genes_study_bg'])

    def _adj_num_genes_list(self):
        """If the number of genes in num_genes_list is less than study_bg, update num_genes_list."""
        lst_orig = self.params['num_genes_list']
        lst_curr = []
        num_bg = len(self.gene_lists['study_bg'])
        for num_genes_orig in sorted(lst_orig):
            if num_genes_orig <= num_bg:
                lst_curr.append(num_genes_orig)
            else:
                lst_curr.append(num_bg)
                break
        if lst_orig != lst_curr:
            sys.stdout.write("**NOTE: num_genes_list WAS: {LIST}\n".format(LIST=lst_orig))
            sys.stdout.write("**NOTE: num_genes_list NOW: {LIST}\n".format(LIST=lst_curr))
            self.params['num_genes_list'] = lst_curr
        return lst_curr

    def _init_get_goids_tgtd(self):
        """Run baseline GOEA to obtain list of 'other' GO IDs which are truly significant."""
        # Run Gene Ontology Analysis w/study genes being entire study gene background.
        attrname = "p_{METHOD}".format(METHOD=self.objbase.method)
        keep_if = lambda nt: getattr(nt, attrname) < self.objbase.alpha
        # Association subset containing only population genes
        assc_all = self.objassc.objassc_all.assc_geneid2gos
        objgoea = self.objbase.get_goeaobj(self.genes['population'], assc_all)
        goea_results = objgoea.run_study(self.genes['study_bg'], keep_if=keep_if)
        # Check study background genes
        genes_signif = get_study_items(goea_results)
        assert self.genes['study_bg'] == genes_signif
        # Get GO IDs to randomize or remove
        goids_signif = set([nt.GO for nt in goea_results])
        goids_study_bg = self.params['goids_study_bg']
        assert goids_signif.intersection(goids_study_bg) == goids_study_bg
        # GO IDs targeted for removal or randomization
        goids_artifacts = goids_signif.difference(goids_study_bg)
        log = self.params['log']
        if log is not None and goea_results:
            self._prt_significant_artifacts(goea_results, goids_artifacts, log)
        return goids_artifacts

    @staticmethod
    def _prt_significant_artifacts(goea_results, goids_artifacts, log):
        """Print significant GO IDs that are artifacts of choosing from a set of candidate genes."""
        res = next(iter(goea_results))
        log.write("{S} study genes. {P} population genes:\n".format(S=res.study_n, P=res.pop_n))
        pat = "ALSO SIG: {NS} {GO} {EP} {FDR:8.2e} S({N:>2}:{S:6.4f}) P({P:6.4f}) {NM}\n"
        for res in sorted(goea_results, key=lambda r: [r.NS, r.p_fdr_bh]):
            if res.GO in goids_artifacts:
                ratio_stu = float(res.study_count)/res.study_n
                ratio_pop = float(res.pop_count)/res.pop_n
                log.write(pat.format(
                    NS=res.NS, GO=res.GO, EP=res.enrichment, FDR=res.p_fdr_bh,
                    N=res.study_count, S=ratio_stu, P=ratio_pop, NM=res.name))

    def _init_params(self, params_usr):
        """Add other new parameters based on user-specfications."""
        randomize_truenull_assc = params_usr['randomize_truenull_assc']
        params_sim = {k:v for k, v in params_usr.items()}
        if 'repo' not in params_usr:
            params_sim['repo'] = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "../../..")
        if 'py_dir_genes' not in params_usr:
            params_sim['py_dir_genes'] = None
        assert set(params_sim.keys()) == self.expected_params, \
            set(params_sim.keys()).symmetric_difference(self.expected_params)
        # Init enriched_only
        params_sim['enriched_only'] = 'enriched' in randomize_truenull_assc
        print("ENRICHED({})".format(params_sim['enriched_only']))
        # Init assc_rm_if_genecnt based on randomize_truenull_assc
        #### params_sim['assc_rm_if_genecnt'] = None
        #### if 'rmgene' in randomize_truenull_assc:
        ####     mtch = re.search(r'rmgene(\d+)', randomize_truenull_assc)
        ####     if mtch:
        ####         params_sim['assc_rm_if_genecnt'] = int(mtch.group(1))
        assert params_sim['genes_population']
        assert params_sim['genes_study_bg']
        assert params_sim['goids_study_bg']
        return params_sim

# Copyright (C) 2016-2019, DV Klopfenstein, Haibao Tang. All rights reserved.
