from setuptools import Extension
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("version.txt","r",encoding="utf-8") as vh:
    version_description = vh.read()
    
setup( name='fetch_sdss_images',
       version=version_description,
       description='A Python package for downloading SDSS images from distinct releases easily!',
       long_description=long_description,      # Long description read from the the readme file
       long_description_content_type="text/markdown",
       author='Jean Gomes',
       author_email='antineutrinomuon@gmail.com',
       url='https://github.com/neutrinomuon/fetch_sdss_images',
       install_requires=[ 'numpy','matplotlib' ],
       classifiers=[
           "Programming Language :: Python :: 3",
           "Operating System :: OS Independent",
                   ],
       package_dir={"fetch_sdss_images": "src/python"},
       packages=['fetch_sdss_images'],
       data_files=[('', ['version.txt']),],
      )
    
