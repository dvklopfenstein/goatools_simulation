# Gene Ontology Enrichment Analyses Simulations

# Method index for Hypotheses Simulations
NTN = 2
E = -3           # 20 x 20
P = False        # Propagate Counts
RUNALL = False

# Max Sig P-values index for hypotheses simulations
P = 0

lst:
	grep vim_ makefile

run:
	src/bin/plt_goea.py e=-1 propcnts=False randomize_truenull_assc=orig_noprune_enriched_ntn$(NTN) \
		title="GOEAs recovering Humoral Response (HR) genes" \
		genes=4,124

plt:
	src/bin/dat_goea_plot.py \
		title="GOEAs recovering Humoral Response (HR) genes" \
		genes=4,124

# make run E=-1
# RUNALL False: Only 4 simulations will be run to create one P-value
# RUNALL True  
run_small:
	src/bin/plt_goea_small.py $(RUNALL) propcnts=$(P) randomize_truenull_assc=orig_noprune_enriched_ntn2 0xdeadbeef \
		title="Test Run genes" genes=4,124

#		title="Test Run genes" genes=4,8,16,20,48,64,80,96,112,124

# -----------------------------------------------------------------------------------------------------
#  Manuscript Figures: Compare Humoral Response gene recovery over a wide range
#  of stochasticly chosen gene groups with gene group sizes ranging from 4 genes to 124 genes
#  5:30 HMS
prop0:
	src/bin/plt_goea.py e=$(E) propcnts=False randomize_truenull_assc=orig_noprune_enriched_ntn$(NTN) \
		title="GOEAs recovering Humoral Response (HR) genes" \
		genes=4,8,16,20,48,64,80,96,112,124

# 13 hours
prop1:
	src/bin/plt_goea.py e=$(E) propcnts=True randomize_truenull_assc=orig_noprune_enriched_ntn$(NTN) \
		title="GOEAs recovering HR genes; propagate_counts=True" \
		genes=4,8,16,20,48,64,80,96,112,124

# Supplemental Figures: Compare Humoral Response gene recovery over a wide range
# 5 hours FAIL
s0:
	src/bin/plt_goea.py e=$(E) propcnts=False randomize_truenull_assc=orig_noprune_ntn$(NTN) \
		title="Viewing both over/under-represented enrichments" \
		genes=4,8,16,20,48,64,80,96,112,124

# 7 hours
s1:
	src/bin/plt_goea.py e=$(E) propcnts=False randomize_truenull_assc=rand_noprune_enriched_ntn$(NTN) \
		title="Stress Tests: Random Annotations; View Enriched" \
		genes=4,8,16,20,48,64,80,96,112,124

s2:
	src/bin/plt_goea.py e=$(E) propcnts=False randomize_truenull_assc=rand_pruned_ntn$(NTN) \
		title="Stress Tests: Random Annotations; Pruned" \
		genes=4,8,16,20,48,64,80,96,112,124

# -----------------------------------------------------------------------------------------------------
run_smalls:
	src/bin/plt_goea_small.py propcnts=$(P) randomize_truenull_assc=orig_noprune_ntn2 0xdeadbeef
	src/bin/plt_goea_small.py propcnts=$(P) randomize_truenull_assc=orig_pruned_ntn2 0xdeadbeef
	src/bin/plt_goea_small.py propcnts=$(P) randomize_truenull_assc=orig_noprune_enriched_ntn2 0xdeadbeef

run_hypo:
	src/bin/plt_benjamini_hochberg.py e=$(E) p=$(P)

# make run_goeas_ntn P=True E=-1    # Fast sim
# make run_goeas_ntn P=True         # Full sim
run_goeas_ntn:
	#src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_noprune_ntn$(NTN)
	#src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_pruned_ntn$(NTN)
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_noprune_enriched_ntn$(NTN)
	#src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_noprune_enriched_ntn$(NTN)
	#src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_pruned_ntn$(NTN)
	#src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_noprune_ntn$(NTN)


run_goeas_orig_enriched:
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_noprune_enriched_ntn3
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_noprune_enriched_ntn2
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_noprune_enriched_ntn1

