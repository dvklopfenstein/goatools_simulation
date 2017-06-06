# Gene Ontology Enrichment Analyses Simulations

pylint:
	find src -name \*.py | xargs pylint -r no

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
	src/pkggosim/goea/objbase.py \
	src/pkggosim/common/true_positive.py

vim_presim_geneontology:
	vim -p \
	src/bin/sim_geneontology.py \
	src/pkggosim/goea_objrun_prelim.py \
	src/pkggosim/goea_objbg.py

vim_sim_benjamini_hochberg:
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

run:
	echo run

getdata:
	../goatools_suppl/src/bin/get_goids_by_section.py ../goatools_simulation/src/pkggosim

clean:
	find src -name \*.pyc | xargs rm -f
	rm -f python*.st*

# Copyright (C) 2017, DV Klopfenstein. All rights reserved.
