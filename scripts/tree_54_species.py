from ete_dev import Tree, TreeStyle, faces
from itertools import combinations

species = {'Hepatitis B',
           'Hepatitis D',
           'Tomato mosaic',
           'Enterobacteria phage m13',
           'HIV 1',
           'Sudan ebolavirus',
           'Enterobacteria phage lambda',
           'Human herpesvirus1',
           'Carsonella ruddii',
           'Buchnera aphidicola',
           'Ureaplasma urealyticum',
           'Synthetic mycoplasma mycoides',
           'Thermococcus sibiricus',
           'Methanocaldococcus vulcanius',
           'Sulfolobus islandicus',
           'Bacillus subtilis',
           'Mycobacterium tuberculosis',
           'Escherichia coli',
           'Burkholderia xenovorans',
           'Saccharomyces cerevisiae',
           'Plasmodium falciparum',
           'Phaeodactylum tricornutum',
           'Thalassiosira pseudonana',
           'Dictyostelium discoideum',
           'Ciona intestinalis',
           'Caenorhabditis elegans',
           'Tribolium castaneum',
           'Arabidopsis thaliana',
           'Drosophila melanogaster',
           'Daphnia pulex',
           'Arabidopsis lyrata',
           'Tetraodon nigroviridis',
           'Apis mellifera',
           'Anopheles gambiae',
           'Brachypodium distachyon',
           'Oryza sativa',
           'Populus trichocarpa',
           'Physcomitrella patens',
           'Sorghum bicolor',
           'Oryzias latipes',
           'Gallus gallus',
           'Taeniopygia guttata',
           'Danio rerio',
           'Zea mays',
           'Canis familiaris',
           'Equus caballus',
           'Bos taurus',
           'Rattus norvegicus',
           'Mus musculus',
           'Pan troglodytes',
           'Macaca mulatta',
           'Pongo abelii',
           'Homo sapiens',
           'Monodelphis domestica'}


#dates = {}
#for spe1, spe2 in combinations(species, 2):
#    res = urllib.urlopen('http://www.timetree.org/index.php?taxon_a='+spe1.replace(' ', '+')+'&taxon_b='+spe2.replace(' ', '+')+'&submit=Search').read()
#    for l in res.split('\n'):
#        if 'Median:</strong>' in l:
#            mya = re.sub('.*Median:\<\/strong\> *([0-9.]+) *Mya.*', '\\1', l)
#            try:
#                mya = float(mya)
#            except ValueError:
#                'ERROR:' + mya, spe1, spe2
#                break
#            dates.setdefault(spe1, {})
#            dates[spe1][spe2] = mya
#            dates.setdefault(spe2, {})
#            dates[spe2][spe1] = mya
#            print spe1, '<--->', spe2, mya, 'Mya'
#            break
#    else:
#        print 'ERROR: not found', spe1, spe2
#

errors = ['Human herpesvirus1', 'Tomato mosaic', 'Enterobacteria phage lambda',
          'Hepatitis B', 'HIV 1', 'Hepatitis D', 'Synthetic mycoplasma mycoides',
          'Sudan ebolavirus', 'Enterobacteria phage m13']
dates['Escherichia coli']['Carsonella ruddii'] = 3000.0
dates['Carsonella ruddii']['Escherichia coli'] = 3000.0
dates['Carsonella ruddii']['Buchnera aphidicola'] = 3000.0
dates['Buchnera aphidicola']['Carsonella ruddii'] = 3000.0

species = list(species)
for spe1 in species:
    if spe1 in errors: continue
    line = spe1[:10].replace(' ', '_')
    for spe2 in species:
        if spe1==spe2:
            line+='\t'+str(0.0)
            continue
        #if species.index(spe1) <= species.index(spe2): continue
        if spe2 in errors: continue
        try:
            line+='\t'+str(dates[spe1][spe2])
        except KeyError:
            line+='\t'
    print line
    
