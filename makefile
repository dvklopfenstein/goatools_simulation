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

run_goeas_rand_rmgene:
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_rmgene$(G)_ntn1
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_rmgene$(G)_ntn2
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_rmgene$(G)_ntn3
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_rmgene$(G)_all

run_goeas_orig:
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_ntn3
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_ntn2
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_ntn1
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=orig_all

run_goeas_rand:
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_ntn3
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_ntn2
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_ntn1
	src/bin/plt_goea.py e=$(E) randomize_truenull_assc=rand_all

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
