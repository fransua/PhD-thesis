#/bin/bash


if [ $1 = 'help' -o $1 = '-h' -o $1 = '--help'  -o $1 = '-help' ];
then
echo "-----------------------"
echo "-- CONGRATULATIONS!! --"
echo "-----------------------"
echo "- YOU FOUND THE HELP! -"
echo "-----------------------"
echo ""
echo "Options that could be provided:"
echo "clean : compile and clean all extra latex files."
echo "help  : displays this help"
echo ""
echo ""
exit
fi


cd ~/Documents/these/tex_source

echo "-----------------------"
echo "------ PDFLATEX1 ------"
echo "-----------------------"
echo ""

pdflatex -draftmode -interaction=nonstopmode --src-specials main > /dev/null 2>&1

echo ""
echo "-----------------------"
echo "------- BIBTEX --------"
echo "-----------------------"
echo ""

bibtex main | egrep -i --color "(.*Warning|Underfull|Overfull|.*error.*|)"

echo ""
echo "-----------------------"
echo "------ MAKEINDEX ------"
echo "-----------------------"
echo ""

makeindex main.nlo -s nomencl.ist -o main.nls

echo ""
echo "-----------------------"
echo "------ PDFLATEX2 ------"
echo "-----------------------"
echo ""

pdflatex -draftmode -interaction=nonstopmode --src-specials main > /dev/null 2>&1

echo ""
echo "-----------------------"
echo "------ PDFLATEX3 ------"
echo "-----------------------"
echo ""

pdflatex -interaction=nonstopmode --src-specials main | egrep -i --color "(.*warning|underfull|overfull|.*error.*|)"

cd ..

if [ $1 = 'clean' ];
then
echo ""
echo "-----------------------"
echo "----- CLEANNING.. -----"
echo "-----------------------"
echo ""
rm -f tex_source/*.aux tex_source/*.bbl tex_source/*.ilg tex_source/*.lot 
rm -f tex_source/*.nlo tex_source/*.nls tex_source/*.toc tex_source/*.out 
rm -f tex_source/*.lof tex_source/*.blg tex_source/*.log tex_source/*.mtc* 
rm -f tex_source/*.idx tex_source/*.maf tex_source/*.plf tex_source/*.plt
rm -f tex_source/*.plc tex_source/*.ptc

rm -f tex_source/*/*.aux tex_source/*/*/*.aux
fi

mv tex_source/main.pdf .

echo ""
echo "-----------------------"
echo "------ THE END.. ------"
echo "-----------------------"
echo ""


#okular main.pdf