tree = Tree ('((Phytophthora infestans:0.122331,(Phytophthora capsici:0.215519,((((((Cryptosporidium hominis:0.0523166,Cryptosporidium parvum:0.0296537)NoName:1.06301,(Toxoplasma gondii:0.929536,(((Plasmodium chabaudi:0.207755,(Plasmodium yoelii:0.114464,Plasmodium berghei:0.172805)NoName:0.0142695)NoName:0.206175,(Plasmodium falciparum:0.287468,(Plasmodium knowlesi:0.14043,Plasmodium vivax:0.13485)NoName:0.201181)NoName:0.0917284)NoName:0.938312,((Theileria parva:0.122486,Theileria annulata:0.124536)NoName:0.581763,Babesia bovis:0.683557)NoName:0.589242)NoName:0.176177)NoName:0.0964916)NoName:0.367776,(Paramecium tetraurelia:1.03519,Tetrahymena thermophila:0.964544)NoName:0.674659)NoName:0.223984,(((Dictyostelium purpureum:0.289131,Dictyostelium discoideum:0.233749)NoName:0.853833,((Capsaspora owczarzaki:0.83314,((((((((Anolis carolinensis:0.203727,(Taeniopygia guttata:0.0838698,Gallus gallus:0.0669647)NoName:0.107595)NoName:0.0393986,(Ornithorhynchus anatinus:0.287227,((Monodelphis domestica:0.108787,Macropus eugenii:0.133563)NoName:0.0488337,((Echinops telfairi:0.253681,(Loxodonta africana:0.184133,Procavia capensis:0.114041)NoName:0.0557694)NoName:0.00457121,(((((Otolemur garnettii:0.143854,Microcebus murinus:0.232839)NoName:0.053669,(Tarsius syrichta:0.235094,(((Pongo abelii:0.106124,((Homo sapiens:0.00813613,Pan troglodytes:0.0483462)NoName:0.00481603,Gorilla gorilla:0.242863)NoName:0.00145655)NoName:0.00754995,Macaca mulatta:0.0577307)NoName:0.00880929,Callithrix jacchus:0.0605039)NoName:0.0205566)NoName:0.00261192)NoName:0.00456261,(((Ictidomys tridecemlineatus:0.204449,(Cavia porcellus:0.0772773,(Dipodomys ordii:0.221837,(Mus musculus:0.0266035,Rattus norvegicus:0.0750942)NoName:0.0461757)NoName:0.00764)NoName:0.00880882)NoName:0.00657224,(Oryctolagus cuniculus:0.202877,Ochotona princeps:0.145872)NoName:0.0638355)NoName:0.0023041,Tupaia belangeri:0.238703)NoName:0.015805)NoName:0.00917864,((((Myotis lucifugus:0.159107,Pteropus vampyrus:0.123197)NoName:0.0119737,(Felis catus:0.252679,Canis familiaris:0.0436977)NoName:0.0332699)NoName:0.00974075,((Vicugna pacos:0.233328,(Sus scrofa:0.194966,(Bos taurus:0.0721446,Tursiops truncatus:0.0849625)NoName:0.00381881)NoName:0.0312174)NoName:0.00890949,Equus caballus:0.0589069)NoName:0.00472376)NoName:0.00602604,(Sorex araneus:0.331544,Erinaceus europaeus:0.173301)NoName:0.0786709)NoName:0.0122055)NoName:0.02006,(Dasypus novemcinctus:0.142986,Choloepus hoffmanni:0.199419)NoName:0.0974878)NoName:0.00559745)NoName:0.0664386)NoName:0.0201763)NoName:0.0352992)NoName:0.0667082,Xenopus :0.400481)NoName:0.0561981,(Danio rerio:0.253567,((Gasterosteus aculeatus:0.160094,(Tetraodon nigroviridis:0.177537,Takifugu rubripes:0.0848838)NoName:0.069509)NoName:0.026982,Oryzias latipes:0.163666)NoName:0.0657831)NoName:0.120356)NoName:0.237299,(Ciona savignyi:0.211518,Ciona intestinalis:0.227022)NoName:0.484043)NoName:0.086661,((Caenorhabditis briggsae:0.287651,Caenorhabditis elegans:0.0988621)NoName:0.939458,(Daphnia pulex:0.474495,(((Tribolium castaneum:0.458641,(Bombyx mori:0.533393,((Anopheles gambiae:0.264319,(Culex pipiens:0.203418,Aedes aegypti:0.163776)NoName:0.0842155)NoName:0.143821,((Drosophila willistoni:0.118932,((Drosophila ananassae:0.09821,((Drosophila yakuba:0.0361813,Drosophila erecta:0.0344438)NoName:0.0104353,(Drosophila melanogaster:0.0274386,(Drosophila sechellia:0.0190908,Drosophila simulans:0.129106)NoName:0.0142595)NoName:0.0160134)NoName:0.0777807)NoName:0.0312419,(Drosophila persimilis:0.0545365,Drosophila pseudoobscura:0.00802841)NoName:0.108199)NoName:0.0302956)NoName:0.0585779,(Drosophila grimshawi:0.0950219,(Drosophila virilis:0.0811857,Drosophila mojavensis:0.101645)NoName:0.0276127)NoName:0.0409234)NoName:0.311389)NoName:0.160057)NoName:0.0353149)NoName:0.0433266,Nasonia vitripennis:0.493019)NoName:0.0546642,(Acyrthosiphon pisum:0.587825,Pediculus humanus:0.469467)NoName:0.0727439)NoName:0.113955)NoName:0.116386)NoName:0.0643657)NoName:0.0571989,Nematostella vectensis:0.602389)NoName:0.162658,Monosiga brevicollis:1.08535)NoName:0.0764555)NoName:0.117521,((((Encephalitozoon cuniculi:0.826109,Nosema ceranae:1.06119)NoName:0.253073,Enterocytozoon bieneusi:1.89302)NoName:0.260546,Antonospora locustae:1.20501)NoName:1.25355,(((Spizellomyces punctatus:0.46189,Batrachochytrium dendrobatidis:0.544453)NoName:0.246863,(Phycomyces blakesleeanus:0.304159,(Mucor circinelloides:0.203516,Rhizopus oryzae:0.279287)NoName:0.11582)NoName:0.345)NoName:0.0820205,((((((Sclerotinia sclerotiorum:0.102601,Botryotinia fuckeliana:0.088277)NoName:0.269843,(((Verticillium dahliae:0.0393024,Verticillium albo-atrum:0.163258)NoName:0.272713,((Trichoderma atroviride:0.0811427,(Hypocrea jecorina:0.0977353,Hypocrea virens:0.0725023)NoName:0.0322485)NoName:0.163851,(Nectria haematococca:0.118644,((Fusarium oxysporum:0.0964532,Gibberella moniliformis:0.0691291)NoName:0.0460617,Gibberella zeae:0.0954161)NoName:0.0545608)NoName:0.11427)NoName:0.080728)NoName:0.0538259,((((Myceliophthora thermophila:0.127458,Chaetomium globosum:0.184848)NoName:0.110291,Podospora anserina:0.215657)NoName:0.0426838,(Neurospora discreta:0.0319003,(Neurospora tetrasperma:0.0163826,Neurospora crassa:0.0295359)NoName:0.0167268)NoName:0.210936)NoName:0.114318,(Cryphonectria parasitica:0.286302,Magnaporthe oryzae:0.293502)NoName:0.0496719)NoName:0.0409845)NoName:0.105157)NoName:0.0928259,(((Phaeosphaeria nodorum:0.19717,((Alternaria brassicicola:0.16357,Pyrenophora tritici-repentis:0.10051)NoName:0.013231,Cochliobolus heterostrophus:0.105368)NoName:0.0801522)NoName:0.234949,(Mycosphaerella fijiensis:0.253368,Zymoseptoria tritici:0.236341)NoName:0.235436)NoName:0.103348,(((Paracoccidioides brasiliensis:0.174699,(Ajellomyces capsulatus:0.145653,Ajellomyces dermatitidis:0.097927)NoName:0.0407488)NoName:0.123506,(((Trichophyton equinum:0.0874824,Microsporum gypseum:0.0885479)NoName:0.0397571,Arthroderma otae:0.0731291)NoName:0.21288,(Uncinocarpus reesii:0.142244,(Coccidioides immitis:0.0202099,Coccidioides posadasii:0.0136648)NoName:0.094431)NoName:0.110637)NoName:0.0399469)NoName:0.0628946,(Penicillium chrysogenum:0.255436,((((Aspergillus oryzae:0.0182968,Aspergillus flavus:0.0367977)NoName:0.114103,Aspergillus terreus:0.147244)NoName:0.0229601,(Aspergillus nidulans:0.266412,Aspergillus niger:0.123469)NoName:0.0263436)NoName:0.0257103,((Aspergillus fumigatus:0.0277784,Neosartorya fischeri:0.0202421)NoName:0.0573864,Aspergillus clavatus:0.0918934)NoName:0.0597795)NoName:0.0475471)NoName:0.105505)NoName:0.149457)NoName:0.0498411)NoName:0.321272,(Yarrowia lipolytica:0.569386,(((((Debaryomyces hansenii:0.240005,Meyerozyma guilliermondii:0.325647)NoName:0.0388437,((((Candida albicans:0.0572746,Candida dubliniensis:0.0501041)NoName:0.101179,Candida tropicalis:0.179674)NoName:0.0880969,(Lodderomyces elongisporus:0.214239,Candida parapsilosis:0.188911)NoName:0.0946303)NoName:0.0963566,Scheffersomyces stipitis:0.217252)NoName:0.0619286)NoName:0.0513252,Clavispora lusitaniae:0.321979)NoName:0.19178,Komagataella pastoris:0.493152)NoName:0.0683444,(((((Candida glabrata:0.287733,(Saccharomyces bayanus:0.141471,(((Saccharomyces cerevisiae:0.0331165,Saccharomyces paradoxus:0.0504049)NoName:0.0203181,Saccharomyces mikatae:0.0856678)NoName:0.0192256,Saccharomyces kudriavzevii:0.110635)NoName:0.0135654)NoName:0.172627)NoName:0.0312816,Naumovozyma castellii:0.268802)NoName:0.0315812,Vanderwaltozyma polyspora:0.283226)NoName:0.0294297,Zygosaccharomyces rouxii:0.285979)NoName:0.0638309,(((Lachancea thermotolerans:0.120152,Lachancea waltii:0.14889)NoName:0.164824,Lachancea kluyveri:0.188667)NoName:0.0436613,(Kluyveromyces lactis:0.306025,Ashbya gossypii:0.315267)NoName:0.0484532)NoName:0.0372483)NoName:0.330746)NoName:0.184994)NoName:0.195235)NoName:0.0869579,((Schizosaccharomyces octosporus:0.237235,Schizosaccharomyces pombe:0.202131)NoName:0.178997,Schizosaccharomyces japonicus:0.295141)NoName:0.490437)NoName:0.1366,((Malassezia globosa:0.544037,Ustilago maydis:0.435196)NoName:0.296158,((Sporobolomyces roseus:0.533488,(Melampsora larici-populina:0.24201,Puccinia graminis:0.333041)NoName:0.351861)NoName:0.14486,(((Heterobasidion annosum:0.272937,(Phanerochaete chrysosporium:0.25536,Postia placenta:0.267769)NoName:0.0874132)NoName:0.035592,(((Laccaria bicolor:0.234334,Coprinopsis cinerea:0.27398)NoName:0.0658602,Pleurotus ostreatus:0.271529)NoName:0.0453082,Schizophyllum commune:0.356648)NoName:0.0472487)NoName:0.269084,(Tremella mesenterica:0.353039,Cryptococcus neoformans:0.325027)NoName:0.388205)NoName:0.0920112)NoName:0.0491572)NoName:0.203411)NoName:0.109689)NoName:0.143325)NoName:0.0946383)NoName:0.111912)NoName:0.0582637,(((Giardia lamblia:2.48105,Trichomonas vaginalis:1.8478)NoName:0.277301,(Entamoeba dispar:0.0841554,Entamoeba histolytica:0.0798277)NoName:1.63275)NoName:0.214613,((((Leishmania infantum:0.0404592,Leishmania major:0.0633053)NoName:0.0589499,Leishmania braziliensis:0.173051)NoName:0.412574,(Trypanosoma cruzi:0.285505,Trypanosoma brucei:0.402724)NoName:0.219751)NoName:1.15668,Naegleria gruberi:1.09379)NoName:0.157147)NoName:0.109039)NoName:0.0376542)NoName:0.0944978,((Chlamydomonas reinhardtii:0.808992,((Ostreococcus lucimarinus:0.0072916,Ostreococcus :0.00900685)NoName:0.181999,Ostreococcus tauri:0.268469)NoName:0.733023)NoName:0.142912,((((Glycine max:0.308117,(Vitis vinifera:0.804581,Populus trichocarpa:0.250545)NoName:0.0110282)NoName:0.0515868,(Arabidopsis thaliana:0.0898463,Arabidopsis lyrata:0.0995407)NoName:0.234677)NoName:0.0821533,((Brachypodium distachyon:0.203841,Oryza sativa:0.295291)NoName:0.0230444,(Zea mays:0.204318,Sorghum bicolor:0.0918347)NoName:0.088112)NoName:0.203712)NoName:0.183381,(Selaginella moellendorffii:0.399603,Physcomitrella patens:0.385355)NoName:0.103886)NoName:0.287042)NoName:0.256704)NoName:0.296185,(Aureococcus anophagefferens:1.04634,(Thalassiosira pseudonana:0.472396,(Fragilariopsis cylindrus:0.526096,Phaeodactylum tricornutum:0.367275)NoName:0.15269)NoName:0.457662)NoName:0.208369)NoName:0.665739)NoName:0.0550695)NoName:0.0203538,Phytophthora sojae:0.101226,Phytophthora ramorum:0.127103):0;', format=1)

