# Gene Ontology Enrichment Analyses Simulations

pylint:
	find src -name \*.py | xargs pylint -r no

vim_sim_geneontology:
	vim -p \
	src/bin/test_goea_sim.py \
	src/pkggosim/goea_sim.py \
	src/pkggosim/goea_utils.py \
	src/pkggosim/goea_objrun_all.py \
	src/pkggosim/goea_objbg.py \
	src/pkggosim/utils.py

vim_presim_geneontology:
	vim -p \
	src/bin/sim_geneontology.py \
	src/pkggosim/goea_objrun_prelim.py \
	src/pkggosim/goea_objbg.py

vim_sim_benjamini_hochberg:
	vim -p \
	src/bin/plt_fdr_benjamini_hochberg.py \
	src/bin/sim_fdr_benjamini_hochberg.py \
	src/pkggosim/hypotheses_sim.py \
	src/pkggosim/hypotheses_sims.py \
	src/pkggosim/hypotheses_experiments.py \
	src/pkggosim/hypotheses_run_all.py \
	src/pkggosim/hypotheses_plot_results.py \
	src/pkggosim/randseed.py \
	src/pkggosim/utils.py

vim_md:
	vim -p \
	README.md \
	doc/md/README_prep.md \
	doc/md/README_main.md

run:
	echo run

getdata:
	../goatools_suppl/src/bin/get_goids_by_section.py ../goatools_simulation/src/pkggosim

clean:
	find src -name \*.pyc | xargs rm -f
	rm -f python*.st*

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
