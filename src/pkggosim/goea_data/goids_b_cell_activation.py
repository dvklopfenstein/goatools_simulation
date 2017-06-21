"""GO IDs in b_cell_activation.

    GO-DAG version:   go-basic.obo: fmt(1.2) rel(2017-06-04) 48,682 GO Terms

    Annotation Information:
        GOC Validation Date: 05/26/2017 $
        Submission Date: 5/26/2017
        gaf-version: 2.0
        Project_name: Mouse Genome Informatics (MGI)
        URL: http://www.informatics.jax.org/
        Contact Email: mgi-help@jax.org
        Funding: NHGRI of US National Institutes of Health
        software version: $Revision$
        date: 05/25/2017 $


Parent Level-01 GOs:
    B BP 11,095 L01 D01 cellular process
    C BP  9,807 L01 D01 single-organism process
    D BP  6,410 L01 D01 metabolic process
    E BP  3,188 L01 D01 developmental process
    L BP    573 L01 D01 immune system process

"""

#pylint: disable=line-too-long

GOIDS = set([ # 20 items
    'GO:0001923', # BP      2 L07 D09 BCEL  B-1 B cell differentiation(1 genes)
    'GO:0002312', # BP     13 L05 D07 BCL   B cell activation involved in immune response(1 genes)
    'GO:0002313', # BP      5 L06 D09 BCEL  mature B cell differentiation involved in immune response(1 genes)
    'GO:0002314', # BP      0 L07 D10 BCEL  germinal center B cell differentiation(3 genes)
    'GO:0002315', # BP      0 L07 D10 BCEL  marginal zone B cell differentiation(10 genes)
    'GO:0002316', # BP      0 L07 D10 BCEL  follicular B cell differentiation(1 genes)
    'GO:0002317', # BP      0 L07 D10 BCEL  plasma cell differentiation(4 genes)
    'GO:0002322', # BP      0 L06 D08 BCL   B cell proliferation involved in immune response(5 genes)
    'GO:0002327', # BP      4 L06 D08 BCEL  immature B cell differentiation(2 genes)
    'GO:0002329', # BP      0 L07 D09 BCEL  pre-B cell differentiation(4 genes)
    'GO:0002333', # BP      0 L08 D10 BCEL  transitional one stage B cell differentiation(1 genes)
    'GO:0002335', # BP      9 L06 D08 BCEL  mature B cell differentiation(1 genes)
    'GO:0002337', # BP      0 L08 D10 BCEL  B-1a B cell differentiation(3 genes)
    'GO:0002358', # BP      0 L06 D08 BCL   B cell homeostatic proliferation(2 genes)
    'GO:0030183', # BP     15 L05 D07 BCEL  B cell differentiation(78 genes)
    'GO:0042100', # BP      3 L05 D07 BCL   B cell proliferation(48 genes)
    'GO:0042113', # BP     27 L04 D06 BCL   B cell activation(29 genes)
    'GO:0045190', # BP      5 L03 D12 BCDL  isotype switching(17 genes)
    'GO:0048290', # BP      0 L04 D13 BCDL  isotype switching to IgA isotypes(1 genes)
    'GO:0048291', # BP      0 L04 D13 BCDL  isotype switching to IgG isotypes(1 genes)
])
