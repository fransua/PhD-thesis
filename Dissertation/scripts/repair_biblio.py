#!/usr/bin/python
"""
09 Jan 2012


"""

__author__  = "Francois-Jose Serra"
__email__   = "francois@barrabin.org"
__licence__ = "GPLv3"
__version__ = "0.0"

from string import letters
import re

biblio = 'biblio/library.bib'

entries = {}
inside = False
key = ''
for line in open (biblio):
    if line.startswith('@'):
        key = line.strip().split('{')[1][:-1]
        if key in entries:
            key += 'a'
        i = 1
        while key in entries:
            key += key[:-1] + letters[i]
            i += 1    
        entries[key] = line
        inside = True
    elif key:
        entries[key] += line

out = open(biblio, 'w')
for key in entries:
    entries[key] = re.sub('@([a-z]+)\{.*,\n',
                          '@\\1{'+ key + ',\n', entries[key])
    out.write(entries[key])
out.close()
