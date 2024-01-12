#!/bin/bash

default_opts=''

if [ $1 ]
then
gal=`echo $1 | cut -f1-3 -d.`
ra=`grep -m1 $gal < ra_dec.txt| awk '{print $2}'`
dec=`grep -m1 $gal < ra_dec.txt| awk '{print $3}'`

if [ $2 ]
then
    opt=$2
else
    opt=$default_opts
fi


if [ $3 ]
then
    link="http://casjobs.sdss.org/ImgCutoutDR5/getjpeg.aspx?ra=$ra&dec=$dec&scale=$3&width=512&height=512&opt=$opt"
else
    link="http://casjobs.sdss.org/ImgCutoutDR5/getjpeg.aspx?ra=$ra&dec=$dec&scale=0.2&width=512&height=512&opt=$opt"
fi


wget -q $link -O img.tmp 
display img.tmp
rm img.tmp

else

echo "Script to get SDSS images with our notation. Needs ra_dec.txt file, wget and ImageMagick!!!"
printf "\nUsage: $0 plate.MJD.fiber [opt] [scale]\n\t\t Default scale is 0.2\n\t\t Default options is \'$default_opts\'\n\n"
echo "Valid options:"
printf "G\tGrid with tickmarks to show image scale\nL\tInformation on the Navigation window view\nP\tMarks photometrically identified objects with light blue circles\nS\tMarks spectroscopic objects with red squares\nT\tMarks potential spectroscopy targets with green Xs\nO\tDraws the outline (green) of each photometric object\nB\tDraws a rectangular box (pink) around each photometric object\nF\tShows each SDSS field (~10x14 arcmin) in gray\nM\tShows masks (pink) around bright objects and data artifacts\nQ\tShows plates (lavender) used to collect spectra\nI\tInformation on the Navigation window view\n"
printf "\nExamples:\t $0 0271.51883.186 GL 0.4\n\t\t $0 0271.51883.186 \'\' 0.4\n\n"
echo "William @ minerva - 03/01/2007"
fi
