"""GO IDs in humoral_rsp.

    GO-DAG version:   go-basic.obo: fmt(1.2) rel(2017-05-20) 48,661 GO Terms

    Annotation Information:
        GOC Validation Date: 05/19/2017 $
        Submission Date: 5/19/2017
        gaf-version: 2.0
        Project_name: Mouse Genome Informatics (MGI)
        URL: http://www.informatics.jax.org/
        Contact Email: mgi-help@jax.org
        Funding: NHGRI of US National Institutes of Health
        software version: $Revision$
        date: 05/18/2017 $


Parent Level-01 GOs:
    A BP 12,571 L01 D01 biological regulation
    D BP  6,409 L01 D01 metabolic process
    F BP  2,260 L01 D01 response to stimulus
    I BP  1,526 L01 D01 multi-organism process
    L BP    573 L01 D01 immune system process

"""

#pylint: disable=line-too-long

GOIDS = set([ # 9 items
    'GO:0006959', # BP     13 L03 D03 FL    humoral immune response(51 genes)
    'GO:0019730', # BP      5 L03 D05 FIL   antimicrobial humoral response(2 genes)
    'GO:0006956', # BP      4 L03 D07 ADFL  complement activation(7 genes)
    'GO:0061844', # BP      0 L04 D06 FIL   antimicrobial humoral immune response mediated by antimicrobial peptide(30 genes)
    'GO:0019732', # BP      0 L04 D07 FIL   antifungal humoral response(3 genes)
    'GO:0002455', # BP      0 L04 D07 FL    humoral immune response mediated by circulating immunoglobulin(4 genes)
    'GO:0001867', # BP      0 L04 D08 ADFL  complement activation, lectin pathway(8 genes)
    'GO:0006957', # BP      0 L04 D08 ADFL  complement activation, alternative pathway(10 genes)
    'GO:0006958', # BP      0 L04 D08 ADFL  complement activation, classical pathway(27 genes)
])
