#!/bin/sh

ACT=`xdotool getactivewindow`

WID=`xdotool search "$1" | head -1`

echo $WID

if [ $WID -gt 1 ];
then 
xdotool windowactivate --sync $WID; xdotool key --clearmodifiers r;
else
mupdf $1;
fi

xdotool windowactivate $ACT;

