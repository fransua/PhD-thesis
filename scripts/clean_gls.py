#/usr/bin/python

"""
find all occurences of s glossary entry in the main text, and put the glossary flag
example: I have the words 'potato' 'bob' and 'garden' in the glossary:

'Bob loves eating potatoes in the garden'
after running this script the sentence becomes:
'\myGls{bob} loves eating \myglspl{potato} in the \mygls{garden}'

.. maybe a bit dangerous :S
"""

import os, re


glossary = os.path.expanduser('~/Documents/these/tex_source/Complements/glossary.tex')

gls_entries = {}
inside = False
for line in open(glossary):
    if line.startswith('\\newglossaryentry'):
        inside = True
        name   = re.sub('.*\{(.*)\}.*\n', '\\1', line)
        gls_entries[name] = {'name'  : name,
                             'plural': name+'s',
                             'title' : name[0].upper() + name[1:]}
        continue
    if inside and 'plural=' in line:
        gls_entries[name]['plural'] = line.strip().split('=')[1]
        if ',' in gls_entries[name]['plural']:
            gls_entries[name]['plural'] = gls_entries[name]['plural'][:-1]


tex_source = os.path.expanduser('~/Documents/these/tex_source/')

glspl   = re.compile(r'\\my[gG]lspl\{([\w -]*)\}')
gls     = re.compile(r'\\my[gG]ls\{([\w -]*)\}')
glsin   = re.compile(r'.*\\my[gG]ls(?:pl)?\{[\w -]*\}.*')

pl_str  = '\\\my[gG]ls(?:pl)?\{here\}'

for tex_dir, _, texs in os.walk(tex_source):
    for tex in texs:
        if not tex.endswith('.tex'):
            continue
        if 'glossary' in tex:
            continue
        if 'nomenclature' in tex:
            continue
        if 'thesis' in tex:
            continue
        corr_lines = []
        print tex_dir, tex
        for line in open(tex_dir + '/' + tex):
            found = True if re.match(glsin, line) else False
            if found: print line,
            line = re.sub(gls, r'\1', line)
            for word in re.findall(glspl, line):
                tmp = re.sub('here', word, pl_str)
                line = re.sub(tmp, gls_entries[word]['plural'], line)
            corr_lines.append(line)
            if found: print line
            
        out = open(tex_dir + '/' + tex, 'w')
        out.write(''.join(corr_lines))
        out.close()


