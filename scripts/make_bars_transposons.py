#!/usr/bin/python

import matplotlib.pyplot as plt
   
names = [ 'Hs', 'Mm', 'Ce', 'Dm', 'De', 'Ag',
          'Aa', 'Ed', 'Eh', 'Ei', 'Em', 'Sc',
          'Sp', 'Os', 'At', 'Gi', 'Tv']

values = {'Sc': (100, 0 ),
          'Sp': (100, 0 ),
          'Hs': (93 , 7 ),
          'Mm': (96 , 4 ),
          'Os': (14 , 86),
          'At': (59 , 41),
          'Ce': (16 , 84),
          'Dm': (78 , 22),
          'De': (83 , 17),
          'Ag': (62 , 38),
          'Aa': (30 , 70),
          'Ed': (98 , 2 ),
          'Eh': (99 , 1 ),
          'Ei': (2  , 98),
          'Em': (2  , 98),
          'Gi': (99 , 1 ),
          'Tv': (1  , 99)}

width = 0.65
ind   = range(len(values))
fig = plt.figure(num=None, figsize=(9,3))
ax = fig.add_subplot(111)
plt.grid(False)

p1 = plt.bar(ind, [values[x][0] for x in names], width, color='grey')
p2 = plt.bar(ind, [values[x][1] for x in names], width, color='black', bottom=[values[x][0] for x in names])

#plt.xlabel('Species')
plt.ylabel('Relative contribution (%)', size=15)
plt.xticks([i+width/2 for i in ind], names, size=13)
plt.yticks(range(0, 100+1, 20), range(0, 100+1, 20), size=13)
plt.legend((p1[0], p2[0]), ('Retrotransposons', 'DNA transposons'),
           bbox_to_anchor=(1,1.28))
#ax.xaxis.grid(True)
ax.yaxis.grid(True, which='major')
plt.xlim(0,len(names))

#plt.show()

plt.savefig ('../figures/introduction/prop_transposons.pdf', format='pdf')

complete_names = {'Hs':  'Homo sapiens',
                  'Mm':  'Mus musculus',
                  'Ce':  'Caenorhabditis elegans',
                  'Dm':  'Drosophila melanogaster',
                  'De':  'Drosophila erecta',
                  'Ag':  'Anopheles gambiae',
                  'Aa':  'Aedes aegypti',
                  'Ed':  'Entamoeba dispar',
                  'Eh':  'Entamoeba histolytica',
                  'Ei':  'Entamoeba invadens',
                  'Em':  'Entamoeba moshkovskii',
                  'Sc':  'Saccharomyces cerevisiae',
                  'Sp':  'Schizosaccharomyces pombe',
                  'At':  'Arabidopsis thaliana',
                  'Os':  'Oryza sativa japonica',
                  'Gi':  'Giardia lamblia',
                  'Tv':  'Trichomonas vaginalis'}

for name in names:
    print '\\textbf{%s}=\\textit{%s},' % (name, complete_names[name]),


 