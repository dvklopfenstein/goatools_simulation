"""Genes in immune.

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

#pylint: disable=too-many-lines

GENES = set([ # 2092 items
    'ENSMUSG00000000120', # Ngfr            nerve growth factor receptor (TNFR superfamily, member 16)
    'ENSMUSG00000000127', # Fer             fer (fms/fps related) protein kinase
    'ENSMUSG00000000134', # Tfe3            transcription factor E3
    'ENSMUSG00000000157', # Itgb2l          integrin beta 2-like
    'ENSMUSG00000000215', # Ins2            insulin II
    'ENSMUSG00000000244', # Tspan32         tetraspanin 32
    'ENSMUSG00000000266', # Mid2            midline 2
    'ENSMUSG00000000275', # Trim25          tripartite motif-containing 25
    'ENSMUSG00000000290', # Itgb2           integrin beta 2
    'ENSMUSG00000000303', # Cdh1            cadherin 1
    'ENSMUSG00000000317', # Bcl6b           B cell CLL/lymphoma 6, member B
    'ENSMUSG00000000320', # Alox12          arachidonate 12-lipoxygenase
    'ENSMUSG00000000386', # Mx1             MX dynamin-like GTPase 1
    'ENSMUSG00000000402', # Egfl6           EGF-like-domain, multiple 6
    'ENSMUSG00000000409', # Lck             lymphocyte protein tyrosine kinase
    'ENSMUSG00000000435', # Myf5            myogenic factor 5
    'ENSMUSG00000000440', # Pparg           peroxisome proliferator activated receptor gamma
    'ENSMUSG00000000489', # Pdgfb           platelet derived growth factor, B polypeptide
    'ENSMUSG00000000530', # Acvrl1          activin A receptor, type II-like 1
    'ENSMUSG00000000555', # Itga5           integrin alpha 5 (fibronectin receptor alpha)
    'ENSMUSG00000000562', # Adora3          adenosine A3 receptor
    'ENSMUSG00000000567', # Sox9            SRY (sex determining region Y)-box 9
    'ENSMUSG00000000631', # Myo18a          myosin XVIIIA
    'ENSMUSG00000000693', # Loxl3           lysyl oxidase-like 3
    'ENSMUSG00000000706', # Btn1a1          butyrophilin, subfamily 1, member A1
    'ENSMUSG00000000711', # Rab5b           RAB5B, member RAS oncogene family
    'ENSMUSG00000000724', # Cryba1          crystallin, beta A1
    'ENSMUSG00000000731', # Aire            autoimmune regulator (autoimmune polyendocrinopathy candidiasis ectodermal dystrophy)
    'ENSMUSG00000000732', # Icosl           icos ligand
    'ENSMUSG00000000738', # Spg7            spastic paraplegia 7 homolog (human)
    'ENSMUSG00000000776', # Polr3d          polymerase (RNA) III (DNA directed) polypeptide D
    'ENSMUSG00000000782', # Tcf7            transcription factor 7, T cell specific
    'ENSMUSG00000000787', # Ddx3x           DEAD/H (Asp-Glu-Ala-Asp/His) box polypeptide 3, X-linked
    'ENSMUSG00000000791', # Il12rb1         interleukin 12 receptor, beta 1
    'ENSMUSG00000000817', # Fasl            Fas ligand (TNF superfamily, member 6)
    'ENSMUSG00000000861', # Bcl11a          B cell CLL/lymphoma 11A (zinc finger protein)
    'ENSMUSG00000000869', # Il4             interleukin 4
    'ENSMUSG00000000889', # Dbh             dopamine beta hydroxylase
    'ENSMUSG00000000903', # Vpreb3          pre-B lymphocyte gene 3
    'ENSMUSG00000000957', # Mmp14           matrix metallopeptidase 14 (membrane-inserted)
    'ENSMUSG00000000982', # Ccl3            chemokine (C-C motif) ligand 3
    'ENSMUSG00000001016', # Ilf2            interleukin enhancer binding factor 2
    'ENSMUSG00000001034', # Mapk7           mitogen-activated protein kinase 7
    'ENSMUSG00000001123', # Lgals9          lectin, galactose binding, soluble 9
    'ENSMUSG00000001128', # Cfp             complement factor properdin
    'ENSMUSG00000001131', # Timp1           tissue inhibitor of metalloproteinase 1
    'ENSMUSG00000001150', # Mcm3ap          minichromosome maintenance complex component 3 associated protein
    'ENSMUSG00000001281', # Itgb7           integrin beta 7
    'ENSMUSG00000001300', # Efnb2           ephrin B2
    'ENSMUSG00000001348', # Acp5            acid phosphatase 5, tartrate resistant
    'ENSMUSG00000001366', # Fbxo9           f-box protein 9
    'ENSMUSG00000001444', # Tbx21           T-box 21
    'ENSMUSG00000001506', # Col1a1          collagen, type I, alpha 1
    'ENSMUSG00000001507', # Itga3           integrin alpha 3
    'ENSMUSG00000001583', # Tnk1            tyrosine kinase, non-receptor, 1
    'ENSMUSG00000001729', # Akt1            thymoma viral proto-oncogene 1
    'ENSMUSG00000001741', # Il16            interleukin 16
    'ENSMUSG00000001761', # Smo             smoothened, frizzled class receptor
    'ENSMUSG00000001847', # Rac1            RAS-related C3 botulinum substrate 1
    'ENSMUSG00000001930', # Vwf             Von Willebrand factor
    'ENSMUSG00000001942', # Siae            sialic acid acetylesterase
    'ENSMUSG00000002015', # Bcap31          B cell receptor associated protein 31
    'ENSMUSG00000002052', # Supt6           suppressor of Ty 6
    'ENSMUSG00000002057', # Foxn1           forkhead box N1
    'ENSMUSG00000002059', # Rab34           RAB34, member RAS oncogene family
    'ENSMUSG00000002108', # Nr1h3           nuclear receptor subfamily 1, group H, member 3
    'ENSMUSG00000002111', # Spi1            spleen focus forming virus (SFFV) proviral integration oncogene
    'ENSMUSG00000002147', # Stat6           signal transducer and activator of transcription 6
    'ENSMUSG00000002221', # Paxip1          PAX interacting (with transcription-activation domain) protein 1
    'ENSMUSG00000002308', # Cd320           CD320 antigen
    'ENSMUSG00000002326', # Gmpr2           guanosine monophosphate reductase 2
    'ENSMUSG00000002413', # Braf            Braf transforming gene
    'ENSMUSG00000002496', # Tsc2            tuberous sclerosis 2
    'ENSMUSG00000002602', # Axl             AXL receptor tyrosine kinase
    'ENSMUSG00000002603', # Tgfb1           transforming growth factor, beta 1
    'ENSMUSG00000002633', # Shh             sonic hedgehog
    'ENSMUSG00000002688', # Prkd1           protein kinase D1
    'ENSMUSG00000002699', # Lcp2            lymphocyte cytosolic protein 2
    'ENSMUSG00000002778', # Kdelr1          KDEL (Lys-Asp-Glu-Leu) endoplasmic reticulum protein retention receptor 1
    'ENSMUSG00000002799', # Jag2            jagged 2
    'ENSMUSG00000002897', # Il17ra          interleukin 17 receptor A
    'ENSMUSG00000002900', # Lamb1           laminin B1
    'ENSMUSG00000002944', # Cd36            CD36 antigen
    'ENSMUSG00000002948', # Map2k7          None
    'ENSMUSG00000002981', # Clptm1          cleft lip and palate associated transmembrane protein 1
    'ENSMUSG00000002983', # Relb            avian reticuloendotheliosis viral (v-rel) oncogene related B
    'ENSMUSG00000003032', # Klf4            Kruppel-like factor 4 (gut)
    'ENSMUSG00000003051', # Elf3            E74-like factor 3
    'ENSMUSG00000003068', # Stk11           serine/threonine kinase 11
    'ENSMUSG00000003070', # Efna2           ephrin A2
    'ENSMUSG00000003184', # Irf3            interferon regulatory factor 3
    'ENSMUSG00000003269', # Cyth2           cytohesin 2
    'ENSMUSG00000003283', # Hck             hemopoietic cell kinase
    'ENSMUSG00000003352', # Cacnb3          calcium channel, voltage-dependent, beta 3 subunit
    'ENSMUSG00000003379', # Cd79a           CD79A antigen (immunoglobulin-associated alpha)
    'ENSMUSG00000003411', # Rab3b           RAB3B, member RAS oncogene family
    'ENSMUSG00000003476', # Crhr2           corticotropin releasing hormone receptor 2
    'ENSMUSG00000003505', # Psg18           pregnancy specific glycoprotein 18
    'ENSMUSG00000003518', # Dusp3           dual specificity phosphatase 3 (vaccinia virus phosphatase VH1-related)
    'ENSMUSG00000003534', # Ddr1            discoidin domain receptor family, member 1
    'ENSMUSG00000003810', # Mast2           microtubule associated serine/threonine kinase 2
    'ENSMUSG00000003814', # Calr            calreticulin
    'ENSMUSG00000003847', # Nfat5           nuclear factor of activated T cells 5
    'ENSMUSG00000003873', # Bax             BCL2-associated X protein
    'ENSMUSG00000003882', # Il7r            interleukin 7 receptor
    'ENSMUSG00000003934', # Efnb3           ephrin B3
    'ENSMUSG00000004040', # Stat3           signal transducer and activator of transcription 3
    'ENSMUSG00000004043', # Stat5a          signal transducer and activator of transcription 5A
    'ENSMUSG00000004069', # Dnaja3          DnaJ heat shock protein family (Hsp40) member A3
    'ENSMUSG00000004266', # Ptpn6           protein tyrosine phosphatase, non-receptor type 6
    'ENSMUSG00000004296', # Il12b           interleukin 12b
    'ENSMUSG00000004364', # Cul3            cullin 3
    'ENSMUSG00000004415', # Col26a1         collagen, type XXVI, alpha 1
    'ENSMUSG00000004508', # Gab2            growth factor receptor bound protein 2-associated protein 2
    'ENSMUSG00000004530', # Coro1c          coronin, actin binding protein 1C
    'ENSMUSG00000004540', # Psg17           pregnancy specific glycoprotein 17
    'ENSMUSG00000004552', # Ctse            cathepsin E
    'ENSMUSG00000004558', # Ndrg2           N-myc downstream regulated gene 2
    'ENSMUSG00000004626', # Stxbp2          syntaxin binding protein 2
    'ENSMUSG00000004677', # Myo9b           myosin IXb
    'ENSMUSG00000004698', # Hdac9           histone deacetylase 9
    'ENSMUSG00000004707', # Ly9             lymphocyte antigen 9
    'ENSMUSG00000004709', # Cd244           CD244 natural killer cell receptor 2B4
    'ENSMUSG00000004730', # Adgre1          adhesion G protein-coupled receptor E1
    'ENSMUSG00000004791', # Pgf             placental growth factor
    'ENSMUSG00000004814', # Ccl24           chemokine (C-C motif) ligand 24
    'ENSMUSG00000004837', # Grap            GRB2-related adaptor protein
    'ENSMUSG00000004864', # Mapk13          mitogen-activated protein kinase 13
    'ENSMUSG00000004933', # Matk            megakaryocyte-associated tyrosine kinase
    'ENSMUSG00000004936', # Map2k1          mitogen-activated protein kinase kinase 1
    'ENSMUSG00000004948', # Zp3             zona pellucida glycoprotein 3
    'ENSMUSG00000004951', # Hspb1           heat shock protein 1
    'ENSMUSG00000005057', # Sh2b2           SH2B adaptor protein 2
    'ENSMUSG00000005087', # Cd44            CD44 antigen
    'ENSMUSG00000005102', # Eif2ak4         eukaryotic translation initiation factor 2 alpha kinase 4
    'ENSMUSG00000005103', # Wdr1            WD repeat domain 1
    'ENSMUSG00000005125', # Ndrg1           N-myc downstream regulated gene 1
    'ENSMUSG00000005161', # Prdx2           peroxiredoxin 2
    'ENSMUSG00000005262', # Ufd1l           ubiquitin fusion degradation 1 like
    'ENSMUSG00000005267', # Zfp287          zinc finger protein 287
    'ENSMUSG00000005268', # Prlr            prolactin receptor
    'ENSMUSG00000005320', # Fgfr4           fibroblast growth factor receptor 4
    'ENSMUSG00000005339', # Fcer1a          Fc receptor, IgE, high affinity I, alpha polypeptide
    'ENSMUSG00000005364', # Il5ra           interleukin 5 receptor, alpha
    'ENSMUSG00000005370', # Msh6            mutS homolog 6
    'ENSMUSG00000005397', # Nid1            nidogen 1
    'ENSMUSG00000005413', # Hmox1           heme oxygenase 1
    'ENSMUSG00000005465', # Il27ra          interleukin 27 receptor, alpha
    'ENSMUSG00000005533', # Igf1r           insulin-like growth factor I receptor
    'ENSMUSG00000005534', # Insr            insulin receptor
    'ENSMUSG00000005540', # Fcer2a          Fc receptor, IgE, low affinity II, alpha polypeptide
    'ENSMUSG00000005566', # Trim28          tripartite motif-containing 28
    'ENSMUSG00000005583', # Mef2c           myocyte enhancer factor 2C
    'ENSMUSG00000005672', # Kit             KIT proto-oncogene receptor tyrosine kinase
    'ENSMUSG00000005681', # Apoa2           apolipoprotein A-II
    'ENSMUSG00000005696', # Sh2d1a          SH2 domain containing 1A
    'ENSMUSG00000005763', # Cd247           CD247 antigen
    'ENSMUSG00000005804', # Bloc1s6         biogenesis of lysosomal organelles complex-1, subunit 6, pallidin
    'ENSMUSG00000005824', # Tnfsf14         tumor necrosis factor (ligand) superfamily, member 14
    'ENSMUSG00000005836', # Gata6           GATA binding protein 6
    'ENSMUSG00000005871', # Apc             adenomatosis polyposis coli
    'ENSMUSG00000005947', # Itgae           integrin alpha E, epithelial-associated
    'ENSMUSG00000005951', # Shpk            sedoheptulokinase
    'ENSMUSG00000005952', # Trpv1           transient receptor potential cation channel, subfamily V, member 1
    'ENSMUSG00000005958', # Ephb3           Eph receptor B3
    'ENSMUSG00000006014', # Prg4            proteoglycan 4 (megakaryocyte stimulating factor, articular superficial zone protein)
    'ENSMUSG00000006310', # Zbtb32          zinc finger and BTB domain containing 32
    'ENSMUSG00000006342', # Susd2           sushi domain containing 2
    'ENSMUSG00000006344', # Ggt5            gamma-glutamyltransferase 5
    'ENSMUSG00000006345', # Ggt1            gamma-glutamyltransferase 1
    'ENSMUSG00000006362', # Cbfa2t3         core-binding factor, runt domain, alpha subunit 2, translocated to, 3 (human)
    'ENSMUSG00000006369', # Fbln1           fibulin 1
    'ENSMUSG00000006386', # Tek             endothelial-specific receptor tyrosine kinase
    'ENSMUSG00000006389', # Mpl             myeloproliferative leukemia virus oncogene
    'ENSMUSG00000006445', # Epha2           Eph receptor A2
    'ENSMUSG00000006519', # Cyba            cytochrome b-245, alpha polypeptide
    'ENSMUSG00000006538', # Ihh             Indian hedgehog
    'ENSMUSG00000006574', # Slc4a1          solute carrier family 4 (anion exchanger), member 1
    'ENSMUSG00000006611', # Hfe             hemochromatosis
    'ENSMUSG00000006699', # Cdc42           cell division cycle 42
    'ENSMUSG00000006705', # Pknox1          Pbx/knotted 1 homeobox
    'ENSMUSG00000006724', # Cyp27b1         cytochrome P450, family 27, subfamily b, polypeptide 1
    'ENSMUSG00000006800', # Sulf2           sulfatase 2
    'ENSMUSG00000006932', # Ctnnb1          catenin (cadherin associated protein), beta 1
    'ENSMUSG00000006958', # Chrd            chordin
    'ENSMUSG00000007655', # Cav1            caveolin 1, caveolae protein
    'ENSMUSG00000007659', # Bcl2l1          BCL2-like 1
    'ENSMUSG00000007805', # Twist2          twist basic helix-loop-helix transcription factor 2
    'ENSMUSG00000007815', # Rhoa            ras homolog family member A
    'ENSMUSG00000007817', # Zmiz1           zinc finger, MIZ-type containing 1
    'ENSMUSG00000007836', # Hnrnpa0         heterogeneous nuclear ribonucleoprotein A0
    'ENSMUSG00000008193', # Spib            Spi-B transcription factor (Spi-1/PU.1 related)
    'ENSMUSG00000008318', # Relt            RELT tumor necrosis factor receptor
    'ENSMUSG00000008450', # Nutf2           nuclear transport factor 2
    'ENSMUSG00000008690', # Ncaph2          non-SMC condensin II complex, subunit H2
    'ENSMUSG00000008734', # Gprc5b          G protein-coupled receptor, family C, group 5, member B
    'ENSMUSG00000008845', # Cd163           CD163 antigen
    'ENSMUSG00000008855', # Hdac5           histone deacetylase 5
    'ENSMUSG00000008999', # Bmp7            bone morphogenetic protein 7
    'ENSMUSG00000009073', # Nf2             neurofibromin 2
    'ENSMUSG00000009185', # Ccl8            chemokine (C-C motif) ligand 8
    'ENSMUSG00000009281', # Rarres2         retinoic acid receptor responder (tazarotene induced) 2
    'ENSMUSG00000009292', # Trpm2           transient receptor potential cation channel, subfamily M, member 2
    'ENSMUSG00000009350', # Mpo             myeloperoxidase
    'ENSMUSG00000009376', # Met             met proto-oncogene
    'ENSMUSG00000009580', # Odam            odontogenic, ameloblast asssociated
    'ENSMUSG00000009585', # Apobec3         apolipoprotein B mRNA editing enzyme, catalytic polypeptide 3
    'ENSMUSG00000009681', # Bcr             breakpoint cluster region
    'ENSMUSG00000009900', # Wnt3a           wingless-type MMTV integration site family, member 3A
    'ENSMUSG00000010047', # Hyal2           hyaluronoglucosaminidase 2
    'ENSMUSG00000010051', # Hyal1           hyaluronoglucosaminidase 1
    'ENSMUSG00000010054', # Tusc2           tumor suppressor candidate 2
    'ENSMUSG00000010142', # Tnfrsf13b       tumor necrosis factor receptor superfamily, member 13b
    'ENSMUSG00000010435', # Spaca7          sperm acrosome associated 7
    'ENSMUSG00000010517', # Faf1            Fas-associated factor 1
    'ENSMUSG00000010609', # Psen2           presenilin 2
    'ENSMUSG00000010751', # Tnfrsf22        tumor necrosis factor receptor superfamily, member 22
    'ENSMUSG00000013236', # Ptprs           protein tyrosine phosphatase, receptor type, S
    'ENSMUSG00000013418', # B4galnt2        beta-1,4-N-acetyl-galactosaminyl transferase 2
    'ENSMUSG00000013584', # Aldh1a2         aldehyde dehydrogenase family 1, subfamily A2
    'ENSMUSG00000013663', # Pten            phosphatase and tensin homolog
    'ENSMUSG00000013707', # Tnfaip8l2       tumor necrosis factor, alpha-induced protein 8-like 2
    'ENSMUSG00000014158', # Trpv4           transient receptor potential cation channel, subfamily V, member 4
    'ENSMUSG00000014361', # Mertk           c-mer proto-oncogene tyrosine kinase
    'ENSMUSG00000014444', # Piezo1          piezo-type mechanosensitive ion channel component 1
    'ENSMUSG00000014453', # Blk             B lymphoid kinase
    'ENSMUSG00000014542', # Clec4f          C-type lectin domain family 4, member f
    'ENSMUSG00000014599', # Csf1            colony stimulating factor 1 (macrophage)
    'ENSMUSG00000014773', # Dll1            delta-like 1 (Drosophila)
    'ENSMUSG00000014932', # Yes1            YES proto-oncogene 1, Src family tyrosine kinase
    'ENSMUSG00000014956', # Ppp1cb          protein phosphatase 1, catalytic subunit, beta isoform
    'ENSMUSG00000015053', # Gata2           GATA binding protein 2
    'ENSMUSG00000015083', # C8g             complement component 8, gamma polypeptide
    'ENSMUSG00000015085', # Entpd2          ectonucleoside triphosphate diphosphohydrolase 2
    'ENSMUSG00000015217', # Hmgb3           high mobility group box 3
    'ENSMUSG00000015314', # Slamf6          SLAM family member 6
    'ENSMUSG00000015316', # Slamf1          signaling lymphocytic activation molecule family member 1
    'ENSMUSG00000015337', # Endog           endonuclease G
    'ENSMUSG00000015340', # Cybb            cytochrome b-245, beta polypeptide
    'ENSMUSG00000015355', # Cd48            CD48 antigen
    'ENSMUSG00000015396', # Cd83            CD83 antigen
    'ENSMUSG00000015437', # Gzmb            granzyme B
    'ENSMUSG00000015452', # Ager            advanced glycosylation end product-specific receptor
    'ENSMUSG00000015522', # Arnt            aryl hydrocarbon receptor nuclear translocator
    'ENSMUSG00000015533', # Itga2           integrin alpha 2
    'ENSMUSG00000015568', # Lpl             lipoprotein lipase
    'ENSMUSG00000015605', # Srf             serum response factor
    'ENSMUSG00000015619', # Gata3           GATA binding protein 3
    'ENSMUSG00000015647', # Lama5           laminin, alpha 5
    'ENSMUSG00000015656', # Hspa8           heat shock protein 8
    'ENSMUSG00000015766', # Eps8            epidermal growth factor receptor pathway substrate 8
    'ENSMUSG00000015812', # Gnrh1           gonadotropin releasing hormone 1
    'ENSMUSG00000015829', # Tnr             tenascin R
    'ENSMUSG00000015837', # Sqstm1          sequestosome 1
    'ENSMUSG00000015839', # Nfe2l2          nuclear factor, erythroid derived 2, like 2
    'ENSMUSG00000015854', # Cd5l            CD5 antigen-like
    'ENSMUSG00000015947', # Fcgr1           Fc receptor, IgG, high affinity I
    'ENSMUSG00000015950', # Ncf1            neutrophil cytosolic factor 1
    'ENSMUSG00000015957', # Wnt11           wingless-type MMTV integration site family, member 11
    'ENSMUSG00000015966', # Il17rb          interleukin 17 receptor B
    'ENSMUSG00000015994', # Fnta            farnesyltransferase, CAAX box, alpha
    'ENSMUSG00000016024', # Lbp             lipopolysaccharide binding protein
    'ENSMUSG00000016206', # H2-M3           histocompatibility 2, M region locus 3
    'ENSMUSG00000016283', # H2-M2           histocompatibility 2, M region locus 2
    'ENSMUSG00000016409', # Nkap            NFKB activating protein
    'ENSMUSG00000016481', # Cr1l            complement component (3b/4b) receptor 1-like
    'ENSMUSG00000016493', # Cd46            CD46 antigen, complement regulatory protein
    'ENSMUSG00000016494', # Cd34            CD34 antigen
    'ENSMUSG00000016495', # Plgrkt          plasminogen receptor, C-terminal lysine transmembrane protein
    'ENSMUSG00000016496', # Cd274           CD274 antigen
    'ENSMUSG00000016498', # Pdcd1lg2        programmed cell death 1 ligand 2
    'ENSMUSG00000016528', # Mapkapk2        MAP kinase-activated protein kinase 2
    'ENSMUSG00000016529', # Il10            interleukin 10
    'ENSMUSG00000016918', # Sulf1           sulfatase 1
    'ENSMUSG00000016933', # Plcg1           phospholipase C, gamma 1
    'ENSMUSG00000017002', # Slpi            secretory leukocyte peptidase inhibitor
    'ENSMUSG00000017009', # Sdc4            syndecan 4
    'ENSMUSG00000017146', # Brca1           breast cancer 1, early onset
    'ENSMUSG00000017309', # Cd300lg         CD300 molecule like family member G
    'ENSMUSG00000017344', # Vtn             vitronectin
    'ENSMUSG00000017412', # Cacnb4          calcium channel, voltage-dependent, beta 4 subunit
    'ENSMUSG00000017446', # C1qtnf1         C1q and tumor necrosis factor related protein 1
    'ENSMUSG00000017466', # Timp2           tissue inhibitor of metalloproteinase 2
    'ENSMUSG00000017548', # Suz12           suppressor of zeste 12 homolog (Drosophila)
    'ENSMUSG00000017550', # Atad5           ATPase family, AAA domain containing 5
    'ENSMUSG00000017631', # Abr             active BCR-related gene
    'ENSMUSG00000017652', # Cd40            CD40 antigen
    'ENSMUSG00000017697', # Ada             adenosine deaminase
    'ENSMUSG00000017707', # Serinc3         serine incorporator 3
    'ENSMUSG00000017737', # Mmp9            matrix metallopeptidase 9
    'ENSMUSG00000017830', # Dhx58           DEXH (Asp-Glu-X-His) box polypeptide 58
    'ENSMUSG00000018001', # Cyth3           cytohesin 3
    'ENSMUSG00000018012', # Rac3            RAS-related C3 botulinum substrate 3
    'ENSMUSG00000018102', # Hist1h2bc       histone cluster 1, H2bc
    'ENSMUSG00000018160', # Med1            mediator complex subunit 1
    'ENSMUSG00000018166', # Erbb3           erb-b2 receptor tyrosine kinase 3
    'ENSMUSG00000018199', # Trove2          TROVE domain family, member 2
    'ENSMUSG00000018341', # Il12rb2         interleukin 12 receptor, beta 2
    'ENSMUSG00000018446', # C1qbp           complement component 1, q subcomponent binding protein
    'ENSMUSG00000018476', # Kdm6b           KDM1 lysine (K)-specific demethylase 6B
    'ENSMUSG00000018500', # Adora2b         adenosine A2b receptor
    'ENSMUSG00000018501', # Ncor1           nuclear receptor co-repressor 1
    'ENSMUSG00000018569', # Cldn7           claudin 7
    'ENSMUSG00000018634', # Crhr1           corticotropin releasing hormone receptor 1
    'ENSMUSG00000018654', # Ikzf1           IKAROS family zinc finger 1
    'ENSMUSG00000018899', # Irf1            interferon regulatory factor 1
    'ENSMUSG00000018909', # Arrb1           arrestin, beta 1
    'ENSMUSG00000018914', # Il3             interleukin 3
    'ENSMUSG00000018916', # Csf2            colony stimulating factor 2 (granulocyte-macrophage)
    'ENSMUSG00000018920', # Cxcl16          chemokine (C-X-C motif) ligand 16
    'ENSMUSG00000018924', # Alox15          arachidonate 15-lipoxygenase
    'ENSMUSG00000018927', # Ccl6            chemokine (C-C motif) ligand 6
    'ENSMUSG00000018930', # Ccl4            chemokine (C-C motif) ligand 4
    'ENSMUSG00000018932', # Map2k3          mitogen-activated protein kinase kinase 3
    'ENSMUSG00000019122', # Ccl9            chemokine (C-C motif) ligand 9
    'ENSMUSG00000019256', # Ahr             aryl-hydrocarbon receptor
    'ENSMUSG00000019326', # Aoc3            amine oxidase, copper containing 3
    'ENSMUSG00000019429', # Ffar3           free fatty acid receptor 3
    'ENSMUSG00000019478', # Rab4a           RAB4A, member RAS oncogene family
    'ENSMUSG00000019489', # Cd70            CD70 antigen
    'ENSMUSG00000019726', # Lyst            lysosomal trafficking regulator
    'ENSMUSG00000019777', # Hdac2           histone deacetylase 2
    'ENSMUSG00000019779', # Frk             fyn-related kinase
    'ENSMUSG00000019820', # Utrn            utrophin
    'ENSMUSG00000019832', # Rab32           RAB32, member RAS oncogene family
    'ENSMUSG00000019843', # Fyn             Fyn proto-oncogene
    'ENSMUSG00000019846', # Lama4           laminin, alpha 4
    'ENSMUSG00000019850', # Tnfaip3         tumor necrosis factor, alpha-induced protein 3
    'ENSMUSG00000019899', # Lama2           laminin, alpha 2
    'ENSMUSG00000019907', # Ppp1r12a        protein phosphatase 1, regulatory (inhibitor) subunit 12A
    'ENSMUSG00000019920', # Lims1           LIM and senescent cell antigen-like domains 1
    'ENSMUSG00000019966', # Kitl            kit ligand
    'ENSMUSG00000019969', # Psen1           presenilin 1
    'ENSMUSG00000019982', # Myb             myeloblastosis oncogene
    'ENSMUSG00000019984', # Med23           mediator complex subunit 23
    'ENSMUSG00000019989', # Enpp3           ectonucleotide pyrophosphatase/phosphodiesterase 3
    'ENSMUSG00000019997', # Ctgf            connective tissue growth factor
    'ENSMUSG00000019998', # Stx7            syntaxin 7
    'ENSMUSG00000020032', # Nuak1           NUAK family, SNF1-like kinase, 1
    'ENSMUSG00000020053', # Igf1            insulin-like growth factor 1
    'ENSMUSG00000020063', # Sirt1           sirtuin 1
    'ENSMUSG00000020077', # Srgn            serglycin
    'ENSMUSG00000020101', # Vsir            V-set immunoregulatory receptor
    'ENSMUSG00000020115', # Tbk1            TANK-binding kinase 1
    'ENSMUSG00000020120', # Plek            pleckstrin
    'ENSMUSG00000020122', # Egfr            epidermal growth factor receptor
    'ENSMUSG00000020125', # Elane           elastase, neutrophil expressed
    'ENSMUSG00000020134', # Peli1           pellino 1
    'ENSMUSG00000020143', # Dock2           dedicator of cyto-kinesis 2
    'ENSMUSG00000020167', # Tcf3            transcription factor 3
    'ENSMUSG00000020178', # Adora2a         adenosine A2a receptor
    'ENSMUSG00000020198', # Ap3d1           adaptor-related protein complex 3, delta 1 subunit
    'ENSMUSG00000020227', # Irak3           interleukin-1 receptor-associated kinase 3
    'ENSMUSG00000020272', # Stk10           serine/threonine kinase 10
    'ENSMUSG00000020275', # Rel             reticuloendotheliosis oncogene
    'ENSMUSG00000020310', # Madcam1         mucosal vascular addressin cell adhesion molecule 1
    'ENSMUSG00000020315', # Sptbn1          spectrin beta, non-erythrocytic 1
    'ENSMUSG00000020319', # Wdpcp           WD repeat containing planar cell polarity effector
    'ENSMUSG00000020325', # Fstl3           follistatin-like 3
    'ENSMUSG00000020357', # Flt4            FMS-like tyrosine kinase 4
    'ENSMUSG00000020366', # Mapk9           mitogen-activated protein kinase 9
    'ENSMUSG00000020383', # Il13            interleukin 13
    'ENSMUSG00000020395', # Itk             IL2 inducible T cell kinase
    'ENSMUSG00000020399', # Havcr2          hepatitis A virus cellular receptor 2
    'ENSMUSG00000020400', # Tnip1           TNFAIP3 interacting protein 1
    'ENSMUSG00000020437', # Myo1g           myosin IG
    'ENSMUSG00000020453', # Patz1           POZ (BTB) and AT hook containing zinc finger 1
    'ENSMUSG00000020455', # Trim11          tripartite motif-containing 11
    'ENSMUSG00000020474', # Polm            polymerase (DNA directed), mu
    'ENSMUSG00000020476', # Dbnl            drebrin-like
    'ENSMUSG00000020484', # Xbp1            X-box binding protein 1
    'ENSMUSG00000020516', # Rps6kb1         ribosomal protein S6 kinase, polypeptide 1
    'ENSMUSG00000020542', # Myocd           myocardin
    'ENSMUSG00000020573', # Pik3cg          phosphoinositide-3-kinase, catalytic, gamma polypeptide
    'ENSMUSG00000020581', # Agr2            anterior gradient 2
    'ENSMUSG00000020592', # Sdc1            syndecan 1
    'ENSMUSG00000020594', # Pum2            pumilio RNA-binding family member 2
    'ENSMUSG00000020601', # Trib2           tribbles pseudokinase 2
    'ENSMUSG00000020605', # Hs1bp3          HCLS1 binding protein 3
    'ENSMUSG00000020611', # Gna13           guanine nucleotide binding protein, alpha 13
    'ENSMUSG00000020612', # Prkar1a         protein kinase, cAMP dependent regulatory, type I, alpha
    'ENSMUSG00000020641', # Rsad2           radical S-adenosyl methionine domain containing 2
    'ENSMUSG00000020644', # Id2             inhibitor of DNA binding 2
    'ENSMUSG00000020659', # Cbll1           Casitas B-lineage lymphoma-like 1
    'ENSMUSG00000020660', # Pomc            pro-opiomelanocortin-alpha
    'ENSMUSG00000020671', # Rab10           RAB10, member RAS oncogene family
    'ENSMUSG00000020676', # Ccl11           chemokine (C-C motif) ligand 11
    'ENSMUSG00000020681', # Ace             angiotensin I converting enzyme (peptidyl-dipeptidase A) 1
    'ENSMUSG00000020682', # Mmp28           matrix metallopeptidase 28 (epilysin)
    'ENSMUSG00000020689', # Itgb3           integrin beta 3
    'ENSMUSG00000020702', # Ccl1            chemokine (C-C motif) ligand 1
    'ENSMUSG00000020707', # Rnf135          ring finger protein 135
    'ENSMUSG00000020716', # Nf1             neurofibromin 1
    'ENSMUSG00000020717', # Pecam1          platelet/endothelial cell adhesion molecule 1
    'ENSMUSG00000020739', # Nup85           nucleoporin 85
    'ENSMUSG00000020758', # Itgb4           integrin beta 4
    'ENSMUSG00000020787', # P2rx1           purinergic receptor P2X, ligand-gated ion channel, 1
    'ENSMUSG00000020823', # Sec14l1         SEC14-like lipid binding 1
    'ENSMUSG00000020826', # Nos2            nitric oxide synthase 2, inducible
    'ENSMUSG00000020827', # Mink1           misshapen-like kinase 1 (zebrafish)
    'ENSMUSG00000020828', # Pld2            phospholipase D2
    'ENSMUSG00000020857', # Nme2            NME/NM23 nucleoside diphosphate kinase 2
    'ENSMUSG00000020872', # Tac4            tachykinin 4
    'ENSMUSG00000020891', # Alox8           arachidonate 8-lipoxygenase
    'ENSMUSG00000020893', # Per1            period circadian clock 1
    'ENSMUSG00000020919', # Stat5b          signal transducer and activator of transcription 5B
    'ENSMUSG00000020941', # Map3k14         mitogen-activated protein kinase kinase kinase 14
    'ENSMUSG00000021022', # Ppp2r3c         protein phosphatase 2, regulatory subunit B'', gamma
    'ENSMUSG00000021025', # Nfkbia          nuclear factor of kappa light polypeptide gene enhancer in B cells inhibitor, alpha
    'ENSMUSG00000021065', # Fut8            fucosyltransferase 8
    'ENSMUSG00000021070', # Bdkrb2          bradykinin receptor, beta 2
    'ENSMUSG00000021091', # Serpina3n       serine (or cysteine) peptidase inhibitor, clade A, member 3N
    'ENSMUSG00000021108', # Prkch           protein kinase C, eta
    'ENSMUSG00000021109', # Hif1a           hypoxia inducible factor 1, alpha subunit
    'ENSMUSG00000021127', # Zfp36l1         zinc finger protein 36, C3H type-like 1
    'ENSMUSG00000021136', # Smoc1           SPARC related modular calcium binding 1
    'ENSMUSG00000021149', # Gtpbp4          GTP binding protein 4
    'ENSMUSG00000021180', # Rps6ka5         ribosomal protein S6 kinase, polypeptide 5
    'ENSMUSG00000021189', # Atxn3           ataxin 3
    'ENSMUSG00000021194', # Chga            chromogranin A
    'ENSMUSG00000021253', # Tgfb3           transforming growth factor, beta 3
    'ENSMUSG00000021262', # Evl             Ena-vasodilator stimulated phosphoprotein
    'ENSMUSG00000021270', # Hsp90aa1        heat shock protein 90, alpha (cytosolic), class A member 1
    'ENSMUSG00000021277', # Traf3           TNF receptor-associated factor 3
    'ENSMUSG00000021318', # Gli3            GLI-Kruppel family member GLI3
    'ENSMUSG00000021326', # Trim27          tripartite motif-containing 27
    'ENSMUSG00000021340', # Gpld1           glycosylphosphatidylinositol specific phospholipase D1
    'ENSMUSG00000021356', # Irf4            interferon regulatory factor 4
    'ENSMUSG00000021360', # Gcnt2           glucosaminyl (N-acetyl) transferase 2, I-branching enzyme
    'ENSMUSG00000021367', # Edn1            endothelin 1
    'ENSMUSG00000021408', # Ripk1           receptor (TNFRSF)-interacting serine-threonine kinase 1
    'ENSMUSG00000021423', # Ly86            lymphocyte antigen 86
    'ENSMUSG00000021451', # Sema4d          sema domain, immunoglobulin domain (Ig), transmembrane domain (TM) and short cytoplasmic domain, (semaphorin) 4D
    'ENSMUSG00000021453', # Gadd45g         growth arrest and DNA-damage-inducible 45 gamma
    'ENSMUSG00000021457', # Syk             spleen tyrosine kinase
    'ENSMUSG00000021464', # Ror2            receptor tyrosine kinase-like orphan receptor 2
    'ENSMUSG00000021486', # Prelid1         PRELI domain containing 1
    'ENSMUSG00000021492', # F12             coagulation factor XII (Hageman factor)
    'ENSMUSG00000021508', # Cxcl14          chemokine (C-X-C motif) ligand 14
    'ENSMUSG00000021538', # Il9             interleukin 9
    'ENSMUSG00000021549', # Rasa1           RAS p21 protein activator 1
    'ENSMUSG00000021583', # Erap1           endoplasmic reticulum aminopeptidase 1
    'ENSMUSG00000021585', # Cast            calpastatin
    'ENSMUSG00000021615', # Xrcc4           X-ray repair complementing defective repair in Chinese hamster cells 4
    'ENSMUSG00000021624', # Cd180           CD180 antigen
    'ENSMUSG00000021638', # Ocln            occludin
    'ENSMUSG00000021678', # F2rl1           coagulation factor II (thrombin) receptor-like 1
    'ENSMUSG00000021680', # Crhbp           corticotropin releasing hormone binding protein
    'ENSMUSG00000021686', # Ap3b1           adaptor-related protein complex 3, beta 1 subunit
    'ENSMUSG00000021699', # Pde4d           phosphodiesterase 4D, cAMP specific
    'ENSMUSG00000021700', # Rab3c           RAB3C, member RAS oncogene family
    'ENSMUSG00000021702', # Thbs4           thrombospondin 4
    'ENSMUSG00000021703', # Serinc5         serine incorporator 5
    'ENSMUSG00000021709', # Erbin           Erbb2 interacting protein
    'ENSMUSG00000021756', # Il6st           interleukin 6 signal transducer
    'ENSMUSG00000021782', # Dlg5            discs, large homolog 5 (Drosophila)
    'ENSMUSG00000021789', # Sftpa1          surfactant associated protein A1
    'ENSMUSG00000021795', # Sftpd           surfactant associated protein D
    'ENSMUSG00000021796', # Bmpr1a          bone morphogenetic protein receptor, type 1A
    'ENSMUSG00000021816', # Ppp3cb          protein phosphatase 3, catalytic subunit, beta isoform
    'ENSMUSG00000021822', # Plau            plasminogen activator, urokinase
    'ENSMUSG00000021835', # Bmp4            bone morphogenetic protein 4
    'ENSMUSG00000021846', # Peli2           pellino 2
    'ENSMUSG00000021871', # Pnp             purine-nucleoside phosphorylase
    'ENSMUSG00000021872', # Rnase10         ribonuclease, RNase A family, 10 (non-active)
    'ENSMUSG00000021901', # Bap1            Brca1 associated protein 1
    'ENSMUSG00000021922', # Itih4           inter alpha-trypsin inhibitor, heavy chain 4
    'ENSMUSG00000021936', # Mapk8           mitogen-activated protein kinase 8
    'ENSMUSG00000021944', # Gata4           GATA binding protein 4
    'ENSMUSG00000021948', # Prkcd           protein kinase C, delta
    'ENSMUSG00000021994', # Wnt5a           wingless-type MMTV integration site family, member 5A
    'ENSMUSG00000021998', # Lcp1            lymphocyte cytosolic protein 1
    'ENSMUSG00000022015', # Tnfsf11         tumor necrosis factor (ligand) superfamily, member 11
    'ENSMUSG00000022018', # Rgcc            regulator of cell cycle
    'ENSMUSG00000022026', # Olfm4           olfactomedin 4
    'ENSMUSG00000022037', # Clu             clusterin
    'ENSMUSG00000022040', # Ephx2           epoxide hydrolase 2, cytoplasmic
    'ENSMUSG00000022043', # Trim35          tripartite motif-containing 35
    'ENSMUSG00000022064', # Pibf1           progesterone immunomodulatory binding factor 1
    'ENSMUSG00000022074', # Tnfrsf10b       tumor necrosis factor receptor superfamily, member 10b
    'ENSMUSG00000022099', # Dmtn            dematin actin binding protein
    'ENSMUSG00000022122', # Ednrb           endothelin receptor type B
    'ENSMUSG00000022126', # Acod1           aconitate decarboxylase 1
    'ENSMUSG00000022146', # Osmr            oncostatin M receptor
    'ENSMUSG00000022148', # Fyb             FYN binding protein
    'ENSMUSG00000022149', # C9              complement component 9
    'ENSMUSG00000022150', # Dab2            disabled 2, mitogen-responsive phosphoprotein
    'ENSMUSG00000022191', # Drosha          drosha, ribonuclease type III
    'ENSMUSG00000022208', # Jph4            junctophilin 4
    'ENSMUSG00000022216', # Psme1           proteasome (prosome, macropain) activator subunit 1 (PA28 alpha)
    'ENSMUSG00000022221', # Ripk3           receptor-interacting serine-threonine kinase 3
    'ENSMUSG00000022231', # Sema5a          sema domain, seven thrombospondin repeats (type 1 and type 1-like), transmembrane domain (TM) and short cytoplasmic domain, (semaphorin) 5A
    'ENSMUSG00000022272', # Myo10           myosin X
    'ENSMUSG00000022297', # Fzd6            frizzled class receptor 6
    'ENSMUSG00000022303', # Dcstamp         dendrocyte expressed seven transmembrane protein
    'ENSMUSG00000022309', # Angpt1          angiopoietin 1
    'ENSMUSG00000022367', # Has2            hyaluronan synthase 2
    'ENSMUSG00000022372', # Sla             src-like adaptor
    'ENSMUSG00000022378', # Fam49b          family with sequence similarity 49, member B
    'ENSMUSG00000022383', # Ppara           peroxisome proliferator activated receptor alpha
    'ENSMUSG00000022425', # Enpp2           ectonucleotide pyrophosphatase/phosphodiesterase 2
    'ENSMUSG00000022455', # Wbp2nl          WBP2 N-terminal like
    'ENSMUSG00000022468', # Endou           endonuclease, polyU-specific
    'ENSMUSG00000022475', # Hdac7           histone deacetylase 7
    'ENSMUSG00000022476', # Polr3h          polymerase (RNA) III (DNA directed) polypeptide H
    'ENSMUSG00000022488', # Nckap1l         NCK associated protein 1 like
    'ENSMUSG00000022496', # Tnfrsf17        tumor necrosis factor receptor superfamily, member 17
    'ENSMUSG00000022500', # Litaf           LPS-induced TN factor
    'ENSMUSG00000022504', # Ciita           class II transactivator
    'ENSMUSG00000022505', # Emp2            epithelial membrane protein 2
    'ENSMUSG00000022508', # Bcl6            B cell leukemia/lymphoma 6
    'ENSMUSG00000022512', # Cldn1           claudin 1
    'ENSMUSG00000022514', # Il1rap          interleukin 1 receptor accessory protein
    'ENSMUSG00000022521', # Crebbp          CREB binding protein
    'ENSMUSG00000022528', # Hes1            hairy and enhancer of split 1 (Drosophila)
    'ENSMUSG00000022534', # Mefv            Mediterranean fever
    'ENSMUSG00000022548', # Apod            apolipoprotein D
    'ENSMUSG00000022556', # Hsf1            heat shock factor 1
    'ENSMUSG00000022575', # Gsdmd           gasdermin D
    'ENSMUSG00000022595', # Lypd2           Ly6/Plaur domain containing 2
    'ENSMUSG00000022596', # Slurp1          secreted Ly6/Plaur domain containing 1
    'ENSMUSG00000022607', # Ptk2            PTK2 protein tyrosine kinase 2
    'ENSMUSG00000022636', # Alcam           activated leukocyte cell adhesion molecule
    'ENSMUSG00000022637', # Cblb            Casitas B-lineage lymphoma b
    'ENSMUSG00000022651', # Retnlg          resistin like gamma
    'ENSMUSG00000022657', # Cd96            CD96 antigen
    'ENSMUSG00000022659', # Gcsam           germinal center associated, signaling and motility
    'ENSMUSG00000022661', # Cd200           CD200 antigen
    'ENSMUSG00000022665', # Ccdc80          coiled-coil domain containing 80
    'ENSMUSG00000022672', # Prkdc           protein kinase, DNA activated, catalytic polypeptide
    'ENSMUSG00000022676', # Snai2           snail family zinc finger 2
    'ENSMUSG00000022683', # Pla2g10         phospholipase A2, group X
    'ENSMUSG00000022708', # Zbtb20          zinc finger and BTB domain containing 20
    'ENSMUSG00000022749', # Tbc1d23         TBC1 domain family, member 23
    'ENSMUSG00000022770', # Dlg1            discs, large homolog 1 (Drosophila)
    'ENSMUSG00000022791', # Tnk2            tyrosine kinase, non-receptor, 2
    'ENSMUSG00000022797', # Tfrc            transferrin receptor
    'ENSMUSG00000022812', # Gsk3b           glycogen synthase kinase 3 beta
    'ENSMUSG00000022817', # Itgb5           integrin beta 5
    'ENSMUSG00000022865', # Cxadr           coxsackie virus and adenovirus receptor
    'ENSMUSG00000022868', # Ahsg            alpha-2-HS-glycoprotein
    'ENSMUSG00000022875', # Kng1            kininogen 1
    'ENSMUSG00000022876', # Samsn1          SAM domain, SH3 domain and nuclear localization signals, 1
    'ENSMUSG00000022877', # Hrg             histidine-rich glycoprotein
    'ENSMUSG00000022878', # Adipoq          adiponectin, C1Q and collagen domain containing
    'ENSMUSG00000022887', # Masp1           mannan-binding lectin serine peptidase 1
    'ENSMUSG00000022892', # App             amyloid beta (A4) precursor protein
    'ENSMUSG00000022901', # Cd86            CD86 antigen
    'ENSMUSG00000022952', # Runx1           runt related transcription factor 1
    'ENSMUSG00000022967', # Ifnar1          interferon (alpha and beta) receptor 1
    'ENSMUSG00000022971', # Ifnar2          interferon (alpha and beta) receptor 2
    'ENSMUSG00000022973', # Synj1           synaptojanin 1
    'ENSMUSG00000022982', # Sod1            superoxide dismutase 1, soluble
    'ENSMUSG00000022997', # Wnt1            wingless-type MMTV integration site family, member 1
    'ENSMUSG00000023010', # Tmbim6          transmembrane BAX inhibitor motif containing 6
    'ENSMUSG00000023031', # Cela1           chymotrypsin-like elastase family, member 1
    'ENSMUSG00000023078', # Cxcl13          chemokine (C-X-C motif) ligand 13
    'ENSMUSG00000023083', # H2-M10.2        histocompatibility 2, M region locus 10.2
    'ENSMUSG00000023110', # Prmt5           protein arginine N-methyltransferase 5
    'ENSMUSG00000023224', # Serping1        serine (or cysteine) peptidase inhibitor, clade G, member 1
    'ENSMUSG00000023235', # Ccl25           chemokine (C-C motif) ligand 25
    'ENSMUSG00000023274', # Cd4             CD4 antigen
    'ENSMUSG00000023349', # Clec4n          C-type lectin domain family 4, member n
    'ENSMUSG00000023411', # Nfatc4          nuclear factor of activated T cells, cytoplasmic, calcineurin dependent 4
    'ENSMUSG00000023886', # Smoc2           SPARC related modular calcium binding 2
    'ENSMUSG00000023903', # Mmp25           matrix metallopeptidase 25
    'ENSMUSG00000023913', # Pla2g7          phospholipase A2, group VII (platelet-activating factor acetylhydrolase, plasma)
    'ENSMUSG00000023915', # Tnfrsf21        tumor necrosis factor receptor superfamily, member 21
    'ENSMUSG00000023927', # Satb1           special AT-rich sequence binding protein 1
    'ENSMUSG00000023944', # Hsp90ab1        heat shock protein 90 alpha (cytosolic), class B member 1
    'ENSMUSG00000023951', # Vegfa           vascular endothelial growth factor A
    'ENSMUSG00000023964', # Calcr           calcitonin receptor
    'ENSMUSG00000023973', # Cnpy3           canopy FGF signaling regulator 3
    'ENSMUSG00000023990', # Tfeb            transcription factor EB
    'ENSMUSG00000023992', # Trem2           triggering receptor expressed on myeloid cells 2
    'ENSMUSG00000023993', # Treml1          triggering receptor expressed on myeloid cells-like 1
    'ENSMUSG00000024026', # Glo1            glyoxalase 1
    'ENSMUSG00000024028', # Tff2            trefoil factor 2 (spasmolytic protein 1)
    'ENSMUSG00000024045', # Akap8           A kinase (PRKA) anchor protein 8
    'ENSMUSG00000024076', # Vit             vitrin
    'ENSMUSG00000024079', # Eif2ak2         eukaryotic translation initiation factor 2-alpha kinase 2
    'ENSMUSG00000024087', # Cyp1b1          cytochrome P450, family 1, subfamily b, polypeptide 1
    'ENSMUSG00000024098', # Twsg1           twisted gastrulation BMP signaling modulator 1
    'ENSMUSG00000024101', # Washc1          WASH complex subunit 1
    'ENSMUSG00000024122', # Pdpk1           3-phosphoinositide dependent protein kinase 1
    'ENSMUSG00000024151', # Msh2            mutS homolog 2
    'ENSMUSG00000024164', # C3              complement component 3
    'ENSMUSG00000024235', # Map3k8          mitogen-activated protein kinase kinase kinase 8
    'ENSMUSG00000024238', # Zeb1            zinc finger E-box binding homeobox 1
    'ENSMUSG00000024241', # Sos1            son of sevenless homolog 1 (Drosophila)
    'ENSMUSG00000024242', # Map4k3          mitogen-activated protein kinase kinase kinase kinase 3
    'ENSMUSG00000024256', # Adcyap1         adenylate cyclase activating polypeptide 1
    'ENSMUSG00000024287', # Thoc1           THO complex 1
    'ENSMUSG00000024290', # Rock1           Rho-associated coiled-coil containing protein kinase 1
    'ENSMUSG00000024300', # Myo1f           myosin IF
    'ENSMUSG00000024308', # Tapbp           TAP binding protein
    'ENSMUSG00000024313', # Mep1b           meprin 1 beta
    'ENSMUSG00000024334', # H2-Oa           histocompatibility 2, O region alpha locus
    'ENSMUSG00000024338', # Psmb8           proteasome (prosome, macropain) subunit, beta type 8 (large multifunctional peptidase 7)
    'ENSMUSG00000024339', # Tap2            transporter 2, ATP-binding cassette, sub-family B (MDR/TAP)
    'ENSMUSG00000024340', # Btnl2           butyrophilin-like 2
    'ENSMUSG00000024349', # Tmem173         transmembrane protein 173
    'ENSMUSG00000024353', # Mzb1            marginal zone B and B1 cell-specific protein 1
    'ENSMUSG00000024359', # Hspa9           heat shock protein 9
    'ENSMUSG00000024371', # C2              complement component 2 (within H-2S)
    'ENSMUSG00000024392', # Bag6            BCL2-associated athanogene 6
    'ENSMUSG00000024397', # Aif1            allograft inflammatory factor 1
    'ENSMUSG00000024399', # Ltb             lymphotoxin B
    'ENSMUSG00000024401', # Tnf             tumor necrosis factor
    'ENSMUSG00000024402', # Lta             lymphotoxin A
    'ENSMUSG00000024404', # Riok3           RIO kinase 3
    'ENSMUSG00000024411', # Aqp4            aquaporin 4
    'ENSMUSG00000024421', # Lama3           laminin, alpha 3
    'ENSMUSG00000024425', # Ndfip1          Nedd4 family interacting protein 1
    'ENSMUSG00000024448', # H2-M10.1        histocompatibility 2, M region locus 10.1
    'ENSMUSG00000024454', # Hdac3           histone deacetylase 3
    'ENSMUSG00000024457', # Trim26          tripartite motif-containing 26
    'ENSMUSG00000024459', # H2-M5           histocompatibility 2, M region locus 5
    'ENSMUSG00000024477', # Pggt1b          protein geranylgeranyltransferase type I, beta subunit
    'ENSMUSG00000024483', # Ankhd1          ankyrin repeat and KH domain containing 1
    'ENSMUSG00000024515', # Smad4           SMAD family member 4
    'ENSMUSG00000024526', # Cidea           cell death-inducing DNA fragmentation factor, alpha subunit-like effector A
    'ENSMUSG00000024539', # Ptpn2           protein tyrosine phosphatase, non-receptor type 2
    'ENSMUSG00000024578', # Il17b           interleukin 17B
    'ENSMUSG00000024593', # Megf10          multiple EGF-like-domains 10
    'ENSMUSG00000024610', # Cd74            CD74 antigen (invariant polypeptide of major histocompatibility complex, class II antigen-associated)
    'ENSMUSG00000024621', # Csf1r           colony stimulating factor 1 receptor
    'ENSMUSG00000024653', # Scgb1a1         secretoglobin, family 1A, member 1 (uteroglobin)
    'ENSMUSG00000024659', # Anxa1           annexin A1
    'ENSMUSG00000024669', # Cd5             CD5 antigen
    'ENSMUSG00000024670', # Cd6             CD6 antigen
    'ENSMUSG00000024680', # Ms4a2           membrane-spanning 4-domains, subfamily A, member 2
    'ENSMUSG00000024696', # Lpxn            leupaxin
    'ENSMUSG00000024713', # Pcsk5           proprotein convertase subtilisin/kexin type 5
    'ENSMUSG00000024767', # Otub1           OTU domain, ubiquitin aldehyde binding 1
    'ENSMUSG00000024778', # Fas             Fas (TNF receptor superfamily member 6)
    'ENSMUSG00000024781', # Lipa            lysosomal acid lipase A
    'ENSMUSG00000024789', # Jak2            Janus kinase 2
    'ENSMUSG00000024790', # Sac3d1          SAC3 domain containing 1
    'ENSMUSG00000024793', # Tnfrsf25        tumor necrosis factor receptor superfamily, member 25
    'ENSMUSG00000024810', # Il33            interleukin 33
    'ENSMUSG00000024863', # Mbl2            mannose-binding lectin (protein C) 2
    'ENSMUSG00000024901', # Peli3           pellino 3
    'ENSMUSG00000024907', # Gal             galanin
    'ENSMUSG00000024926', # Kat5            K(lysine) acetyltransferase 5
    'ENSMUSG00000024927', # Rela            v-rel reticuloendotheliosis viral oncogene homolog A (avian)
    'ENSMUSG00000024947', # Men1            multiple endocrine neoplasia 1
    'ENSMUSG00000024948', # Map4k2          mitogen-activated protein kinase kinase kinase kinase 2
    'ENSMUSG00000024952', # Rps6ka4         ribosomal protein S6 kinase, polypeptide 4
    'ENSMUSG00000024959', # Bad             BCL2-associated agonist of cell death
    'ENSMUSG00000024962', # Vegfb           vascular endothelial growth factor B
    'ENSMUSG00000024965', # Fermt3          fermitin family member 3
    'ENSMUSG00000024975', # Pdcd4           programmed cell death 4
    'ENSMUSG00000024978', # Gpam            glycerol-3-phosphate acyltransferase, mitochondrial
    'ENSMUSG00000024986', # Hhex            hematopoietically expressed homeobox
    'ENSMUSG00000024990', # Rbp4            retinol binding protein 4, plasma
    'ENSMUSG00000025001', # Hells           helicase, lymphoid specific
    'ENSMUSG00000025017', # Pik3ap1         phosphoinositide-3-kinase adaptor protein 1
    'ENSMUSG00000025034', # Trim8           tripartite motif-containing 8
    'ENSMUSG00000025060', # Slk             STE20-like kinase
    'ENSMUSG00000025083', # Afap1l2         actin filament associated protein 1-like 2
    'ENSMUSG00000025139', # Tollip          toll interacting protein
    'ENSMUSG00000025153', # Fasn            fatty acid synthase
    'ENSMUSG00000025163', # Cd7             CD7 antigen
    'ENSMUSG00000025165', # Sectm1a         secreted and transmembrane 1A
    'ENSMUSG00000025172', # Ankrd2          ankyrin repeat domain 2 (stretch responsive muscle)
    'ENSMUSG00000025188', # Hps1            Hermansky-Pudlak syndrome 1
    'ENSMUSG00000025199', # Chuk            conserved helix-loop-helix ubiquitous kinase
    'ENSMUSG00000025223', # Ldb1            LIM domain binding 1
    'ENSMUSG00000025224', # Gbf1            golgi-specific brefeldin A-resistance factor 1
    'ENSMUSG00000025225', # Nfkb2           nuclear factor of kappa light polypeptide gene enhancer in B cells 2, p49/p100
    'ENSMUSG00000025280', # Polr3a          polymerase (RNA) III (DNA directed) polypeptide A
    'ENSMUSG00000025314', # Ptprj           protein tyrosine phosphatase, receptor type, J
    'ENSMUSG00000025330', # Padi4           peptidyl arginine deiminase, type IV
    'ENSMUSG00000025337', # Sbds            Shwachman-Bodian-Diamond syndrome homolog (human)
    'ENSMUSG00000025340', # Rabgef1         RAB guanine nucleotide exchange factor (GEF) 1
    'ENSMUSG00000025348', # Itga7           integrin alpha 7
    'ENSMUSG00000025351', # Cd63            CD63 antigen
    'ENSMUSG00000025383', # Il23a           interleukin 23, alpha subunit p19
    'ENSMUSG00000025389', # Mip             major intrinsic protein of lens fiber
    'ENSMUSG00000025393', # Atp5b           ATP synthase, H+ transporting mitochondrial F1 complex, beta subunit
    'ENSMUSG00000025403', # Shmt2           serine hydroxymethyltransferase 2 (mitochondrial)
    'ENSMUSG00000025408', # Ddit3           DNA-damage inducible transcript 3
    'ENSMUSG00000025473', # Adam8           a disintegrin and metallopeptidase domain 8
    'ENSMUSG00000025491', # Ifitm1          interferon induced transmembrane protein 1
    'ENSMUSG00000025492', # Ifitm3          interferon induced transmembrane protein 3
    'ENSMUSG00000025494', # Sigirr          single immunoglobulin and toll-interleukin 1 receptor (TIR) domain
    'ENSMUSG00000025498', # Irf7            interferon regulatory factor 7
    'ENSMUSG00000025499', # Hras            Harvey rat sarcoma virus oncogene
    'ENSMUSG00000025512', # Chid1           chitinase domain containing 1
    'ENSMUSG00000025532', # Crcp            calcitonin gene-related peptide-receptor component protein
    'ENSMUSG00000025608', # Podxl           podocalyxin-like
    'ENSMUSG00000025701', # Alox5           arachidonate 5-lipoxygenase
    'ENSMUSG00000025702', # March8          membrane-associated ring finger (C3HC4) 8
    'ENSMUSG00000025746', # Il6             interleukin 6
    'ENSMUSG00000025779', # Ly96            lymphocyte antigen 96
    'ENSMUSG00000025804', # Ccr1            chemokine (C-C motif) receptor 1
    'ENSMUSG00000025809', # Itgb1           integrin beta 1 (fibronectin receptor beta)
    'ENSMUSG00000025880', # Smad7           SMAD family member 7
    'ENSMUSG00000025888', # Casp1           caspase 1
    'ENSMUSG00000025889', # Snca            synuclein, alpha
    'ENSMUSG00000025905', # Oprk1           opioid receptor, kappa 1
    'ENSMUSG00000025929', # Il17a           interleukin 17A
    'ENSMUSG00000025958', # Creb1           cAMP responsive element binding protein 1
    'ENSMUSG00000025978', # Rftn2           raftlin family member 2
    'ENSMUSG00000025980', # Hspd1           heat shock protein 1 (chaperonin)
    'ENSMUSG00000025986', # Slc39a10        solute carrier family 39 (zinc transporter), member 10
    'ENSMUSG00000026009', # Icos            inducible T cell co-stimulator
    'ENSMUSG00000026011', # Ctla4           cytotoxic T-lymphocyte-associated protein 4
    'ENSMUSG00000026012', # Cd28            CD28 antigen
    'ENSMUSG00000026029', # Casp8           caspase 8
    'ENSMUSG00000026043', # Col3a1          collagen, type III, alpha 1
    'ENSMUSG00000026069', # Il1rl1          interleukin 1 receptor-like 1
    'ENSMUSG00000026070', # Il18r1          interleukin 18 receptor 1
    'ENSMUSG00000026072', # Il1r1           interleukin 1 receptor, type I
    'ENSMUSG00000026073', # Il1r2           interleukin 1 receptor, type II
    'ENSMUSG00000026104', # Stat1           signal transducer and activator of transcription 1
    'ENSMUSG00000026117', # Zap70           zeta-chain (TCR) associated protein kinase
    'ENSMUSG00000026154', # Sdhaf4          succinate dehydrogenase complex assembly factor 4
    'ENSMUSG00000026162', # Nhej1           nonhomologous end-joining factor 1
    'ENSMUSG00000026166', # Ccl20           chemokine (C-C motif) ligand 20
    'ENSMUSG00000026177', # Slc11a1         solute carrier family 11 (proton-coupled divalent metal ion transporters), member 1
    'ENSMUSG00000026180', # Cxcr2           chemokine (C-X-C motif) receptor 2
    'ENSMUSG00000026181', # Ppm1f           protein phosphatase 1F (PP2C domain containing)
    'ENSMUSG00000026193', # Fn1             fibronectin 1
    'ENSMUSG00000026228', # Htr2b           5-hydroxytryptamine (serotonin) receptor 2B
    'ENSMUSG00000026234', # Ncl             nucleolin
    'ENSMUSG00000026249', # Serpine2        serine (or cysteine) peptidase inhibitor, clade E, member 2
    'ENSMUSG00000026271', # Gpr35           G protein-coupled receptor 35
    'ENSMUSG00000026285', # Pdcd1           programmed cell death 1
    'ENSMUSG00000026288', # Inpp5d          inositol polyphosphate-5-phosphatase D
    'ENSMUSG00000026313', # Hdac4           histone deacetylase 4
    'ENSMUSG00000026321', # Tnfrsf11a       tumor necrosis factor receptor superfamily, member 11a, NFKB activator
    'ENSMUSG00000026344', # Lypd1           Ly6/Plaur domain containing 1
    'ENSMUSG00000026365', # Cfh             complement component factor h
    'ENSMUSG00000026383', # Epb41l5         erythrocyte membrane protein band 4.1 like 5
    'ENSMUSG00000026390', # Marco           macrophage receptor with collagenous structure
    'ENSMUSG00000026395', # Ptprc           protein tyrosine phosphatase, receptor type, C
    'ENSMUSG00000026399', # Cd55            CD55 molecule, decay accelerating factor for complement
    'ENSMUSG00000026401', # Cd55b           CD55 molecule, decay accelerating factor for complement B
    'ENSMUSG00000026405', # C4bp            complement component 4 binding protein
    'ENSMUSG00000026415', # Fcamr           Fc receptor, IgA, IgM, high affinity
    'ENSMUSG00000026433', # Rab29           RAB29, member RAS oncogene family
    'ENSMUSG00000026471', # Mr1             major histocompatibility complex, class I-related
    'ENSMUSG00000026494', # Kif26b          kinesin family member 26B
    'ENSMUSG00000026496', # Parp1           poly (ADP-ribose) polymerase family, member 1
    'ENSMUSG00000026532', # Spta1           spectrin alpha, erythrocytic 1
    'ENSMUSG00000026542', # Apcs            serum amyloid P-component
    'ENSMUSG00000026573', # Xcl1            chemokine (C motif) ligand 1
    'ENSMUSG00000026580', # Selp            selectin, platelet
    'ENSMUSG00000026581', # Sell            selectin, lymphocyte
    'ENSMUSG00000026582', # Sele            selectin, endothelial cell
    'ENSMUSG00000026585', # Kifap3          kinesin-associated protein 3
    'ENSMUSG00000026596', # Abl2            v-abl Abelson murine leukemia viral oncogene 2 (arg, Abelson-related gene)
    'ENSMUSG00000026616', # Cr2             complement receptor 2
    'ENSMUSG00000026630', # Batf3           basic leucine zipper transcription factor, ATF-like 3
    'ENSMUSG00000026648', # Dclre1c         DNA cross-link repair 1C
    'ENSMUSG00000026656', # Fcgr2b          Fc receptor, IgG, low affinity IIb
    'ENSMUSG00000026697', # Myoc            myocilin
    'ENSMUSG00000026700', # Tnfsf4          tumor necrosis factor (ligand) superfamily, member 4
    'ENSMUSG00000026705', # Klhl20          kelch-like 20
    'ENSMUSG00000026727', # Rsu1            Ras suppressor protein 1
    'ENSMUSG00000026739', # Bmi1            Bmi1 polycomb ring finger oncogene
    'ENSMUSG00000026768', # Itga8           integrin alpha 8
    'ENSMUSG00000026770', # Il2ra           interleukin 2 receptor, alpha chain
    'ENSMUSG00000026778', # Prkcq           protein kinase C, theta
    'ENSMUSG00000026786', # Apbb1ip         amyloid beta (A4) precursor protein-binding, family B, member 1 interacting protein
    'ENSMUSG00000026812', # Tsc1            tuberous sclerosis 1
    'ENSMUSG00000026822', # Lcn2            lipocalin 2
    'ENSMUSG00000026832', # Cytip           cytohesin 1 interacting protein
    'ENSMUSG00000026835', # Fcnb            ficolin B
    'ENSMUSG00000026836', # Acvr1           activin A receptor, type 1
    'ENSMUSG00000026842', # Abl1            c-abl oncogene 1, non-receptor tyrosine kinase
    'ENSMUSG00000026866', # Kynu            kynureninase (L-kynurenine hydrolase)
    'ENSMUSG00000026874', # Hc              hemolytic complement
    'ENSMUSG00000026879', # Gsn             gelsolin
    'ENSMUSG00000026883', # Dab2ip          disabled 2 interacting protein
    'ENSMUSG00000026896', # Ifih1           interferon induced with helicase C domain 1
    'ENSMUSG00000026922', # Agpat2          1-acylglycerol-3-phosphate O-acyltransferase 2 (lysophosphatidic acid acyltransferase, beta)
    'ENSMUSG00000026923', # Notch1          notch 1
    'ENSMUSG00000026928', # Card9           caspase recruitment domain family, member 9
    'ENSMUSG00000026938', # Fcna            ficolin A
    'ENSMUSG00000026942', # Traf2           TNF receptor-associated factor 2
    'ENSMUSG00000026946', # Nmi             N-myc (and STAT) interactor
    'ENSMUSG00000026971', # Itgb6           integrin beta 6
    'ENSMUSG00000026977', # March7          membrane-associated ring finger (C3HC4) 7
    'ENSMUSG00000026981', # Il1rn           interleukin 1 receptor antagonist
    'ENSMUSG00000026983', # Il1f5           interleukin 1 family, member 5 (delta)
    'ENSMUSG00000026984', # Il1f6           interleukin 1 family, member 6
    'ENSMUSG00000026985', # Il1f8           interleukin 1 family, member 8
    'ENSMUSG00000027009', # Itga4           integrin alpha 4
    'ENSMUSG00000027072', # Prg3            proteoglycan 3
    'ENSMUSG00000027073', # Prg2            proteoglycan 2, bone marrow
    'ENSMUSG00000027087', # Itgav           integrin alpha V
    'ENSMUSG00000027104', # Atf2            activating transcription factor 2
    'ENSMUSG00000027109', # Sp3             trans-acting transcription factor 3
    'ENSMUSG00000027111', # Itga6           integrin alpha 6
    'ENSMUSG00000027164', # Traf6           TNF receptor-associated factor 6
    'ENSMUSG00000027195', # Hsd17b12        hydroxysteroid (17-beta) dehydrogenase 12
    'ENSMUSG00000027221', # Chst1           carbohydrate (keratan sulfate Gal-6) sulfotransferase 1
    'ENSMUSG00000027238', # Frmd5           FERM domain containing 5
    'ENSMUSG00000027249', # F2              coagulation factor II
    'ENSMUSG00000027276', # Jag1            jagged 1
    'ENSMUSG00000027298', # Tyro3           TYRO3 protein tyrosine kinase 3
    'ENSMUSG00000027312', # Atrn            attractin
    'ENSMUSG00000027314', # Dll4            delta-like 4 (Drosophila)
    'ENSMUSG00000027318', # Adam33          a disintegrin and metallopeptidase domain 33
    'ENSMUSG00000027347', # Rasgrp1         RAS guanyl releasing protein 1
    'ENSMUSG00000027356', # Fermt1          fermitin family member 1
    'ENSMUSG00000027358', # Bmp2            bone morphogenetic protein 2
    'ENSMUSG00000027366', # Sppl2a          signal peptide peptidase like 2A
    'ENSMUSG00000027387', # Zc3h8           zinc finger CCCH type containing 8
    'ENSMUSG00000027398', # Il1b            interleukin 1 beta
    'ENSMUSG00000027399', # Il1a            interleukin 1 alpha
    'ENSMUSG00000027427', # Polr3f          polymerase (RNA) III (DNA directed) polypeptide F
    'ENSMUSG00000027466', # Rbck1           RanBP-type and C3HC4-type zinc finger containing 1
    'ENSMUSG00000027468', # Defb22          defensin beta 22
    'ENSMUSG00000027474', # Ccm2l           cerebral cavernous malformation 2-like
    'ENSMUSG00000027483', # Bpifa1          BPI fold containing family A, member 1
    'ENSMUSG00000027485', # Bpifb1          BPI fold containing family B, member 1
    'ENSMUSG00000027508', # Pag1            phosphoprotein associated with glycosphingolipid microdomains 1
    'ENSMUSG00000027514', # Zbp1            Z-DNA binding protein 1
    'ENSMUSG00000027524', # Edn3            endothelin 3
    'ENSMUSG00000027544', # Nfatc2          nuclear factor of activated T cells, cytoplasmic, calcineurin dependent 2
    'ENSMUSG00000027551', # Zfp64           zinc finger protein 64
    'ENSMUSG00000027579', # Srms            src-related kinase lacking C-terminal regulatory tyrosine and N-terminal myristylation sites
    'ENSMUSG00000027597', # Ahcy            S-adenosylhomocysteine hydrolase
    'ENSMUSG00000027598', # Itch            itchy, E3 ubiquitin protein ligase
    'ENSMUSG00000027636', # Sla2            Src-like-adaptor 2
    'ENSMUSG00000027639', # Samhd1          SAM domain and HD domain, 1
    'ENSMUSG00000027646', # Src             Rous sarcoma oncogene
    'ENSMUSG00000027649', # Ctnnbl1         catenin, beta like 1
    'ENSMUSG00000027665', # Pik3ca          phosphatidylinositol 3-kinase, catalytic, alpha polypeptide
    'ENSMUSG00000027670', # Ocstamp         osteoclast stimulatory transmembrane protein
    'ENSMUSG00000027684', # Mecom           MDS1 and EVI1 complex locus
    'ENSMUSG00000027718', # Il21            interleukin 21
    'ENSMUSG00000027720', # Il2             interleukin 2
    'ENSMUSG00000027750', # Postn           periostin, osteoblast specific factor
    'ENSMUSG00000027765', # P2ry1           purinergic receptor P2Y, G-protein coupled 1
    'ENSMUSG00000027776', # Il12a           interleukin 12a
    'ENSMUSG00000027832', # Ptx3            pentraxin related gene
    'ENSMUSG00000027834', # Serpini1        serine (or cysteine) peptidase inhibitor, clade I, member 1
    'ENSMUSG00000027843', # Ptpn22          protein tyrosine phosphatase, non-receptor type 22 (lymphoid)
    'ENSMUSG00000027852', # Nras            neuroblastoma ras oncogene
    'ENSMUSG00000027858', # Tspan2          tetraspanin 2
    'ENSMUSG00000027863', # Cd2             CD2 antigen
    'ENSMUSG00000027878', # Notch2          notch 2
    'ENSMUSG00000027947', # Il6ra           interleukin 6 receptor, alpha
    'ENSMUSG00000027951', # Adar            adenosine deaminase, RNA-specific
    'ENSMUSG00000027954', # Efna1           ephrin A1
    'ENSMUSG00000027962', # Vcam1           vascular cell adhesion molecule 1
    'ENSMUSG00000027985', # Lef1            lymphoid enhancer binding factor 1
    'ENSMUSG00000027995', # Tlr2            toll-like receptor 2
    'ENSMUSG00000027997', # Casp6           caspase 6
    'ENSMUSG00000028001', # Fga             fibrinogen alpha chain
    'ENSMUSG00000028004', # Npy2r           neuropeptide Y receptor Y2
    'ENSMUSG00000028029', # Aimp1           aminoacyl tRNA synthetase complex-interacting multifunctional protein 1
    'ENSMUSG00000028040', # Efna4           ephrin A4
    'ENSMUSG00000028041', # Adam15          a disintegrin and metallopeptidase domain 15 (metargidin)
    'ENSMUSG00000028042', # Zbtb7b          zinc finger and BTB domain containing 7B
    'ENSMUSG00000028048', # Gba             glucosidase, beta, acid
    'ENSMUSG00000028053', # Ash1l           ash1 (absent, small, or homeotic)-like (Drosophila)
    'ENSMUSG00000028059', # Arhgef2         rho/rac guanine nucleotide exchange factor (GEF) 2
    'ENSMUSG00000028064', # Sema4a          sema domain, immunoglobulin domain (Ig), transmembrane domain (TM) and short cytoplasmic domain, (semaphorin) 4A
    'ENSMUSG00000028076', # Cd1d1           CD1d1 antigen
    'ENSMUSG00000028099', # Polr3c          polymerase (RNA) III (DNA directed) polypeptide C
    'ENSMUSG00000028108', # Ecm1            extracellular matrix protein 1
    'ENSMUSG00000028150', # Rorc            RAR-related orphan receptor gamma
    'ENSMUSG00000028163', # Nfkb1           nuclear factor of kappa light polypeptide gene enhancer in B cells 1, p105
    'ENSMUSG00000028191', # Bcl10           B cell leukemia/lymphoma 10
    'ENSMUSG00000028195', # Cyr61           cysteine rich protein 61
    'ENSMUSG00000028217', # Cdh17           cadherin 17
    'ENSMUSG00000028277', # Ube2j1          ubiquitin-conjugating enzyme E2J 1
    'ENSMUSG00000028289', # Epha7           Eph receptor A7
    'ENSMUSG00000028291', # Akirin2         akirin 2
    'ENSMUSG00000028322', # Exosc3          exosome component 3
    'ENSMUSG00000028341', # Nr4a3           nuclear receptor subfamily 4, group A, member 3
    'ENSMUSG00000028362', # Tnfsf8          tumor necrosis factor (ligand) superfamily, member 8
    'ENSMUSG00000028364', # Tnc             tenascin C
    'ENSMUSG00000028386', # Slc46a2         solute carrier family 46, member 2
    'ENSMUSG00000028399', # Ptprd           protein tyrosine phosphatase, receptor type, D
    'ENSMUSG00000028413', # B4galt1         UDP-Gal:betaGlcNAc beta 1,4- galactosyltransferase, polypeptide 1
    'ENSMUSG00000028434', # Epb41l4b        erythrocyte membrane protein band 4.1 like 4b
    'ENSMUSG00000028435', # Aqp3            aquaporin 3
    'ENSMUSG00000028455', # Stoml2          stomatin (Epb7.2)-like 2
    'ENSMUSG00000028460', # Sit1            suppression inducing transmembrane adaptor 1
    'ENSMUSG00000028465', # Tln1            talin 1
    'ENSMUSG00000028466', # Creb3           cAMP responsive element binding protein 3
    'ENSMUSG00000028495', # Rps6            ribosomal protein S6
    'ENSMUSG00000028519', # Dab1            disabled 1
    'ENSMUSG00000028525', # Pde4b           phosphodiesterase 4B, cAMP specific
    'ENSMUSG00000028530', # Jak1            Janus kinase 1
    'ENSMUSG00000028539', # Artn            artemin
    'ENSMUSG00000028576', # Ift74           intraflagellar transport 74
    'ENSMUSG00000028577', # Plaa            phospholipase A2, activating protein
    'ENSMUSG00000028580', # Pum1            pumilio RNA-binding family member 1
    'ENSMUSG00000028599', # Tnfrsf1b        tumor necrosis factor receptor superfamily, member 1b
    'ENSMUSG00000028602', # Tnfrsf8         tumor necrosis factor receptor superfamily, member 8
    'ENSMUSG00000028633', # Ctps            cytidine 5'-triphosphate synthase
    'ENSMUSG00000028635', # Edn2            endothelin 2
    'ENSMUSG00000028649', # Macf1           microtubule-actin crosslinking factor 1
    'ENSMUSG00000028661', # Epha8           Eph receptor A8
    'ENSMUSG00000028691', # Prdx1           peroxiredoxin 1
    'ENSMUSG00000028701', # Lurap1          leucine rich adaptor protein 1
    'ENSMUSG00000028749', # Pla2g2f         phospholipase A2, group IIF
    'ENSMUSG00000028757', # Ddost           dolichyl-di-phosphooligosaccharide-protein glycotransferase
    'ENSMUSG00000028776', # Tinagl1         tubulointerstitial nephritis antigen-like 1
    'ENSMUSG00000028793', # Rnf19b          ring finger protein 19B
    'ENSMUSG00000028800', # Hdac1           histone deacetylase 1
    'ENSMUSG00000028803', # Nipal3          NIPA-like domain containing 3
    'ENSMUSG00000028859', # Csf3r           colony stimulating factor 3 receptor (granulocyte)
    'ENSMUSG00000028864', # Hgf             hepatocyte growth factor
    'ENSMUSG00000028874', # Fgr             FGR proto-oncogene, Src family tyrosine kinase
    'ENSMUSG00000028885', # Smpdl3b         sphingomyelin phosphodiesterase, acid-like 3B
    'ENSMUSG00000028927', # Padi2           peptidyl arginine deiminase, type II
    'ENSMUSG00000028936', # Rpl22           ribosomal protein L22
    'ENSMUSG00000028964', # Park7           Parkinson disease (autosomal recessive, early onset) 7
    'ENSMUSG00000028965', # Tnfrsf9         tumor necrosis factor receptor superfamily, member 9
    'ENSMUSG00000028967', # Errfi1          ERBB receptor feedback inhibitor 1
    'ENSMUSG00000028979', # Masp2           mannan-binding lectin serine peptidase 2
    'ENSMUSG00000029003', # Mad2l2          MAD2 mitotic arrest deficient-like 2
    'ENSMUSG00000029004', # Kmt2e           lysine (K)-specific methyltransferase 2E
    'ENSMUSG00000029026', # Trp73           transformation related protein 73
    'ENSMUSG00000029053', # Prkcz           protein kinase C, zeta
    'ENSMUSG00000029075', # Tnfrsf4         tumor necrosis factor receptor superfamily, member 4
    'ENSMUSG00000029082', # Bst1            bone marrow stromal cell antigen 1
    'ENSMUSG00000029084', # Cd38            CD38 antigen
    'ENSMUSG00000029163', # Emilin1         elastin microfibril interfacer 1
    'ENSMUSG00000029199', # Lias            lipoic acid synthetase
    'ENSMUSG00000029204', # Rhoh            ras homolog family member H
    'ENSMUSG00000029217', # Tec             tec protein tyrosine kinase
    'ENSMUSG00000029245', # Epha5           Eph receptor A5
    'ENSMUSG00000029254', # Stap1           signal transducing adaptor family member 1
    'ENSMUSG00000029276', # Glmn            glomulin, FKBP associated protein
    'ENSMUSG00000029287', # Tgfbr3          transforming growth factor, beta receptor III
    'ENSMUSG00000029304', # Spp1            secreted phosphoprotein 1
    'ENSMUSG00000029306', # Ibsp            integrin binding sialoprotein
    'ENSMUSG00000029307', # Dmp1            dentin matrix protein 1
    'ENSMUSG00000029359', # Tesc            tescalcin
    'ENSMUSG00000029371', # Cxcl5           chemokine (C-X-C motif) ligand 5
    'ENSMUSG00000029372', # Ppbp            pro-platelet basic protein
    'ENSMUSG00000029373', # Pf4             platelet factor 4
    'ENSMUSG00000029375', # Cxcl15          chemokine (C-X-C motif) ligand 15
    'ENSMUSG00000029377', # Ereg            epiregulin
    'ENSMUSG00000029379', # Cxcl3           chemokine (C-X-C motif) ligand 3
    'ENSMUSG00000029380', # Cxcl1           chemokine (C-X-C motif) ligand 1
    'ENSMUSG00000029417', # Cxcl9           chemokine (C-X-C motif) ligand 9
    'ENSMUSG00000029437', # Il31            interleukin 31
    'ENSMUSG00000029468', # P2rx7           purinergic receptor P2X, ligand-gated ion channel, 7
    'ENSMUSG00000029518', # Rab35           RAB35, member RAS oncogene family
    'ENSMUSG00000029522', # Pla2g1b         phospholipase A2, group IB, pancreas
    'ENSMUSG00000029528', # Pxn             paxillin
    'ENSMUSG00000029530', # Ccr9            chemokine (C-C motif) receptor 9
    'ENSMUSG00000029550', # Sppl3           signal peptide peptidase 3
    'ENSMUSG00000029554', # Mad1l1          MAD1 mitotic arrest deficient 1-like 1
    'ENSMUSG00000029556', # Hnf1a           HNF1 homeobox A
    'ENSMUSG00000029561', # Oasl2           2'-5' oligoadenylate synthetase-like 2
    'ENSMUSG00000029570', # Lfng            LFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase
    'ENSMUSG00000029591', # Ung             uracil DNA glycosylase
    'ENSMUSG00000029603', # Dtx1            deltex 1, E3 ubiquitin ligase
    'ENSMUSG00000029613', # Eif2ak1         eukaryotic translation initiation factor 2 alpha kinase 1
    'ENSMUSG00000029640', # Usp12           ubiquitin specific peptidase 12
    'ENSMUSG00000029648', # Flt1            FMS-like tyrosine kinase 1
    'ENSMUSG00000029656', # C8b             complement component 8, beta polypeptide
    'ENSMUSG00000029657', # Hsph1           heat shock 105kDa/110kDa protein 1
    'ENSMUSG00000029710', # Ephb4           Eph receptor B4
    'ENSMUSG00000029711', # Epo             erythropoietin
    'ENSMUSG00000029771', # Irf5            interferon regulatory factor 5
    'ENSMUSG00000029798', # Herc6           hect domain and RLD 6
    'ENSMUSG00000029816', # Gpnmb           glycoprotein (transmembrane) nmb
    'ENSMUSG00000029826', # Zc3hav1         zinc finger CCCH type, antiviral 1
    'ENSMUSG00000029838', # Ptn             pleiotrophin
    'ENSMUSG00000029859', # Epha1           Eph receptor A1
    'ENSMUSG00000029860', # Zyx             zyxin
    'ENSMUSG00000029869', # Ephb6           Eph receptor B6
    'ENSMUSG00000029915', # Clec5a          C-type lectin domain family 5, member a
    'ENSMUSG00000029994', # Anxa4           annexin A4
    'ENSMUSG00000030000', # Add2            adducin 2 (beta)
    'ENSMUSG00000030004', # Nat8            N-acetyltransferase 8 (GCN5-related)
    'ENSMUSG00000030017', # Reg3g           regenerating islet-derived 3 gamma
    'ENSMUSG00000030043', # Tacr1           tachykinin receptor 1
    'ENSMUSG00000030051', # Aplf            aprataxin and PNKP like factor
    'ENSMUSG00000030059', # Tmf1            TATA element modulatory factor 1
    'ENSMUSG00000030067', # Foxp1           forkhead box P1
    'ENSMUSG00000030093', # Wnt7a           wingless-type MMTV integration site family, member 7A
    'ENSMUSG00000030110', # Ret             ret proto-oncogene
    'ENSMUSG00000030114', # Klrg1           killer cell lectin-like receptor subfamily G, member 1
    'ENSMUSG00000030122', # Ptms            parathymosin
    'ENSMUSG00000030123', # Plxnd1          plexin D1
    'ENSMUSG00000030124', # Lag3            lymphocyte-activation gene 3
    'ENSMUSG00000030142', # Clec4e          C-type lectin domain family 4, member e
    'ENSMUSG00000030144', # Clec4d          C-type lectin domain family 4, member d
    'ENSMUSG00000030148', # Clec4a2         C-type lectin domain family 4, member a2
    'ENSMUSG00000030149', # Klrk1           killer cell lectin-like receptor subfamily K, member 1
    'ENSMUSG00000030162', # Olr1            oxidized low density lipoprotein (lectin-like) receptor 1
    'ENSMUSG00000030165', # Klrd1           killer cell lectin-like receptor, subfamily D, member 1
    'ENSMUSG00000030223', # Ptpro           protein tyrosine phosphatase, receptor type, O
    'ENSMUSG00000030230', # Plcz1           phospholipase C, zeta 1
    'ENSMUSG00000030263', # Lrmp            lymphoid-restricted membrane protein
    'ENSMUSG00000030281', # Il17rc          interleukin 17 receptor C
    'ENSMUSG00000030314', # Atg7            autophagy related 7
    'ENSMUSG00000030317', # Timp4           tissue inhibitor of metalloproteinase 4
    'ENSMUSG00000030325', # Klrb1c          killer cell lectin-like receptor subfamily B member 1C
    'ENSMUSG00000030336', # Cd27            CD27 antigen
    'ENSMUSG00000030339', # Ltbr            lymphotoxin B receptor
    'ENSMUSG00000030341', # Tnfrsf1a        tumor necrosis factor receptor superfamily, member 1a
    'ENSMUSG00000030347', # D6Wsu163e       DNA segment, Chr 6, Wayne State University 163, expressed
    'ENSMUSG00000030365', # Clec2i          C-type lectin domain family 2, member i
    'ENSMUSG00000030413', # Pglyrp1         peptidoglycan recognition protein 1
    'ENSMUSG00000030525', # Chrna7          cholinergic receptor, nicotinic, alpha polypeptide 7
    'ENSMUSG00000030527', # Crtc3           CREB regulated transcription coactivator 3
    'ENSMUSG00000030528', # Blm             Bloom syndrome, RecQ helicase-like
    'ENSMUSG00000030530', # Furin           furin (paired basic amino acid cleaving enzyme)
    'ENSMUSG00000030534', # Vps33b          vacuolar protein sorting 33B
    'ENSMUSG00000030536', # Iqgap1          IQ motif containing GTPase activating protein 1
    'ENSMUSG00000030538', # Cib1            calcium and integrin binding 1 (calmyrin)
    'ENSMUSG00000030560', # Ctsc            cathepsin C
    'ENSMUSG00000030579', # Tyrobp          TYRO protein tyrosine kinase binding protein
    'ENSMUSG00000030669', # Calca           calcitonin/calcitonin-related polypeptide, alpha
    'ENSMUSG00000030671', # Pde3b           phosphodiesterase 3B, cGMP-inhibited
    'ENSMUSG00000030680', # Pagr1a          PAXIP1 associated glutamate rich protein 1A
    'ENSMUSG00000030704', # Rab6a           RAB6A, member RAS oncogene family
    'ENSMUSG00000030707', # Coro1a          coronin, actin binding protein 1A
    'ENSMUSG00000030717', # Nupr1           nuclear protein transcription regulator 1
    'ENSMUSG00000030722', # Nfatc2ip        nuclear factor of activated T cells, cytoplasmic, calcineurin dependent 2 interacting protein
    'ENSMUSG00000030724', # Cd19            CD19 antigen
    'ENSMUSG00000030742', # Lat             linker for activation of T cells
    'ENSMUSG00000030744', # Rps3            ribosomal protein S3
    'ENSMUSG00000030748', # Il4ra           interleukin 4 receptor, alpha
    'ENSMUSG00000030751', # Psma1           proteasome (prosome, macropain) subunit, alpha type 1
    'ENSMUSG00000030775', # Trat1           T cell receptor associated transmembrane adaptor 1
    'ENSMUSG00000030786', # Itgam           None
    'ENSMUSG00000030789', # Itgax           integrin alpha X
    'ENSMUSG00000030793', # Pycard          PYD and CARD domain containing
    'ENSMUSG00000030798', # Cd37            CD37 antigen
    'ENSMUSG00000030805', # Stx4a           syntaxin 4A (placental)
    'ENSMUSG00000030830', # Itgal           integrin alpha L
    'ENSMUSG00000030880', # Polr3e          polymerase (RNA) III (DNA directed) polypeptide E
    'ENSMUSG00000030890', # Ilk             integrin linked kinase
    'ENSMUSG00000030895', # Hpx             hemopexin
    'ENSMUSG00000030921', # Trim30a         tripartite motif-containing 30A
    'ENSMUSG00000030963', # Umod            uromodulin
    'ENSMUSG00000030966', # Trim21          tripartite motif-containing 21
    'ENSMUSG00000031007', # Atp6ap2         ATPase, H+ transporting, lysosomal accessory protein 2
    'ENSMUSG00000031010', # Usp9x           ubiquitin specific peptidase 9, X chromosome
    'ENSMUSG00000031012', # Cask            calcium/calmodulin-dependent serine protein kinase (MAGUK family)
    'ENSMUSG00000031015', # Swap70          SWA-70 protein
    'ENSMUSG00000031077', # Fadd            Fas (TNFRSF6)-associated via death domain
    'ENSMUSG00000031101', # Sash3           SAM and SH3 domain containing 3
    'ENSMUSG00000031103', # Elf4            E74-like factor 4 (ets domain transcription factor)
    'ENSMUSG00000031104', # Rab33a          RAB33A, member RAS oncogene family
    'ENSMUSG00000031132', # Cd40lg          CD40 ligand
    'ENSMUSG00000031142', # Cacna1f         calcium channel, voltage-dependent, alpha 1F subunit
    'ENSMUSG00000031154', # Otud5           OTU domain containing 5
    'ENSMUSG00000031162', # Gata1           GATA binding protein 1
    'ENSMUSG00000031165', # Was             Wiskott-Aldrich syndrome
    'ENSMUSG00000031196', # F8              coagulation factor VIII
    'ENSMUSG00000031207', # Msn             moesin
    'ENSMUSG00000031217', # Efnb1           ephrin B1
    'ENSMUSG00000031221', # Igbp1           immunoglobulin (CD79A) binding protein 1
    'ENSMUSG00000031239', # Itm2a           integral membrane protein 2A
    'ENSMUSG00000031264', # Btk             Bruton agammaglobulinemia tyrosine kinase
    'ENSMUSG00000031289', # Il13ra2         interleukin 13 receptor, alpha 2
    'ENSMUSG00000031304', # Il2rg           interleukin 2 receptor, gamma chain
    'ENSMUSG00000031309', # Rps6ka3         ribosomal protein S6 kinase polypeptide 3
    'ENSMUSG00000031342', # Gpm6b           glycoprotein m6b
    'ENSMUSG00000031355', # Arhgap6         Rho GTPase activating protein 6
    'ENSMUSG00000031377', # Bmx             BMX non-receptor tyrosine kinase
    'ENSMUSG00000031379', # Pir             pirin
    'ENSMUSG00000031380', # Vegfd           vascular endothelial growth factor D
    'ENSMUSG00000031385', # Plxnb3          plexin B3
    'ENSMUSG00000031390', # Avpr2           arginine vasopressin receptor 2
    'ENSMUSG00000031391', # L1cam           L1 cell adhesion molecule
    'ENSMUSG00000031392', # Irak1           interleukin-1 receptor-associated kinase 1
    'ENSMUSG00000031400', # G6pdx           glucose-6-phosphate dehydrogenase X-linked
    'ENSMUSG00000031402', # Mpp1            membrane protein, palmitoylated
    'ENSMUSG00000031425', # Plp1            proteolipid protein (myelin) 1
    'ENSMUSG00000031438', # Rnf128          ring finger protein 128
    'ENSMUSG00000031443', # F7              coagulation factor VII
    'ENSMUSG00000031451', # Gas6            growth arrest specific 6
    'ENSMUSG00000031465', # Angpt2          angiopoietin 2
    'ENSMUSG00000031494', # Cd209a          CD209a antigen
    'ENSMUSG00000031495', # Cd209d          CD209d antigen
    'ENSMUSG00000031497', # Tnfsf13b        tumor necrosis factor (ligand) superfamily, member 13b
    'ENSMUSG00000031520', # Vegfc           vascular endothelial growth factor C
    'ENSMUSG00000031523', # Dlc1            deleted in liver cancer 1
    'ENSMUSG00000031536', # Polb            polymerase (DNA directed), beta
    'ENSMUSG00000031537', # Ikbkb           inhibitor of kappaB kinase beta
    'ENSMUSG00000031549', # Ido2            indoleamine 2,3-dioxygenase 2
    'ENSMUSG00000031551', # Ido1            indoleamine 2,3-dioxygenase 1
    'ENSMUSG00000031555', # Adam9           a disintegrin and metallopeptidase domain 9 (meltrin gamma)
    'ENSMUSG00000031557', # Plekha2         pleckstrin homology domain-containing, family A (phosphoinositide binding specific) member 2
    'ENSMUSG00000031558', # Slit2           slit homolog 2 (Drosophila)
    'ENSMUSG00000031565', # Fgfr1           fibroblast growth factor receptor 1
    'ENSMUSG00000031596', # Slc7a2          solute carrier family 7 (cationic amino acid transporter, y+ system), member 2
    'ENSMUSG00000031616', # Ednra           endothelin receptor type A
    'ENSMUSG00000031628', # Casp3           caspase 3
    'ENSMUSG00000031639', # Tlr3            toll-like receptor 3
    'ENSMUSG00000031668', # Eif2ak3         eukaryotic translation initiation factor 2 alpha kinase 3
    'ENSMUSG00000031681', # Smad1           SMAD family member 1
    'ENSMUSG00000031706', # Rfx1            regulatory factor X, 1 (influences HLA class II expression)
    'ENSMUSG00000031712', # Il15            interleukin 15
    'ENSMUSG00000031722', # Hp              haptoglobin
    'ENSMUSG00000031740', # Mmp2            matrix metallopeptidase 2
    'ENSMUSG00000031750', # Il34            interleukin 34
    'ENSMUSG00000031778', # Cx3cl1          chemokine (C-X3-C motif) ligand 1
    'ENSMUSG00000031779', # Ccl22           chemokine (C-C motif) ligand 22
    'ENSMUSG00000031780', # Ccl17           chemokine (C-C motif) ligand 17
    'ENSMUSG00000031785', # Adgrg1          adhesion G protein-coupled receptor G1
    'ENSMUSG00000031805', # Jak3            Janus kinase 3
    'ENSMUSG00000031834', # Pik3r2          phosphatidylinositol 3-kinase, regulatory subunit, polypeptide 2 (p85 beta)
    'ENSMUSG00000031838', # Ifi30           interferon gamma inducible protein 30
    'ENSMUSG00000031841', # Cdh13           cadherin 13
    'ENSMUSG00000031875', # Cmtm3           CKLF-like MARVEL transmembrane domain containing 3
    'ENSMUSG00000031885', # Cbfb            core binding factor beta
    'ENSMUSG00000031897', # Psmb10          proteasome (prosome, macropain) subunit, beta type 10
    'ENSMUSG00000031902', # Nfatc3          nuclear factor of activated T cells, cytoplasmic, calcineurin dependent 3
    'ENSMUSG00000031934', # Panx1           pannexin 1
    'ENSMUSG00000031948', # Kars            lysyl-tRNA synthetase
    'ENSMUSG00000031955', # Bcar1           breast cancer anti-estrogen resistance 1
    'ENSMUSG00000031957', # Ctrb1           chymotrypsinogen B1
    'ENSMUSG00000031963', # Bmper           BMP-binding endothelial regulator
    'ENSMUSG00000031980', # Agt             angiotensinogen (serpin peptidase inhibitor, clade A, member 8)
    'ENSMUSG00000031990', # Jam3            junction adhesion molecule 3
    'ENSMUSG00000032006', # Pdgfd           platelet-derived growth factor, D polypeptide
    'ENSMUSG00000032011', # Thy1            thymus cell antigen 1, theta
    'ENSMUSG00000032020', # Ubash3b         ubiquitin associated and SH3 domain containing, B
    'ENSMUSG00000032021', # Crtam           cytotoxic and regulatory T cell molecule
    'ENSMUSG00000032035', # Ets1            E26 avian leukemia oncogene 1, 5' domain
    'ENSMUSG00000032041', # Tirap           toll-interleukin 1 receptor (TIR) domain-containing adaptor protein
    'ENSMUSG00000032050', # Rdx             radixin
    'ENSMUSG00000032068', # Plet1           placenta expressed transcript 1
    'ENSMUSG00000032076', # Cadm1           cell adhesion molecule 1
    'ENSMUSG00000032080', # Apoa4           apolipoprotein A-IV
    'ENSMUSG00000032083', # Apoa1           apolipoprotein A-I
    'ENSMUSG00000032087', # Dscaml1         Down syndrome cell adhesion molecule like 1
    'ENSMUSG00000032092', # Mpzl2           myelin protein zero-like 2
    'ENSMUSG00000032093', # Cd3e            CD3 antigen, epsilon polypeptide
    'ENSMUSG00000032094', # Cd3d            CD3 antigen, delta polypeptide
    'ENSMUSG00000032109', # Nlrx1           NLR family member X1
    'ENSMUSG00000032114', # Slc37a4         solute carrier family 37 (glucose-6-phosphate transporter), member 4
    'ENSMUSG00000032175', # Tyk2            tyrosine kinase 2
    'ENSMUSG00000032202', # Rab27a          RAB27A, member RAS oncogene family
    'ENSMUSG00000032216', # Nedd4           neural precursor cell expressed, developmentally down-regulated 4
    'ENSMUSG00000032226', # Gcnt3           glucosaminyl (N-acetyl) transferase 3, mucin type
    'ENSMUSG00000032238', # Rora            RAR-related orphan receptor alpha
    'ENSMUSG00000032243', # Itga11          integrin alpha 11
    'ENSMUSG00000032251', # Irak1bp1        interleukin-1 receptor-associated kinase 1 binding protein 1
    'ENSMUSG00000032259', # Drd2            dopamine receptor D2
    'ENSMUSG00000032274', # Cyp19a1         cytochrome P450, family 19, subfamily a, polypeptide 1
    'ENSMUSG00000032293', # Ireb2           iron responsive element binding protein 2
    'ENSMUSG00000032312', # Csk             c-src tyrosine kinase
    'ENSMUSG00000032322', # Pstpip1         proline-serine-threonine phosphatase-interacting protein 1
    'ENSMUSG00000032344', # Mb21d1          Mab-21 domain containing 1
    'ENSMUSG00000032359', # Ctsh            cathepsin H
    'ENSMUSG00000032366', # Tpm1            tropomyosin 1, alpha
    'ENSMUSG00000032369', # Plscr1          phospholipid scramblase 1
    'ENSMUSG00000032380', # Dapk2           death-associated protein kinase 2
    'ENSMUSG00000032402', # Smad3           SMAD family member 3
    'ENSMUSG00000032419', # Tbx18           T-box18
    'ENSMUSG00000032440', # Tgfbr2          transforming growth factor, beta receptor II
    'ENSMUSG00000032446', # Eomes           eomesodermin
    'ENSMUSG00000032462', # Pik3cb          phosphatidylinositol 3-kinase, catalytic, beta polypeptide
    'ENSMUSG00000032475', # Nck1            non-catalytic region of tyrosine kinase adaptor protein 1
    'ENSMUSG00000032487', # Ptgs2           prostaglandin-endoperoxide synthase 2
    'ENSMUSG00000032491', # Nradd           neurotrophin receptor associated death domain
    'ENSMUSG00000032494', # Tdgf1           teratocarcinoma-derived growth factor 1
    'ENSMUSG00000032496', # Ltf             lactotransferrin
    'ENSMUSG00000032497', # Lrrfip2         leucine rich repeat (in FLII) interacting protein 2
    'ENSMUSG00000032498', # Mlh1            mutL homolog 1
    'ENSMUSG00000032508', # Myd88           myeloid differentiation primary response gene 88
    'ENSMUSG00000032537', # Ephb1           Eph receptor B1
    'ENSMUSG00000032554', # Trf             transferrin
    'ENSMUSG00000032577', # Mapkapk3        mitogen-activated protein kinase-activated protein kinase 3
    'ENSMUSG00000032584', # Mst1r           macrophage stimulating 1 receptor (c-met-related tyrosine kinase)
    'ENSMUSG00000032586', # Traip           TRAF-interacting protein
    'ENSMUSG00000032591', # Mst1            macrophage stimulating 1 (hepatocyte growth factor-like)
    'ENSMUSG00000032633', # Flcn            folliculin
    'ENSMUSG00000032661', # Oas3            2'-5' oligoadenylate synthetase 3
    'ENSMUSG00000032679', # Cd59a           CD59a antigen
    'ENSMUSG00000032688', # Malt1           MALT1 paracaspase
    'ENSMUSG00000032690', # Oas2            2'-5' oligoadenylate synthetase 2
    'ENSMUSG00000032691', # Nlrp3           NLR family, pyrin domain containing 3
    'ENSMUSG00000032719', # Sbspon          somatomedin B and thrombospondin, type 1 domain containing
    'ENSMUSG00000032737', # Inppl1          inositol polyphosphate phosphatase-like 1
    'ENSMUSG00000032739', # Pram1           PML-RAR alpha-regulated adaptor molecule 1
    'ENSMUSG00000032750', # Gab3            growth factor receptor bound protein 2-associated protein 3
    'ENSMUSG00000032796', # Lama1           laminin, alpha 1
    'ENSMUSG00000032815', # Fanca           Fanconi anemia, complementation group A
    'ENSMUSG00000032855', # Pkd1            polycystic kidney disease 1 homolog
    'ENSMUSG00000032860', # P2ry2           purinergic receptor P2Y, G-protein coupled 2
    'ENSMUSG00000032864', # Rag2            recombination activating gene 2
    'ENSMUSG00000032899', # Styk1           serine/threonine/tyrosine kinase 1
    'ENSMUSG00000032905', # Atg12           autophagy related 12
    'ENSMUSG00000032911', # Cspg4           chondroitin sulfate proteoglycan 4
    'ENSMUSG00000032966', # Fkbp1a          FK506 binding protein 1a
    'ENSMUSG00000032999', # Nlrp4f          NLR family, pyrin domain containing 4F
    'ENSMUSG00000033016', # Nfatc1          nuclear factor of activated T cells, cytoplasmic, calcineurin dependent 1
    'ENSMUSG00000033107', # Rnf125          ring finger protein 125
    'ENSMUSG00000033124', # Atg9a           autophagy related 9A
    'ENSMUSG00000033149', # Phldb2          pleckstrin homology like domain, family B, member 2
    'ENSMUSG00000033208', # S100b           S100 protein, beta polypeptide, neural
    'ENSMUSG00000033220', # Rac2            RAS-related C3 botulinum substrate 2
    'ENSMUSG00000033307', # Mif             macrophage migration inhibitory factor
    'ENSMUSG00000033350', # Chst2           carbohydrate sulfotransferase 2
    'ENSMUSG00000033373', # Fntb            farnesyltransferase, CAAX box, beta
    'ENSMUSG00000033392', # Clasp2          CLIP associating protein 2
    'ENSMUSG00000033454', # Zbtb1           zinc finger and BTB domain containing 1
    'ENSMUSG00000033467', # Crlf2           cytokine receptor-like factor 2
    'ENSMUSG00000033510', # Otud7a          OTU domain containing 7A
    'ENSMUSG00000033538', # Casp4           caspase 4, apoptosis-related cysteine peptidase
    'ENSMUSG00000033542', # Arhgef5         Rho guanine nucleotide exchange factor (GEF) 5
    'ENSMUSG00000033634', # Nat8f2          N-acetyltransferase 8 (GCN5-related) family member 2
    'ENSMUSG00000033717', # Adra2a          adrenergic receptor, alpha 2a
    'ENSMUSG00000033721', # Vav3            vav 3 oncogene
    'ENSMUSG00000033730', # Egr3            early growth response 3
    'ENSMUSG00000033767', # D930015E06Rik   RIKEN cDNA D930015E06 gene
    'ENSMUSG00000033777', # Tlr13           toll-like receptor 13
    'ENSMUSG00000033792', # Atp7a           ATPase, Cu++ transporting, alpha polypeptide
    'ENSMUSG00000033825', # Tpsb2           tryptase beta 2
    'ENSMUSG00000033831', # Fgb             fibrinogen beta chain
    'ENSMUSG00000033860', # Fgg             fibrinogen gamma chain
    'ENSMUSG00000033885', # Pxk             PX domain containing serine/threonine kinase
    'ENSMUSG00000033902', # Mapkbp1         mitogen-activated protein kinase binding protein 1
    'ENSMUSG00000034023', # Fancd2          Fanconi anemia, complementation group D2
    'ENSMUSG00000034028', # Cd226           CD226 antigen
    'ENSMUSG00000034066', # Farp2           FERM, RhoGEF and pleckstrin domain protein 2
    'ENSMUSG00000034087', # Nlrp4b          NLR family, pyrin domain containing 4B
    'ENSMUSG00000034116', # Vav1            vav 1 oncogene
    'ENSMUSG00000034139', # Serpini2        serine (or cysteine) peptidase inhibitor, clade I, member 2
    'ENSMUSG00000034175', # Rhbdd3          rhomboid domain containing 3
    'ENSMUSG00000034206', # Polq            polymerase (DNA directed), theta
    'ENSMUSG00000034218', # Atm             ataxia telangiectasia mutated
    'ENSMUSG00000034227', # Foxj1           forkhead box J1
    'ENSMUSG00000034254', # Agpat1          1-acylglycerol-3-phosphate O-acyltransferase 1 (lysophosphatidic acid acyltransferase, alpha)
    'ENSMUSG00000034266', # Batf            basic leucine zipper transcription factor, ATF-like
    'ENSMUSG00000034274', # Thoc5           THO complex 5
    'ENSMUSG00000034292', # Traf3ip1        TRAF3 interacting protein 1
    'ENSMUSG00000034317', # Trim59          tripartite motif-containing 59
    'ENSMUSG00000034330', # Plcg2           phospholipase C, gamma 2
    'ENSMUSG00000034359', # Skint2          selection and upkeep of intraepithelial T cells 2
    'ENSMUSG00000034371', # Tkfc            triokinase, FMN cyclase
    'ENSMUSG00000034394', # Lif             leukemia inhibitory factor
    'ENSMUSG00000034453', # Polr3b          polymerase (RNA) III (DNA directed) polypeptide B
    'ENSMUSG00000034459', # Ifit1           interferon-induced protein with tetratricopeptide repeats 1
    'ENSMUSG00000034488', # Edil3           EGF-like repeats and discoidin I-like domains 3
    'ENSMUSG00000034610', # Zcchc11         zinc finger, CCHC domain containing 11
    'ENSMUSG00000034634', # Ly6d            lymphocyte antigen 6 complex, locus D
    'ENSMUSG00000034641', # Cd300ld         CD300 molecule like family member d
    'ENSMUSG00000034652', # Cd300a          CD300A molecule
    'ENSMUSG00000034653', # Ythdc2          YTH domain containing 2
    'ENSMUSG00000034664', # Itga2b          integrin alpha 2b
    'ENSMUSG00000034675', # Dbn1            drebrin 1
    'ENSMUSG00000034690', # Nlrp4c          NLR family, pyrin domain containing 4C
    'ENSMUSG00000034786', # Gpsm3           G-protein signalling modulator 3 (AGS3-like, C. elegans)
    'ENSMUSG00000034801', # Sos2            son of sevenless homolog 2 (Drosophila)
    'ENSMUSG00000034833', # Tespa1          thymocyte expressed, positive selection associated 1
    'ENSMUSG00000034845', # Plvap           plasmalemma vesicle associated protein
    'ENSMUSG00000034855', # Cxcl10          chemokine (C-X-C motif) ligand 10
    'ENSMUSG00000034881', # Tbxa2r          thromboxane A2 receptor
    'ENSMUSG00000034889', # Cactin          cactin, spliceosome C complex subunit
    'ENSMUSG00000034957', # Cebpa           CCAAT/enhancer binding protein (C/EBP), alpha
    'ENSMUSG00000034974', # Dapk3           death-associated protein kinase 3
    'ENSMUSG00000034987', # Hrh2            histamine receptor H2
    'ENSMUSG00000035000', # Dpp4            dipeptidylpeptidase 4
    'ENSMUSG00000035031', # C8a             complement component 8, alpha polypeptide
    'ENSMUSG00000035042', # Ccl5            chemokine (C-C motif) ligand 5
    'ENSMUSG00000035148', # Gpr33           G protein-coupled receptor 33
    'ENSMUSG00000035158', # Mitf            microphthalmia-associated transcription factor
    'ENSMUSG00000035177', # Nlrp2           NLR family, pyrin domain containing 2
    'ENSMUSG00000035186', # Ubd             ubiquitin D
    'ENSMUSG00000035206', # Sppl2b          signal peptide peptidase like 2B
    'ENSMUSG00000035235', # Trim13          tripartite motif-containing 13
    'ENSMUSG00000035247', # Hectd1          HECT domain containing 1
    'ENSMUSG00000035258', # Abi3bp          ABI gene family, member 3 (NESH) binding protein
    'ENSMUSG00000035273', # Hpse            heparanase
    'ENSMUSG00000035279', # Ssc5d           scavenger receptor cysteine rich family, 5 domains
    'ENSMUSG00000035352', # Ccl12           chemokine (C-C motif) ligand 12
    'ENSMUSG00000035356', # Nfkbiz          nuclear factor of kappa light polypeptide gene enhancer in B cells inhibitor, zeta
    'ENSMUSG00000035373', # Ccl7            chemokine (C-C motif) ligand 7
    'ENSMUSG00000035385', # Ccl2            chemokine (C-C motif) ligand 2
    'ENSMUSG00000035448', # Ccr3            chemokine (C-C motif) receptor 3
    'ENSMUSG00000035629', # Rubcn           RUN domain and cysteine-rich domain containing, Beclin 1-interacting protein
    'ENSMUSG00000035673', # Sbno2           strawberry notch homolog 2 (Drosophila)
    'ENSMUSG00000035678', # Tnfsf9          tumor necrosis factor (ligand) superfamily, member 9
    'ENSMUSG00000035692', # Isg15           ISG15 ubiquitin-like modifier
    'ENSMUSG00000035725', # Prkx            protein kinase, X-linked
    'ENSMUSG00000035799', # Twist1          twist basic helix-loop-helix transcription factor 1
    'ENSMUSG00000035834', # Polr3g          polymerase (RNA) III (DNA directed) polypeptide G
    'ENSMUSG00000035873', # Pawr            PRKC, apoptosis, WT1, regulator
    'ENSMUSG00000035914', # Cd276           CD276 antigen
    'ENSMUSG00000035929', # H2-Q4           histocompatibility 2, Q region locus 4
    'ENSMUSG00000035930', # Chst4           carbohydrate (chondroitin 6/keratan) sulfotransferase 4
    'ENSMUSG00000036006', # Fam65b          family with sequence similarity 65, member B
    'ENSMUSG00000036057', # Ptpn23          protein tyrosine phosphatase, non-receptor type 23
    'ENSMUSG00000036091', # Hyal3           hyaluronoglucosaminidase 3
    'ENSMUSG00000036103', # Colec12         collectin sub-family member 12
    'ENSMUSG00000036111', # Lmo1            LIM domain only 1
    'ENSMUSG00000036117', # Il5             interleukin 5
    'ENSMUSG00000036202', # Rif1            replication timing regulatory factor 1
    'ENSMUSG00000036353', # P2ry12          purinergic receptor P2Y, G-protein coupled 12
    'ENSMUSG00000036381', # P2ry14          purinergic receptor P2Y, G-protein coupled, 14
    'ENSMUSG00000036427', # Gpi1            glucose phosphate isomerase 1
    'ENSMUSG00000036446', # Lum             lumican
    'ENSMUSG00000036461', # Elf1            E74-like factor 1
    'ENSMUSG00000036469', # March1          membrane-associated ring finger (C3HC4) 1
    'ENSMUSG00000036504', # Phpt1           phosphohistidine phosphatase 1
    'ENSMUSG00000036526', # Card11          caspase recruitment domain family, member 11
    'ENSMUSG00000036587', # Fut7            fucosyltransferase 7
    'ENSMUSG00000036594', # H2-Aa           histocompatibility 2, class II antigen A, alpha
    'ENSMUSG00000036606', # Plxnb2          plexin B2
    'ENSMUSG00000036712', # Cyld            CYLD lysine 63 deubiquitinase
    'ENSMUSG00000036748', # Cuedc2          CUE domain containing 2
    'ENSMUSG00000036856', # Wnt4            wingless-type MMTV integration site family, member 4
    'ENSMUSG00000036867', # Smad6           SMAD family member 6
    'ENSMUSG00000036887', # C1qa            complement component 1, q subcomponent, alpha polypeptide
    'ENSMUSG00000036894', # Rap2b           RAP2B, member of RAS oncogene family
    'ENSMUSG00000036896', # C1qc            complement component 1, q subcomponent, C chain
    'ENSMUSG00000036904', # Fzd8            frizzled class receptor 8
    'ENSMUSG00000036905', # C1qb            complement component 1, q subcomponent, beta polypeptide
    'ENSMUSG00000036908', # Unc93b1         unc-93 homolog B1 (C. elegans)
    'ENSMUSG00000036931', # Nfkbid          nuclear factor of kappa light polypeptide gene enhancer in B cells inhibitor, delta
    'ENSMUSG00000036940', # Kdm1a           lysine (K)-specific demethylase 1A
    'ENSMUSG00000036943', # Rab8b           RAB8B, member RAS oncogene family
    'ENSMUSG00000036986', # Pml             promyelocytic leukemia
    'ENSMUSG00000037025', # Foxa2           forkhead box A2
    'ENSMUSG00000037034', # Pax1            paired box 1
    'ENSMUSG00000037035', # Inhbb           inhibin beta-B
    'ENSMUSG00000037104', # Socs5           suppressor of cytokine signaling 5
    'ENSMUSG00000037130', # H2-M10.6        histocompatibility 2, M region locus 10.6
    'ENSMUSG00000037138', # Aff3            AF4/FMR2 family, member 3
    'ENSMUSG00000037171', # Nodal           nodal
    'ENSMUSG00000037202', # Prf1            perforin 1 (pore forming protein)
    'ENSMUSG00000037246', # H2-M10.5        histocompatibility 2, M region locus 10.5
    'ENSMUSG00000037316', # Bag4            BCL2-associated athanogene 4
    'ENSMUSG00000037321', # Tap1            transporter 1, ATP-binding cassette, sub-family B (MDR/TAP)
    'ENSMUSG00000037334', # H2-M1           histocompatibility 2, M region locus 1
    'ENSMUSG00000037346', # Hrh4            histamine receptor H4
    'ENSMUSG00000037362', # Nov             nephroblastoma overexpressed gene
    'ENSMUSG00000037370', # Enpp1           ectonucleotide pyrophosphatase/phosphodiesterase 1
    'ENSMUSG00000037379', # Spon2           spondin 2, extracellular matrix protein
    'ENSMUSG00000037405', # Icam1           intercellular adhesion molecule 1
    'ENSMUSG00000037411', # Serpine1        serine (or cysteine) peptidase inhibitor, clade E, member 1
    'ENSMUSG00000037440', # Vnn1            vanin 1
    'ENSMUSG00000037447', # Arid5a          AT rich interactive domain 5A (MRF1-like)
    'ENSMUSG00000037487', # Ubr5            ubiquitin protein ligase E3 component n-recognin 5
    'ENSMUSG00000037523', # Mavs            mitochondrial antiviral signaling protein
    'ENSMUSG00000037537', # H2-M11          histocompatibility 2, M region locus 11
    'ENSMUSG00000037548', # H2-DMb2         histocompatibility 2, class II, locus Mb2
    'ENSMUSG00000037580', # Gch1            GTP cyclohydrolase 1
    'ENSMUSG00000037613', # Tnfrsf23        tumor necrosis factor receptor superfamily, member 23
    'ENSMUSG00000037643', # Prkci           protein kinase C, iota
    'ENSMUSG00000037649', # H2-DMa          histocompatibility 2, class II, locus DMa
    'ENSMUSG00000037712', # Fermt2          fermitin family member 2
    'ENSMUSG00000037731', # Themis2         thymocyte selection associated family member 2
    'ENSMUSG00000037780', # Mbl1            mannose-binding lectin (protein A) 1
    'ENSMUSG00000037820', # Tgm2            transglutaminase 2, C polypeptide
    'ENSMUSG00000037860', # Aim2            absent in melanoma 2
    'ENSMUSG00000037872', # Ackr1           atypical chemokine receptor 1 (Duffy blood group)
    'ENSMUSG00000037921', # Ddx60           DEAD (Asp-Glu-Ala-Asp) box polypeptide 60
    'ENSMUSG00000037922', # Bank1           B cell scaffold protein with ankyrin repeats 1
    'ENSMUSG00000037942', # Crp             C-reactive protein, pentraxin-related
    'ENSMUSG00000037944', # Ccr7            chemokine (C-C motif) receptor 7
    'ENSMUSG00000037966', # Ninj1           ninjurin 1
    'ENSMUSG00000037992', # Rara            retinoic acid receptor, alpha
    'ENSMUSG00000038007', # Acer2           alkaline ceramidase 2
    'ENSMUSG00000038037', # Socs1           suppressor of cytokine signaling 1
    'ENSMUSG00000038058', # Nod1            nucleotide-binding oligomerization domain containing 1
    'ENSMUSG00000038067', # Csf3            colony stimulating factor 3 (granulocyte)
    'ENSMUSG00000038128', # Camk4           calcium/calmodulin-dependent protein kinase IV
    'ENSMUSG00000038147', # Cd84            CD84 antigen
    'ENSMUSG00000038151', # Prdm1           PR domain containing 1, with ZNF domain
    'ENSMUSG00000038160', # Atg5            autophagy related 5
    'ENSMUSG00000038179', # Slamf7          SLAM family member 7
    'ENSMUSG00000038213', # Tapbpl          TAP binding protein-like
    'ENSMUSG00000038224', # Serpinf2        serine (or cysteine) peptidase inhibitor, clade F, member 2
    'ENSMUSG00000038227', # Hoxa9           homeobox A9
    'ENSMUSG00000038235', # F11r            F11 receptor
    'ENSMUSG00000038236', # Hoxa7           homeobox A7
    'ENSMUSG00000038260', # Trpm4           transient receptor potential cation channel, subfamily M, member 4
    'ENSMUSG00000038264', # Sema7a          sema domain, immunoglobulin domain (Ig), and GPI membrane anchor, (semaphorin) 7A
    'ENSMUSG00000038274', # Fau             Finkel-Biskis-Reilly murine sarcoma virus (FBR-MuSV) ubiquitously expressed (fox derived)
    'ENSMUSG00000038280', # Ostm1           osteopetrosis associated transmembrane protein 1
    'ENSMUSG00000038301', # Snx10           sorting nexin 10
    'ENSMUSG00000038357', # Camp            cathelicidin antimicrobial peptide
    'ENSMUSG00000038387', # Rras            related RAS viral (r-ras) oncogene
    'ENSMUSG00000038418', # Egr1            early growth response 1
    'ENSMUSG00000038453', # Srcin1          SRC kinase signaling inhibitor 1
    'ENSMUSG00000038495', # Otud7b          OTU domain containing 7B
    'ENSMUSG00000038517', # Tbkbp1          TBK1 binding protein 1
    'ENSMUSG00000038521', # C1s1            complement component 1, s subcomponent 1
    'ENSMUSG00000038527', # C1rl            complement component 1, r subcomponent-like
    'ENSMUSG00000038612', # Mcl1            myeloid cell leukemia sequence 1
    'ENSMUSG00000038628', # Polr3k          polymerase (RNA) III (DNA directed) polypeptide K
    'ENSMUSG00000038642', # Ctss            cathepsin S
    'ENSMUSG00000038676', # Ucn             urocortin
    'ENSMUSG00000038745', # Nlrp6           NLR family, pyrin domain containing 6
    'ENSMUSG00000038751', # Ptk6            PTK6 protein tyrosine kinase 6
    'ENSMUSG00000038855', # Itpkb           inositol 1,4,5-trisphosphate 3-kinase B
    'ENSMUSG00000038884', # A230050P20Rik   RIKEN cDNA A230050P20 gene
    'ENSMUSG00000038910', # Plcl2           phospholipase C-like 2
    'ENSMUSG00000039004', # Bmp6            bone morphogenetic protein 6
    'ENSMUSG00000039005', # Tlr4            toll-like receptor 4
    'ENSMUSG00000039041', # Adrm1           adhesion regulating molecule 1
    'ENSMUSG00000039089', # L3mbtl3         l(3)mbt-like 3 (Drosophila)
    'ENSMUSG00000039115', # Itga9           integrin alpha 9
    'ENSMUSG00000039145', # Camk1d          calcium/calmodulin-dependent protein kinase ID
    'ENSMUSG00000039146', # Ifi44l          interferon-induced protein 44 like
    'ENSMUSG00000039148', # Sart1           squamous cell carcinoma antigen recognized by T cells 1
    'ENSMUSG00000039153', # Runx2           runt related transcription factor 2
    'ENSMUSG00000039191', # Rbpj            recombination signal binding protein for immunoglobulin kappa J region
    'ENSMUSG00000039193', # Nlrc4           NLR family, CARD domain containing 4
    'ENSMUSG00000039196', # Orm1            orosomucoid 1
    'ENSMUSG00000039197', # Adk             adenosine kinase
    'ENSMUSG00000039217', # Il18            interleukin 18
    'ENSMUSG00000039232', # Stx11           syntaxin 11
    'ENSMUSG00000039236', # Isg20           interferon-stimulated protein
    'ENSMUSG00000039239', # Tgfb2           transforming growth factor, beta 2
    'ENSMUSG00000039285', # Azi2            5-azacytidine induced gene 2
    'ENSMUSG00000039304', # Tnfsf10         tumor necrosis factor (ligand) superfamily, member 10
    'ENSMUSG00000039315', # Clnk            cytokine-dependent hematopoietic cell linker
    'ENSMUSG00000039316', # Rftn1           raftlin lipid raft linker 1
    'ENSMUSG00000039323', # Igfbp2          insulin-like growth factor binding protein 2
    'ENSMUSG00000039364', # Sectm1b         secreted and transmembrane 1B
    'ENSMUSG00000039377', # Hlx             H2.0-like homeobox
    'ENSMUSG00000039384', # Dusp10          dual specificity phosphatase 10
    'ENSMUSG00000039519', # Cyp7b1          cytochrome P450, family 7, subfamily b, polypeptide 1
    'ENSMUSG00000039521', # Foxp3           forkhead box P3
    'ENSMUSG00000039621', # Prex1           phosphatidylinositol-3,4,5-trisphosphate-dependent Rac exchange factor 1
    'ENSMUSG00000039661', # Dusp26          dual specificity phosphatase 26 (putative)
    'ENSMUSG00000039699', # Batf2           basic leucine zipper transcription factor, ATF-like 2
    'ENSMUSG00000039703', # Nploc4          NPL4 homolog, ubiquitin recognition factor
    'ENSMUSG00000039748', # Exo1            exonuclease 1
    'ENSMUSG00000039844', # Rapgef1         Rap guanine nucleotide exchange factor (GEF) 1
    'ENSMUSG00000039853', # Trim14          tripartite motif-containing 14
    'ENSMUSG00000039910', # Cited2          Cbp/p300-interacting transactivator, with Glu/Asp-rich carboxy-terminal domain, 2
    'ENSMUSG00000039936', # Pik3cd          phosphatidylinositol 3-kinase catalytic delta polypeptide
    'ENSMUSG00000039942', # Ptger4          prostaglandin E receptor 4 (subtype EP4)
    'ENSMUSG00000039952', # Dag1            dystroglycan 1
    'ENSMUSG00000039981', # Zc3h12d         zinc finger CCCH type containing 12D
    'ENSMUSG00000040016', # Ptger3          prostaglandin E receptor 3 (subtype EP3)
    'ENSMUSG00000040017', # Saa4            serum amyloid A 4
    'ENSMUSG00000040026', # Saa3            serum amyloid A 3
    'ENSMUSG00000040136', # Abcc8           ATP-binding cassette, sub-family C (CFTR/MRP), member 8
    'ENSMUSG00000040152', # Thbs1           thrombospondin 1
    'ENSMUSG00000040247', # Tbc1d10c        TBC1 domain family, member 10c
    'ENSMUSG00000040249', # Lrp1            low density lipoprotein receptor-related protein 1
    'ENSMUSG00000040264', # Gbp2b           guanylate binding protein 2b
    'ENSMUSG00000040268', # Plekha1         pleckstrin homology domain containing, family A (phosphoinositide binding specific) member 1
    'ENSMUSG00000040274', # Cdk6            cyclin-dependent kinase 6
    'ENSMUSG00000040296', # Ddx58           DEAD (Asp-Glu-Ala-Asp) box polypeptide 58
    'ENSMUSG00000040314', # Ctsg            cathepsin G
    'ENSMUSG00000040329', # Il7             interleukin 7
    'ENSMUSG00000040405', # Havcr1          hepatitis A virus cellular receptor 1
    'ENSMUSG00000040423', # Rc3h1           RING CCCH (C3H) domains 1
    'ENSMUSG00000040447', # Spns2           spinster homolog 2
    'ENSMUSG00000040451', # Sgms1           sphingomyelin synthase 1
    'ENSMUSG00000040483', # Xaf1            XIAP associated factor 1
    'ENSMUSG00000040511', # Pvr             poliovirus receptor
    'ENSMUSG00000040522', # Tlr8            toll-like receptor 8
    'ENSMUSG00000040528', # Milr1           mast cell immunoglobulin like receptor 1
    'ENSMUSG00000040552', # C3ar1           complement component 3a receptor 1
    'ENSMUSG00000040592', # Cd79b           CD79B antigen
    'ENSMUSG00000040601', # Nlrp4a          NLR family, pyrin domain containing 4A
    'ENSMUSG00000040627', # Aicda           activation-induced cytidine deaminase
    'ENSMUSG00000040663', # Clcf1           cardiotrophin-like cytokine factor 1
    'ENSMUSG00000040690', # Col16a1         collagen, type XVI, alpha 1
    'ENSMUSG00000040722', # Scamp5          secretory carrier membrane protein 5
    'ENSMUSG00000040751', # Lat2            linker for activation of T cells family, member 2
    'ENSMUSG00000040770', # Il25            interleukin 25
    'ENSMUSG00000040809', # Chil3           chitinase-like 3
    'ENSMUSG00000040818', # Dennd6a         DENN/MADD domain containing 6A
    'ENSMUSG00000040899', # Ccr6            chemokine (C-C motif) receptor 6
    'ENSMUSG00000040945', # Rcc2            regulator of chromosome condensation 2
    'ENSMUSG00000040952', # Rps19           ribosomal protein S19
    'ENSMUSG00000040987', # Mill2           MHC I like leukocyte 2
    'ENSMUSG00000040998', # Npnt            nephronectin
    'ENSMUSG00000041000', # Trim62          tripartite motif-containing 62
    'ENSMUSG00000041058', # Wwp1            WW domain containing E3 ubiquitin protein ligase 1
    'ENSMUSG00000041075', # Fzd7            frizzled class receptor 7
    'ENSMUSG00000041120', # Nbl1            neuroblastoma, suppression of tumorigenicity 1
    'ENSMUSG00000041135', # Ripk2           receptor (TNFRSF)-interacting serine-threonine kinase 2
    'ENSMUSG00000041187', # Prkd2           protein kinase D2
    'ENSMUSG00000041193', # Pla2g5          phospholipase A2, group V
    'ENSMUSG00000041202', # Pla2g2d         phospholipase A2, group IID
    'ENSMUSG00000041235', # Chd7            chromodomain helicase DNA binding protein 7
    'ENSMUSG00000041241', # Mul1            mitochondrial ubiquitin ligase activator of NFKB 1
    'ENSMUSG00000041247', # Lamp3           lysosomal-associated membrane protein 3
    'ENSMUSG00000041301', # Cftr            cystic fibrosis transmembrane conductance regulator
    'ENSMUSG00000041323', # Ak7             adenylate kinase 7
    'ENSMUSG00000041343', # Ankrd42         ankyrin repeat domain 42
    'ENSMUSG00000041347', # Bdkrb1          bradykinin receptor, beta 1
    'ENSMUSG00000041351', # Rap1gap         Rap1 GTPase-activating protein
    'ENSMUSG00000041415', # Dicer1          dicer 1, ribonuclease type III
    'ENSMUSG00000041417', # Pik3r1          phosphatidylinositol 3-kinase, regulatory subunit, polypeptide 1 (p85 alpha)
    'ENSMUSG00000041439', # Mfsd6           major facilitator superfamily domain containing 6
    'ENSMUSG00000041481', # Serpina3g       serine (or cysteine) peptidase inhibitor, clade A, member 3G
    'ENSMUSG00000041488', # Stx3            syntaxin 3
    'ENSMUSG00000041498', # Kif14           kinesin family member 14
    'ENSMUSG00000041515', # Irf8            interferon regulatory factor 8
    'ENSMUSG00000041538', # H2-Ob           histocompatibility 2, O region beta locus
    'ENSMUSG00000041607', # Mbp             myelin basic protein
    'ENSMUSG00000041736', # Tspo            translocator protein
    'ENSMUSG00000041754', # Trem3           triggering receptor expressed on myeloid cells 3
    'ENSMUSG00000041827', # Oasl1           2'-5' oligoadenylate synthetase-like 1
    'ENSMUSG00000041836', # Ptpre           protein tyrosine phosphatase, receptor type, E
    'ENSMUSG00000041845', # Rhod            ras homolog family member D
    'ENSMUSG00000041872', # Il17f           interleukin 17F
    'ENSMUSG00000041954', # Tnfrsf18        tumor necrosis factor receptor superfamily, member 18
    'ENSMUSG00000041959', # S100a10         S100 calcium binding protein A10 (calpactin)
    'ENSMUSG00000042190', # Cmklr1          chemokine-like receptor 1
    'ENSMUSG00000042228', # Lyn             LYN proto-oncogene, Src family tyrosine kinase
    'ENSMUSG00000042244', # Pglyrp3         peptidoglycan recognition protein 3
    'ENSMUSG00000042250', # Pglyrp4         peptidoglycan recognition protein 4
    'ENSMUSG00000042258', # Isl1            ISL1 transcription factor, LIM/homeodomain
    'ENSMUSG00000042262', # Ccr8            chemokine (C-C motif) receptor 8
    'ENSMUSG00000042265', # Trem1           triggering receptor expressed on myeloid cells 1
    'ENSMUSG00000042284', # Itga1           integrin alpha 1
    'ENSMUSG00000042286', # Stab1           stabilin 1
    'ENSMUSG00000042289', # Hsd3b7          hydroxy-delta-5-steroid dehydrogenase, 3 beta- and steroid delta-isomerase 7
    'ENSMUSG00000042306', # S100a14         S100 calcium binding protein A14
    'ENSMUSG00000042333', # Tnfrsf14        tumor necrosis factor receptor superfamily, member 14 (herpesvirus entry mediator)
    'ENSMUSG00000042345', # Ubash3a         ubiquitin associated and SH3 domain containing, A
    'ENSMUSG00000042349', # Ikbke           inhibitor of kappaB kinase epsilon
    'ENSMUSG00000042351', # Grap2           GRB2-related adaptor protein 2
    'ENSMUSG00000042406', # Atf4            activating transcription factor 4
    'ENSMUSG00000042419', # Nfkbil1         nuclear factor of kappa light polypeptide gene enhancer in B cells inhibitor like 1
    'ENSMUSG00000042429', # Adora1          adenosine A1 receptor
    'ENSMUSG00000042474', # Fcmr            Fc fragment of IgM receptor
    'ENSMUSG00000042557', # Sin3a           transcriptional regulator, SIN3A (yeast)
    'ENSMUSG00000042569', # Dhrs7b          dehydrogenase/reductase (SDR family) member 7B
    'ENSMUSG00000042677', # Zc3h12a         zinc finger CCCH type containing 12A
    'ENSMUSG00000042682', # Selenok         selenoprotein K
    'ENSMUSG00000042726', # Trafd1          TRAF type zinc finger domain containing 1
    'ENSMUSG00000042812', # Foxf1           forkhead box F1
    'ENSMUSG00000042817', # Flt3            FMS-like tyrosine kinase 3
    'ENSMUSG00000042961', # Egflam          EGF-like, fibronectin type III and laminin G domains
    'ENSMUSG00000042993', # Ifnk            interferon kappa
    'ENSMUSG00000043008', # Klhl6           kelch-like 6
    'ENSMUSG00000043013', # Onecut1         one cut domain, family member 1
    'ENSMUSG00000043051', # Disc1           disrupted in schizophrenia 1
    'ENSMUSG00000043088', # Il17re          interleukin 17 receptor E
    'ENSMUSG00000043279', # Trim56          tripartite motif-containing 56
    'ENSMUSG00000043421', # Hilpda          hypoxia inducible lipid droplet associated
    'ENSMUSG00000043496', # Tril            TLR4 interactor with leucine-rich repeats
    'ENSMUSG00000043631', # Ecm2            extracellular matrix protein 2, female organ and adipocyte specific
    'ENSMUSG00000043635', # Adamts3         a disintegrin-like and metallopeptidase (reprolysin type) with thrombospondin type 1 motif, 3
    'ENSMUSG00000043733', # Ptpn11          protein tyrosine phosphatase, non-receptor type 11
    'ENSMUSG00000043787', # Defb12          defensin beta 12
    'ENSMUSG00000043909', # Trp53bp1        transformation related protein 53 binding protein 1
    'ENSMUSG00000043953', # Ccrl2           chemokine (C-C motif) receptor-like 2
    'ENSMUSG00000044024', # Rell2           RELT-like 2
    'ENSMUSG00000044042', # Fmn1            formin 1
    'ENSMUSG00000044052', # Ccr10           chemokine (C-C motif) receptor 10
    'ENSMUSG00000044103', # Il1f9           interleukin 1 family, member 9
    'ENSMUSG00000044162', # Tnip3           TNFAIP3 interacting protein 3
    'ENSMUSG00000044206', # Vsig4           V-set and immunoglobulin domain containing 4
    'ENSMUSG00000044220', # Nkx2-3          NK2 homeobox 3
    'ENSMUSG00000044222', # Defb13          defensin beta 13
    'ENSMUSG00000044244', # Il20rb          interleukin 20 receptor beta
    'ENSMUSG00000044249', # Defb29          defensin beta 29
    'ENSMUSG00000044258', # Ctla2a          cytotoxic T lymphocyte-associated protein 2 alpha
    'ENSMUSG00000044288', # Cnr1            cannabinoid receptor 1 (brain)
    'ENSMUSG00000044303', # Cdkn2a          cyclin-dependent kinase inhibitor 2A
    'ENSMUSG00000044340', # Phlpp1          PH domain and leucine rich repeat protein phosphatase 1
    'ENSMUSG00000044534', # Ackr2           atypical chemokine receptor 2
    'ENSMUSG00000044583', # Tlr7            toll-like receptor 7
    'ENSMUSG00000044701', # Il27            interleukin 27
    'ENSMUSG00000044703', # Phf11a          PHD finger protein 11A
    'ENSMUSG00000044748', # Defb1           defensin beta 1
    'ENSMUSG00000044768', # D1Ertd622e      DNA segment, Chr 1, ERATO Doi 622, expressed
    'ENSMUSG00000044786', # Zfp36           zinc finger protein 36
    'ENSMUSG00000044811', # Cd300c2         CD300C molecule 2
    'ENSMUSG00000044813', # Shb             src homology 2 domain-containing transforming protein B
    'ENSMUSG00000044827', # Tlr1            toll-like receptor 1
    'ENSMUSG00000044863', # Defb36          defensin beta 36
    'ENSMUSG00000044903', # Psg22           pregnancy-specific glycoprotein 22
    'ENSMUSG00000045005', # Fzd5            frizzled class receptor 5
    'ENSMUSG00000045038', # Prkce           protein kinase C, epsilon
    'ENSMUSG00000045078', # Rnf216          ring finger protein 216
    'ENSMUSG00000045092', # S1pr1           sphingosine-1-phosphate receptor 1
    'ENSMUSG00000045103', # Dmd             dystrophin, muscular dystrophy
    'ENSMUSG00000045318', # Adra2c          adrenergic receptor, alpha 2c
    'ENSMUSG00000045322', # Tlr9            toll-like receptor 9
    'ENSMUSG00000045362', # Tnfrsf26        tumor necrosis factor receptor superfamily, member 26
    'ENSMUSG00000045364', # Ifne            interferon epsilon
    'ENSMUSG00000045394', # Epcam           epithelial cell adhesion molecule
    'ENSMUSG00000045551', # Fpr1            formyl peptide receptor 1
    'ENSMUSG00000045636', # Mtus1           mitochondrial tumor suppressor 1
    'ENSMUSG00000045693', # Nlrp4e          NLR family, pyrin domain containing 4E
    'ENSMUSG00000045730', # Adrb2           adrenergic receptor, beta 2
    'ENSMUSG00000045817', # Zfp36l2         zinc finger protein 36, C3H type-like 2
    'ENSMUSG00000045827', # Serpinb9        serine (or cysteine) peptidase inhibitor, clade B, member 9
    'ENSMUSG00000045932', # Ifit2           interferon-induced protein with tetratricopeptide repeats 2
    'ENSMUSG00000045991', # Onecut2         one cut domain, family member 2
    'ENSMUSG00000046006', # Gapt            Grb2-binding adaptor, transmembrane
    'ENSMUSG00000046034', # Otulin          OTU deubiquitinase with linear linkage specificity
    'ENSMUSG00000046080', # Clec9a          C-type lectin domain family 9, member a
    'ENSMUSG00000046108', # Il17c           interleukin 17C
    'ENSMUSG00000046207', # Pik3r6          phosphoinositide-3-kinase, regulatory subunit 6
    'ENSMUSG00000046318', # Ccbe1           collagen and calcium binding EGF domains 1
    'ENSMUSG00000046714', # Foxc2           forkhead box C2
    'ENSMUSG00000046718', # Bst2            bone marrow stromal cell antigen 2
    'ENSMUSG00000046845', # Il1f10          interleukin 1 family, member 10
    'ENSMUSG00000046879', # Irgm1           immunity-related GTPase family M member 1
    'ENSMUSG00000047098', # Rnf31           ring finger protein 31
    'ENSMUSG00000047123', # Ticam1          toll-like receptor adaptor molecule 1
    'ENSMUSG00000047139', # Cd24a           CD24a antigen
    'ENSMUSG00000047246', # Hist1h2be       histone cluster 1, H2be
    'ENSMUSG00000047250', # Ptgs1           prostaglandin-endoperoxide synthase 1
    'ENSMUSG00000047293', # Gpr15           G protein-coupled receptor 15
    'ENSMUSG00000047557', # Lxn             latexin
    'ENSMUSG00000047638', # Nr1h4           nuclear receptor subfamily 1, group H, member 4
    'ENSMUSG00000047798', # Cd300lf         CD300 molecule like family member F
    'ENSMUSG00000047810', # Ccdc88b         coiled-coil domain containing 88B
    'ENSMUSG00000047821', # Trim16          tripartite motif-containing 16
    'ENSMUSG00000047880', # Cxcr5           chemokine (C-X-C motif) receptor 5
    'ENSMUSG00000047898', # Ccr4            chemokine (C-C motif) receptor 4
    'ENSMUSG00000048031', # Fcrl5           Fc receptor-like 5
    'ENSMUSG00000048062', # Fpr-rs4         formyl peptide receptor, related sequence 4
    'ENSMUSG00000048120', # Entpd1          ectonucleoside triphosphate diphosphohydrolase 1
    'ENSMUSG00000048163', # Selplg          selectin, platelet (p-selectin) ligand
    'ENSMUSG00000048231', # H2-M10.4        histocompatibility 2, M region locus 10.4
    'ENSMUSG00000048251', # Bcl11b          B cell leukemia/lymphoma 11B
    'ENSMUSG00000048376', # F2r             coagulation factor II (thrombin) receptor
    'ENSMUSG00000048498', # Cd300e          CD300E molecule
    'ENSMUSG00000048500', # Defb15          defensin beta 15
    'ENSMUSG00000048502', # Duxbl1          double homeobox B-like 1
    'ENSMUSG00000048521', # Cxcr6           chemokine (C-X-C motif) receptor 6
    'ENSMUSG00000048534', # Jaml            None
    'ENSMUSG00000048583', # Igf2            insulin-like growth factor 2
    'ENSMUSG00000048806', # Ifnb1           interferon beta 1, fibroblast
    'ENSMUSG00000048826', # Dact2           dishevelled-binding antagonist of beta-catenin 2
    'ENSMUSG00000048915', # Efna5           ephrin A5
    'ENSMUSG00000048970', # C1galt1c1       C1GALT1-specific chaperone 1
    'ENSMUSG00000049001', # Ndnf            neuron-derived neurotrophic factor
    'ENSMUSG00000049093', # Il23r           interleukin 23 receptor
    'ENSMUSG00000049103', # Ccr2            chemokine (C-C motif) receptor 2
    'ENSMUSG00000049109', # Themis          thymocyte selection associated
    'ENSMUSG00000049115', # Agtr1a          angiotensin II receptor, type 1a
    'ENSMUSG00000049130', # C5ar1           complement component 5a receptor 1
    'ENSMUSG00000049410', # Zfp683          zinc finger protein 683
    'ENSMUSG00000049560', # Defb20          defensin beta 20
    'ENSMUSG00000049577', # Zfpm1           zinc finger protein, multitype 1
    'ENSMUSG00000049686', # Orai1           ORAI calcium release-activated calcium modulator 1
    'ENSMUSG00000049709', # Nlrp10          NLR family, pyrin domain containing 10
    'ENSMUSG00000049717', # Lig4            ligase IV, DNA, ATP-dependent
    'ENSMUSG00000049723', # Mmp12           matrix metallopeptidase 12
    'ENSMUSG00000049791', # Fzd4            frizzled class receptor 4
    'ENSMUSG00000049796', # Crh             corticotropin releasing hormone
    'ENSMUSG00000049871', # Nlrc3           NLR family, CARD domain containing 3
    'ENSMUSG00000050132', # Sarm1           sterile alpha and HEAT/Armadillo motif containing 1
    'ENSMUSG00000050199', # Lgr4            leucine-rich repeat-containing G protein-coupled receptor 4
    'ENSMUSG00000050232', # Cxcr3           chemokine (C-X-C motif) receptor 3
    'ENSMUSG00000050241', # Klre1           killer cell lectin-like receptor family E member 1
    'ENSMUSG00000050272', # Dscam           Down syndrome cell adhesion molecule
    'ENSMUSG00000050335', # Lgals3          lectin, galactose binding, soluble 3
    'ENSMUSG00000050350', # Gpr18           G protein-coupled receptor 18
    'ENSMUSG00000050357', # Carmil2         capping protein regulator and myosin 1 linker 2
    'ENSMUSG00000050370', # Ch25h           cholesterol 25-hydroxylase
    'ENSMUSG00000050377', # Il31ra          interleukin 31 receptor A
    'ENSMUSG00000050395', # Tnfsf15         tumor necrosis factor (ligand) superfamily, member 15
    'ENSMUSG00000050440', # Hamp            hepcidin antimicrobial peptide
    'ENSMUSG00000050645', # Defb19          defensin beta 19
    'ENSMUSG00000050711', # Scg2            secretogranin II
    'ENSMUSG00000050747', # Trim15          tripartite motif-containing 15
    'ENSMUSG00000050799', # Hist1h2ba       histone cluster 1, H2ba
    'ENSMUSG00000050830', # Vwc2            von Willebrand factor C domain containing 2
    'ENSMUSG00000050953', # Gja1            gap junction protein, alpha 1
    'ENSMUSG00000050965', # Prkca           protein kinase C, alpha
    'ENSMUSG00000051076', # Vtcn1           V-set domain containing T cell activation inhibitor 1
    'ENSMUSG00000051136', # Ghsr            growth hormone secretagogue receptor
    'ENSMUSG00000051159', # Cited1          Cbp/p300-interacting transactivator with Glu/Asp-rich carboxy-terminal domain 1
    'ENSMUSG00000051177', # Plcb1           phospholipase C, beta 1
    'ENSMUSG00000051212', # Gpr183          G protein-coupled receptor 183
    'ENSMUSG00000051256', # Jagn1           jagunal homolog 1
    'ENSMUSG00000051262', # Nat8f3          N-acetyltransferase 8 (GCN5-related) family member 3
    'ENSMUSG00000051314', # Ffar2           free fatty acid receptor 2
    'ENSMUSG00000051331', # Cacna1c         calcium channel, voltage-dependent, L type, alpha 1C subunit
    'ENSMUSG00000051439', # Cd14            CD14 antigen
    'ENSMUSG00000051457', # Spn             sialophorin
    'ENSMUSG00000051498', # Tlr6            toll-like receptor 6
    'ENSMUSG00000051675', # Trim32          tripartite motif-containing 32
    'ENSMUSG00000051682', # Treml4          triggering receptor expressed on myeloid cells-like 4
    'ENSMUSG00000051748', # Wfdc21          WAP four-disulfide core domain 21
    'ENSMUSG00000051969', # Tlr11           toll-like receptor 11
    'ENSMUSG00000051998', # Lax1            lymphocyte transmembrane adaptor 1
    'ENSMUSG00000052013', # Btla            B and T lymphocyte associated
    'ENSMUSG00000052085', # Dock8           dedicator of cytokinesis 8
    'ENSMUSG00000052142', # Rasal3          RAS protein activator like 3
    'ENSMUSG00000052234', # Epx             eosinophil peroxidase
    'ENSMUSG00000052270', # Fpr2            formyl peptide receptor 2
    'ENSMUSG00000052293', # Taf9            TATA-box binding protein associated factor 9
    'ENSMUSG00000052336', # Cx3cr1          chemokine (C-X3-C motif) receptor 1
    'ENSMUSG00000052384', # Nrros           negative regulator of reactive oxygen species
    'ENSMUSG00000052397', # Ezr             ezrin
    'ENSMUSG00000052430', # Bmpr1b          bone morphogenetic protein receptor, type 1B
    'ENSMUSG00000052435', # Cebpe           CCAAT/enhancer binding protein (C/EBP), epsilon
    'ENSMUSG00000052504', # Epha3           Eph receptor A3
    'ENSMUSG00000052554', # Defb34          defensin beta 34
    'ENSMUSG00000052593', # Adam17          a disintegrin and metallopeptidase domain 17
    'ENSMUSG00000052631', # Sh2d6           SH2 domain containing 6
    'ENSMUSG00000052684', # Jun             jun proto-oncogene
    'ENSMUSG00000052688', # Rab7b           RAB7B, member RAS oncogene family
    'ENSMUSG00000052821', # Cysltr1         cysteinyl leukotriene receptor 1
    'ENSMUSG00000052837', # Junb            jun B proto-oncogene
    'ENSMUSG00000052889', # Prkcb           protein kinase C, beta
    'ENSMUSG00000052920', # Prkg1           protein kinase, cGMP-dependent, type I
    'ENSMUSG00000052922', # Bpi             bactericidal permeablility increasing protein
    'ENSMUSG00000053004', # Hrh1            histamine receptor H1
    'ENSMUSG00000053044', # Cd8b1           CD8 antigen, beta chain 1
    'ENSMUSG00000053062', # Jam2            junction adhesion molecule 2
    'ENSMUSG00000053063', # Clec12a         C-type lectin domain family 12, member a
    'ENSMUSG00000053128', # Rnf26           None
    'ENSMUSG00000053137', # Mapk11          mitogen-activated protein kinase 11
    'ENSMUSG00000053158', # Fes             feline sarcoma oncogene
    'ENSMUSG00000053175', # Bcl3            B cell leukemia/lymphoma 3
    'ENSMUSG00000053216', # Btn2a2          butyrophilin, subfamily 2, member A2
    'ENSMUSG00000053219', # Raet1e          retinoic acid early transcript 1E
    'ENSMUSG00000053318', # Slamf8          SLAM family member 8
    'ENSMUSG00000053399', # Adamts18        a disintegrin-like and metallopeptidase (reprolysin type) with thrombospondin type 1 motif, 18
    'ENSMUSG00000053436', # Mapk14          mitogen-activated protein kinase 14
    'ENSMUSG00000053477', # Tcf4            transcription factor 4
    'ENSMUSG00000053646', # Plxnb1          plexin B1
    'ENSMUSG00000053647', # Gper1           G protein-coupled estrogen receptor 1
    'ENSMUSG00000053797', # Krt16           keratin 16
    'ENSMUSG00000053835', # H2-T24          histocompatibility 2, T region locus 24
    'ENSMUSG00000053965', # Pde5a           phosphodiesterase 5A, cGMP-specific
    'ENSMUSG00000053977', # Cd8a            CD8 antigen, alpha chain
    'ENSMUSG00000054008', # Ndst1           N-deacetylase/N-sulfotransferase (heparan glucosaminyl) 1
    'ENSMUSG00000054072', # Iigp1           interferon inducible GTPase 1
    'ENSMUSG00000054128', # H2-T3           histocompatibility 2, T region locus 3
    'ENSMUSG00000054200', # Ffar4           free fatty acid receptor 4
    'ENSMUSG00000054263', # Lifr            leukemia inhibitory factor receptor
    'ENSMUSG00000054342', # Kcnn4           potassium intermediate/small conductance calcium-activated channel, subfamily N, member 4
    'ENSMUSG00000054383', # Pnma1           paraneoplastic antigen MA1
    'ENSMUSG00000054400', # Cklf            chemokine-like factor
    'ENSMUSG00000054452', # Aes             amino-terminal enhancer of split
    'ENSMUSG00000054509', # Parp4           poly (ADP-ribose) polymerase family, member 4
    'ENSMUSG00000054580', # Pla2r1          phospholipase A2 receptor 1
    'ENSMUSG00000054672', # 5830411N06Rik   RIKEN cDNA 5830411N06 gene
    'ENSMUSG00000054693', # Adam10          a disintegrin and metallopeptidase domain 10
    'ENSMUSG00000054717', # Hmgb2           high mobility group box 2
    'ENSMUSG00000054814', # Usp46           ubiquitin specific peptidase 46
    'ENSMUSG00000054855', # Rnd1            Rho family GTPase 1
    'ENSMUSG00000054892', # Txk             TXK tyrosine kinase
    'ENSMUSG00000054988', # Agtr1b          angiotensin II receptor, type 1b
    'ENSMUSG00000055065', # Ddx17           DEAD (Asp-Glu-Ala-Asp) box polypeptide 17
    'ENSMUSG00000055148', # Klf2            Kruppel-like factor 2 (lung)
    'ENSMUSG00000055170', # Ifng            interferon gamma
    'ENSMUSG00000055172', # C1ra            complement component 1, r subcomponent A
    'ENSMUSG00000055204', # Ankrd17         ankyrin repeat domain 17
    'ENSMUSG00000055435', # Maf             avian musculoaponeurotic fibrosarcoma oncogene homolog
    'ENSMUSG00000055447', # Cd47            CD47 antigen (Rh-related antigen, integrin-associated signal transducer)
    'ENSMUSG00000055561', # Spink5          serine peptidase inhibitor, Kazal type 5
    'ENSMUSG00000055633', # Zfp580          zinc finger protein 580
    'ENSMUSG00000055653', # Gpc3            glypican 3
    'ENSMUSG00000055865', # Fam19a3         family with sequence similarity 19, member A3
    'ENSMUSG00000055994', # Nod2            nucleotide-binding oligomerization domain containing 2
    'ENSMUSG00000056050', # Mia3            melanoma inhibitory activity 3
    'ENSMUSG00000056054', # S100a8          S100 calcium binding protein A8 (calgranulin A)
    'ENSMUSG00000056071', # S100a9          S100 calcium binding protein A9 (calgranulin B)
    'ENSMUSG00000056116', # H2-T22          histocompatibility 2, T region locus 22
    'ENSMUSG00000056130', # Ticam2          toll-like receptor adaptor molecule 2
    'ENSMUSG00000056153', # Socs6           suppressor of cytokine signaling 6
    'ENSMUSG00000056201', # Cfl1            cofilin 1, non-muscle
    'ENSMUSG00000056216', # Cebpg           CCAAT/enhancer binding protein (C/EBP), gamma
    'ENSMUSG00000056222', # Spock1          sparc/osteonectin, cwcv and kazal-like domains proteoglycan 1
    'ENSMUSG00000056268', # Dennd1b         DENN/MADD domain containing 1B
    'ENSMUSG00000056313', # 1810011O10Rik   RIKEN cDNA 1810011O10 gene
    'ENSMUSG00000056492', # Adgrf5          adhesion G protein-coupled receptor F5
    'ENSMUSG00000056501', # Cebpb           CCAAT/enhancer binding protein (C/EBP), beta
    'ENSMUSG00000056529', # Ptafr           platelet-activating factor receptor
    'ENSMUSG00000056544', # Defb21          defensin beta 21
    'ENSMUSG00000056612', # Ppp1r14b        protein phosphatase 1, regulatory (inhibitor) subunit 14B
    'ENSMUSG00000056673', # Kdm5d           lysine (K)-specific demethylase 5D
    'ENSMUSG00000056749', # Nfil3           nuclear factor, interleukin 3, regulated
    'ENSMUSG00000056851', # Pcbp2           poly(rC) binding protein 2
    'ENSMUSG00000056962', # Jmjd6           jumonji domain containing 6
    'ENSMUSG00000057058', # Skap1           src family associated phosphoprotein 1
    'ENSMUSG00000057103', # Nat8f1          N-acetyltransferase 8 (GCN5-related) family member 1
    'ENSMUSG00000057329', # Bcl2            B cell leukemia/lymphoma 2
    'ENSMUSG00000057406', # Nsd2            None
    'ENSMUSG00000057465', # Saa2            serum amyloid A 2
    'ENSMUSG00000057554', # Lgals8          lectin, galactose binding, soluble 8
    'ENSMUSG00000057666', # Gapdh           glyceraldehyde-3-phosphate dehydrogenase
    'ENSMUSG00000057667', # Bloc1s3         biogenesis of lysosomal organelles complex-1, subunit 3
    'ENSMUSG00000057672', # Pkn1            protein kinase N1
    'ENSMUSG00000057706', # Mex3b           mex3 RNA binding family member B
    'ENSMUSG00000057722', # Lepr            leptin receptor
    'ENSMUSG00000057729', # Prtn3           proteinase 3
    'ENSMUSG00000057789', # Bak1            BCL2-antagonist/killer 1
    'ENSMUSG00000057880', # Abat            4-aminobutyrate aminotransferase
    'ENSMUSG00000057948', # Unc13d          unc-13 homolog D (C. elegans)
    'ENSMUSG00000057982', # Zfp809          zinc finger protein 809
    'ENSMUSG00000058052', # Defb35          defensin beta 35
    'ENSMUSG00000058063', # Trim31          tripartite motif-containing 31
    'ENSMUSG00000058099', # Nfam1           Nfat activating molecule with ITAM motif 1
    'ENSMUSG00000058124', # H2-M10.3        histocompatibility 2, M region locus 10.3
    'ENSMUSG00000058207', # Serpina3k       serine (or cysteine) peptidase inhibitor, clade A, member 3K
    'ENSMUSG00000058230', # Arhgap35        Rho GTPase activating protein 35
    'ENSMUSG00000058297', # Spock2          sparc/osteonectin, cwcv and kazal-like domains proteoglycan 2
    'ENSMUSG00000058385', # Hist1h2bg       histone cluster 1, H2bg
    'ENSMUSG00000058427', # Cxcl2           chemokine (C-X-C motif) ligand 2
    'ENSMUSG00000058444', # Map2k5          mitogen-activated protein kinase kinase 5
    'ENSMUSG00000058488', # Kl              klotho
    'ENSMUSG00000058499', # Pip             prolactin induced protein
    'ENSMUSG00000058715', # Fcer1g          Fc receptor, IgE, high affinity I, gamma polypeptide
    'ENSMUSG00000058728', # Cd300c          CD300C molecule
    'ENSMUSG00000058755', # Osm             oncostatin M
    'ENSMUSG00000058818', # Pirb            paired Ig-like receptor B
    'ENSMUSG00000058914', # C1qtnf3         C1q and tumor necrosis factor related protein 3
    'ENSMUSG00000058952', # Cfi             complement component factor i
    'ENSMUSG00000059089', # Fcgr4           Fc receptor, IgG, low affinity IV
    'ENSMUSG00000059128', # Ifnl2           interferon lambda 2
    'ENSMUSG00000059182', # Skap2           src family associated phosphoprotein 2
    'ENSMUSG00000059201', # Lep             leptin
    'ENSMUSG00000059280', # Vpreb2          pre-B lymphocyte gene 2
    'ENSMUSG00000059305', # Vpreb1          pre-B lymphocyte gene 1
    'ENSMUSG00000059327', # Eda             ectodysplasin-A
    'ENSMUSG00000059439', # Bcas3           breast carcinoma amplified sequence 3
    'ENSMUSG00000059456', # Ptk2b           PTK2 protein tyrosine kinase 2 beta
    'ENSMUSG00000059481', # Plg             plasminogen
    'ENSMUSG00000059498', # Fcgr3           Fc receptor, IgG, low affinity III
    'ENSMUSG00000059518', # Znhit1          zinc finger, HIT domain containing 1
    'ENSMUSG00000059552', # Trp53           transformation related protein 53
    'ENSMUSG00000059714', # Flot1           flotillin 1
    'ENSMUSG00000059866', # Tnip2           TNFAIP3 interacting protein 2
    'ENSMUSG00000059883', # Irak4           interleukin-1 receptor-associated kinase 4
    'ENSMUSG00000059923', # Grb2            growth factor receptor bound protein 2
    'ENSMUSG00000060038', # Dhps            deoxyhypusine synthase
    'ENSMUSG00000060188', # Cxcl17          chemokine (C-X-C motif) ligand 17
    'ENSMUSG00000060216', # Arrb2           arrestin, beta 2
    'ENSMUSG00000060477', # Irak2           interleukin-1 receptor-associated kinase 2
    'ENSMUSG00000060509', # Xcr1            chemokine (C motif) receptor 1
    'ENSMUSG00000060550', # H2-Q7           histocompatibility 2, Q region locus 7
    'ENSMUSG00000060586', # H2-Eb1          histocompatibility 2, class II antigen E beta
    'ENSMUSG00000060591', # Ifitm2          interferon induced transmembrane protein 2
    'ENSMUSG00000060701', # Fpr-rs3         formyl peptide receptor, related sequence 3
    'ENSMUSG00000060747', # Ifnl3           interferon lambda 3
    'ENSMUSG00000060802', # B2m             beta-2 microglobulin
    'ENSMUSG00000060803', # Gstp1           glutathione S-transferase, pi 1
    'ENSMUSG00000061048', # Cdh3            cadherin 3
    'ENSMUSG00000061119', # Prcp            prolylcarboxypeptidase (angiotensinase C)
    'ENSMUSG00000061130', # Ppm1b           protein phosphatase 1B, magnesium dependent, beta isoform
    'ENSMUSG00000061132', # Blnk            B cell linker
    'ENSMUSG00000061232', # H2-K1           histocompatibility 2, K1, K region
    'ENSMUSG00000061311', # Rag1            recombination activating gene 1
    'ENSMUSG00000061353', # Cxcl12          chemokine (C-X-C motif) ligand 12
    'ENSMUSG00000061356', # Nuggc           nuclear GTPase, germinal center associated
    'ENSMUSG00000061414', # Cracr2a         calcium release activated channel regulator 2A
    'ENSMUSG00000061540', # Orm2            orosomucoid 2
    'ENSMUSG00000061665', # Cd2ap           CD2-associated protein
    'ENSMUSG00000061762', # Tac1            tachykinin 1
    'ENSMUSG00000061780', # Cfd             complement factor D (adipsin)
    'ENSMUSG00000061878', # Sphk1           sphingosine kinase 1
    'ENSMUSG00000061981', # Flot2           flotillin 2
    'ENSMUSG00000062007', # Hsh2d           hematopoietic SH2 domain containing
    'ENSMUSG00000062124', # Defb45          defensin beta 45
    'ENSMUSG00000062157', # Ifnlr1          interferon lambda receptor 1
    'ENSMUSG00000062210', # Tnfaip8         tumor necrosis factor, alpha-induced protein 8
    'ENSMUSG00000062300', # Nectin2         nectin cell adhesion molecule 2
    'ENSMUSG00000062312', # Erbb2           erb-b2 receptor tyrosine kinase 2
    'ENSMUSG00000062352', # Itgb1bp1        integrin beta 1 binding protein 1
    'ENSMUSG00000062515', # Fabp4           fatty acid binding protein 4, adipocyte
    'ENSMUSG00000062545', # Tlr12           toll-like receptor 12
    'ENSMUSG00000062585', # Cnr2            cannabinoid receptor 2 (macrophage)
    'ENSMUSG00000062638', # Btnl1           butyrophilin-like 1
    'ENSMUSG00000062727', # Hist1h2bk       histone cluster 1, H2bk
    'ENSMUSG00000062773', # Tex101          testis expressed gene 101
    'ENSMUSG00000062778', # Chia1           chitinase, acidic 1
    'ENSMUSG00000062960', # Kdr             kinase insert domain protein receptor
    'ENSMUSG00000063065', # Mapk3           mitogen-activated protein kinase 3
    'ENSMUSG00000063133', # Klk1b1          kallikrein 1-related peptidase b1
    'ENSMUSG00000063193', # Cd300lb         CD300 molecule like family member B
    'ENSMUSG00000063275', # Hacd1           3-hydroxyacyl-CoA dehydratase 1
    'ENSMUSG00000063281', # Zfp35           zinc finger protein 35
    'ENSMUSG00000063358', # Mapk1           mitogen-activated protein kinase 1
    'ENSMUSG00000063376', # Ifna13          interferon alpha 13
    'ENSMUSG00000063415', # Cyp26b1         cytochrome P450, family 26, subfamily b, polypeptide 1
    'ENSMUSG00000063531', # Sema3e          sema domain, immunoglobulin domain (Ig), short basic domain, secreted, (semaphorin) 3E
    'ENSMUSG00000063727', # Tnfrsf11b       tumor necrosis factor receptor superfamily, member 11b (osteoprotegerin)
    'ENSMUSG00000063767', # S100a7a         S100 calcium binding protein A7A
    'ENSMUSG00000063779', # Chil4           chitinase-like 4
    'ENSMUSG00000064039', # Ccr1l1          chemokine (C-C motif) receptor 1-like 1
    'ENSMUSG00000064080', # Fbln2           fibulin 2
    'ENSMUSG00000064109', # Hcst            hematopoietic cell signal transducer
    'ENSMUSG00000064140', # Trim38          tripartite motif-containing 38
    'ENSMUSG00000064177', # Ghrl            ghrelin
    'ENSMUSG00000064210', # Ano6            anoctamin 6
    'ENSMUSG00000064246', # Chil1           chitinase-like 1
    'ENSMUSG00000064302', # Clasp1          CLIP associating protein 1
    'ENSMUSG00000065987', # Cd209b          CD209b antigen
    'ENSMUSG00000066108', # Muc5b           mucin 5, subtype B, tracheobronchial
    'ENSMUSG00000066232', # Ipo7            importin 7
    'ENSMUSG00000066258', # Trim12a         tripartite motif-containing 12A
    'ENSMUSG00000066361', # Serpina3c       serine (or cysteine) peptidase inhibitor, clade A, member 3C
    'ENSMUSG00000066363', # Serpina3f       serine (or cysteine) peptidase inhibitor, clade A, member 3F
    'ENSMUSG00000066366', # Serpina1a       serine (or cysteine) peptidase inhibitor, clade A, member 1A
    'ENSMUSG00000066551', # Hmgb1           high mobility group box 1
    'ENSMUSG00000066568', # Lsm14a          LSM14A mRNA processing body assembly factor
    'ENSMUSG00000066684', # Pilrb1          paired immunoglobin-like type 2 receptor beta 1
    'ENSMUSG00000066687', # Zbtb16          zinc finger and BTB domain containing 16
    'ENSMUSG00000066755', # Tnfsf18         tumor necrosis factor (ligand) superfamily, member 18
    'ENSMUSG00000066839', # Ecsit           ECSIT signalling integrator
    'ENSMUSG00000066877', # Nck2            non-catalytic region of tyrosine kinase adaptor protein 2
    'ENSMUSG00000067001', # Serpinb7        serine (or cysteine) peptidase inhibitor, clade B, member 7
    'ENSMUSG00000067149', # Jchain          immunoglobulin joining chain
    'ENSMUSG00000067201', # H2-M9           histocompatibility 2, M region locus 9
    'ENSMUSG00000067212', # H2-T23          histocompatibility 2, T region locus 23
    'ENSMUSG00000067235', # H2-Q10          histocompatibility 2, Q region locus 10
    'ENSMUSG00000067377', # Tspan6          tetraspanin 6
    'ENSMUSG00000067586', # S1pr3           sphingosine-1-phosphate receptor 3
    'ENSMUSG00000067767', # Clec4b2         C-type lectin domain family 4, member b2
    'ENSMUSG00000067773', # Defb41          defensin beta 41
    'ENSMUSG00000068008', # Bpifb3          BPI fold containing family B, member 3
    'ENSMUSG00000068105', # Tnfrsf13c       tumor necrosis factor receptor superfamily, member 13c
    'ENSMUSG00000068122', # Agtr2           angiotensin II receptor, type 2
    'ENSMUSG00000068196', # Col8a1          collagen, type VIII, alpha 1
    'ENSMUSG00000068220', # Lgals1          lectin, galactose binding, soluble 1
    'ENSMUSG00000068227', # Il2rb           interleukin 2 receptor, beta chain
    'ENSMUSG00000068566', # Myadm           myeloid-associated differentiation marker
    'ENSMUSG00000068686', # Cd59b           CD59b antigen
    'ENSMUSG00000068740', # Celsr2          cadherin, EGF LAG seven-pass G-type receptor 2
    'ENSMUSG00000068748', # Ptprz1          protein tyrosine phosphatase, receptor type Z, polypeptide 1
    'ENSMUSG00000068758', # Il3ra           interleukin 3 receptor, alpha chain
    'ENSMUSG00000068798', # Rap1a           RAS-related protein-1a
    'ENSMUSG00000068854', # Hist2h2be       histone cluster 2, H2be
    'ENSMUSG00000068923', # Syt11           synaptotagmin XI
    'ENSMUSG00000069255', # Dusp22          dual specificity phosphatase 22
    'ENSMUSG00000069268', # Hist1h2bf       histone cluster 1, H2bf
    'ENSMUSG00000069601', # Ank3            ankyrin 3, epithelial
    'ENSMUSG00000069607', # Cd300ld3        CD300 molecule like family member D3
    'ENSMUSG00000069830', # Nlrp1a          NLR family, pyrin domain containing 1A
    'ENSMUSG00000069874', # Irgm2           immunity-related GTPase family M member 2
    'ENSMUSG00000070034', # Sp110           Sp110 nuclear body protein
    'ENSMUSG00000070369', # Itgad           integrin, alpha D
    'ENSMUSG00000070390', # Nlrp1b          NLR family, pyrin domain containing 1B
    'ENSMUSG00000070427', # Il18bp          interleukin 18 binding protein
    'ENSMUSG00000070464', # Ccl26           chemokine (C-C motif) ligand 26
    'ENSMUSG00000070524', # Fcrlb           Fc receptor-like B
    'ENSMUSG00000070691', # Runx3           runt related transcription factor 3
    'ENSMUSG00000070777', # Ceacam20        carcinoembryonic antigen-related cell adhesion molecule 20
    'ENSMUSG00000070904', # Ifna4           interferon alpha 4
    'ENSMUSG00000070908', # Gm13288         predicted gene 13288
    'ENSMUSG00000070942', # Il1rl2          interleukin 1 receptor-like 2
    'ENSMUSG00000071005', # Ccl19           None
    'ENSMUSG00000071068', # Treml2          triggering receptor expressed on myeloid cells-like 2
    'ENSMUSG00000071076', # Jund            jun D proto-oncogene
    'ENSMUSG00000071177', # Serpina1d       serine (or cysteine) peptidase inhibitor, clade A, member 1D
    'ENSMUSG00000071178', # Serpina1b       serine (or cysteine) preptidase inhibitor, clade A, member 1B
    'ENSMUSG00000071203', # Naip5           NLR family, apoptosis inhibitory protein 5
    'ENSMUSG00000071275', # Fpr-rs6         formyl peptide receptor, related sequence 6
    'ENSMUSG00000071276', # Fpr-rs7         formyl peptide receptor, related sequence 7
    'ENSMUSG00000071337', # Tia1            cytotoxic granule-associated RNA binding protein 1
    'ENSMUSG00000071356', # Reg3b           regenerating islet-derived 3 beta
    'ENSMUSG00000071369', # Map3k5          mitogen-activated protein kinase kinase kinase 5
    'ENSMUSG00000071489', # Ptgdr           prostaglandin D receptor
    'ENSMUSG00000071552', # Tigit           T cell immunoreceptor with Ig and ITIM domains
    'ENSMUSG00000072244', # Trim6           tripartite motif-containing 6
    'ENSMUSG00000072423', # Psmb11          proteasome (prosome, macropain) subunit, beta type, 11
    'ENSMUSG00000072625', # Gdf2            growth differentiation factor 2
    'ENSMUSG00000072849', # Serpina1e       serine (or cysteine) peptidase inhibitor, clade A, member 1E
    'ENSMUSG00000073400', # Trim10          tripartite motif-containing 10
    'ENSMUSG00000073402', # Gm8909          predicted gene 8909
    'ENSMUSG00000073409', # H2-Q6           histocompatibility 2, Q region locus 6
    'ENSMUSG00000073411', # H2-D1           histocompatibility 2, D region locus 1
    'ENSMUSG00000073412', # Lst1            leukocyte specific transcript 1
    'ENSMUSG00000073414', # G6b             immunoreceptor tyrosine-based inhibitory motif (ITIM) containing platelet receptor
    'ENSMUSG00000073418', # C4b             complement component 4B (Chido blood group)
    'ENSMUSG00000073421', # H2-Ab1          histocompatibility 2, class II antigen A, beta 1
    'ENSMUSG00000073494', # Sh2d1b2         SH2 domain containing 1B2
    'ENSMUSG00000073730', # 4933415F23Rik   RIKEN cDNA 4933415F23 gene
    'ENSMUSG00000073735', # Defb18          defensin beta 18
    'ENSMUSG00000073811', # Ifna12          interferon alpha 12
    'ENSMUSG00000073888', # Ccl27a          None
    'ENSMUSG00000073889', # Il11ra1         interleukin 11 receptor, alpha chain 1
    'ENSMUSG00000074037', # Mc1r            melanocortin 1 receptor
    'ENSMUSG00000074109', # Mrgprx2         MAS-related GPR, member X2
    'ENSMUSG00000074115', # Saa1            serum amyloid A 1
    'ENSMUSG00000074129', # Rpl13a          ribosomal protein L13A
    'ENSMUSG00000074151', # Nlrc5           NLR family, CARD domain containing 5
    'ENSMUSG00000074227', # Spint2          serine protease inhibitor, Kunitz type 2
    'ENSMUSG00000074272', # Ceacam1         carcinoembryonic antigen-related cell adhesion molecule 1
    'ENSMUSG00000074361', # C5ar2           complement component 5a receptor 2
    'ENSMUSG00000074491', # Clec4g          C-type lectin domain family 4, member g
    'ENSMUSG00000074582', # Arfgef2         ADP-ribosylation factor guanine nucleotide-exchange factor 2 (brefeldin A-inhibited)
    'ENSMUSG00000074622', # Mafb            v-maf musculoaponeurotic fibrosarcoma oncogene family, protein B (avian)
    'ENSMUSG00000074637', # Sox2            SRY (sex determining region Y)-box 2
    'ENSMUSG00000074678', # Defb25          defensin beta 25
    'ENSMUSG00000074679', # Defb28          defensin beta 28
    'ENSMUSG00000074680', # Defb26          defensin beta 26
    'ENSMUSG00000074681', # Defb23          defensin beta 23
    'ENSMUSG00000074715', # Ccl28           chemokine (C-C motif) ligand 28
    'ENSMUSG00000074781', # Ube2n           ubiquitin-conjugating enzyme E2N
    'ENSMUSG00000074785', # Plxnc1          plexin C1
    'ENSMUSG00000074896', # Ifit3           interferon-induced protein with tetratricopeptide repeats 3
    'ENSMUSG00000074934', # Grem1           gremlin 1, DAN family BMP antagonist
    'ENSMUSG00000075122', # Cd80            CD80 antigen
    'ENSMUSG00000075254', # Heg1            heart development protein with EGF-like domains 1
    'ENSMUSG00000075297', # H60b            histocompatibility 60b
    'ENSMUSG00000075316', # Scn9a           sodium channel, voltage-gated, type IX, alpha
    'ENSMUSG00000075370', # Igll1           immunoglobulin lambda-like polypeptide 1
    'ENSMUSG00000075376', # Rc3h2           ring finger and CCCH-type zinc finger domains 2
    'ENSMUSG00000075571', # Defb30          defensin beta 30
    'ENSMUSG00000075572', # Defb43          defensin beta 43
    'ENSMUSG00000075701', # Selenos         selenoprotein S
    'ENSMUSG00000075705', # Msrb1           methionine sulfoxide reductase B1
    'ENSMUSG00000076431', # Sox4            SRY (sex determining region Y)-box 4
    'ENSMUSG00000076441', # Ass1            argininosuccinate synthetase 1
    'ENSMUSG00000078202', # Nrarp           Notch-regulated ankyrin repeat protein
    'ENSMUSG00000078354', # Ifna2           interferon alpha 2
    'ENSMUSG00000078355', # Ifna16          interferon alpha 16
    'ENSMUSG00000078452', # Raet1d          retinoic acid early transcript delta
    'ENSMUSG00000078612', # 1700024P16Rik   RIKEN cDNA 1700024P16 gene
    'ENSMUSG00000078698', # Mrgpra3         MAS-related GPR, member A3
    'ENSMUSG00000078763', # Slfn1           schlafen 1
    'ENSMUSG00000078817', # Nlrp12          NLR family, pyrin domain containing 12
    'ENSMUSG00000078922', # Tgtp1           T cell specific GTPase 1
    'ENSMUSG00000078942', # Naip6           NLR family, apoptosis inhibitory protein 6
    'ENSMUSG00000078945', # Naip2           NLR family, apoptosis inhibitory protein 2
    'ENSMUSG00000079012', # Serpina3m       serine (or cysteine) peptidase inhibitor, clade A, member 3M
    'ENSMUSG00000079014', # Serpina3i       serine (or cysteine) peptidase inhibitor, clade A, member 3I
    'ENSMUSG00000079015', # Serpina1c       serine (or cysteine) peptidase inhibitor, clade A, member 1C
    'ENSMUSG00000079037', # Prnp            prion protein
    'ENSMUSG00000079109', # Pms2            postmeiotic segregation increased 2 (S. cerevisiae)
    'ENSMUSG00000079164', # Tlr5            toll-like receptor 5
    'ENSMUSG00000079197', # Psme2           proteasome (prosome, macropain) activator subunit 2 (PA28 beta)
    'ENSMUSG00000079227', # Ccr5            chemokine (C-C motif) receptor 5
    'ENSMUSG00000079362', # Gm43302         None
    'ENSMUSG00000079363', # Gbp4            guanylate binding protein 4
    'ENSMUSG00000079415', # Cntf            ciliary neurotrophic factor
    'ENSMUSG00000079492', # Gm11127         predicted gene 11127
    'ENSMUSG00000079494', # Nat8f5          N-acetyltransferase 8 (GCN5-related) family member 5
    'ENSMUSG00000079507', # H2-Q1           histocompatibility 2, Q region locus 1
    'ENSMUSG00000079516', # Reg3a           regenerating islet-derived 3 alpha
    'ENSMUSG00000079547', # H2-DMb1         histocompatibility 2, class II, locus Mb1
    'ENSMUSG00000079563', # Pglyrp2         peptidoglycan recognition protein 2
    'ENSMUSG00000079614', # Seh1l           SEH1-like (S. cerevisiae
    'ENSMUSG00000079620', # Muc4            mucin 4
    'ENSMUSG00000079641', # Rpl39           ribosomal protein L39
    'ENSMUSG00000079685', # Ulbp1           UL16 binding protein 1
    'ENSMUSG00000079700', # Fpr3            formyl peptide receptor 3
    'ENSMUSG00000085795', # Zfp703          zinc finger protein 703
    'ENSMUSG00000089669', # Tnfsf13         tumor necrosis factor (ligand) superfamily, member 13
    'ENSMUSG00000089773', # Skint1          selection and upkeep of intraepithelial T cells 1
    'ENSMUSG00000089876', # Tmem102         transmembrane protein 102
    'ENSMUSG00000090019', # Gimap1          GTPase, IMAP family member 1
    'ENSMUSG00000090077', # Lime1           Lck interacting transmembrane adaptor 1
    'ENSMUSG00000090210', # Itga10          integrin, alpha 10
    'ENSMUSG00000090231', # Cfb             complement factor B
    'ENSMUSG00000090485', # Gm17416         None
    'ENSMUSG00000090588', # Gm9573          predicted gene 9573
    'ENSMUSG00000090958', # Lrrc32          leucine rich repeat containing 32
    'ENSMUSG00000091618', # H60c            histocompatibility 60c
    'ENSMUSG00000091705', # H2-Q2           histocompatibility 2, Q region locus 2
    'ENSMUSG00000091938', # Gm2564          predicted gene 2564
    'ENSMUSG00000092243', # Gm7030          predicted gene 7030
    'ENSMUSG00000092618', # Btnl6           butyrophilin-like 6
    'ENSMUSG00000094271', # Gm13290         predicted gene 13290
    'ENSMUSG00000094338', # Hist1h2bl       histone cluster 1, H2bl
    'ENSMUSG00000094618', # Gm13271         predicted gene 13271
    'ENSMUSG00000094648', # Gm13287         predicted gene 13287
    'ENSMUSG00000094686', # Ccl21a          None
    'ENSMUSG00000095101', # Gm13285         predicted gene 13285
    'ENSMUSG00000095270', # Ifna9           interferon alpha 9
    'ENSMUSG00000095498', # Ifna1           interferon alpha 1
    'ENSMUSG00000095675', # Ccl21b          chemokine (C-C motif) ligand 21B (leucine)
    'ENSMUSG00000095896', # Ifna14          interferon alpha 14
    'ENSMUSG00000096011', # Ifna15          interferon alpha 15
    'ENSMUSG00000096582', # Gm13289         predicted gene 13289
    'ENSMUSG00000096591', # Gm13272         predicted gene 13272
    'ENSMUSG00000096682', # Ifna5           interferon alpha 5
    'ENSMUSG00000096727', # Psmb9           proteasome (prosome, macropain) subunit, beta type 9 (large multifunctional peptidase 2)
    'ENSMUSG00000096854', # Ifnz            interferon zeta
    'ENSMUSG00000097328', # Tnfsf12         tumor necrosis factor (ligand) superfamily, member 12
    'ENSMUSG00000098470', # C1rb            complement component 1, r subcomponent B
    'ENSMUSG00000099420', # Gm13279         predicted gene 13279
    'ENSMUSG00000099518', # Gm13275         predicted gene 13275
    'ENSMUSG00000099545', # Gm13276         predicted gene 13276
    'ENSMUSG00000099974', # Bcl2a1d         B cell leukemia/lymphoma 2 related protein A1d
    'ENSMUSG00000100079', # Ifnab           interferon alpha B
    'ENSMUSG00000100234', # Gm13277         predicted gene 13277
    'ENSMUSG00000100505', # Gm13283         predicted gene 13283
    'ENSMUSG00000100549', # Ifna11          interferon alpha 11
    'ENSMUSG00000100713', # Ifna7           interferon alpha 7
    'ENSMUSG00000101163', # Gm13278         predicted gene 13278
    'ENSMUSG00000101252', # Ifna6           interferon alpha 6
    'ENSMUSG00000102418', # Sh2d1b1         SH2 domain containing 1B1
    'ENSMUSG00000105504', # Gbp5            guanylate binding protein 5
    'ENSMUSG00000109564', # Muc16           mucin 16
    'ENSMUSG00000109941', # Exosc6          exosome component 6
])
