# Gene Ontology Enrichment Analyses Simulations

vim_sim_fdr_benjamini_hochberg:
	vim -p \
	src/bin/sim_fdr_benjamini_hochberg.py \
	src/pkgsim/hypotheses_sim.py \
	src/pkgsim/hypotheses_sims.py \
	src/pkgsim/hypotheses_experiments.py \
	src/pkgsim/hypotheses_run_all.py \
	src/pkgsim/hypotheses_plot_results.py \
	src/pkgsim/randseed.py \
	src/pkgsim/utils.py

vim_md:
	vim -p \
	README.md \
	doc/md/README_prep.md \
	doc/md/README_main.md

run:
	echo run

clean:
	find src -name \*.pyc | xargs rm -f
	rm -f python*.st*

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