#ensembl:
#((((((((((((((((((((((((Homo_sapiens:0.0067,Pan_troglodytes:0.006667):0.00225,Gorilla_gorilla:0.008825):0.00968,Pongo_abelii:0.018318):0.00717,Nomascus_leucogenys:0.025488):0.00717,(Macaca_mulatta:0.007853,?Papio_hamadryas:0.007637):0.029618):0.021965,Callithrix_jacchus:0.066131):0.05759,Tarsius_syrichta:0.137823):0.011062,(Microcebus_murinus:0.092749,Otolemur_garnettii:0.129725):0.035463):0.015494,Tupaia_belangeri:0.186203):0.004937,(((((Mus_musculus:0.084509,Rattus_norvegicus:0.091589):0.197773,Dipodomys_ordii:0.211609):0.022992,Cavia_porcellus:0.225629):0.01015,Spermophilus_tridecemlineatus:0.148468):0.025746,(Oryctolagus_cuniculus:0.114227,Ochotona_princeps:0.201069):0.101463):0.015313):0.020593,((((Vicugna_pacos:0.107275,(Tursiops_truncatus:0.064688,(Bos_taurus:0.061796,?Ovis_aries:0.061796):0.061796):0.025153):0.0201675,Sus_scrofa:0.079):0.0201675,((Equus_caballus:0.109397,(Felis_catus:0.098612,(Ailuropoda_melanoleuca:0.051229,Canis_familiaris:0.051229):0.051229):0.049845):0.006219,(Myotis_lucifugus:0.14254,Pteropus_vampyrus:0.113399):0.033706):0.004508):0.011671,(Erinaceus_europaeus:0.221785,Sorex_araneus:0.269562):0.056393):0.021227):0.023664,(((Loxodonta_africana:0.082242,Procavia_capensis:0.155358):0.02699,Echinops_telfairi:0.245936):0.049697,(Dasypus_novemcinctus:0.116664,Choloepus_hoffmanni:0.096357):0.053145):0.006717):0.234728,(Monodelphis_domestica:0.125686,(Macropus_eugenii:0.101004,Sarcophilus_harrisii:0.101004):0.021004):0.2151):0.071664,Ornithorhynchus_anatinus:0.456592):0.109504,((((Gallus_gallus:0.041384,Meleagris_gallopavo:0.041384):0.041384,Anas_platyrhynchos:0.082768):0.082768,Taeniopygia_guttata:0.171542):0.199223,Anolis_carolinensis:0.489241):0.105143):0.172371,Xenopus_tropicalis:0.855573):0.155677,Latimeria_chalumnae:0.155677):0.155677,(((Oreochromis_niloticus:0.45,(Tetraodon_nigroviridis:0.224159,Takifugu_rubripes:0.203847):0.195181,(Gasterosteus_aculeatus:0.316413,Oryzias_latipes:0.48197):0.05915):0.16282,Gadus_morhua:0.16282):0.16282,Danio_rerio:0.730752):0.147949):0.526688,Petromyzon_marinus:0.526688):0.526688,(Ciona_savignyi:0.8,Ciona_intestinalis:0.8)Cionidae:0.6)Chordata:0.2,(?Apis_mellifera:0.9,(((?Aedes_aegypti:0.25,?Culex_quinquefasciatus:0.25):0.25,?Anopheles_gambiae:0.5)Culicinae:0.2,Drosophila_melanogaster:0.8)Diptera:0.1)Endopterygota:0.7)Coelomata:0.1,Caenorhabditis_elegans:1.7)Bilateria:0.3,Saccharomyces_cerevisiae:1.9)Fungi_Metazoa_group:0.3);

