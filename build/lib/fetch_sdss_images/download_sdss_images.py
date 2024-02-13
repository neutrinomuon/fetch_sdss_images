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
import re
import argparse

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

def print_how_to_use_it(error=''):
    '''Print "How to Use it?" instructions'''
    print("####################################################")
    print("#     Version 01 -- SDSS DR18 - How to use it?     #")
    print("#            Script to get SDSS images             #")
    print("#   Needs a file with objects, RA & DEC columns!   #")
    print("####################################################")

    print(f"\nError in commands: {error}")

    print("\n####################################################")
    print("Usage in terminal. Command line:")
    print("Obs.: The only mandatory flag is --filename or -filename")
    print("Obs.: Flags can be used in any order")
    print(f"1)\n\t {sys.argv[0]}" \
          + " --filename [file]" \
          + " --default_opts [SDSS options]" \
          + " --scale [scale]" \
          + " --width [width]" \
          + " --height [height]" \
          + " --data_release [data_release]" \
          + " --create_link_flag [boolean symbolic link]")
    print(f"2)\n\t {sys.argv[0]}" \
          + " -filename [file]" \
          + " -default_opts [SDSS options]" \
          + " -scale [scale]" \
          + " -width [width]" \
          + " -height [height]" \
          + " -data_release [data_release]" \
          + " -create_link_flag [boolean symbolic link]")
    print()
    print("Usage as a library:")
    print("Obs.: Flags can be used in any order")
    print()
    print("from fetch_sdss_images.download_sdss_images import main")
    print("main(filename=...," \
         +"\n     default_opts=...," \
         +"\n     scale=...," \
         +"\n     width=...," \
         +"\n     height=...," \
         +"\n     data_release=...," \
         +"\n     create_link_flag=...")
    print()
    print("Default scale for SDSS DRXX is 0.1\nDefault options [default_opts] are \
''\n")
    print("- [default_opts]: need to be placed together, e.g. GLI:")
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
    print("- [scale]           : works as a zoom-out scale.")
    print("\n  Image size: advisable to have the same sizes width=height.")
    print("- [width]           : width of downloaded image.")
    print("- [height]          : height of downloaded image.")
    print("- [data_release]    : SDSS data release as a string \
from 5 to 18, i.e. dr5, ..., dr18.")

    print("- [create_link_flag]: boolean value, in order to create \
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

    # Debug
    # print("opt ============> ",kwargs['opt'])
    if data_release_lower in ('dr5','dr6','dr7','dr8','dr9','dr10'):
        link = (
            f"http://skyservice.pha.jhu.edu/{data_release_lower.capitalize()}/"
            f"ImgCutout/getjpeg.aspx?ra={kwargs['ra_value']}&dec={kwargs['decvalue']}&"
            f"scale={kwargs['scale']}&width={kwargs['width']}&height={kwargs['height']}&"
            f"opt={kwargs['opt']}"
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

    # Debug
    # print(link)
    return link

def download_sdss_image(galaxy_name, **kwargs):
    '''Download SDSS image'''

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

    # Debug
    # print()
    # print("opt ===> ",kwargs['opt'])
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

def check_create_link_flag(create_link_flag):
    '''Check boolean variable and set up if necessary'''
    # if isinstance(create_link_flag, str):
    #     create_link_flag = create_link_flag.lower() == 'true'
    # elif isinstance(create_link_flag, bool):
    #     create_link_flag = create_link_flag
    # else:
    #     create_link_flag = False
    if isinstance(create_link_flag, str):
        create_link_flag = create_link_flag.lower() == 'true'
    elif not isinstance(create_link_flag, bool):
        create_link_flag = False

    return create_link_flag

    # if isinstance(create_link_flag, str):
    #     create_link_flag = create_link_flag.lower()
    #     if create_link_flag == 'true':
    #         create_link_flag = True
    #     else:
    #         create_link_flag = False
    # # elif isinstance(create_link_flag, bool):
    #     # return create_link_flag
    # else:
    #     create_link_flag = False
    #     # return create_link_flag
    # # Handle the case where create_link_flag is neither a string nor a boolean
    # return create_link_flag  # or raise an exception, print a warning, etc.

def check_main_options(width=600,
                       height=600,
                       scale=0.1,
                       default_opts='',
                       create_link_flag=False):
    '''Check Main options'''
    ierror = False
    valid_letters = "GLPSTOBFMQI"
    # raw_opt = sys.argv[2] if len(sys.argv) > 2 else default_opts
    raw_opt = default_opts
    # raw_opt = default_opts
    # print(raw_opt)

    if not all(char in valid_letters for char in raw_opt):
        print(f"WARNING: Invalid value for SDSS options. Only the letters \
GLPSTOBFMQI are allowed, but {raw_opt} used.")
        opt = "".join(OrderedDict.fromkeys(raw_opt))
        opt = "".join(char for char in opt if char in valid_letters)
        excluded_letters = "".join(char for char in raw_opt if char not in valid_letters)
        print(f"WARNING: only unique set {opt} kept and {excluded_letters} were excluded")
    else:
        opt = raw_opt

    try:
        scale = float(scale)
    except ValueError:
        pass
    # print(scale)
    if not isinstance(scale, float) or float(scale) <= 0.0:
        error = f'scale == {scale}' \
              + ' ==> Should be float > 0.0!'
        print_how_to_use_it(error)
        ierror = True
        return opt,width,height,scale,create_link_flag,ierror
    # if scale <= 0:
    #     print("WARNING: Invalid value for scale. Scale must be greater than 0.")
    #     scale = 0.1

    try:
        width = int(width)
    except ValueError:
        # print('Error value')
        pass
    if not isinstance(width, int) or int(width) < 1:
        error = f'width == {width}' \
              + ' ==> Should be integer > 1!'
        print_how_to_use_it(error)
        ierror = True
        return opt,width,height,scale,create_link_flag,ierror

    try:
        height = int(height)
    except ValueError:
        # print('Error value')
        pass
    if not isinstance(height, int) or int(height) < 1:
        error = f'height == {height}' \
              + ' ==> Should be integer > 1!'
        print_how_to_use_it(error)
        ierror = True
        return opt,width,height,scale,create_link_flag,ierror
    # if height <= 0:
    #     print("WARNING: Invalid value for height. Height must be greater than 0.")
    #     height = 600

    # Assuming the sixth argument is the flag to create the symbolic link
    # Check if the string represents a boolean value
    # create_link_flag = create_link_flag
    # print(create_link_flag,type(create_link_flag))
    create_link_flag = check_create_link_flag(create_link_flag)

    return opt,width,height,scale,create_link_flag,ierror

def verify_data_release(dictionary):
    '''Verify SDSS data release, if available'''
    if "data_release" in dictionary:

        data_release_ = dictionary['data_release'].lower()
        # Debug
        # print(data_release_)
        # print(data_release_[0:2] == 'dr')

        if data_release_[0:2] == 'dr':
            if data_release_ in ('dr5',
                                 'dr6',
                                 'dr7',
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
                if data_release_ in ('dr5', 'dr6', 'dr7'):
                    print(f"Using DR5 if SDSS Data Release: {data_release_.upper()}")
                dictionary['data_release'] = data_release_
                # Reduce the number of arguments in sys.argv
                # sys.argv = sys.argv[:-1]
            else:
                # print("Nothing")
                print(f"Unsupported  SDSS Data Release: {data_release_.upper()}")
                dictionary['data_release'] = 'dr18'
        else:
            print(f"Unsupported  SDSS Data Release: {data_release_.upper()}")
            # Reduce the number of arguments in sys.argv
            # sys.argv = sys.argv[:-1]
            dictionary['data_release'] = 'dr18'
    else:
        dictionary['data_release'] = 'dr18'

    # else: # In case command line is not used!
    #     data_release_ = data_release.lower()
    #     if data_release_[0:2] == 'dr':
    #         if data_release_ in ('dr7',
    #                              'dr8',
    #                              'dr9',
    #                              'dr10',
    #                              'dr12',
    #                              'dr13',
    #                              'dr14',
    #                              'dr15',
    #                              'dr16',
    #                              'dr17',
    #                              'dr18'):
    #             data_release = data_release_
    #         else:
    #             data_release = 'dr18'
    #     else:
    #         if data_release_[0:2] == 'dr':
    #             print(f"Unsupported SDSS Data Release: {data_release_.upper()}")
    #         data_release = 'dr18'

    return dictionary['data_release']

def is_valid_filename(filename):
    '''Check if filename is valid'''
    # Check if the filename is not empty and does not contain any illegal characters
    return bool(filename and re.match(r'^[^\\/:*?"<>|]+$', filename))

def check_irerror(ierror):
    '''Check for errors in reading flags'''
    if ierror:
        sys.exit()

def check_args(filename=None,
               **kwargs):
    '''Check arguments in argparse or directly from function'''
    def set_default_value(key, default_value):
        if kwargs_['args'][key] is None:
            kwargs_['args'][key] = default_value
            kwargs_[key] = default_value
        else:
            kwargs_['args'][key] = kwargs_['args'].get(key, default_value)
            kwargs_[key] = kwargs_['args'].get(key, default_value)

    kwargs_ = kwargs['kwargs']
    # print(kwargs_)

    # Check if 'args' key exists in the dictionary
    if 'args' in kwargs_ and kwargs_['args'] is not None:
        # Access dictionary
        kwargs_['filename'] = kwargs_['args'].get('filename', None)

        set_default_value('scale', 0.1)
        set_default_value('width', 600)
        set_default_value('height', 600)
        set_default_value('create_link_flag', False)
        set_default_value('data_release', 'dr18')
        set_default_value('default_opts', '')

        # if kwargs_['args']['scale'] is None:
        #     kwargs_['args']['scale'] = 0.1
        #     kwargs_['scale'] = 0.1
        # else:
        #     kwargs_['args']['scale'] = kwargs_['args'].get('scale', 0.1)
        #     kwargs_['scale'] = kwargs_['args'].get('scale', 0.1)

        # if kwargs_['args']['width'] is None:
        #     kwargs_['args']['width'] = 600
        #     kwargs_['width']= 600
        # else:
        #     kwargs_['args']['width'] = kwargs_['args'].get('width', 600)
        #     kwargs_['width'] = kwargs_['args'].get('width', 600)

        # if kwargs_['args']['height'] is None:
        #     kwargs_['args']['height'] = 600
        #     kwargs_['height']= 600
        # else:
        #     kwargs_['args']['height'] = kwargs_['args'].get('height', 600)
        #     kwargs_['height'] = kwargs_['args'].get('height', 600)

        # if kwargs_['args']['create_link_flag'] is None:
        #     kwargs_['args']['create_link_flag'] = False
        #     kwargs_['create_link_flag']= False
        # else:
        #     kwargs_['args']['create_link_flag'] = kwargs_['args'].get('create_link_flag', False)
        #     kwargs_['create_link_flag'] = kwargs_['args'].get('create_link_flag', False)

        # if kwargs_['args']['data_release'] is None:
        #     kwargs_['args']['data_release'] = 'dr18'
        #     kwargs_['data_release']= 'dr18'
        # else:
        #     kwargs_['args']['data_release'] = kwargs_['args'].get('data_release', 'dr18')
        #     kwargs_['data_release'] = kwargs_['args'].get('data_release', 'dr18')

        # if kwargs_['args']['default_opts'] is None:
        #     kwargs_['args']['default_opts'] = ''
        #     kwargs_['default_opts']= ''
        # else:
        #     kwargs_['args']['default_opts'] = kwargs_['args'].get('default_opts', 'dr18')
        #     kwargs_['default_opts'] = kwargs_['args'].get('default_opts', 'dr18')

        # print(kwargs['args'])
        # return

    else:
        # Access dictionary
        kwargs_['filename'] = filename
        kwargs_['scale'] = kwargs_.get('scale', 0.1)
        kwargs_['width'] = kwargs_.get('width', 600)
        kwargs_['height'] = kwargs_.get('height', 600)
        kwargs_['create_link_flag'] = kwargs_.get('create_link_flag', False)
        kwargs_['data_release']  = kwargs_.get('data_release', 'dr18')
        kwargs_['default_opts']  = kwargs_.get('default_opts', '')

    return kwargs_

def main(filename=None,
         **kwargs):
    '''Main function for downloading a list of objects from SDSS

####################################################
#    Version 0.0.2 - SDSS DR18 - How to use it?    #
#            Script to get SDSS images             #
#   Needs a file with objects, RA & DEC columns!   #
####################################################

####################################################
Usage in terminal. Command line:
Obs.: The only mandatory flag is --filename or -filename
Obs.: Flags can be used in any order
1)    
      download_sdss_images --filename [file] --default_opts [SDSS options] \
--scale [scale] --width [width] --height [height] --data_release [data_release] \
--create_link_flag [boolean symbolic link]
2)
      download_sdss_images -filename [file] -default_opts [SDSS options] \
-scale [scale] -width [width] -height [height] -data_release [data_release] \
-create_link_flag [boolean symbolic link]

Usage as a library:
Obs.: Flags can be used in any order

from fetch_sdss_images.download_sdss_images import main
main(filename=...,
     default_opts=...,
     scale=...,
     width=...,
     height=...,
     data_release=...,
     create_link_flag=...)

Default scale for SDSS DRXX is 0.1\nDefault options [default_opts] are

- [default_opts]: need to be placed together, e.g. GLI:

* G     Display a grid with tickmarks to indicate the image scale.
* L     Provide information on the Navigation window view.
* P     Indicate photometrically identified objects with light blue circles.
* S     Highlight spectroscopic objects with red squares.
* T     Mark potential spectroscopy targets with green Xs.
* O     Draw the outline (in green) of each photometric object.
* B     Draw a rectangular box (in pink) around each photometric object.
* F     Display each SDSS field (~10x14 arcmin) in grayscale.
* M     Show masks (in pink) around bright objects and data artifacts.
* Q     Present plates (in lavender) used to collect spectra.
* I     Invert black and white in the image.

- [scale]           : works as a zoom-out scale.

Image size: advisable to have the same sizes width=height.
 
- [width]           : width of downloaded image.
- [height]          : height of downloaded image.
- [data_release]    : SDSS data release as a string from 5 to 18, i.e. dr5, ..., dr18
- [create_link_flag]: boolean value, in order to create a file with name \
spec-plateid-mjd-fiberid.jpg

Example: Display images with a grid of tickmarks and the information on the navigation window.
         download_sdss_images -filename file -default_opts='GL' -scale=0.4

Example: Display images with a grid of tickmarks and the information on the navigation window.
         Also, increase the size of downloaded image.
         download_sdss_images -filename file -default_opts='GL' -scale=0.4 -width=1000 -height=1000
####################################################

####################################################
Jean@Porto - 05/04/2017
https://skyserver.sdss.org/dr18/en/help/docs/api.aspx#imgcutout
####################################################'''

    # print(filename)

    kwargs['args'] = kwargs.get('args', None)
    kwargs = check_args(filename=filename,kwargs=kwargs)
    # print(kwargs['args'])

    # Check if 'args' key exists in the dictionary
    # if 'args' in kwargs:
    #     # print(kwargs['args']['scale'])
    #     # print(kwargs['args'])

    #     # Access dictionary
    #     kwargs['filename'] = kwargs['args'].get('filename', None)
    #     if kwargs['args']['scale'] is None:
    #         kwargs['args']['scale'] = 0.1
    #         kwargs['scale'] = 0.1
    #     else:
    #         kwargs['args']['scale'] = kwargs['args'].get('scale', 0.1)
    #         kwargs['scale'] = kwargs['args'].get('scale', 0.1)

    #     if kwargs['args']['width'] is None:
    #         kwargs['args']['width'] = 600
    #         kwargs['width']= 600
    #     else:
    #         kwargs['args']['width'] = kwargs['args'].get('width', 600)
    #         kwargs['width'] = kwargs['args'].get('width', 600)

    #     if kwargs['args']['height'] is None:
    #         kwargs['args']['height'] = 600
    #         kwargs['height']= 600
    #     else:
    #         kwargs['args']['height'] = kwargs['args'].get('height', 600)
    #         kwargs['height'] = kwargs['args'].get('height', 600)

    #     if kwargs['args']['create_link_flag'] is None:
    #         kwargs['args']['create_link_flag'] = False
    #         kwargs['create_link_flag']= False
    #     else:
    #         kwargs['args']['create_link_flag'] = kwargs['args'].get('create_link_flag', False)
    #         kwargs['create_link_flag'] = kwargs['args'].get('create_link_flag', False)

    #     if kwargs['args']['data_release'] is None:
    #         kwargs['args']['data_release'] = 'dr18'
    #         kwargs['data_release']= 'dr18'
    #     else:
    #         kwargs['args']['data_release'] = kwargs['args'].get('data_release', 'dr18')
    #         kwargs['data_release'] = kwargs['args'].get('data_release', 'dr18')

    #     if kwargs['args']['default_opts'] is None:
    #         kwargs['args']['default_opts'] = ''
    #         kwargs['default_opts']= ''
    #     else:
    #         kwargs['args']['default_opts'] = kwargs['args'].get('default_opts', 'dr18')
    #         kwargs['default_opts'] = kwargs['args'].get('default_opts', 'dr18')

    #     # print(kwargs['args'])
    #     # return

    # else:
    #     # Access dictionary
    #     kwargs['filename'] = filename
    #     kwargs['scale'] = kwargs.get('scale', 0.1)
    #     kwargs['width'] = kwargs.get('width', 600)
    #     kwargs['height'] = kwargs.get('height', 600)
    #     kwargs['create_link_flag'] = kwargs.get('create_link_flag', False)
    #     kwargs['data_release']  = kwargs.get('data_release', 'dr18')
    #     kwargs['default_opts']  = kwargs.get('default_opts', '')

    if filename is not None:
        # If called without a filename, use sys.argv
        # print(kwargs['args']['filename'])
        kwargs['filename'] = filename
        if not os.path.exists(kwargs['filename']):
            # print("... File does not exist:", kwargs['filename'])
            error = f"... File does not exist: --filename {kwargs['filename']}"
            print_how_to_use_it(error)
            return
    else:
        if not isinstance(kwargs['filename'], str):
            error = f"... File does not exist: --filename {kwargs['filename']}"
            print_how_to_use_it(error)
            return
        if not os.path.exists(kwargs['filename']):
            error = f"... File does not exist: --filename {kwargs['filename']}"
            # print("... File does not exist:", kwargs['filename'])
            print_how_to_use_it(error)
            return

    print_welcome_message()
    kwargs['data_release'] = verify_data_release(kwargs)

    # kwargs['data_release'] = data_release
    # kwargs['create_link_flag'] = create_link_flag

    # Read file
    with open(kwargs['filename'], 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if not line.startswith('#')]

    print(f"We are using SDSS Data Release: {kwargs['data_release'].upper()}")

    # numb_lines = len(lines)

    # Define arguments
    # valid_letters = "GLPSTOBFMQI"
    # print(kwargs['scale'])

    # print(kwargs['data_release'])
    # print(kwargs['scale'])
    kwargs['opt'], \
    kwargs['width'], \
    kwargs['height'], \
    kwargs['scale'], \
    kwargs['create_link_flag'], \
        ierror = check_main_options(
        width=kwargs['width'],
        height=kwargs['height'],
        scale=kwargs['scale'],
        default_opts=kwargs['default_opts'],
        create_link_flag=kwargs['create_link_flag']
    )

    # check_ierror
    check_irerror(ierror)

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
                            data_release=kwargs['data_release'],
                            progress=False)

        total_progress_bar.update(1)

    total_progress_bar.close()

# Custom ArgumentParser subclass
class MyArgumentParser(argparse.ArgumentParser):
    '''Class for parsing the error in argparse'''
    def error(self, message):
        if 'one of the arguments -filename --filename is required' in message:
            print("Try 'python download_sdss_images.py -h' for more information.")
            print()
            error = "\nUsage: python download_sdss_images.py [-h]" \
                    " (-filename FILENAME | --filename FILENAME) is required"
            print_how_to_use_it(error)
            sys.exit()
        else:
            print("Try 'python download_sdss_images.py -h' for more information.")
            print()
            print_how_to_use_it()
            sys.exit()
            #super().error(message)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', type=str, help='The filename to be run')
    # Parse command-line arguments
    # Try to parse the arguments
    parser = MyArgumentParser()

    # Define mutually exclusive group for filename options
    group_filename = parser.add_mutually_exclusive_group(required=True)
    group_filename.add_argument('-filename', type=str, help='The filename to be run')
    group_filename.add_argument('--filename', type=str, help='The filename to be run')

    # Define default_opts
    group_default = parser.add_mutually_exclusive_group(required=False)
    group_default.add_argument('-default_opts',
                               type=str,
                               help='The default SDSS options from the API')
    group_default.add_argument('--default_opts',
                               type=str,
                               help='The default SDSS options from the API')

    # Define scale
    group_scale = parser.add_mutually_exclusive_group(required=False)
    group_scale.add_argument('-scale', type=float, help='The scale of the SDSS image')
    group_scale.add_argument('--scale', type=float, help='The scale of the SDSS image')

    # Define width
    group_width = parser.add_mutually_exclusive_group(required=False)
    group_width.add_argument('-width', type=int, help='The width of the downloaded SDSS image')
    group_width.add_argument('--width', type=int, help='The width of the downloaded SDSS image')

    # Define height
    group_height = parser.add_mutually_exclusive_group(required=False)
    group_height.add_argument('-height', type=int, help='The height of the downloaded SDSS image')
    group_height.add_argument('--height', type=int, help='The height of the downloaded SDSS image')

    # Define create_link_flag
    group_create_link_flag = parser.add_mutually_exclusive_group(required=False)
    group_create_link_flag.add_argument('-create_link_flag',
                                        type=str,
                                        help='Boolean value to create or not link')
    group_create_link_flag.add_argument('--create_link_flag',
                                        type=str,
                                        help='Boolean value to create or not link')

    # Define data_release
    group_data_release = parser.add_mutually_exclusive_group(required=False)
    group_data_release.add_argument('-data_release',
                                        type=str,
                                        help='SDSS data release')
    group_data_release.add_argument('--data_release',
                                        type=str,
                                        help='Sdss data release')

    args = parser.parse_args()
    num_arguments = len(vars(args))

    args = vars(args)
    args['name_of_script'] = sys.argv[0]
    # print(args)
    # print(sys.argv)
    if len(args) > 0:
    #     print(sys.argv)
    #     print(args)
    #     sys.argv[1] = args['filename']
    #     sys.argv = sys.argv[:2]
    #     print(sys.argv)
        main(args=args)
