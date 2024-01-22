#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:07:21 2021

RESUME : Download SDSS images using its API
    
Version: v01

@author: Jean Gomes Copyright (c)

@email: antineutrinomuon@gmail.com

Written: Jean Michel Gomes © Copyright
"""
import os
import sys

# import subprocess
from collections import OrderedDict
import requests

# Progressing bar to look awsome
from tqdm import tqdm  # Import the tqdm module

def print_welcome_message():
    '''Print welcome message to user'''
    print()
    print("####################################################")
    print("#   Welcome to the SDSS Image Downloader Script    #")
    print("#  This script allows you to download images from  #")
    print("#       the Sloan Digital Sky Survey (SDSS)!       #")
    print("####################################################")
    print()

def print_how_to_use_it():
    '''Print "How to Use it?" instructions'''
    print("####################################################")
    print("#     Version 01 -- SDSS DR18 - How to use it?     #")
    print("#            Script to get SDSS images             #")
    print("#   Needs a file with objects, RA & DEC columns!   #")
    print("####################################################")

    print("\n####################################################")
    print("Usage:")
    print(f"\t {sys.argv[0]} file [SDSS options] [scale] [width] [height] \
[symbolic link]")
    print("\t Default scale for SDSS DRXX is 0.1\n\t Default options are \
'{default_opts}'\n")
    print("- [SDSS options]: need to be placed together, e.g. GLI:")
    print("\n* G\t Display a grid with tickmarks to indicate the image scale.")
    print("* L\t Provide information on the Navigation window view.")
    print("* P\t Indicate photometrically identified objects with light blue \
circles.")
    print("* S\t Highlight spectroscopic objects with red squares.")
    print("* T\t Mark potential spectroscopy targets with green Xs.")
    print("* O\t Draw the outline (in green) of each photometric object.")
    print("* B\t Draw a rectangular box (in pink) around each photometric \
object.")
    print("* F\t Display each SDSS field (~10x14 arcmin) in grayscale.")
    print("* M\t Show masks (in pink) around bright objects and data \
artifacts.")
    print("* Q\t Present plates (in lavender) used to collect spectra.")
    print("* I\t Invert black and white in the image.\n")
    print("- [scale]        : works as a zoom-out scale.")
    print("\n  Image size: advisable to have the same sizes width=height.")
    print("- [width]        : width of downloaded image.")
    print("- [height]       : height of downloaded image.")
    print("- [symbolic link]: boolean value, in order to create \
a file with name spec-plateid-mjd-fiberid.jpg")
    print("\nExample: Display images with a grid of tickmarks and \
the information on the navigation window.")
    print(f"\t {sys.argv[0]} file GL 0.4")
    print("\nExample: Display images with a grid of tickmarks and \
the information on the navigation window.")
    print("\t Also, increase the size of downloaded image.")
    print(f"\t {sys.argv[0]} file GL 0.4 1000 1000")
    print("####################################################")

    print("\n####################################################")
    print("Jean@Porto - 05/04/2017")
    print("https://skyserver.sdss.org/dr18/en/help/docs/api.aspx#imgcutout")
    print("####################################################")

def define_sdss_link(**kwargs):
    '''Define sdss API link to download'''
    data_release_lower = kwargs['data_release'].lower()
    data_release_upper = kwargs['data_release'].upper()

    if data_release_lower in ('dr7','dr8','dr9','dr10'):
        link = (
            f"http://skyservice.pha.jhu.edu/{data_release_lower.capitalize()}/"
            f"ImgCutout/getjpeg.aspx?ra={kwargs['ra_value']}&dec={kwargs['decvalue']}&"
            f"scale={kwargs['scale']}&width={kwargs['width']}&height={kwargs['height']}&"
            "opt={kwargs['opt']}"
        )
    elif data_release_upper in ('DR12','DR13','DR14','DR15','DR16','DR17','DR18'):
        link = (
            f"http://skyserver.sdss.org/{data_release_lower}/" 
            f"SkyServerWS/ImgCutout/getjpeg?ra={kwargs['ra_value']}&dec={kwargs['decvalue']}&"
            f"scale={kwargs['scale']}&"
            f"width={kwargs['width']}&height={kwargs['height']}&opt={kwargs['opt']}"
        )
    else:
        print(f"Unsupported SDSS Data Release: {kwargs['data_release']}")
        link = ''

    return link

def download_sdss_image(galaxy_name, **kwargs):
    '''Download SDSS images'''

    # Extract kwargs values from dictionary
    # ra_value = kwargs.get('ra_value', 0.0)
    # decvalue = kwargs.get('decvalue', 0.0)
    # plateid = kwargs.get('ra_value', 0)
    # mjd = kwargs.get('mjd', 0)
    # fiberid = kwargs.get('fiberid', 0)
    # opt = kwargs.get('opt', '')
    # scale = kwargs.get('scale', 0.1)
    # width = kwargs.get('width', 600)
    # height = kwargs.get('height', 600)
    # create_link_flag = kwargs.get('create_link_flag', False)
    # data_release=kwargs.get('data_release','DR18')
    # progress=kwargs.get('progress',False)

    # print(kwargs['data_release'])

    # data_release_lower = kwargs['data_release'].lower()
    # kwargs['data_release'] = kwargs['data_release'].upper()
    # data_release_upper = kwargs['data_release']

    link = define_sdss_link(ra_value=kwargs['ra_value'],
                            decvalue=kwargs['decvalue'],
                            plateid=kwargs['plateid'],
                            mjd=kwargs['mjd'],
                            fiberid=kwargs['fiberid'],
                            opt=kwargs['opt'],
                            scale=kwargs['scale'],
                            width=kwargs['width'],
                            height=kwargs['height'],
                            data_release=kwargs['data_release'])

    if link == '':
        return

    # if data_release_lower in ('dr7','dr8','dr9','dr10'):
    #     link = (
    #         f"http://skyservice.pha.jhu.edu/{data_release_lower.capitalize()}/"
    #         f"ImgCutout/getjpeg.aspx?ra={kwargs['ra_value']}&dec={kwargs['decvalue']}&"
    #         f"scale={kwargs['scale']}&width={kwargs['width']}&height={kwargs['height']}&"
    #         "opt={kwargs['opt']}"
    #     )
    # elif kwargs['data_release'] in ('DR12','DR13','DR14','DR15','DR16','DR17','DR18'):
    #     link = (
    #         f"http://skyserver.sdss.org/{data_release_lower}/"
    #         f"SkyServerWS/ImgCutout/getjpeg?ra={kwargs['ra_value']}&dec={kwargs['decvalue']}&"
    #         f"scale={kwargs['scale']}&"
    #         f"width={kwargs['width']}&height={kwargs['height']}&opt={kwargs['opt']}"
    #     )
    # else:
    #     raise ValueError(f"Unsupported SDSS Data Release: {kwargs['data_release']}")

    image_filename = f"{galaxy_name}.jpg"

    # Remove existing image file only if it exists
    if os.path.exists(image_filename):
        os.remove(image_filename)

    # Download image using system wget
    # subprocess.run(["wget", "-qc", link, "-O", image_filename])

    # Download image using response
    your_timeout_value = 30
    response = requests.get(link, stream=True, timeout=your_timeout_value)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024 # 1 Kibibyte
    if kwargs['progress']:
        progress_bar = tqdm(total=total_size,
                            desc=f'Downloading {image_filename}: ',
                            unit='iB',
                            unit_scale=True)

    if response.status_code == 200:
        with open(image_filename, 'wb') as image_file:
            image_file.write(response.content)

        with open(image_filename, 'wb') as image_file:
            for data in response.iter_content(block_size):
                if kwargs['progress']:
                    progress_bar.update(len(data))
                image_file.write(data)

        if kwargs['progress']:
            progress_bar.close()
    else:
        print(f"Failed to download image for {galaxy_name}. Status code: {response.status_code}")

    # Debug
    # subprocess.run(["ls", image_filename])

    # Assuming the sixth argument is the flag to create the symbolic link
    if kwargs['create_link_flag'] and \
        kwargs['plateid'] and \
        kwargs['mjd'] and \
        kwargs['fiberid']:
        existing_file = f"spec-{kwargs['plateid']}-{kwargs['mjd']}-{kwargs['fiberid']}.jpg"

        # Check if the existing file is a symlink, and if so, unlink it
        if os.path.islink(existing_file):
            os.unlink(existing_file)

        # Remove in case it was not a symlink
        if os.path.exists(existing_file):
            os.remove(existing_file)

        os.symlink(image_filename, existing_file)

def check_main_options(width=600,
                       height=600,
                       scale=0.1,
                       default_opts='',
                       create_link_flag=False):
    '''Check Main options'''
    valid_letters = "GLPSTOBFMQI"
    raw_opt = sys.argv[2] if len(sys.argv) > 2 else default_opts
    # raw_opt = default_opts

    if not all(char in valid_letters for char in raw_opt):
        print(f"WARNING: Invalid value for SDSS options. Only the letters \
GLPSTOBFMQI are allowed, but {raw_opt} used.")
        opt = "".join(OrderedDict.fromkeys(raw_opt))
        opt = "".join(char for char in opt if char in valid_letters)
        excluded_letters = "".join(char for char in raw_opt if char not in valid_letters)
        print(f"WARNING: only unique set {opt} kept and {excluded_letters} were excluded")
    else:
        opt = raw_opt

    scale  = float(sys.argv[3]) if len(sys.argv) > 3 else scale
    if scale <= 0:
        print("WARNING: Invalid value for scale. Scale must be greater than 0.0.")
        scale = 0.1

    width  = int(sys.argv[4]) if len(sys.argv) > 4 else width
    if width <= 0:
        print("WARNING: Invalid value for width. Width must be greater than 0.")
        width = 600

    height = int(sys.argv[5]) if len(sys.argv) > 5 else height
    if height <= 0:
        print("WARNING: Invalid value for height. Height must be greater than 0.")
        height = 600

    # Assuming the sixth argument is the flag to create the symbolic link
    create_link_flag = bool(sys.argv[6]) if len(sys.argv) > 6 else False

    return opt,width,height,scale,create_link_flag

def verify_data_release(data_release):
    '''Verify SDSS data release, if available'''
    if len(sys.argv) > 2:
        data_release_ = str(sys.argv[-1]).lower()

        if data_release_ in ('dr7',
                             'dr8',
                             'dr9',
                             'dr10',
                             'dr12',
                             'dr13',
                             'dr14',
                             'dr15',
                             'dr16',
                             'dr17',
                             'dr18'):
            data_release = data_release_
            # Reduce the number of arguments in sys.argv
            sys.argv = sys.argv[:-1]
        else:
            if data_release_[0:2] == 'dr':
                print(f"Unsupported SDSS Data Release: {data_release_.upper()}")
                # Reduce the number of arguments in sys.argv
                sys.argv = sys.argv[:-1]
            data_release = 'dr18'
    else:
        data_release_ = data_release.lower()
        if data_release_ in ('dr7',
                             'dr8',
                             'dr9',
                             'dr10',
                             'dr12',
                             'dr13',
                             'dr14',
                             'dr15',
                             'dr16',
                             'dr17',
                             'dr18'):
            data_release = data_release_
        else:
            if data_release_[0:2] == 'dr':
                print(f"Unsupported SDSS Data Release: {data_release_.upper()}")
            data_release = 'dr18'

    return data_release

def main(filename=None,
         data_release='dr18',
         default_opts='',
         create_link_flag=False,
         **kwargs):
    '''Main function for downloading a list of objects from SDSS'''
    # print(filename)
    # print("sys????? ==== ",sys.argv[:])

    # Access dictionary
    kwargs['scale'] = kwargs.get('scale', 0.1)
    kwargs['width'] = kwargs.get('width', 600)
    kwargs['height'] = kwargs.get('height', 600)

    if filename is None:
        # If called without a filename, use sys.argv
        # print(filename)
        if len(sys.argv) > 1:
            filename = sys.argv[1]
        else:
            print_how_to_use_it()
            return

    print_welcome_message()
    verify_data_release(data_release)

    kwargs['data_release'] = data_release
    kwargs['create_link_flag'] = create_link_flag

    # Read file
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if not line.startswith('#')]

    print(f'We are using SDSS Data Release: {data_release.upper()}')
    # numb_lines = len(lines)

    # Define arguments
    # valid_letters = "GLPSTOBFMQI"

    # print(kwargs['data_release'])
    kwargs['opt'], \
    kwargs['width'], \
    kwargs['height'], \
    kwargs['scale'], \
    kwargs['create_link_flag'] = check_main_options(
        width=kwargs['width'],
        height=kwargs['height'],
        scale=kwargs['scale'],
        default_opts=default_opts,
        create_link_flag=kwargs['create_link_flag']
    )

    # Create a progress bar for the overall download process
    total_progress_bar = tqdm(total=len(lines),
                              unit='galaxy',
                              desc='Total Progress: ',
                              position=0,
                              leave=True,
                              bar_format='{desc}{percentage:10.2f}%|{bar:23}{r_bar}')

    for numb, line in enumerate(lines):
        parts = line.split()
        # galaxy_name = parts[0]

        # Continue only if it does not start with # (the header)
        if parts[0].startswith('#'):
            continue

        if len(parts) >= 2:
            # Validate ra and dec
            kwargs['ra_value'], kwargs['decvalue'] = map(float, parts[1:3])
            if not 0 <= kwargs['ra_value'] <= 360 or not -90 <= kwargs['decvalue'] <= 90:
                raise ValueError(f"Invalid values for RA or DEC in line: \
{line}. RA should be between 0 and 360, and DEC between -90 and 90.")

            # Validate plateid, mjd, and fiberid
            if len(parts) >= 6:
                kwargs['plateid'], \
                kwargs['mjd'], \
                kwargs['fiberid'] = map(int, parts[3:6])
            else:
                print(f"{line} -- Plateid, MJD, or Fiberid not present or not integers")
        else:
            print(f"\nUnexpected error: # {numb}")
            continue

        # print()
        # print("=======> ",data_release)
        # print("=======> ",kwargs['data_release'])
        # return

        download_sdss_image(parts[0],
                            ra_value=kwargs['ra_value'],
                            decvalue=kwargs['decvalue'],
                            plateid=kwargs['plateid'],
                            mjd=kwargs['mjd'],
                            fiberid=kwargs['fiberid'],
                            opt=kwargs['opt'],
                            scale=kwargs['scale'],
                            width=kwargs['width'],
                            height=kwargs['height'],
                            create_link_flag=kwargs['create_link_flag'],
                            data_release=data_release,
                            progress=False)

        total_progress_bar.update(1)

    total_progress_bar.close()

if __name__ == "__main__":
    # If called from the terminal with sys.argv
    if len(sys.argv) > 0:
        main()