tree = Tree('/home/francisco/Downloads/ncbi_complete_with_names.newick', format=1)

tree_ncbi = Tree('tree_54_NCBI.nw', format=1)

i = 0
for spe in species:
    if not spe in tree:
        print spe
        i+=1
print i

for spe in tree:
    if not spe.name in species:
        spe.delete(prevent_nondicotomic=False)

while len (tree)*2-1 != len (tree.get_descendants()):
for node in tree.get_descendants()+[tree]:
    if node.is_leaf():
        if node.name == 'NoName':
            node.delete(prevent_nondicotomic=False)
        continue
    if len (node.get_children()) == 1:
        node.get_children()[0].dist += node.dist
        if node.is_root():
            node.get_children()[0].delete(prevent_nondicotomic=False)
        else:
            node.delete(prevent_nondicotomic=False)

for n in tree.iter_descendants():
    n.dist=1

tree.dist=0

def my_basic(node):
    """
    because i want bigger font"""
    node.img_style["hz_line_width"] = 2
    node.img_style["vt_line_width"] = 2
    node.img_style["size"]=2
    node.img_style["shape"] = "square"
    node.img_style["fgcolor"] = 'black'
    if node.is_root():
        node.img_style["size"]=0
        node.img_style["hz_line_color"]='white'
    if node.is_leaf():
        node.img_style["size"]=1
        node.img_style["shape"] = "circle"
        faces.add_face_to_node(faces.AttrFace("name","Courier", 15,
                                              'black', None),
                               node, 0, aligned=True)


