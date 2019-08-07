#!/usr/bin/python

from pylab import get_cmap, annotate, pi, cos, sin
import matplotlib.pyplot as plt
from matplotlib import rcParams

# make a square figure and axes
fig = plt.figure(1, figsize=(7, 7))

labels = ('SINEs', 'LINEs', 'Protein-coding\ngenes', 'Introns',
          'Miscellaneous\nunique sequences', 'Miscellaneous\nheterochromatine',
          'Segmental\nduplications', 'Simple sequence\nrepeats',
          'DNA transposons', 'LTR\nretrotransposons')
fracs = [13.1, 20.4, 1.5, 25.9, 11.6, 8, 5, 3, 2.9, 8.3]

cm = get_cmap('gray_r')
colors = [cm(float(i+1)/25) for i in xrange (len (labels))]

p = plt.pie(fracs, autopct='%1.1f%%', colors=colors, pctdistance=0.75)

for perc in p[2]:
    perc.set_fontsize('small')

for p1, l1 in zip(p[0], labels):
    r = p1.r
    dr = r*0.1
    t1, t2 = p1.theta1, p1.theta2
    theta = (t1+t2)/2.
    xc, yc = r/2.*cos(theta/180.*pi), r/2.*sin(theta/180.*pi)
    x1, y1 = (r+dr)*cos(theta/180.*pi), (r+dr)*sin(theta/180.*pi)
    if x1 > 0 :
        x1 = r+1*dr
        ha, va = "left", "center"
        tt = -180
        cstyle="angle,angleA=0,angleB=%f"%(theta,)
    else:
        x1 = -(r+1*dr)
        ha, va = "right", "center"
        tt = 0
        cstyle="angle,angleA=0,angleB=%f"%(theta,)
    annotate(l1,
             (xc, yc), xycoords="data",
             xytext=(x1, y1), textcoords="data", ha=ha, va=va,
             arrowprops=dict(arrowstyle="-",color='grey',
                             connectionstyle=cstyle,
                             patchB=p1),
             fontweight='extra bold' if l1.startswith('Prot') else 'normal')
# zoom out in order to display entire labels
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.savefig ('../tex_source/figures/dna_struct/prop_rep.pdf', format='pdf')

