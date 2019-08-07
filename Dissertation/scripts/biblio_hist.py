#!/usr/bin/python
"""
21 Jul 2012


"""

__author__  = "Francois-Jose Serra"
__email__   = "francois@barrabin.org"
__licence__ = "GPLv3"
__version__ = "0.0"

import re
import pylab as pb

years = []
inside = False
for line in open('thesis_main.bbl'):
    if 'bibitem' in line:
        inside = True
    if not inside: continue
    year = re.findall('\{[1,2][0-9]{3}\}', line)
    if year:
        years.append(int(year[0][1:-1]))

fig = pb.figure(figsize=(2,10))
ax = fig.add_subplot(111)
pb.grid(alpha=.6,color='white',ls='-',lw=1.5)

bp = ax.boxplot(years, notch=1)
pb.setp(bp['boxes'], color='black')
pb.setp(bp['medians'], color='black',lw=2)
pb.setp(bp['whiskers'], color='black')
pb.setp(bp['fliers'], color='grey', marker='+')

ax.set_ylim((1870,2013))
ax.set_xlim((0.8,1.2))
ax.set_yticks([y for y in range(1872,2013,10)])
ax.set_xticks([])
ax.set_xticklabels([])
pb.subplots_adjust(left=.4)
pb.savefig('test.pdf', format='pdf')

