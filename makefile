# Gene Ontology Enrichment Analyses Simulations

# Method index for Hypotheses Simulations
E = -3

# Max Sig P-values index for hypothese simulations
P = 0

# Remove associations with less than G genes
G = 5

lst:
	grep vim_ makefile

# make run E=-1
run:
	src/bin/plt_goea_small.py e=$(E) randomize_truenull_assc=rand_ntn3 0xdeadbeef

run_hypo:
	src/bin/plt_benjamini_hochberg.py e=$(E) p=$(P)

run_goeas_orig_enriched:
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_noprune_enriched_ntn3
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_noprune_enriched_ntn2
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_noprune_enriched_ntn1

run_goeas_rand_enriched:
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_noprune_enriched_ntn3
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_noprune_enriched_ntn2
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_noprune_enriched_ntn1
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_noprune_enriched_all


run_goeas_orig:
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_pruned_ntn3
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_pruned_ntn2
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_pruned_ntn1

run_goeas_rand:
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_pruned_ntn3
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_pruned_ntn2
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_pruned_ntn1
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_pruned_all


run_goeas_orig_noprune:
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_noprune_ntn3
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_noprune_ntn2
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_noprune_ntn1

run_goeas_rand_noprune:
	#src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_noprune_ntn3
	#src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_noprune_ntn2
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_noprune_ntn1
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_noprune_all

PNG := 100to000_004to124_N00020_00020_humoral_rsp.png
CP := cp 
cp_figs_goea:
	rm -f doc/md/images/*.*
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
	$(CP) doc/logs/fig_goea_rand_noprune_enriched_all_$(PNG)  doc/md/images/fig9a_PASS_goea_rand_noprune_enriched_all_$(PNG)
	$(CP) doc/logs/fig_goea_rand_noprune_enriched_ntn1_$(PNG) doc/md/images/fig4a_okay_goea_rand_noprune_enriched_ntn1_$(PNG)
	$(CP) doc/logs/fig_goea_rand_noprune_enriched_ntn2_$(PNG) doc/md/images/fig4b_okay_goea_rand_noprune_enriched_ntn2_$(PNG)
	$(CP) doc/logs/fig_goea_rand_noprune_enriched_ntn3_$(PNG) doc/md/images/fig4c_PASS_goea_rand_noprune_enriched_ntn3_$(PNG)
	@echo
	$(CP) doc/logs/fig_goea_rand_noprune_ntn3_$(PNG)          doc/md/images/fig11_goea_rand_noprune_ntn3_$(PNG)
	@echo
	$(CP) doc/logs/fig_goea_rand_pruned_all_$(PNG)            doc/md/images/fig9b_PASS_goea_rand_pruned_all_$(PNG)
	$(CP) doc/logs/fig_goea_rand_pruned_ntn1_$(PNG)           doc/md/images/fig5a_PASS_goea_rand_pruned_ntn1_$(PNG)
	$(CP) doc/logs/fig_goea_rand_pruned_ntn2_$(PNG)           doc/md/images/fig5b_PASS_goea_rand_pruned_ntn2_$(PNG)
	$(CP) doc/logs/fig_goea_rand_pruned_ntn3_$(PNG)           doc/md/images/fig5c_PASS_goea_rand_pruned_ntn3_$(PNG)             


pylint:
	find src -name \*.py | xargs pylint -r no

# src/bin/plt_goea_small.py 
vim_sim_geneontology:
	vim -p \
	src/bin/plt_goea.py \
	src/pkggosim/goea/sim.py \
	src/pkggosim/goea/sims.py \
	src/pkggosim/goea/experiments.py \
	src/pkggosim/goea/run_all.py \
	src/pkggosim/goea/run_all_params.py \
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
