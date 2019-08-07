"""
prepare a table of repetitive elements
AND
CDS and introns
"""

import re

species = {'Gallus gallus'           : 'Birds',                 
           'Taeniopygia guttata'     : 'Birds',                 
           'Danio rerio'             : 'Fishes',                
           'Oryzias latipes'         : 'Fishes',                
           'Tetraodon nigroviridis'  : 'Fishes',                
           'Saccharomyces cerevisiae': 'Fungi',                 
           'Anopheles gambiae'       : 'Invertebrates',         
           'Caenorhabditis elegans'  : 'Invertebrates',         
           'Drosophila melanogaster' : 'Invertebrates',         
           'Tribolium castaneum'     : 'Invertebrates',         
           'Bos taurus'              : 'Mammals',               
           'Canis familiaris'        : 'Mammals',               
           'Equus caballus'          : 'Mammals',               
           'Homo sapiens'            : 'Mammals',               
           'Macaca mulatta'          : 'Mammals',               
           'Monodelphis domestica'   : 'Mammals',               
           'Mus musculus'            : 'Mammals',               
           'Pan troglodytes'         : 'Mammals',               
           'Pongo abelii'            : 'Mammals',               
           'Rattus norvegicus'       : 'Mammals',               
           'Arabidopsis lyrata'      : 'Plants',                
           'Arabidopsis thaliana'    : 'Plants',                
           'Brachypodium distachyon' : 'Plants',                
           'Oryza sativa'            : 'Plants',                
           'Populus trichocarpa'     : 'Plants',                
           'Sorghum bicolor'         : 'Plants',                
           'Zea mays'                : 'Plants',                
           'Dictyostelium discoideum': 'unicellular Eukaryotes',
           'Plasmodium falciparum'   : 'unicellular Eukaryotes',
           'Thalassiosira pseudonana': 'unicellular Eukaryotes',
           'Ciona intestinalis'      : 'Urochordate'}           

def parse_repeat_masker_tbl(spe, wanteds):
    elements={}
    intbl = False
    for line in open('prop_ge/'+spe.replace(' ', '_')+'.all_chromosomes.fasta.tbl'):
        if re.match('^------------', line):
            intbl=True
            continue
        if 'total length: ' in line:
            elements['total'] = float(line.split()[2])
        if 'Total ' in line: continue
        for name in wanteds:
            if name in line:
                length = re.findall('[A-Za-z -]*:? +[0-9]* *([0-9]+) ?bp *[0-9]*.[0-9]* %\n', line)[0]
                elements[name] = float(length)
    for name in wanteds:
        if not name in elements:
            elements[name] = 0.0
    return elements

cds_introns = {}
for line in open('prop_ge/genes_cds.tbl'):
    spe, cds, genes = line.strip().split('\t')
    cds_introns[spe] = [int(cds), int(genes)-int(cds)]


elements={}
wanteds = ['Coding sequence', 'Introns', 'SINEs', 'LINEs', 'LTR',
           'DNA', 'Satellites', 'Small RNA', 'Simple repeats', 'Low complexity',
           'Unclassified']

for spe in species:
    elements[spe] = parse_repeat_masker_tbl(spe, wanteds)
    elements[spe]['Coding sequence']      = cds_introns[spe][0]
    elements[spe]['Introns']  = cds_introns[spe][1]
    elements[spe]['percents'] = []
    total = 0
    for el in wanteds:
        if not el in elements[spe]:
            percent = 0.0
        else:
            percent = elements[spe][el] / elements[spe]['total']
            total += elements[spe][el]
        elements[spe]['percents'].append(percent*100)
    elements[spe]['Miscellaneous sequence'] = elements[spe]['total'] - total
    elements[spe]['percents'].append(100 * elements[spe]['Miscellaneous sequence'] / elements[spe]['total'])

nice = {'Coding sequence'       : 'Protein coding',
        'Introns'               : 'Intronic',
        'SINEs'                 : 'SINE',
        'LINEs'                 : 'LINE',
        'LTR'                   : 'LTR',
        'DNA'                   : 'DNA transposon',
        'Satellites'            : 'Satellite',
        'Small RNA'             : 'Small RNA',
        'Simple repeats'        : 'Simple repeat',
        'Low complexity'        : 'Low complexity',
        'Unclassified'          : 'Unclassified repeat',
        'Miscellaneous sequence': 'Miscellaneous unique',
        'total'                 : 'Total'
    }

nice_ord = ['Coding sequence', 'Introns', 'SINEs', 'LINEs', 'LTR', 'DNA',
            'Satellites', 'Small RNA', 'Simple repeats', 'Low complexity',
            'Unclassified', 'Miscellaneous sequence', 'total']

out = open('prop_ge/all_GS.tbl','w')
out.write('#Species\t' + '\t'.join([nice [n] for n in nice_ord]) + '\n')
for spe in species:
    out.write(spe + '\t' + '\t'.join([str(elements[spe][n]) for n in nice_ord]) + '\n')
out.close()

