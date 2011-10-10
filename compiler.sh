#/bin/bash

cd /home/garamonfok/Documents/these/tex_source

pdflatex -draftmode -interaction=nonstopmode --src-specials main > /dev/null 2>&1

bibtex main

pdflatex -draftmode -interaction=nonstopmode --src-specials main > /dev/null 2>&1

makeindex main.nlo -s nomencl.ist -o main.nls

pdflatex -interaction=nonstopmode --src-specials main


cd ..

rm -f */*.aux */*.bbl */*.ilg */*.lot */*.nlo */*.nls */*.toc */*.out */*.lof */*.blg */*.log 
rm -f */*/*.aux */*/*/*.aux

mv tex_source/main.pdf .

okular main.pdf

