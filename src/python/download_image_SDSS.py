#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:07:21 2021

RESUME : Numerical integration using Fortran legacy routines
    
Version: v01

@author: Jean Gomes Copyright (c)

@email: antineutrinomuon@gmail.com

Written: Jean Michel Gomes © Copyright
"""

import os
import sys

import subprocess
import requests

# Progressing bar to look awsome
from tqdm import tqdm  # Import the tqdm module

from collections import OrderedDict

def print_welcome_message():
    print()
    print("####################################################")
    print("#   Welcome to the SDSS Image Downloader Script    #")
    print("#  This script allows you to download images from  #")
    print("#       the Sloan Digital Sky Survey (SDSS)!       #")
    print("####################################################")
    print()

def download_sdss_image(galaxy_name, ra, dec, plateid, mjd, fiberid, opt, scale, width, height, create_link_flag, data_release='DR18', progress=False):

    data_release_lower = data_release.lower()
    data_release = data_release.upper()

    if data_release_lower in ('dr7','dr8','dr9','dr10'):
        link = f"http://skyservice.pha.jhu.edu/{data_release_lower.capitalize()}/ImgCutout/getjpeg.aspx?ra={ra}&dec={dec}&scale={scale}&width={width}&height={height}&opt={opt}"
    elif data_release in ('DR12','DR13','DR14','DR15','DR16','DR17','DR18'):
        link = f"http://skyserver.sdss.org/{data_release_lower}/SkyServerWS/ImgCutout/getjpeg?ra={ra}&dec={dec}&scale={scale}&width={width}&height={height}&opt={opt}"
    else:
        raise ValueError(f"Unsupported SDSS Data Release: {data_release}")
    
    image_filename = f"{galaxy_name}.jpg"

    # Remove existing image file only if it exists
    if os.path.exists(image_filename):
        os.remove(image_filename)

    # Download image using system wget
    # subprocess.run(["wget", "-qc", link, "-O", image_filename])

    # Download image using response
    response = requests.get(link, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    if progress:
        progress_bar = tqdm(total=total_size, desc=f'Downloading {image_filename}: ', unit='iB', unit_scale=True)

    if response.status_code == 200:
        with open(image_filename, 'wb') as image_file:
            image_file.write(response.content)

        with open(image_filename, 'wb') as image_file:
            for data in response.iter_content(block_size):
                if progress:
                    progress_bar.update(len(data))
                image_file.write(data)

        if progress:
            progress_bar.close()
    else:
        print(f"Failed to download image for {galaxy_name}. Status code: {response.status_code}")

    # Debug
    # subprocess.run(["ls", image_filename])

    # Assuming the sixth argument is the flag to create the symbolic link
    if create_link_flag and plateid:
        existing_file = f"spec-{plateid}-{mjd}-{fiberid}.jpg"

        # Check if the existing file is a symlink, and if so, unlink it
        if os.path.islink(existing_file):
            os.unlink(existing_file)

        # Remove in case it was not a symlink
        if os.path.exists(existing_file):
            os.remove(existing_file)

        os.symlink(image_filename, existing_file)
    
def main():
    print_welcome_message()
    default_opts = ''
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            # lines = file.readlines()
            # Filter out lines starting with #
            lines = [line.strip() for line in file if not line.startswith('#')]

        # Check if data release is set
        if len(sys.argv) > 2:
            data_release_ = str(sys.argv[-1]).lower()
            
            if data_release_ in ('dr7','dr8','dr9','dr10','dr12','dr13','dr14','dr15','dr16','dr17','dr18'):
                data_release = data_release_

                # Reduce the number of arguments in sys.argv
                sys.argv = sys.argv[:-1]
            else:
                data_release = 'dr18'

        print(f'We are using SDSS Data Release: {data_release.upper()}')
        numb_lines = len(lines)

        # Define arguments
        valid_letters = "GLPSTOBFMQI"
        raw_opt = sys.argv[2]                if len(sys.argv) > 2 else default_opts
        if not all(char in valid_letters for char in raw_opt):
            print(f"WARNING: Invalid value for SDSS options. Only the letters GLPSTOBFMQI are allowed, but {raw_opt} used.")
            #opt = "".join(char for char in set(raw_opt) if char in valid_letters)
            opt = "".join(OrderedDict.fromkeys(raw_opt))
            opt = "".join(char for char in opt if char in valid_letters)
            excluded_letters = "".join(char for char in raw_opt if char not in valid_letters)
            print(f"WARNING: only unique set {opt} kept and {excluded_letters} where excluded")
            #opt = default_opts
        else:
            opt = raw_opt
            
        scale  = float(sys.argv[3])          if len(sys.argv) > 3 else 0.1
        if scale <= 0:
            print(f"WARNING: Invalid value for scale. Scale must be greater than 0.0.")
            scale = 0.1

        width  = int(sys.argv[4])            if len(sys.argv) > 4 else 600
        if width <= 0:
            print(f"WARNING: Invalid value for width. Width must be greater than 0.")
            width = 600
                
        height = int(sys.argv[5])            if len(sys.argv) > 5 else 600
        if height <= 0:
            print(f"WARNING: Invalid value for height. Height must be greater than 0.")
            height = 600

        # Assuming the sixth argument is the flag to create the symbolic link
        create_link_flag = bool(sys.argv[6]) if len(sys.argv) > 6 else False

        # Create a progress bar for the overall download process
        total_progress_bar = tqdm(total=numb_lines, unit='galaxy', desc='Total Progress: ', position=0, leave=True, bar_format='{desc}{percentage:10.2f}%|{bar:23}{r_bar}')
        # print()       

        for numb,line in enumerate(lines):
            parts = line.split()
            galaxy_name = parts[0]

            # Continue only if it does not start with # (the header)
            if galaxy_name.startswith('#'):
                continue

            try:
                # Validate ra and dec
                ra, dec = map(float, parts[1:3])
                if not (0 <= ra <= 360) or not (-90 <= dec <= 90):
                    raise ValueError(f"Invalid values for RA or DEC in line: {line}. RA should be between 0 and 360, and DEC between -90 and 90.")

                # Validate plateid, mjd, and fiberid
                plateid, mjd, fiberid = map(int, parts[3:6])
                # ra, dec, plateid, mjd, fiberid = map(float, parts[1:6])
            except ValueError as e:
                print(f"\nSkipping invalid line: {e} -- # {numb}")
                total_progress_bar.update(1)
                continue
            
            #ra, dec, plateid, mjd, fiberid = map(float, parts[1:6])

            # if plateid:
            #     print(f"galaxy={galaxy_name} | RA={ra:12.6f} | DEC={f'{dec:+12.6f}' if dec != 0.0 else ' ' * 10} | plateID={int(plateid):10d} | MJD={int(mjd):10d} | fiberID={int(fiberid):10d}")
            # else:
            #     print(f"galaxy={galaxy_name} | RA={ra:12.6f} | DEC={f'{dec:+12.6f}' if dec != 0.0 else ' ' * 10}")

            download_sdss_image(galaxy_name, ra, dec, plateid, mjd, fiberid, opt, scale, width, height, create_link_flag, data_release=data_release)
            total_progress_bar.update(1)
            #print("\r", end="")

        total_progress_bar.close()

    else:
        print("####################################################")
        print("#     Version 01 -- SDSS DR18 - How to use it?     #")
        print("#            Script to get SDSS images             #")
        print("#   Needs a file with objects, RA & DEC columns!   #")
        print("####################################################")

        print("\n####################################################")
        print("Usage:")
        print(f"\t {sys.argv[0]} file [SDSS options] [scale] [width] [height] [symbolic link]")
        print("\t Default scale for SDSS DRXX is 0.1\n\t Default options are '{default_opts}'\n")
        print("- [SDSS options]: need to be placed together, e.g. GLI:")
        print("\n* G\t Display a grid with tickmarks to indicate the image scale.")
        print("* L\t Provide information on the Navigation window view.")
        print("* P\t Indicate photometrically identified objects with light blue circles.")
        print("* S\t Highlight spectroscopic objects with red squares.")
        print("* T\t Mark potential spectroscopy targets with green Xs.")
        print("* O\t Draw the outline (in green) of each photometric object.")
        print("* B\t Draw a rectangular box (in pink) around each photometric object.")
        print("* F\t Display each SDSS field (~10x14 arcmin) in grayscale.")
        print("* M\t Show masks (in pink) around bright objects and data artifacts.")
        print("* Q\t Present plates (in lavender) used to collect spectra.")
        print("* I\t Invert black and white in the image.\n")
        print("- [scale]        : works as a zoom-out scale.")
        print("\n  Image size: advisable to have the same sizes width=height.")
        print("- [width]        : width of downloaded image.")
        print("- [height]       : height of downloaded image.")
        print("- [symbolic link]: boolean value, in order to create a file with name spec-plateid-mjd-fiberid.jpg")
        print("\nExample: Display images with a grid of tickmarks and the information on the navigation window.")
        print(f"\t {sys.argv[0]} file GL 0.4")
        print("\nExample: Display images with a grid of tickmarks and the information on the navigation window.")
        print("\t Also, increase the size of downloaded image.")
        print(f"\t {sys.argv[0]} file GL 0.4 1000 1000")
        print("####################################################")

        print("\n####################################################")
        print("Jean@Porto - 05/04/2017")
        print("https://skyserver.sdss.org/dr18/en/help/docs/api.aspx#imgcutout")
        print("####################################################")

if __name__ == "__main__":
    main()
