# Gene Ontology Enrichment Analyses Simulations

vim_sim_fdr_benjamini_hochberg:
	vim -p \
	src/bin/sim_fdr_benjamini_hochberg2.py \
	src/bin/sim_fdr_benjamini_hochberg.py \
	src/pkgsim/pval_sim.py \
	src/pkgsim/pval_sims.py \
	src/pkgsim/experiments.py \
	src/pkgsim/run_all_experiments.py \
	src/pkgsim/pval_mtcorr_sims.py \
	src/pkgsim/report_results.py \
	src/pkgsim/plot_results.py \
	src/pkgsim/randseed.py

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
