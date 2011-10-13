#/bin/bash

cd ~/Documents/these/tex_source

pdflatex -draftmode -interaction=nonstopmode --src-specials main > /dev/null 2>&1

bibtex main

pdflatex -draftmode -interaction=nonstopmode --src-specials main > /dev/null 2>&1

makeindex main.nlo -s nomencl.ist -o main.nls

pdflatex -interaction=nonstopmode --src-specials main


cd ..

rm -f tex_source/*.aux tex_source/*.bbl tex_source/*.ilg tex_source/*.lot tex_source/*.nlo tex_source/*.nls tex_source/*.toc tex_source/*.out tex_source/*.lof tex_source/*.blg tex_source/*.log tex_source/*.mtc* tex_source/*.idx tex_source/*.maf
rm -f tex_source/*/*.aux tex_source/*/*/*.aux

mv tex_source/main.pdf .

okular main.pdf

