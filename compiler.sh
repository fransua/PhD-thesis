#/bin/bash

help=0
verbose=0
clean=0

# option parser
for opt in $*;
do
  if [ $opt = 'help' -o $opt = '-h' -o $opt = '--help'  -o $opt = '-help' ];
  then
  help=1
  elif [ $opt = 'verbose' ];
  then
  verbose=1
  elif [ $opt = 'clean' ];
  then
  clean=1
  fi
done

if [ $help = 1 ];
then
echo "-----------------------"
echo "-- CONGRATULATIONS!! --"
echo "-----------------------"
echo "- YOU FOUND THE HELP! -"
echo "-----------------------"
echo ""
echo "Options that could be provided:"
echo "clean   : compile and clean all extra latex files."
echo "verbose : display more details about compilation."
echo "clean   : compile and clean all extra latex files."
echo "help    : displays this help"
echo ""
echo ""
exit
fi


# compilation #1
pdflatex -draftmode -interaction=nonstopmode --src-specials master > /dev/null 2>&1

echo "  ------- BIBTEX --------"

bibtex master | egrep -i --color "(.*Warning|Underfull|Overfull|.*error.*|)"
echo ""

echo "  ------ MAKEINDEX ------"

makeindex master.nlo -s nomencl.ist -o master.nls
echo ""

echo "  ------ PDFLATEX -------"

# compilation #2
pdflatex -draftmode -interaction=nonstopmode --src-specials master > /dev/null 2>&1

# compilation #3
if [ $verbose = 1 ];
then
pdflatex -interaction=nonstopmode --src-specials master | egrep -i --color "(.*warning|underfull|illegal|overfull|undefined|.*error.*|)"
else
pdflatex -interaction=nonstopmode --src-specials master | egrep -v "^[a-z()<>0-9,/]" | egrep -i --color "(.*warning|underfull|illegal|overfull|undefined|.*error.*|)"
fi

if [ $clean = 1 ];
then
echo ""
echo "  ----- CLEANNING.. -----"
rm -f *.aux *.bbl *.ilg *.lot 
rm -f *.nlo *.nls *.toc *.out 
rm -f *.lof *.blg *.log *.mtc* 
rm -f *.idx *.maf *.plf *.plt
rm -f *.plc *.ptc
rm -f */*.aux */*/*.aux
fi


echo ""
echo "  ------ THE END.. ------"
echo ""


#okular master.pdf
