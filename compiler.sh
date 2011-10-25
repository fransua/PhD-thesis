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


echo "-----------------------"
echo "------ PDFLATEX1 ------"
echo "-----------------------"
echo ""

pdflatex -draftmode -interaction=nonstopmode --src-specials tex_source/main > /dev/null 2>&1

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

pdflatex -draftmode -interaction=nonstopmode --src-specials tex_source/main > /dev/null 2>&1

echo ""
echo "-----------------------"
echo "------ PDFLATEX3 ------"
echo "-----------------------"
echo ""

pdflatex -interaction=nonstopmode --src-specials tex_source/main | egrep -i --color "(.*warning|underfull|overfull|.*error.*|)"


if [ $1 = 'clean' ];
then
echo ""
echo "-----------------------"
echo "----- CLEANNING.. -----"
echo "-----------------------"
echo ""
rm -f *.aux *.bbl *.ilg *.lot 
rm -f *.nlo *.nls *.toc *.out 
rm -f *.lof *.blg *.log *.mtc* 
rm -f *.idx *.maf *.plf *.plt
rm -f *.plc *.ptc
rm -f */*.aux */*/*.aux
fi


echo ""
echo "-----------------------"
echo "------ THE END.. ------"
echo "-----------------------"
echo ""


#okular main.pdf

