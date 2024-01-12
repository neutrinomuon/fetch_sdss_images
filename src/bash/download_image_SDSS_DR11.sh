#!/bin/bash

# Created on 05/04/2017
#
# RESUME : SDSS DR11 Image Downloader Script
#    
# Version: v01
#
# @author: Jean Gomes Copyright (c)
#
# @email: antineutrinomuon@gmail.com

echo
echo "####################################################"
echo "# Welcome to the SDSS DR11 Image Downloader Script #"
echo "#  This script allows you to download images from  #"
echo "#     the Sloan Digital Sky Survey (SDSS) DR11     #"
echo "####################################################"
echo

default_opts=''

if [ -n "$1" ]; then
    filename=$1
    awk '{print $1}' "$filename" > lix

    while IFS= read -r gal; do
        galaxy_info=$(grep -m1 "$gal" < "$filename")
        galaxy_name=$(echo "$galaxy_info" | awk '{print $1}')

	# Continue only if it does not start with # the header
	if [[ "$gal" == \#* ]]; then
            continue
	fi

	ra=$(echo "$galaxy_info" | awk '{print $2}')
        dec=$(echo "$galaxy_info" | awk '{print $3}')

        plateid=$(echo "$galaxy_info" | awk '{print $4}')
        mjd=$(echo "$galaxy_info" | awk '{print $5}')
        fiberid=$(echo "$galaxy_info" | awk '{print $6}')

	if [ -n "$plateid" ]; then
            # echo "galaxy=$galaxy_name | RA=$ra | DEC=$dec | plateID=$plateid | MJD=$mjd | fiberID=$fiberid"
	    printf "galaxy=%-15s | RA=%-10s | DEC=%-10s | plateID=%-10s | MJD=%-10s | fiberID=%s\n" "$galaxy_name" "$ra" "$dec" "$plateid" "$mjd" "$fiberid"
	else
            # echo "galaxy=$galaxy_name | RA=$ra | DEC=$dec"
	    printf "galaxy=%-15s | RA=%-10s | DEC=%-10s\n" "$galaxy_name" "$ra" "$dec"
	fi
	   
        opt=${2:-$default_opts}
	scale=${3:-0.1}

	# Set default width and height to 600, or use user-provided values
        width=${4:-600}
        height=${5:-600}

	# Image cut-off
	# link="http://skyserver.sdss.org/dr11/SkyServerWS/ImgCutout/getjpeg?ra=$ra&dec=$dec&scale=$scale&width=$width&height=$height&opt=$opt"
	link="http://skyservice.pha.jhu.edu/DR11/ImgCutout/getjpeg.aspx?ra=$ra&dec=$dec&scale=$scale&width=$width&height=$height&opt=$opt"
	# Remove existing image file only if it exists
	[ -e "$gal".jpg ] && rm "$gal".jpg

	# Download image
        wget -qc "$link" -O "$gal".jpg

	# Debug
        # ls "$gal".jpg

	# Assuming the sixth argument is the flag to create the symbolic link
	create_link_flag=${6:-false}
	
        if [ "$create_link_flag" = true ] && [ -n "$plateid" ]; then
	    existing_file="spec-$plateid-$mjd-$fiberid.jpg"
	    # Check if the existing file is a symlink, and if so, unlink it
	    if [ -h "$existing_file" ]; then
		unlink "$existing_file"
	    fi
	    
	    # Remove in case it was not a symlink	    
	    [ -e "spec-$plateid-$mjd-$fiberid.jpg" ] && rm "spec-$plateid-$mjd-$fiberid.jpg"
            ln -s "$gal".jpg "spec-$plateid-$mjd-$fiberid.jpg"
        fi

    done < lix

    # Remove existing lix file if it exists                                                                                                                                 
    [ -e lix ] && rm lix
    
else
    echo "####################################################"
    echo "#     Version 01 -- SDSS DR11 - How to use it?     #"
    echo "#       Script to get SDSS images from DR11        #"
    echo "#   Needs a file with objects, RA & DEC columns!   #"
    echo "#      The script uses wget and ImageMagick!       #"
    echo "####################################################"
    echo
    echo "####################################################"
    printf "Usage:"
    printf "\n\t $0 file [SDSS options] [scale] [width] [height] [symbolic link]"
    printf "\n\t Default scale for SDSS DR11 is 0.1\n\t Default options are '$default_opts'\n\n"

    echo "- [SDSS options]: need to be placed together, e.g. GLI:"

    printf "\n* G\t Display a grid with tickmarks to indicate the image scale."
    printf "\n* L\t Provide information on the Navigation window view."
    printf "\n* P\t Indicate photometrically identified objects with light blue circles."
    printf "\n* S\t Highlight spectroscopic objects with red squares."
    printf "\n* T\t Mark potential spectroscopy targets with green Xs."
    printf "\n* O\t Draw the outline (in green) of each photometric object."
    printf "\n* B\t Draw a rectangular box (in pink) around each photometric object."
    printf "\n* F\t Display each SDSS field (~10x14 arcmin) in grayscale."
    printf "\n* M\t Show masks (in pink) around bright objects and data artifacts."
    printf "\n* Q\t Present plates (in lavender) used to collect spectra."
    printf "\n* I\t Invert black and white in the image.\n"

    echo ""
    echo "- [scale]        : works as a zoom-out scale."
    echo ""
    echo "  Image size: advisable to have the same sizes width=height."
    echo "- [width]        : width of downloaded image."
    echo "- [height]       : height of downloaded image."
    echo "- [symbolic link]: boolean value, in order to create a file with name spec-plateid-mjd-fiberid.jpg"

    printf "\nExample: Display images with a grid of tickmarks and the information on the navigation window."
    printf "\n\t $0 file GL 0.4\n"
    
    printf "\nExample: Display images with a grid of tickmarks and the information on the navigation window."
    printf "\n\t Also, increase the size of downloaded image."
    printf "\n\t $0 file GL 0.4 1000 1000\n"
    printf "####################################################\n"

    printf "\n####################################################"
    printf "\nJean@Porto - 05/04/2017"
    printf "\nBased on old scripts from"
    printf "\nWilliam Schoenell for SDSS DR5"
    printf "\nhttp://cas.sdss.org/DR7/pt/tools/chart/chartinfo.asp\n"
    echo "####################################################"
fi