tree= Tree('((((Arabidopsis thaliana:0.0898463,Arabidopsis lyrata:0.0995407)NoName:0.234677,Populus trichocarpa:0.31316)NoName:0.0821533,((Brachypodium distachyon:0.203841,Oryza sativa:0.295291)NoName:0.0230444,(Zea mays:0.204318,Sorghum bicolor:0.0918347)NoName:0.088112)NoName:0.203712)NoName:0.825127,((((((Danio rerio:0.253567,(Oryzias latipes:0.163666,Tetraodon nigroviridis:0.274028)NoName:0.0657831)NoName:0.120356,((Taeniopygia guttata:0.0838698,Gallus gallus:0.0669647)NoName:0.146994,(Monodelphis domestica:0.157621,((((Pongo abelii:0.106124,(Homo sapiens:0.00813613,Pan troglodytes:0.0483462)NoName:0.00627258)NoName:0.00754995,Macaca mulatta:0.0577307)NoName:0.0365404,(Mus musculus:0.0266035,Rattus norvegicus:0.0750942)NoName:0.0873059)NoName:0.00917864,((Equus caballus:0.0589069,Bos taurus:0.11609)NoName:0.00472376,Canis familiaris:0.0867083)NoName:0.0182315)NoName:0.0920961)NoName:0.0554755)NoName:0.122906)NoName:0.237299,Ciona intestinalis:0.711065)NoName:0.086661,(Caenorhabditis elegans:1.03832,(Tribolium castaneum:0.458641,(Anopheles gambiae:0.40814,Drosophila melanogaster:0.552737)NoName:0.195372)NoName:0.328332)NoName:0.0643657)NoName:0.413833,Saccharomyces cerevisiae:1.69716)NoName:0.111912,Dictyostelium discoideum:1.08758)NoName:0.0959179,(Thalassiosira pseudonana:0.988429,Plasmodium falciparum:2.03194)NoName:0.15):0;', format=1)
tree = Tree('(((((Plasmodium alciparum:2.18194,((((((Danio rerio:0.253567,(Oryzias latipes:0.163666,Tetraodon nigroviridis:0.274028)NoName:0.0657831)NoName:0.120356,((Taeniopygia guttata:0.0838698,Gallus gallus:0.0669647)NoName:0.146994,(Monodelphis domestica:0.157621,((((Pongo abelii:0.106124,(Homo sapiens:0.00813613,Pan troglodytes:0.0483462)NoName:0.00627258)NoName:0.00754995,Macaca mulatta:0.0577307)NoName:0.0365404,(Mus musculus:0.0266035,Rattus norvegicus:0.0750942)NoName:0.0873059)NoName:0.00917864,((Equus caballus:0.0589069,Bos taurus:0.11609)NoName:0.00472376,Canis familiaris:0.0867083)NoName:0.0182315)NoName:0.0920961)NoName:0.0554755)NoName:0.122906)NoName:0.237299,Ciona intestinalis:0.711065)NoName:0.086661,((Daphnia pulex:0.474495,(Tribolium castaneum:0.458641,(Anopheles gambiae:0.40814,Drosophila melanogaster:0.552737)NoName:0.195372)NoName:0.211946)NoName:0.116386,Caenorhabditis elegans:1.03832)NoName:0.0643657)NoName:0.413833,Saccharomyces cerevisiae:1.69716)NoName:0.111912,Dictyostelium discoideum:1.08758)NoName:0.0959179)NoName:0.0944978,((((Arabidopsis thaliana:0.0898463,Arabidopsis lyrata:0.0995407)NoName:0.234677,Populus trichocarpa:0.31316)NoName:0.0821533,((Brachypodium distachyon:0.203841,Oryza sativa:0.295291)NoName:0.0230444,(Zea mays:0.204318,Sorghum bicolor:0.0918347)NoName:0.088112)NoName:0.203712)NoName:0.183381,Physcomitrella patens:0.489241)NoName:0.543746)NoName:0.296185,(Thalassiosira pseudonana:0.472396,Phaeodactylum tricornutum:0.519965)NoName:0.666031)NoName:0.3,((((Buchnera aphidicola:0.3,Escherichia coli:0.3)Enterobacteriaceae:0.3,Carsonella ruddii:0.3)Gammaproteobacteria:0.3,Burkholderia xenovorans:0.3)Proteobacteria:0.3,Ureaplasma urealyticum:0.3,Mycobacterium tuberculosis:0.3,Bacillus subtilis:0.3)Bacteria:0.3,((Methanocaldococcus vulcanius:0.3,Thermococcus sibiricus:0.3)Euryarchaeota:0.3,Sulfolobus islandicus:0.3)Archaea:0.3)NoName:0.3,((Hepatitis B virus:0.3,Human immunodeficiency virus 1:0.3)Retro-transcribing_viruses:0.3,(Human herpesvirus 1:0.3,Enterobacteria phage lambda:0.3)dsDNA_viruses__no_RNA_stage:0.3,(Tomato mosaic virus:0.3,Sudan ebolavirus:0.3)ssRNA_viruses:0.3,Hepatitis D virus:0.3,Enterobacteria phage M13:0.3)Viruses:0.3):0.0;', format=1)
        
ts = TreeStyle()
ts.mode='c'
ts.show_leaf_name = False
#ts.tree_width=300
#ts.legend = {'why a dict of lists??': [Legend(colors, keys,fsize=14,columns=4)]}
#ts.legend_position=3
ts.draw_aligned_faces_as_table=True

tree.show(tree_style=ts, layout=my_basic)








