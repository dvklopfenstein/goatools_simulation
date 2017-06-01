"""GO IDs in viral/bacteria.

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
    B BP 11,094 L01 D01 cellular process
    F BP  2,260 L01 D01 response to stimulus
    I BP  1,526 L01 D01 multi-organism process
    L BP    573 L01 D01 immune system process
    M BP    400 L01 D01 locomotion
    U BP     31 L01 D01 cell killing

"""

GOIDS = set([ # 86 items
    'GO:0016032', # BP    297 L04 D04 I     viral process(26 genes)
    'GO:0019048', # BP    173 L05 D05 I     modulation by virus of host morphology or physiology(4 genes)
    'GO:0050792', # BP     60 L05 D05 A     regulation of viral process(6 genes)
    'GO:0039507', # BP     60 L07 D07 AI    suppression by virus of host molecular function(1 genes)
    'GO:0019049', # BP     49 L06 D09 FI    evasion or tolerance of host defenses by virus(2 genes)
    'GO:1903900', # BP     37 L06 D06 A     regulation of viral life cycle(2 genes)
    'GO:0098542', # BP     33 L03 D05 FI    defense response to other organism(1 genes)
    'GO:0048525', # BP     19 L05 D06 A     negative regulation of viral process(5 genes)
    'GO:0048524', # BP     18 L05 D06 A     positive regulation of viral process(7 genes)
    'GO:0019079', # BP     13 L05 D05 I     viral genome replication(4 genes)
    'GO:0009617', # BP     12 L03 D05 FI    response to bacterium(35 genes)
    'GO:1903902', # BP     11 L06 D07 A     positive regulation of viral life cycle(2 genes)
    'GO:0045069', # BP      9 L07 D07 A     regulation of viral genome replication(4 genes)
    'GO:0042742', # BP      8 L04 D06 FI    defense response to bacterium(139 genes)
    'GO:0046755', # BP      7 L05 D05 I     viral budding(6 genes)
    'GO:1902186', # BP      7 L04 D07 A     regulation of viral release from host cell(3 genes)
    'GO:0046782', # BP      6 L06 D06 A     regulation of viral transcription(1 genes)
    'GO:0051873', # BP      6 L04 D07 FIU   killing by host of symbiont cells(5 genes)
    'GO:0046596', # BP      5 L07 D07 A     regulation of viral entry into host cell(4 genes)
    'GO:0019043', # BP      4 L05 D05 I     establishment of viral latency(1 genes)
    'GO:0039694', # BP      4 L06 D06 I     viral RNA genome replication(8 genes)
    'GO:0019076', # BP      4 L05 D07 IM    viral release from host cell(4 genes)
    'GO:0051607', # BP      3 L03 D06 FIL   defense response to virus(137 genes)
    'GO:0050832', # BP      3 L04 D06 FI    defense response to fungus(17 genes)
    'GO:0044793', # BP      3 L06 D07 AI    negative regulation by host of viral process(2 genes)
    'GO:0043921', # BP      3 L06 D10 AI    modulation by host of viral transcription(1 genes)
    'GO:0019731', # BP      2 L04 D07 FIL   antibacterial humoral response(21 genes)
    'GO:0044794', # BP      2 L06 D07 AI    positive regulation by host of viral process(7 genes)
    'GO:1903772', # BP      2 L07 D07 A     regulation of viral budding via host ESCRT complex(3 genes)
    'GO:0045070', # BP      2 L07 D08 A     positive regulation of viral genome replication(23 genes)
    'GO:0045071', # BP      2 L07 D08 A     negative regulation of viral genome replication(29 genes)
    'GO:1902187', # BP      2 L05 D08 A     negative regulation of viral release from host cell(15 genes)
    'GO:0060139', # BP      2 L07 D12 AI    positive regulation of apoptotic process by virus(3 genes)
    'GO:0019081', # BP      1 L05 D05 I     viral translation(1 genes)
    'GO:0019046', # BP      1 L05 D05 I     release from viral latency(3 genes)
    'GO:0009609', # BP      1 L04 D06 FI    response to symbiotic bacterium(2 genes)
    'GO:0019087', # BP      1 L06 D06 I     transformation of host cell by virus(4 genes)
    'GO:0016045', # BP      1 L04 D06 FI    detection of bacterium(12 genes)
    'GO:0042832', # BP      1 L04 D06 FI    defense response to protozoan(31 genes)
    'GO:0032897', # BP      1 L06 D07 A     negative regulation of viral transcription(12 genes)
    'GO:0050434', # BP      1 L06 D07 A     positive regulation of viral transcription(4 genes)
    'GO:1902188', # BP      1 L05 D08 A     positive regulation of viral release from host cell(10 genes)
    'GO:0046597', # BP      1 L07 D08 A     negative regulation of viral entry into host cell(20 genes)
    'GO:0046598', # BP      1 L07 D08 A     positive regulation of viral entry into host cell(9 genes)
    'GO:0019058', # BP      0 L05 D05 I     viral life cycle(1 genes)
    'GO:0019068', # BP      0 L05 D05 I     virion assembly(5 genes)
    'GO:0075522', # BP      0 L05 D05 I     IRES-dependent viral translational initiation(7 genes)
    'GO:0075525', # BP      0 L05 D05 I     viral translational termination-reinitiation(5 genes)
    'GO:0046786', # BP      0 L05 D05 I     viral replication complex formation and maintenance(1 genes)
    'GO:0019075', # BP      0 L05 D05 I     virus maturation(2 genes)
    'GO:0046745', # BP      0 L05 D05 I     viral capsid secondary envelopment(1 genes)
    'GO:0019085', # BP      0 L06 D06 I     early viral transcription(2 genes)
    'GO:0019086', # BP      0 L06 D06 I     late viral transcription(3 genes)
    'GO:0039702', # BP      0 L06 D06 I     viral budding via host ESCRT complex(9 genes)
    'GO:0019074', # BP      0 L06 D06 I     viral RNA genome packaging(2 genes)
    'GO:0075713', # BP      0 L06 D06 I     establishment of integrated proviral latency(1 genes)
    'GO:1904188', # BP      0 L06 D07 A     negative regulation of transformation of host cell by virus(1 genes)
    'GO:0009682', # BP      0 L04 D07 FIL   induced systemic resistance(1 genes)
    'GO:0046725', # BP      0 L06 D07 A     negative regulation by virus of viral protein levels in host cell(2 genes)
    'GO:0050830', # BP      0 L05 D07 FI    defense response to Gram-positive bacterium(83 genes)
    'GO:0046726', # BP      0 L06 D07 A     positive regulation by virus of viral protein levels in host cell(4 genes)
    'GO:0039692', # BP      0 L07 D07 I     single stranded viral RNA replication via double stranded DNA intermediate(1 genes)
    'GO:0050829', # BP      0 L05 D07 FI    defense response to Gram-negative bacterium(61 genes)
    'GO:0039689', # BP      0 L07 D07 I     negative stranded viral RNA replication(4 genes)
    'GO:0006948', # BP      0 L07 D07 I     induction by virus of host cell-cell fusion(1 genes)
    'GO:1903774', # BP      0 L07 D08 A     positive regulation of viral budding via host ESCRT complex(3 genes)
    'GO:0039521', # BP      0 L08 D08 AI    suppression by virus of host autophagy(1 genes)
    'GO:0039520', # BP      0 L08 D08 AI    induction by virus of host autophagy(1 genes)
    'GO:0044871', # BP      0 L07 D08 AI    negative regulation by host of viral glycoprotein metabolic process(2 genes)
    'GO:0043152', # BP      0 L05 D08 FIL   induction of bacterial agglutination(3 genes)
    'GO:0051838', # BP      0 L05 D08 BFIU  cytolysis by host of symbiont cells(1 genes)
    'GO:1901253', # BP      0 L05 D08 A     negative regulation of intracellular transport of viral material(2 genes)
    'GO:1901254', # BP      0 L05 D08 A     positive regulation of intracellular transport of viral material(1 genes)
    'GO:0044790', # BP      0 L06 D09 AI    negative regulation by host of viral release from host cell(1 genes)
    'GO:0044791', # BP      0 L06 D09 AI    positive regulation by host of viral release from host cell(6 genes)
    'GO:0045870', # BP      0 L08 D09 A     positive regulation of single stranded viral RNA replication via double stranded DNA intermediate(1 genes)
    'GO:0044828', # BP      0 L07 D09 AI    negative regulation by host of viral genome replication(7 genes)
    'GO:0044829', # BP      0 L07 D09 AI    positive regulation by host of viral genome replication(8 genes)
    'GO:0070947', # BP      0 L05 D09 FILU  neutrophil mediated killing of fungus(2 genes)
    'GO:0045869', # BP      0 L08 D09 A     negative regulation of single stranded viral RNA replication via double stranded DNA intermediate(3 genes)
    'GO:0044830', # BP      0 L07 D09 AI    modulation by host of viral RNA genome replication(2 genes)
    'GO:0070945', # BP      0 L06 D10 FILU  neutrophil mediated killing of gram-negative bacterium(5 genes)
    'GO:0070946', # BP      0 L06 D10 FILU  neutrophil mediated killing of gram-positive bacterium(2 genes)
    'GO:0043922', # BP      0 L07 D11 AI    negative regulation by host of viral transcription(10 genes)
    'GO:0043923', # BP      0 L07 D11 AI    positive regulation by host of viral transcription(14 genes)
    'GO:1990969', # BP      0 L04 D11 AI    modulation by host of viral RNA-binding transcription factor activity(1 genes)
])
