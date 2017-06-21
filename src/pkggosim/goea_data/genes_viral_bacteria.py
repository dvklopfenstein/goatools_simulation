"""Genes in viral/bacteria.

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

"""

GENES = set([ # 592 items
    'ENSMUSG00000000058', # Cav2            caveolin 2
    'ENSMUSG00000000244', # Tspan32         tetraspanin 32
    'ENSMUSG00000000266', # Mid2            midline 2
    'ENSMUSG00000000275', # Trim25          tripartite motif-containing 25
    'ENSMUSG00000000385', # Tmprss2         transmembrane protease, serine 2
    'ENSMUSG00000000386', # Mx1             MX dynamin-like GTPase 1
    'ENSMUSG00000000776', # Polr3d          polymerase (RNA) III (DNA directed) polypeptide D
    'ENSMUSG00000000787', # Ddx3x           DEAD/H (Asp-Glu-Ala-Asp/His) box polypeptide 3, X-linked
    'ENSMUSG00000000838', # Fmr1            fragile X mental retardation syndrome 1
    'ENSMUSG00000000869', # Il4             interleukin 4
    'ENSMUSG00000000902', # Smarcb1         SWI/SNF related, matrix associated, actin dependent regulator of chromatin, subfamily b, member 1
    'ENSMUSG00000001249', # Hpn             hepsin
    'ENSMUSG00000001280', # Sp1             trans-acting transcription factor 1
    'ENSMUSG00000001348', # Acp5            acid phosphatase 5, tartrate resistant
    'ENSMUSG00000002102', # Psmc3           proteasome (prosome, macropain) 26S subunit, ATPase 3
    'ENSMUSG00000002603', # Tgfb1           transforming growth factor, beta 1
    'ENSMUSG00000002688', # Prkd1           protein kinase D1
    'ENSMUSG00000002897', # Il17ra          interleukin 17 receptor A
    'ENSMUSG00000002944', # Cd36            CD36 antigen
    'ENSMUSG00000002985', # Apoe            apolipoprotein E
    'ENSMUSG00000003184', # Irf3            interferon regulatory factor 3
    'ENSMUSG00000003234', # Abcf3           ATP-binding cassette, sub-family F (GCN20), member 3
    'ENSMUSG00000003283', # Hck             hemopoietic cell kinase
    'ENSMUSG00000003452', # Bicd1           bicaudal D homolog 1 (Drosophila)
    'ENSMUSG00000003813', # Rad23a          RAD23 homolog A, nucleotide excision repair protein
    'ENSMUSG00000004296', # Il12b           interleukin 12b
    'ENSMUSG00000004591', # Pkn2            protein kinase N2
    'ENSMUSG00000004843', # Chmp2b          charged multivesicular body protein 2B
    'ENSMUSG00000004865', # Srpk1           serine/arginine-rich protein specific kinase 1
    'ENSMUSG00000004934', # Pias4           protein inhibitor of activated STAT 4
    'ENSMUSG00000005102', # Eif2ak4         eukaryotic translation initiation factor 2 alpha kinase 4
    'ENSMUSG00000005465', # Il27ra          interleukin 27 receptor, alpha
    'ENSMUSG00000005534', # Insr            insulin receptor
    'ENSMUSG00000005566', # Trim28          tripartite motif-containing 28
    'ENSMUSG00000005718', # Tfap4           transcription factor AP4
    'ENSMUSG00000006058', # Snf8            SNF8, ESCRT-II complex subunit, homolog (S. cerevisiae)
    'ENSMUSG00000006127', # Inpp5k          inositol polyphosphate 5-phosphatase K
    'ENSMUSG00000006235', # Epor            erythropoietin receptor
    'ENSMUSG00000006369', # Fbln1           fibulin 1
    'ENSMUSG00000006403', # Adamts4         a disintegrin-like and metallopeptidase (reprolysin type) with thrombospondin type 1 motif, 4
    'ENSMUSG00000006445', # Epha2           Eph receptor A2
    'ENSMUSG00000006498', # Ptbp1           polypyrimidine tract binding protein 1
    'ENSMUSG00000006570', # Defb2           defensin beta 2
    'ENSMUSG00000007655', # Cav1            caveolin 1, caveolae protein
    'ENSMUSG00000009350', # Mpo             myeloperoxidase
    'ENSMUSG00000009356', # Lpo             lactoperoxidase
    'ENSMUSG00000009585', # Apobec3         apolipoprotein B mRNA editing enzyme, catalytic polypeptide 3
    'ENSMUSG00000009907', # Vps4b           vacuolar protein sorting 4B
    'ENSMUSG00000010047', # Hyal2           hyaluronoglucosaminidase 2
    'ENSMUSG00000010054', # Tusc2           tumor suppressor candidate 2
    'ENSMUSG00000010175', # Prox1           prospero homeobox 1
    'ENSMUSG00000010435', # Spaca7          sperm acrosome associated 7
    'ENSMUSG00000013643', # Lypd8           LY6/PLAUR domain containing 8
    'ENSMUSG00000014402', # Tsg101          tumor susceptibility gene 101
    'ENSMUSG00000015120', # Ube2i           ubiquitin-conjugating enzyme E2I
    'ENSMUSG00000015478', # Rnf5            ring finger protein 5
    'ENSMUSG00000015656', # Hspa8           heat shock protein 8
    'ENSMUSG00000015846', # Rxra            retinoid X receptor alpha
    'ENSMUSG00000015947', # Fcgr1           Fc receptor, IgG, high affinity I
    'ENSMUSG00000015950', # Ncf1            neutrophil cytosolic factor 1
    'ENSMUSG00000016024', # Lbp             lipopolysaccharide binding protein
    'ENSMUSG00000016206', # H2-M3           histocompatibility 2, M region locus 3
    'ENSMUSG00000016529', # Il10            interleukin 10
    'ENSMUSG00000016554', # Eif3d           eukaryotic translation initiation factor 3, subunit D
    'ENSMUSG00000017002', # Slpi            secretory leukocyte peptidase inhibitor
    'ENSMUSG00000017652', # Cd40            CD40 antigen
    'ENSMUSG00000017707', # Serinc3         serine incorporator 3
    'ENSMUSG00000017737', # Mmp9            matrix metallopeptidase 9
    'ENSMUSG00000017830', # Dhx58           DEXH (Asp-Glu-X-His) box polypeptide 58
    'ENSMUSG00000017831', # Rab5a           RAB5A, member RAS oncogene family
    'ENSMUSG00000018102', # Hist1h2bc       histone cluster 1, H2bc
    'ENSMUSG00000018211', # Wfdc15b         WAP four-disulfide core domain 15B
    'ENSMUSG00000018293', # Pfn1            profilin 1
    'ENSMUSG00000018623', # Mmp7            matrix metallopeptidase 7
    'ENSMUSG00000018899', # Irf1            interferon regulatory factor 1
    'ENSMUSG00000018930', # Ccl4            chemokine (C-C motif) ligand 4
    'ENSMUSG00000019726', # Lyst            lysosomal trafficking regulator
    'ENSMUSG00000019804', # Snx3            sorting nexin 3
    'ENSMUSG00000019810', # Fuca2           fucosidase, alpha-L- 2, plasma
    'ENSMUSG00000019868', # Vta1            vesicle (multivesicular body) trafficking 1
    'ENSMUSG00000020009', # Ifngr1          interferon gamma receptor 1
    'ENSMUSG00000020108', # Ddit4           DNA-damage-inducible transcript 4
    'ENSMUSG00000020115', # Tbk1            TANK-binding kinase 1
    'ENSMUSG00000020125', # Elane           elastase, neutrophil expressed
    'ENSMUSG00000020149', # Rab1a           RAB1A, member RAS oncogene family
    'ENSMUSG00000020177', # 9530003J23Rik   RIKEN cDNA 9530003J23 gene
    'ENSMUSG00000020262', # Adarb1          adenosine deaminase, RNA-specific, B1
    'ENSMUSG00000020380', # Rad50           RAD50 double strand break repair protein
    'ENSMUSG00000020399', # Havcr2          hepatitis A virus cellular receptor 2
    'ENSMUSG00000020455', # Trim11          tripartite motif-containing 11
    'ENSMUSG00000020525', # Ppm1d           protein phosphatase 1D magnesium-dependent, delta isoform
    'ENSMUSG00000020580', # Rock2           Rho-associated coiled-coil containing protein kinase 2
    'ENSMUSG00000020641', # Rsad2           radical S-adenosyl methionine domain containing 2
    'ENSMUSG00000020719', # Ddx5            DEAD (Asp-Glu-Ala-Asp) box polypeptide 5
    'ENSMUSG00000020783', # Ncbp3           nuclear cap binding subunit 3
    'ENSMUSG00000020826', # Nos2            nitric oxide synthase 2, inducible
    'ENSMUSG00000020914', # Top2a           topoisomerase (DNA) II alpha
    'ENSMUSG00000020945', # Lyzl6           lysozyme-like 6
    'ENSMUSG00000020953', # Coch            cochlin
    'ENSMUSG00000021039', # Snw1            SNW domain containing 1
    'ENSMUSG00000021194', # Chga            chromogranin A
    'ENSMUSG00000021258', # Ccnk            cyclin K
    'ENSMUSG00000021326', # Trim27          tripartite motif-containing 27
    'ENSMUSG00000021356', # Irf4            interferon regulatory factor 4
    'ENSMUSG00000021408', # Ripk1           receptor (TNFRSF)-interacting serine-threonine kinase 1
    'ENSMUSG00000021457', # Syk             spleen tyrosine kinase
    'ENSMUSG00000021494', # Ddx41           DEAD (Asp-Glu-Ala-Asp) box polypeptide 41
    'ENSMUSG00000021678', # F2rl1           coagulation factor II (thrombin) receptor-like 1
    'ENSMUSG00000021703', # Serinc5         serine incorporator 5
    'ENSMUSG00000021911', # Parg            poly (ADP-ribose) glycohydrolase
    'ENSMUSG00000021948', # Prkcd           protein kinase C, delta
    'ENSMUSG00000022043', # Trim35          tripartite motif-containing 35
    'ENSMUSG00000022051', # Bnip3l          BCL2/adenovirus E1B interacting protein 3-like
    'ENSMUSG00000022191', # Drosha          drosha, ribonuclease type III
    'ENSMUSG00000022221', # Ripk3           receptor-interacting serine-threonine kinase 3
    'ENSMUSG00000022283', # Pabpc1          poly(A) binding protein, cytoplasmic 1
    'ENSMUSG00000022346', # Myc             myelocytomatosis oncogene
    'ENSMUSG00000022476', # Polr3h          polymerase (RNA) III (DNA directed) polypeptide H
    'ENSMUSG00000022521', # Crebbp          CREB binding protein
    'ENSMUSG00000022575', # Gsdmd           gasdermin D
    'ENSMUSG00000022865', # Cxadr           coxsackie virus and adenovirus receptor
    'ENSMUSG00000022877', # Hrg             histidine-rich glycoprotein
    'ENSMUSG00000022894', # Adamts5         a disintegrin-like and metallopeptidase (reprolysin type) with thrombospondin type 1 motif, 5 (aggrecanase-2)
    'ENSMUSG00000022901', # Cd86            CD86 antigen
    'ENSMUSG00000022965', # Ifngr2          interferon gamma receptor 2
    'ENSMUSG00000022967', # Ifnar1          interferon (alpha and beta) receptor 1
    'ENSMUSG00000022969', # Il10rb          interleukin 10 receptor, beta
    'ENSMUSG00000022971', # Ifnar2          interferon (alpha and beta) receptor 2
    'ENSMUSG00000022991', # Lalba           lactalbumin, alpha
    'ENSMUSG00000023051', # Tarbp2          TARBP2, RISC loading complex RNA binding subunit
    'ENSMUSG00000023078', # Cxcl13          chemokine (C-X-C motif) ligand 13
    'ENSMUSG00000023274', # Cd4             CD4 antigen
    'ENSMUSG00000023349', # Clec4n          C-type lectin domain family 4, member n
    'ENSMUSG00000023826', # Park2           Parkinson disease (autosomal recessive, juvenile) 2, parkin
    'ENSMUSG00000023852', # Chd1            chromodomain helicase DNA binding protein 1
    'ENSMUSG00000023990', # Tfeb            transcription factor EB
    'ENSMUSG00000024079', # Eif2ak2         eukaryotic translation initiation factor 2-alpha kinase 2
    'ENSMUSG00000024091', # Vapa            vesicle-associated membrane protein, associated protein A
    'ENSMUSG00000024218', # Taf11           TATA-box binding protein associated factor 11
    'ENSMUSG00000024233', # Lyzl1           lysozyme-like 1
    'ENSMUSG00000024300', # Myo1f           myosin IF
    'ENSMUSG00000024349', # Tmem173         transmembrane protein 173
    'ENSMUSG00000024360', # Etf1            eukaryotic translation termination factor 1
    'ENSMUSG00000024401', # Tnf             tumor necrosis factor
    'ENSMUSG00000024402', # Lta             lymphotoxin A
    'ENSMUSG00000024404', # Riok3           RIO kinase 3
    'ENSMUSG00000024457', # Trim26          tripartite motif-containing 26
    'ENSMUSG00000024610', # Cd74            CD74 antigen (invariant polypeptide of major histocompatibility complex, class II antigen-associated)
    'ENSMUSG00000024691', # Fam111a         family with sequence similarity 111, member A
    'ENSMUSG00000024713', # Pcsk5           proprotein convertase subtilisin/kexin type 5
    'ENSMUSG00000024740', # Ddb1            damage specific DNA binding protein 1
    'ENSMUSG00000024810', # Il33            interleukin 33
    'ENSMUSG00000024844', # Banf1           barrier to autointegration factor 1
    'ENSMUSG00000024858', # Grk2            G protein-coupled receptor kinase 2
    'ENSMUSG00000024863', # Mbl2            mannose-binding lectin (protein C) 2
    'ENSMUSG00000024892', # Pcx             pyruvate carboxylase
    'ENSMUSG00000024901', # Peli3           pellino 3
    'ENSMUSG00000024927', # Rela            v-rel reticuloendotheliosis viral oncogene homolog A (avian)
    'ENSMUSG00000024959', # Bad             BCL2-associated agonist of cell death
    'ENSMUSG00000024974', # Smc3            structural maintenance of chromosomes 3
    'ENSMUSG00000024978', # Gpam            glycerol-3-phosphate acyltransferase, mitochondrial
    'ENSMUSG00000024991', # Eif3a           eukaryotic translation initiation factor 3, subunit A
    'ENSMUSG00000025034', # Trim8           tripartite motif-containing 8
    'ENSMUSG00000025130', # P4hb            prolyl 4-hydroxylase, beta polypeptide
    'ENSMUSG00000025199', # Chuk            conserved helix-loop-helix ubiquitous kinase
    'ENSMUSG00000025371', # Chmp6           charged multivesicular body protein 6
    'ENSMUSG00000025372', # Baiap2          brain-specific angiogenesis inhibitor 1-associated protein 2
    'ENSMUSG00000025383', # Il23a           interleukin 23, alpha subunit p19
    'ENSMUSG00000025491', # Ifitm1          interferon induced transmembrane protein 1
    'ENSMUSG00000025492', # Ifitm3          interferon induced transmembrane protein 3
    'ENSMUSG00000025499', # Hras            Harvey rat sarcoma virus oncogene
    'ENSMUSG00000025532', # Crcp            calcitonin gene-related peptide-receptor component protein
    'ENSMUSG00000025746', # Il6             interleukin 6
    'ENSMUSG00000025888', # Casp1           caspase 1
    'ENSMUSG00000025905', # Oprk1           opioid receptor, kappa 1
    'ENSMUSG00000025929', # Il17a           interleukin 17A
    'ENSMUSG00000026104', # Stat1           signal transducer and activator of transcription 1
    'ENSMUSG00000026175', # Vil1            villin 1
    'ENSMUSG00000026177', # Slc11a1         solute carrier family 11 (proton-coupled divalent metal ion transporters), member 1
    'ENSMUSG00000026289', # Atg16l1         autophagy related 16-like 1 (S. cerevisiae)
    'ENSMUSG00000026349', # Ccnt2           cyclin T2
    'ENSMUSG00000026395', # Ptprc           protein tyrosine phosphatase, receptor type, C
    'ENSMUSG00000026398', # Nr5a2           nuclear receptor subfamily 5, group A, member 2
    'ENSMUSG00000026433', # Rab29           RAB29, member RAS oncogene family
    'ENSMUSG00000026434', # Nucks1          nuclear casein kinase and cyclin-dependent kinase substrate 1
    'ENSMUSG00000026471', # Mr1             major histocompatibility complex, class I-related
    'ENSMUSG00000026542', # Apcs            serum amyloid P-component
    'ENSMUSG00000026641', # Usf1            upstream transcription factor 1
    'ENSMUSG00000026656', # Fcgr2b          Fc receptor, IgG, low affinity IIb
    'ENSMUSG00000026672', # Optn            optineurin
    'ENSMUSG00000026792', # Lrsam1          leucine rich repeat and sterile alpha motif containing 1
    'ENSMUSG00000026835', # Fcnb            ficolin B
    'ENSMUSG00000026878', # Rab14           RAB14, member RAS oncogene family
    'ENSMUSG00000026879', # Gsn             gelsolin
    'ENSMUSG00000026880', # Stom            stomatin
    'ENSMUSG00000026896', # Ifih1           interferon induced with helicase C domain 1
    'ENSMUSG00000026923', # Notch1          notch 1
    'ENSMUSG00000026928', # Card9           caspase recruitment domain family, member 9
    'ENSMUSG00000027073', # Prg2            proteoglycan 2, bone marrow
    'ENSMUSG00000027249', # F2              coagulation factor II
    'ENSMUSG00000027381', # Bcl2l11         BCL2-like 11 (apoptosis facilitator)
    'ENSMUSG00000027427', # Polr3f          polymerase (RNA) III (DNA directed) polypeptide F
    'ENSMUSG00000027465', # Tbc1d20         TBC1 domain family, member 20
    'ENSMUSG00000027468', # Defb22          defensin beta 22
    'ENSMUSG00000027483', # Bpifa1          BPI fold containing family A, member 1
    'ENSMUSG00000027514', # Zbp1            Z-DNA binding protein 1
    'ENSMUSG00000027536', # Chmp4c          charged multivesicular body protein 4C
    'ENSMUSG00000027598', # Itch            itchy, E3 ubiquitin protein ligase
    'ENSMUSG00000027639', # Samhd1          SAM domain and HD domain, 1
    'ENSMUSG00000027667', # Zfp639          zinc finger protein 639
    'ENSMUSG00000027684', # Mecom           MDS1 and EVI1 complex locus
    'ENSMUSG00000027695', # Pld1            phospholipase D1
    'ENSMUSG00000027776', # Il12a           interleukin 12a
    'ENSMUSG00000027804', # Ppid            peptidylprolyl isomerase D (cyclophilin D)
    'ENSMUSG00000027832', # Ptx3            pentraxin related gene
    'ENSMUSG00000027852', # Nras            neuroblastoma ras oncogene
    'ENSMUSG00000027878', # Notch2          notch 2
    'ENSMUSG00000027951', # Adar            adenosine deaminase, RNA-specific
    'ENSMUSG00000027962', # Vcam1           vascular cell adhesion molecule 1
    'ENSMUSG00000027985', # Lef1            lymphoid enhancer binding factor 1
    'ENSMUSG00000027995', # Tlr2            toll-like receptor 2
    'ENSMUSG00000028001', # Fga             fibrinogen alpha chain
    'ENSMUSG00000028099', # Polr3c          polymerase (RNA) III (DNA directed) polypeptide C
    'ENSMUSG00000028145', # Them4           thioesterase superfamily member 4
    'ENSMUSG00000028224', # Nbn             nibrin
    'ENSMUSG00000028264', # Spaca1          sperm acrosome associated 1
    'ENSMUSG00000028268', # Gbp3            guanylate binding protein 3
    'ENSMUSG00000028270', # Gbp2            guanylate binding protein 2
    'ENSMUSG00000028271', # Gtf2b           general transcription factor IIB
    'ENSMUSG00000028362', # Tnfsf8          tumor necrosis factor (ligand) superfamily, member 8
    'ENSMUSG00000028419', # Chmp5           charged multivesicular body protein 5
    'ENSMUSG00000028452', # Vcp             valosin containing protein
    'ENSMUSG00000028466', # Creb3           cAMP responsive element binding protein 3
    'ENSMUSG00000028651', # Ppie            peptidylprolyl isomerase E (cyclophilin E)
    'ENSMUSG00000028800', # Hdac1           histone deacetylase 1
    'ENSMUSG00000028874', # Fgr             FGR proto-oncogene, Src family tyrosine kinase
    'ENSMUSG00000029165', # Agbl5           ATP/GTP binding protein-like 5
    'ENSMUSG00000029249', # Rest            RE1-silencing transcription factor
    'ENSMUSG00000029298', # Gbp9            guanylate-binding protein 9
    'ENSMUSG00000029322', # Plac8           placenta-specific 8
    'ENSMUSG00000029373', # Pf4             platelet factor 4
    'ENSMUSG00000029417', # Cxcl9           chemokine (C-X-C motif) ligand 9
    'ENSMUSG00000029468', # P2rx7           purinergic receptor P2X, ligand-gated ion channel, 7
    'ENSMUSG00000029484', # Anxa3           annexin A3
    'ENSMUSG00000029522', # Pla2g1b         phospholipase A2, group IB, pancreas
    'ENSMUSG00000029561', # Oasl2           2'-5' oligoadenylate synthetase-like 2
    'ENSMUSG00000029684', # Wasl            Wiskott-Aldrich syndrome-like (human)
    'ENSMUSG00000029686', # Cul1            cullin 1
    'ENSMUSG00000029771', # Irf5            interferon regulatory factor 5
    'ENSMUSG00000029826', # Zc3hav1         zinc finger CCCH type, antiviral 1
    'ENSMUSG00000030017', # Reg3g           regenerating islet-derived 3 gamma
    'ENSMUSG00000030055', # Rab43           RAB43, member RAS oncogene family
    'ENSMUSG00000030059', # Tmf1            TATA element modulatory factor 1
    'ENSMUSG00000030142', # Clec4e          C-type lectin domain family 4, member e
    'ENSMUSG00000030144', # Clec4d          C-type lectin domain family 4, member d
    'ENSMUSG00000030149', # Klrk1           killer cell lectin-like receptor subfamily K, member 1
    'ENSMUSG00000030228', # Pik3c2g         phosphatidylinositol 3-kinase, C2 domain containing, gamma polypeptide
    'ENSMUSG00000030247', # Kcnj8           potassium inwardly-rectifying channel, subfamily J, member 8
    'ENSMUSG00000030249', # Abcc9           ATP-binding cassette, sub-family C (CFTR/MRP), member 9
    'ENSMUSG00000030281', # Il17rc          interleukin 17 receptor C
    'ENSMUSG00000030314', # Atg7            autophagy related 7
    'ENSMUSG00000030341', # Tnfrsf1a        tumor necrosis factor receptor superfamily, member 1a
    'ENSMUSG00000030413', # Pglyrp1         peptidoglycan recognition protein 1
    'ENSMUSG00000030748', # Il4ra           interleukin 4 receptor, alpha
    'ENSMUSG00000030789', # Itgax           integrin alpha X
    'ENSMUSG00000030793', # Pycard          PYD and CARD domain containing
    'ENSMUSG00000030798', # Cd37            CD37 antigen
    'ENSMUSG00000030880', # Polr3e          polymerase (RNA) III (DNA directed) polypeptide E
    'ENSMUSG00000030921', # Trim30a         tripartite motif-containing 30A
    'ENSMUSG00000030966', # Trim21          tripartite motif-containing 21
    'ENSMUSG00000031029', # Eif3f           eukaryotic translation initiation factor 3, subunit F
    'ENSMUSG00000031077', # Fadd            Fas (TNFRSF6)-associated via death domain
    'ENSMUSG00000031386', # Hcfc1           host cell factor C1
    'ENSMUSG00000031446', # Cul4a           cullin 4A
    'ENSMUSG00000031451', # Gas6            growth arrest specific 6
    'ENSMUSG00000031471', # Defb8           defensin beta 8
    'ENSMUSG00000031495', # Cd209d          CD209d antigen
    'ENSMUSG00000031509', # 1700016D06Rik   RIKEN cDNA 1700016D06 gene
    'ENSMUSG00000031639', # Tlr3            toll-like receptor 3
    'ENSMUSG00000031722', # Hp              haptoglobin
    'ENSMUSG00000031729', # Ist1            increased sodium tolerance 1 homolog (yeast)
    'ENSMUSG00000031813', # Mvb12a          multivesicular body subunit 12A
    'ENSMUSG00000031827', # Cotl1           coactosin-like 1 (Dictyostelium)
    'ENSMUSG00000031913', # Vps4a           vacuolar protein sorting 4A
    'ENSMUSG00000031928', # Mre11a          MRE11A homolog A, double strand break repair nuclease
    'ENSMUSG00000032012', # Nectin1         nectin cell adhesion molecule 1
    'ENSMUSG00000032015', # Pou2f3          POU domain, class 2, transcription factor 3
    'ENSMUSG00000032041', # Tirap           toll-interleukin 1 receptor (TIR) domain-containing adaptor protein
    'ENSMUSG00000032097', # Ddx6            DEAD (Asp-Glu-Ala-Asp) box polypeptide 6
    'ENSMUSG00000032109', # Nlrx1           NLR family member X1
    'ENSMUSG00000032178', # Ilf3            interleukin enhancer binding factor 3
    'ENSMUSG00000032187', # Smarca4         SWI/SNF related, matrix associated, actin dependent regulator of chromatin, subfamily a, member 4
    'ENSMUSG00000032344', # Mb21d1          Mab-21 domain containing 1
    'ENSMUSG00000032369', # Plscr1          phospholipid scramblase 1
    'ENSMUSG00000032383', # Ppib            peptidylprolyl isomerase B
    'ENSMUSG00000032402', # Smad3           SMAD family member 3
    'ENSMUSG00000032496', # Ltf             lactotransferrin
    'ENSMUSG00000032504', # Pdcd6ip         programmed cell death 6 interacting protein
    'ENSMUSG00000032508', # Myd88           myeloid differentiation primary response gene 88
    'ENSMUSG00000032584', # Mst1r           macrophage stimulating 1 receptor (c-met-related tyrosine kinase)
    'ENSMUSG00000032661', # Oas3            2'-5' oligoadenylate synthetase 3
    'ENSMUSG00000032690', # Oas2            2'-5' oligoadenylate synthetase 2
    'ENSMUSG00000032691', # Nlrp3           NLR family, pyrin domain containing 3
    'ENSMUSG00000032864', # Rag2            recombination activating gene 2
    'ENSMUSG00000033047', # Eif3l           eukaryotic translation initiation factor 3, subunit L
    'ENSMUSG00000033323', # Ctdp1           CTD (carboxy-terminal domain, RNA polymerase II, polypeptide A) phosphatase, subunit 1
    'ENSMUSG00000033450', # Tagap           T cell activation Rho GTPase activating protein
    'ENSMUSG00000033629', # Hacd3           3-hydroxyacyl-CoA dehydratase 3
    'ENSMUSG00000033831', # Fgb             fibrinogen beta chain
    'ENSMUSG00000033916', # Chmp2a          charged multivesicular body protein 2A
    'ENSMUSG00000034259', # Exosc4          exosome component 4
    'ENSMUSG00000034266', # Batf            basic leucine zipper transcription factor, ATF-like
    'ENSMUSG00000034317', # Trim59          tripartite motif-containing 59
    'ENSMUSG00000034453', # Polr3b          polymerase (RNA) III (DNA directed) polypeptide B
    'ENSMUSG00000034459', # Ifit1           interferon-induced protein with tetratricopeptide repeats 1
    'ENSMUSG00000034653', # Ythdc2          YTH domain containing 2
    'ENSMUSG00000034660', # Galp            galanin-like peptide
    'ENSMUSG00000034783', # Cd207           CD207 antigen
    'ENSMUSG00000034855', # Cxcl10          chemokine (C-X-C motif) ligand 10
    'ENSMUSG00000035042', # Ccl5            chemokine (C-C motif) ligand 5
    'ENSMUSG00000035086', # Becn1           beclin 1, autophagy related
    'ENSMUSG00000035235', # Trim13          tripartite motif-containing 13
    'ENSMUSG00000035279', # Ssc5d           scavenger receptor cysteine rich family, 5 domains
    'ENSMUSG00000035459', # Stab2           stabilin 2
    'ENSMUSG00000035623', # Rsf1            remodeling and spacing factor 1
    'ENSMUSG00000035692', # Isg15           ISG15 ubiquitin-like modifier
    'ENSMUSG00000035834', # Polr3g          polymerase (RNA) III (DNA directed) polypeptide G
    'ENSMUSG00000036216', # Leap2           liver-expressed antimicrobial peptide 2
    'ENSMUSG00000036499', # Eea1            early endosome antigen 1
    'ENSMUSG00000036908', # Unc93b1         unc-93 homolog B1 (C. elegans)
    'ENSMUSG00000036958', # Cst11           cystatin 11
    'ENSMUSG00000036986', # Pml             promyelocytic leukemia
    'ENSMUSG00000037071', # Scd1            stearoyl-Coenzyme A desaturase 1
    'ENSMUSG00000037157', # Il22ra1         interleukin 22 receptor, alpha 1
    'ENSMUSG00000037167', # Spaca5          sperm acrosome associated 5
    'ENSMUSG00000037202', # Prf1            perforin 1 (pore forming protein)
    'ENSMUSG00000037331', # Larp1           La ribonucleoprotein domain family, member 1
    'ENSMUSG00000037379', # Spon2           spondin 2, extracellular matrix protein
    'ENSMUSG00000037411', # Serpine1        serine (or cysteine) peptidase inhibitor, clade E, member 1
    'ENSMUSG00000037523', # Mavs            mitochondrial antiviral signaling protein
    'ENSMUSG00000037656', # Slc20a2         solute carrier family 20, member 2
    'ENSMUSG00000037780', # Mbl1            mannose-binding lectin (protein A) 1
    'ENSMUSG00000037790', # Defb7           defensin beta 7
    'ENSMUSG00000037921', # Ddx60           DEAD (Asp-Glu-Ala-Asp) box polypeptide 60
    'ENSMUSG00000038058', # Nod1            nucleotide-binding oligomerization domain containing 1
    'ENSMUSG00000038160', # Atg5            autophagy related 5
    'ENSMUSG00000038274', # Fau             Finkel-Biskis-Reilly murine sarcoma virus (FBR-MuSV) ubiquitously expressed (fox derived)
    'ENSMUSG00000038304', # Cd160           CD160 antigen
    'ENSMUSG00000038357', # Camp            cathelicidin antimicrobial peptide
    'ENSMUSG00000038467', # Chmp4b          charged multivesicular body protein 4B
    'ENSMUSG00000038628', # Polr3k          polymerase (RNA) III (DNA directed) polypeptide K
    'ENSMUSG00000038740', # Mvb12b          multivesicular body subunit 12B
    'ENSMUSG00000038745', # Nlrp6           NLR family, pyrin domain containing 6
    'ENSMUSG00000038859', # Baiap2l1        BAI1-associated protein 2-like 1
    'ENSMUSG00000038884', # A230050P20Rik   RIKEN cDNA A230050P20 gene
    'ENSMUSG00000039005', # Tlr4            toll-like receptor 4
    'ENSMUSG00000039046', # Usp6nl          USP6 N-terminal like
    'ENSMUSG00000039191', # Rbpj            recombination signal binding protein for immunoglobulin kappa J region
    'ENSMUSG00000039193', # Nlrc4           NLR family, CARD domain containing 4
    'ENSMUSG00000039236', # Isg20           interferon-stimulated protein
    'ENSMUSG00000039536', # Stau1           staufen (RNA binding protein) homolog 1 (Drosophila)
    'ENSMUSG00000039699', # Batf2           basic leucine zipper transcription factor, ATF-like 2
    'ENSMUSG00000039775', # Defb3           defensin beta 3
    'ENSMUSG00000039785', # Defb5           defensin beta 5
    'ENSMUSG00000039853', # Trim14          tripartite motif-containing 14
    'ENSMUSG00000039936', # Pik3cd          phosphatidylinositol 3-kinase catalytic delta polypeptide
    'ENSMUSG00000039952', # Dag1            dystroglycan 1
    'ENSMUSG00000040013', # Fkbp6           FK506 binding protein 6
    'ENSMUSG00000040033', # Stat2           signal transducer and activator of transcription 2
    'ENSMUSG00000040253', # Gbp7            guanylate binding protein 7
    'ENSMUSG00000040264', # Gbp2b           guanylate binding protein 2b
    'ENSMUSG00000040296', # Ddx58           DEAD (Asp-Glu-Ala-Asp) box polypeptide 58
    'ENSMUSG00000040314', # Ctsg            cathepsin G
    'ENSMUSG00000040325', # Vprbp           Vpr (HIV-1) binding protein
    'ENSMUSG00000040522', # Tlr8            toll-like receptor 8
    'ENSMUSG00000040613', # Apobec1         apolipoprotein B mRNA editing enzyme, catalytic polypeptide 1
    'ENSMUSG00000040627', # Aicda           activation-induced cytidine deaminase
    'ENSMUSG00000040952', # Rps19           ribosomal protein S19
    'ENSMUSG00000041000', # Trim62          tripartite motif-containing 62
    'ENSMUSG00000041135', # Ripk2           receptor (TNFRSF)-interacting serine-threonine kinase 2
    'ENSMUSG00000041247', # Lamp3           lysosomal-associated membrane protein 3
    'ENSMUSG00000041390', # Mdfic           MyoD family inhibitor domain containing
    'ENSMUSG00000041415', # Dicer1          dicer 1, ribonuclease type III
    'ENSMUSG00000041459', # Tardbp          TAR DNA binding protein
    'ENSMUSG00000041515', # Irf8            interferon regulatory factor 8
    'ENSMUSG00000041720', # Pi4ka           phosphatidylinositol 4-kinase, catalytic, alpha polypeptide
    'ENSMUSG00000041754', # Trem3           triggering receptor expressed on myeloid cells 3
    'ENSMUSG00000041827', # Oasl1           2'-5' oligoadenylate synthetase-like 1
    'ENSMUSG00000042244', # Pglyrp3         peptidoglycan recognition protein 3
    'ENSMUSG00000042250', # Pglyrp4         peptidoglycan recognition protein 4
    'ENSMUSG00000042265', # Trem1           triggering receptor expressed on myeloid cells 1
    'ENSMUSG00000042286', # Stab1           stabilin 1
    'ENSMUSG00000042333', # Tnfrsf14        tumor necrosis factor receptor superfamily, member 14 (herpesvirus entry mediator)
    'ENSMUSG00000042459', # Bpifa2          BPI fold containing family A, member 2
    'ENSMUSG00000042626', # Shc1            src homology 2 domain-containing transforming protein C1
    'ENSMUSG00000042632', # Pla2g6          phospholipase A2, group VI
    'ENSMUSG00000042677', # Zc3h12a         zinc finger CCCH type containing 12A
    'ENSMUSG00000042808', # Gpx2            glutathione peroxidase 2
    'ENSMUSG00000042845', # Wfdc12          WAP four-disulfide core domain 12
    'ENSMUSG00000042993', # Ifnk            interferon kappa
    'ENSMUSG00000043279', # Trim56          tripartite motif-containing 56
    'ENSMUSG00000043787', # Defb12          defensin beta 12
    'ENSMUSG00000044222', # Defb13          defensin beta 13
    'ENSMUSG00000044249', # Defb29          defensin beta 29
    'ENSMUSG00000044499', # Hs3st5          heparan sulfate (glucosamine) 3-O-sulfotransferase 5
    'ENSMUSG00000044583', # Tlr7            toll-like receptor 7
    'ENSMUSG00000044743', # Defb10          defensin beta 10
    'ENSMUSG00000044748', # Defb1           defensin beta 1
    'ENSMUSG00000044786', # Zfp36           zinc finger protein 36
    'ENSMUSG00000044827', # Tlr1            toll-like receptor 1
    'ENSMUSG00000044863', # Defb36          defensin beta 36
    'ENSMUSG00000045322', # Tlr9            toll-like receptor 9
    'ENSMUSG00000045337', # Defb11          defensin beta 11
    'ENSMUSG00000045364', # Ifne            interferon epsilon
    'ENSMUSG00000045382', # Cxcr4           chemokine (C-X-C motif) receptor 4
    'ENSMUSG00000045827', # Serpinb9        serine (or cysteine) peptidase inhibitor, clade B, member 9
    'ENSMUSG00000045932', # Ifit2           interferon-induced protein with tetratricopeptide repeats 2
    'ENSMUSG00000046354', # Defb14          defensin beta 14
    'ENSMUSG00000046718', # Bst2            bone marrow stromal cell antigen 2
    'ENSMUSG00000047123', # Ticam1          toll-like receptor adaptor molecule 1
    'ENSMUSG00000047246', # Hist1h2be       histone cluster 1, H2be
    'ENSMUSG00000047390', # Defb9           defensin beta 9
    'ENSMUSG00000047517', # Dmbt1           deleted in malignant brain tumors 1
    'ENSMUSG00000047638', # Nr1h4           nuclear receptor subfamily 1, group H, member 4
    'ENSMUSG00000047767', # Atg16l2         autophagy related 16-like 2 (S. cerevisiae)
    'ENSMUSG00000047810', # Ccdc88b         coiled-coil domain containing 88B
    'ENSMUSG00000048500', # Defb15          defensin beta 15
    'ENSMUSG00000048806', # Ifnb1           interferon beta 1, fibroblast
    'ENSMUSG00000049130', # C5ar1           complement component 5a receptor 1
    'ENSMUSG00000049560', # Defb20          defensin beta 20
    'ENSMUSG00000049709', # Nlrp10          NLR family, pyrin domain containing 10
    'ENSMUSG00000050377', # Il31ra          interleukin 31 receptor A
    'ENSMUSG00000050440', # Hamp            hepcidin antimicrobial peptide
    'ENSMUSG00000050645', # Defb19          defensin beta 19
    'ENSMUSG00000050747', # Trim15          tripartite motif-containing 15
    'ENSMUSG00000050756', # Defb6           defensin beta 6
    'ENSMUSG00000051256', # Jagn1           jagunal homolog 1
    'ENSMUSG00000051439', # Cd14            CD14 antigen
    'ENSMUSG00000051457', # Spn             sialophorin
    'ENSMUSG00000051498', # Tlr6            toll-like receptor 6
    'ENSMUSG00000051675', # Trim32          tripartite motif-containing 32
    'ENSMUSG00000051695', # Pcbp1           poly(rC) binding protein 1
    'ENSMUSG00000051769', # Wfdc15a         WAP four-disulfide core domain 15A
    'ENSMUSG00000051969', # Tlr11           toll-like receptor 11
    'ENSMUSG00000052435', # Cebpe           CCAAT/enhancer binding protein (C/EBP), epsilon
    'ENSMUSG00000052554', # Defb34          defensin beta 34
    'ENSMUSG00000052593', # Adam17          a disintegrin and metallopeptidase domain 17
    'ENSMUSG00000052684', # Jun             jun proto-oncogene
    'ENSMUSG00000052776', # Oas1a           2'-5' oligoadenylate synthetase 1A
    'ENSMUSG00000052922', # Bpi             bactericidal permeablility increasing protein
    'ENSMUSG00000053119', # Chmp3           charged multivesicular body protein 3
    'ENSMUSG00000053175', # Bcl3            B cell leukemia/lymphoma 3
    'ENSMUSG00000053184', # Spaca3          sperm acrosome associated 3
    'ENSMUSG00000053318', # Slamf8          SLAM family member 8
    'ENSMUSG00000053678', # Defb40          defensin beta 40
    'ENSMUSG00000053695', # Defb37          defensin beta 37
    'ENSMUSG00000053790', # Defb38          defensin beta 38
    'ENSMUSG00000053977', # Cd8a            CD8 antigen, alpha chain
    'ENSMUSG00000054072', # Iigp1           interferon inducible GTPase 1
    'ENSMUSG00000054385', # Ceacam2         carcinoembryonic antigen-related cell adhesion molecule 2
    'ENSMUSG00000054455', # Vapb            vesicle-associated membrane protein, associated protein B and C
    'ENSMUSG00000054717', # Hmgb2           high mobility group box 2
    'ENSMUSG00000054763', # Defb42          defensin beta 42
    'ENSMUSG00000055024', # Ep300           E1A binding protein p300
    'ENSMUSG00000055065', # Ddx17           DEAD (Asp-Glu-Ala-Asp) box polypeptide 17
    'ENSMUSG00000055170', # Ifng            interferon gamma
    'ENSMUSG00000055204', # Ankrd17         ankyrin repeat domain 17
    'ENSMUSG00000055301', # Adh7            alcohol dehydrogenase 7 (class IV), mu or sigma polypeptide
    'ENSMUSG00000055447', # Cd47            CD47 antigen (Rh-related antigen, integrin-associated signal transducer)
    'ENSMUSG00000055994', # Nod2            nucleotide-binding oligomerization domain containing 2
    'ENSMUSG00000056076', # Eif3b           eukaryotic translation initiation factor 3, subunit B
    'ENSMUSG00000056130', # Ticam2          toll-like receptor adaptor molecule 2
    'ENSMUSG00000056144', # Trim34a         tripartite motif-containing 34A
    'ENSMUSG00000056201', # Cfl1            cofilin 1, non-muscle
    'ENSMUSG00000056501', # Cebpb           CCAAT/enhancer binding protein (C/EBP), beta
    'ENSMUSG00000056544', # Defb21          defensin beta 21
    'ENSMUSG00000056851', # Pcbp2           poly(rC) binding protein 2
    'ENSMUSG00000056978', # Hamp2           hepcidin antimicrobial peptide 2
    'ENSMUSG00000057329', # Bcl2            B cell leukemia/lymphoma 2
    'ENSMUSG00000057666', # Gapdh           glyceraldehyde-3-phosphate dehydrogenase
    'ENSMUSG00000057948', # Unc13d          unc-13 homolog D (C. elegans)
    'ENSMUSG00000057982', # Zfp809          zinc finger protein 809
    'ENSMUSG00000058052', # Defb35          defensin beta 35
    'ENSMUSG00000058063', # Trim31          tripartite motif-containing 31
    'ENSMUSG00000058354', # Krt6a           keratin 6A
    'ENSMUSG00000058385', # Hist1h2bg       histone cluster 1, H2bg
    'ENSMUSG00000058568', # Defb50          defensin beta 50
    'ENSMUSG00000058600', # Rpl30           ribosomal protein L30
    'ENSMUSG00000058715', # Fcer1g          Fc receptor, IgE, high affinity I, gamma polypeptide
    'ENSMUSG00000059128', # Ifnl2           interferon lambda 2
    'ENSMUSG00000059230', # Defb4           defensin beta 4
    'ENSMUSG00000059552', # Trp53           transformation related protein 53
    'ENSMUSG00000060070', # Defa26          defensin, alpha, 26
    'ENSMUSG00000060288', # Ppih            peptidyl prolyl isomerase H
    'ENSMUSG00000060591', # Ifitm2          interferon induced transmembrane protein 2
    'ENSMUSG00000060615', # Ang4            angiogenin, ribonuclease A family, member 4
    'ENSMUSG00000060747', # Ifnl3           interferon lambda 3
    'ENSMUSG00000061232', # H2-K1           histocompatibility 2, K1, K region
    'ENSMUSG00000061286', # Exosc5          exosome component 5
    'ENSMUSG00000061298', # Agbl4           ATP/GTP binding protein-like 4
    'ENSMUSG00000061847', # Defb39          defensin beta 39
    'ENSMUSG00000062124', # Defb45          defensin beta 45
    'ENSMUSG00000062157', # Ifnlr1          interferon lambda receptor 1
    'ENSMUSG00000062210', # Tnfaip8         tumor necrosis factor, alpha-induced protein 8
    'ENSMUSG00000062300', # Nectin2         nectin cell adhesion molecule 2
    'ENSMUSG00000062488', # Ifit3b          interferon-induced protein with tetratricopeptide repeats 3B
    'ENSMUSG00000062524', # Ncr1            natural cytotoxicity triggering receptor 1
    'ENSMUSG00000062545', # Tlr12           toll-like receptor 12
    'ENSMUSG00000062604', # Srpk2           serine/arginine-rich protein specific kinase 2
    'ENSMUSG00000062727', # Hist1h2bk       histone cluster 1, H2bk
    'ENSMUSG00000063268', # Parp10          poly (ADP-ribose) polymerase family, member 10
    'ENSMUSG00000063376', # Ifna13          interferon alpha 13
    'ENSMUSG00000063856', # Gpx1            glutathione peroxidase 1
    'ENSMUSG00000064140', # Trim38          tripartite motif-containing 38
    'ENSMUSG00000064213', # Defa24          defensin, alpha, 24
    'ENSMUSG00000065987', # Cd209b          CD209b antigen
    'ENSMUSG00000066108', # Muc5b           mucin 5, subtype B, tracheobronchial
    'ENSMUSG00000066258', # Trim12a         tripartite motif-containing 12A
    'ENSMUSG00000066278', # Vps37b          vacuolar protein sorting 37B
    'ENSMUSG00000066568', # Lsm14a          LSM14A mRNA processing body assembly factor
    'ENSMUSG00000066800', # Rnasel          ribonuclease L (2', 5'-oligoisoadenylate synthetase-dependent)
    'ENSMUSG00000067149', # Jchain          immunoglobulin joining chain
    'ENSMUSG00000067212', # H2-T23          histocompatibility 2, T region locus 23
    'ENSMUSG00000067297', # Ifit1bl2        interferon induced protein with tetratricopeptide repeats 1B like 2
    'ENSMUSG00000067773', # Defb41          defensin beta 41
    'ENSMUSG00000067847', # Romo1           reactive oxygen species modulator 1
    'ENSMUSG00000068220', # Lgals1          lectin, galactose binding, soluble 1
    'ENSMUSG00000068854', # Hist2h2be       histone cluster 2, H2be
    'ENSMUSG00000068882', # Ssb             Sjogren syndrome antigen B
    'ENSMUSG00000069184', # Zfp72           zinc finger protein 72
    'ENSMUSG00000069268', # Hist1h2bf       histone cluster 1, H2bf
    'ENSMUSG00000069515', # Lyz1            lysozyme 1
    'ENSMUSG00000069516', # Lyz2            lysozyme 2
    'ENSMUSG00000069830', # Nlrp1a          NLR family, pyrin domain containing 1A
    'ENSMUSG00000069874', # Irgm2           immunity-related GTPase family M member 2
    'ENSMUSG00000070034', # Sp110           Sp110 nuclear body protein
    'ENSMUSG00000070319', # Eif3g           eukaryotic translation initiation factor 3, subunit G
    'ENSMUSG00000070563', # Spaca4          sperm acrosome associated 4
    'ENSMUSG00000070583', # Fv1             Friend virus susceptibility 1
    'ENSMUSG00000070777', # Ceacam20        carcinoembryonic antigen-related cell adhesion molecule 20
    'ENSMUSG00000070904', # Ifna4           interferon alpha 4
    'ENSMUSG00000070934', # Rraga           Ras-related GTP binding A
    'ENSMUSG00000071203', # Naip5           NLR family, apoptosis inhibitory protein 5
    'ENSMUSG00000071356', # Reg3b           regenerating islet-derived 3 beta
    'ENSMUSG00000071866', # Ppia            peptidylprolyl isomerase A
    'ENSMUSG00000072244', # Trim6           tripartite motif-containing 6
    'ENSMUSG00000073400', # Trim10          tripartite motif-containing 10
    'ENSMUSG00000073735', # Defb18          defensin beta 18
    'ENSMUSG00000073811', # Ifna12          interferon alpha 12
    'ENSMUSG00000074272', # Ceacam1         carcinoembryonic antigen-related cell adhesion molecule 1
    'ENSMUSG00000074439', # Defa5           defensin, alpha, 5
    'ENSMUSG00000074440', # Defa3           defensin, alpha, 3
    'ENSMUSG00000074442', # Defa31          defensin, alpha, 31
    'ENSMUSG00000074443', # Defa22          defensin, alpha, 22
    'ENSMUSG00000074447', # Defa21          defensin, alpha, 21
    'ENSMUSG00000074454', # Defb33          defensin beta 33
    'ENSMUSG00000074595', # Wfdc6a          WAP four-disulfide core domain 6A
    'ENSMUSG00000074678', # Defb25          defensin beta 25
    'ENSMUSG00000074679', # Defb28          defensin beta 28
    'ENSMUSG00000074680', # Defb26          defensin beta 26
    'ENSMUSG00000074681', # Defb23          defensin beta 23
    'ENSMUSG00000074896', # Ifit3           interferon-induced protein with tetratricopeptide repeats 3
    'ENSMUSG00000075370', # Igll1           immunoglobulin lambda-like polypeptide 1
    'ENSMUSG00000075571', # Defb30          defensin beta 30
    'ENSMUSG00000075572', # Defb43          defensin beta 43
    'ENSMUSG00000078354', # Ifna2           interferon alpha 2
    'ENSMUSG00000078566', # Bnip3           BCL2/adenovirus E1B interacting protein 3
    'ENSMUSG00000078908', # Mon1b           MON1 homolog B, secretory traffciking associated
    'ENSMUSG00000078942', # Naip6           NLR family, apoptosis inhibitory protein 6
    'ENSMUSG00000078945', # Naip2           NLR family, apoptosis inhibitory protein 2
    'ENSMUSG00000079164', # Tlr5            toll-like receptor 5
    'ENSMUSG00000079227', # Ccr5            chemokine (C-C motif) receptor 5
    'ENSMUSG00000079339', # Ifit1bl1        interferon induced protein with tetratricpeptide repeats 1B like 1
    'ENSMUSG00000079362', # Gm43302         None
    'ENSMUSG00000079477', # Rab7            RAB7, member RAS oncogene family
    'ENSMUSG00000079563', # Pglyrp2         peptidoglycan recognition protein 2
    'ENSMUSG00000079614', # Seh1l           SEH1-like (S. cerevisiae
    'ENSMUSG00000079641', # Rpl39           ribosomal protein L39
    'ENSMUSG00000079842', # Spag11a         sperm associated antigen 11A
    'ENSMUSG00000087260', # Lamtor5         late endosomal/lysosomal adaptor, MAPK and MTOR activator 5
    'ENSMUSG00000090485', # Gm17416         None
    'ENSMUSG00000094338', # Hist1h2bl       histone cluster 1, H2bl
    'ENSMUSG00000094687', # Defa25          defensin, alpha, 25
    'ENSMUSG00000095066', # Defa20          defensin, alpha, 20
    'ENSMUSG00000095270', # Ifna9           interferon alpha 9
    'ENSMUSG00000095498', # Ifna1           interferon alpha 1
    'ENSMUSG00000096295', # Defa2           defensin, alpha, 2
    'ENSMUSG00000100549', # Ifna11          interferon alpha 11
    'ENSMUSG00000101252', # Ifna6           interferon alpha 6
    'ENSMUSG00000104713', # Gbp6            guanylate binding protein 6
    'ENSMUSG00000105096', # Gbp10           guanylate-binding protein 10
    'ENSMUSG00000109901', # Chmp1b          charged multivesicular body protein 1B
])
