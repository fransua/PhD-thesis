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
            found = 0
            i = 200000000
            plural=False
            title =False
            while True:
                if '\\caption' in line:
                    break
                for gls in sorted(gls_entries, key=len, reverse=True):
                    if gls_entries[gls]['plural'] in line:
                        cur_gls = gls_entries[gls]['plural']
                        plural=True
                    elif gls_entries[gls]['plural'] in line.lower():
                        cur_gls = gls[0].upper() + gls_entries[gls]['plural'][1:]
                        plural=True
                        title =True
                    elif gls in line:
                        cur_gls = gls
                    elif gls in line.lower():
                        cur_gls = gls_entries[gls]['title']
                        title =True
                    else:
                        continue
                    if not plural:
                        gls_str = 'mygls'
                        if title:
                            gls_str = 'myGls'
                    else:
                        gls_str = 'myglspl'
                        if title:
                            gls_str = 'myGlspl'
                    #re.sub('\\mygsl(?:pl)?', '', line)
                    if found:
                        try:
                            i = line[found+len(cur_gls):].index(cur_gls)+found+len(cur_gls)
                            j = i + len(cur_gls)
                        except ValueError:
                            break
                    else:
                        i = line.index(cur_gls)
                        j = i + len(cur_gls)
                    if (not 'tools' in tex) and gls in ['object', 'instance', 'class']:
                        continue
                    if 'class' in cur_gls and ('of site' in line[j:j+9] or 'site' in line[i-7:i]):
                        continue
                    if line[j].isalpha():
                        continue
                    if line[i-1].isalpha() or line[i+len(cur_gls)] == '}' or line[i-1] == '\\':
                        if not '\\text' in line[i-8:i]:
                            continue
                    if i == found:
                        break
                    dbl_break = False
                    for c in xrange(i,0,-1):
                        if line[c] == ' ':
                            break
                        if line[c] in ['/', ':']:
                            dbl_break = True
                    if dbl_break:
                        continue
                    print line,
                    line = re.sub('(.*)('+cur_gls+')(.*)', '\\1\\'+gls_str+'{'+gls+'}\\3',
                                  line[:i+len(cur_gls)]) + line[i+len(cur_gls):]
                    print line
                if found == i:
                    break
                found = i
            corr_lines.append(line)
        out = open(tex_dir + '/' + tex, 'w')
        out.write(''.join(corr_lines))
        out.close()


