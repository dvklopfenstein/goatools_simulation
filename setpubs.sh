# Use the bibliography in this repo
export PYTHONPATH=.:./src:./src/py:${GIT}/dvk:${GIT}/pubscite/src:${GIT}/pmidcite/src:${GIT}/bibliography/src:${GIT}/pubs:${GIT}/enrichmentanalysis/src:${GIT}/ReactomePy/src:${GIT}/flashcards/src:${GIT}/biodnld/src:${GIT}/biocode/src:${GIT}/goatools_alpha/src:${GIT}/goatools/:${GIT}/genanki/:${GIT}/prtgitlog/src:${GIT}/PrincetonAlgorithms/py/

export PCD=${GIT}/proj_dis_clu/disease_clu_hsa_pcd.txt
echo 'PCD:' $PCD

#echo '!!!!!! WARNING: YOU MUST RUN: source setpubs.sh !!!!!!!'
echo 'PUBSCONF BEFORE:' $PUBSCONF
export PUBSCONF=`pwd`/pubs/dot_pubsrc
echo 'PUBSCONF AFTER: ' $PUBSCONF
#pubs statistics

echo 'PMIDCITECONF:' $PMIDCITECONF
#echo '!!!!!! TEST PUBSCONF IS SET CORRECTLY BY DOING:!!!!!'
#echo 'printenv PUBSCONF'
