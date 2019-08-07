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

replace = {'\fref': [re.compile('(.*)\\fref\{(.*?)\}(?:\{.+\})?(.*)'),
                     '\\1\\ref{\\2}\\3'],
           'FPfigure':['FPfigure', 'figure']
           
}

tex_source = os.path.expanduser('~/Documents/these/tex_source/')

for tex_dir, _, texs in os.walk(tex_source):
    for tex in texs:
        if not tex.endswith('.tex'):
            continue
        corr_lines = []
        print tex_dir, tex
        for line in open(tex_dir + '/' + tex):
            if 'mythumb' in line:
                if len(line)>20:
                    line = line[:-11]
                else:
                    continue
            if '\my' in line:
                line = re.sub('\\my', '', line)
            for repl in replace:
                while repl in line:
                    line = re.sub(replace[repl][0], replace[repl][1], line)
            line = re.sub(r'\\[a-z]+ref\{([a-z]+:?)',r'\1 \\ref{\1',line)
            corr_lines.append(line)
        os.system('cp %s %s' % (tex_dir + '/' + tex, tex_dir + '/' + tex.replace('.tex', '.bkp')))
        out = open(tex_dir + '/' + tex, 'w')
        out.write(''.join(corr_lines))
        out.close()

os.system('latex2rtf thesis_main.tex')

for tex_dir, _, texs in os.walk(tex_source):
    for tex in texs:
        if not tex.endswith('.tex'):
            continue
        corr_lines = []
        print tex_dir, tex
        os.system('cp %s %s' % (tex_dir + '/' + tex.replace('.tex', '.bkp'), tex_dir + '/' + tex))