run_goeas_rand_enriched:
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_noprune_enriched_ntn3
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_noprune_enriched_ntn2
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_noprune_enriched_ntn1


run_goeas_orig_pruned:
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_pruned_ntn3
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_pruned_ntn2
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_pruned_ntn1

run_goeas_rand_pruned:
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_pruned_ntn3
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_pruned_ntn2
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_pruned_ntn1


run_goeas_orig_noprune:
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_noprune_ntn3
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_noprune_ntn2
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=orig_noprune_ntn1

run_goeas_rand_noprune:
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_noprune_ntn3
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_noprune_ntn2
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_noprune_ntn1


run_rand_all:
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_noprune_all
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_pruned_all
	src/bin/plt_goea.py e=$(E) propcnts=$(P) randomize_truenull_assc=rand_noprune_enriched_all


cp_goea:
	rm -f doc/md/images/*.*
	make cp_figs_goea PNG=100to000_004to124_N00020_00020_humoral_rsp.png
	make cp_figs_goea PNG=100to000_004to124_N00020_00020.log

PNG := 100to000_004to124_N00020_00020_humoral_rsp.png
CP := cp 
cp_figs_goea:
	@echo Orig. FAIL. TOO MANY False Positives
	$(CP) doc/logs/fig_goea_orig_noprune_ntn1_$(PNG)          doc/md/images/fig1a_FAIL_goea_orig_noprune_ntn1_$(PNG)
	$(CP) doc/logs/fig_goea_orig_noprune_ntn2_$(PNG)          doc/md/images/fig1b_FAIL_goea_orig_noprune_ntn2_$(PNG)
	$(CP) doc/logs/fig_goea_orig_noprune_ntn3_$(PNG)          doc/md/images/fig1c_FAIL_goea_orig_noprune_ntn3_$(PNG)
	@echo Orig. PASS. ~30 Pruned
	$(CP) doc/logs/fig_goea_orig_pruned_ntn1_$(PNG)           doc/md/images/fig2a_PASS_goea_orig_pruned_ntn1_$(PNG)
	$(CP) doc/logs/fig_goea_orig_pruned_ntn2_$(PNG)           doc/md/images/fig2b_PASS_goea_orig_pruned_ntn2_$(PNG)
	$(CP) doc/logs/fig_goea_orig_pruned_ntn3_$(PNG)           doc/md/images/fig2c_PASS_goea_orig_pruned_ntn3_$(PNG)
	@echo Orig. PASS. Use Enriched GOEAs Only in analyses. Ignore purified GOEA results.
	$(CP) doc/logs/fig_goea_orig_noprune_enriched_ntn1_$(PNG) doc/md/images/fig3a_okay_goea_orig_noprune_enriched_ntn1_$(PNG)
	$(CP) doc/logs/fig_goea_orig_noprune_enriched_ntn2_$(PNG) doc/md/images/fig3b_PASS_goea_orig_noprune_enriched_ntn2_$(PNG)
	$(CP) doc/logs/fig_goea_orig_noprune_enriched_ntn3_$(PNG) doc/md/images/fig3c_PASS_goea_orig_noprune_enriched_ntn3_$(PNG)
	@echo Rand. PASS. Use Enriched GOEAs Only in analyses. Ignore purified GOEA results.
	$(CP) doc/logs/fig_goea_rand_noprune_enriched_all_$(PNG)  doc/md/images/fig4R_PASS_goea_rand_noprune_enriched_all_$(PNG)
	$(CP) doc/logs/fig_goea_rand_noprune_enriched_ntn1_$(PNG) doc/md/images/fig4a_okay_goea_rand_noprune_enriched_ntn1_$(PNG)
	$(CP) doc/logs/fig_goea_rand_noprune_enriched_ntn2_$(PNG) doc/md/images/fig4b_FAIL_goea_rand_noprune_enriched_ntn2_$(PNG)
	$(CP) doc/logs/fig_goea_rand_noprune_enriched_ntn3_$(PNG) doc/md/images/fig4c_PASS_goea_rand_noprune_enriched_ntn3_$(PNG)
	@echo
	$(CP) doc/logs/fig_goea_rand_noprune_all_$(PNG)           doc/md/images/fig1R_PASS_goea_rand_noprune_all_$(PNG)
	$(CP) doc/logs/fig_goea_rand_noprune_ntn1_$(PNG)          doc/md/images/fig1Ra_FAIL_goea_rand_noprune_ntn1_$(PNG)
	$(CP) doc/logs/fig_goea_rand_noprune_ntn2_$(PNG)          doc/md/images/fig1Rb_FAIL_goea_rand_noprune_ntn2_$(PNG)
	$(CP) doc/logs/fig_goea_rand_noprune_ntn3_$(PNG)          doc/md/images/fig1Rc_FAIL_goea_rand_noprune_ntn3_$(PNG)
	@echo
	$(CP) doc/logs/fig_goea_rand_pruned_all_$(PNG)            doc/md/images/fig5R_PASS_goea_rand_pruned_all_$(PNG)
	$(CP) doc/logs/fig_goea_rand_pruned_ntn1_$(PNG)           doc/md/images/fig5a_PASS_goea_rand_pruned_ntn1_$(PNG)
	$(CP) doc/logs/fig_goea_rand_pruned_ntn2_$(PNG)           doc/md/images/fig5b_PASS_goea_rand_pruned_ntn2_$(PNG)
	$(CP) doc/logs/fig_goea_rand_pruned_ntn3_$(PNG)           doc/md/images/fig5c_PASS_goea_rand_pruned_ntn3_$(PNG)             

pylint:
	find src -name \*.py | grep -v pkggosim.data | xargs pylint -r no

# src/bin/plt_goea_small.py 
vim_fig:
	vim -p \
	src/bin/plt_goea_fig3ab.py \
	src/pkggosim/goea/fig_tiled.py \
	src/pkggosim/goea/sim.py \
	src/pkggosim/goea/sims.py \
	src/pkggosim/goea/experiments.py \
	src/pkggosim/goea/run_all.py \
	src/pkggosim/goea/run_all_params.py \
	src/pkggosim/goea/basename.py \
	src/pkggosim/goea/plot_results.py \
	src/pkggosim/common/plot_results.py \
	src/pkggosim/goea/utils.py \
	src/pkggosim/goea/objassc.py \
	src/pkggosim/goea/assc_shuffle.py \
	src/pkggosim/goea/objbase.py \
	src/pkggosim/common/true_positive.py

vim_presim_geneontology:
	vim -p \
	src/bin/simquick_geneontology.py \
	src/pkggosim/goea/objrun_prelim.py \
	src/pkggosim/goea/sim.py \
	src/pkggosim/goea/sims.py \
	src/pkggosim/goea/experiments.py \
	src/pkggosim/goea/run_all.py \
	src/pkggosim/goea/run_all_params.py \
	src/pkggosim/goea/basename.py \
	src/pkggosim/goea/plot_results.py \
	src/pkggosim/common/plot_results.py \
	src/pkggosim/goea/utils.py \
	src/pkggosim/goea/objassc.py \
	src/pkggosim/goea/assc_shuffle.py \
	src/pkggosim/goea/objbase.py \
	src/pkggosim/common/true_positive.py

vim_sim_hypotheses:
	vim -p \
	src/bin/plt_benjamini_hochberg.py \
	src/bin/sim_fdr_benjamini_hochberg.py \
	src/pkggosim/hypotheses/sim.py \
	src/pkggosim/hypotheses/sims.py \
	src/pkggosim/hypotheses/experiments.py \
	src/pkggosim/hypotheses/run_all.py \
	src/pkggosim/hypotheses/plot_results.py \
	src/pkggosim/common/plot_results.py \
	src/pkggosim/common/true_positive.py \
	src/pkggosim/common/randseed.py

vim_md:
	vim -p \
	README.md \
	doc/md/README_prep.md \
	doc/md/README_main.md

getdata:
	../goatools_suppl/src/bin/get_goids_by_section.py ../goatools_simulation/src/pkggosim

clean:
	find src -name \*.pyc | xargs rm -f
	rm -f python*.st*

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
