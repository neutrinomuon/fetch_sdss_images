<p align="left">
  <img src="https://github.com/neutrinomuon/fetch_sdss_images/blob/main/figures/Fetch_SDSS_Images.png?raw=true" alt="Fetch SDSS Images" width="120px">
</p>

### fetch_sdss_images

####  A Python package for downloading SDSS images from distinct releases easily!
email: [antineutrinomuon@gmail.com](mailto:antineutrinomuon@gmail.com), [jean@astro.up.pt](mailto:jean@astro.up.pt)

© Copyright ®

J.G. - Jean Gomes

last stable version: 0.0.2
<!-- https://zenodo.org/badge/doi/10.5281/zenodo.10433044.svg -->
[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.10571521.svg)](https://zenodo.org/badge/doi/10.5281/zenodo.10571521.svg)

<hr>

![My Skills](https://skillicons.dev/icons?i=python,bash,numpy&theme=light)<br>
<a href="https://www.djangoproject.com">
  <img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" alt="DJANGO" width="50">
</a><br>
<!-- [![DJANGO](https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif)](https://www.djangoproject.com)<br>-->
[![python3](https://img.shields.io/pypi/pyversions/fetch_sdss_images)](https://img.shields.io/pypi/pyversions/PyIntegral)
[![badgetlicense](https://anaconda.org/neutrinomuon/fetch_sdss_images/badges/license.svg)](https://anaconda.org/neutrinomuon/fetch_sdss_images/badges/license.svg)

<hr>

<center>
Example of a galaxy retrieved from the SDSS API for Data Release 18: NGC 5750
</center>

<br>

<div align="center">
<img src='https://github.com/neutrinomuon/fetch_sdss_images/blob/main/figures/NGC5750.jpg?raw=true' width="400px">
</div>

<hr>

#### <b>RESUME</b>

<img src="https://github.com/neutrinomuon/fetch_sdss_images/blob/main/figures/Fetch_SDSS_Images.png?raw=true" width=120px>
Download images from SDSS. Read the
<a href='https://github.com/neutrinomuon/fetch_sdss_images/blob/main/LICENSE.txt'>LICENSE.txt</a> file.

$\color{#58A6FF}\textsf{\Large\&#x24D8;\kern{0.2cm}\normalsize Note}$

<!-- This does not work on github
![Light Mode Icon](https://raw.githubusercontent.com/neutrinomuon/fetch_sdss_images/main/figures/Education,_Studying,_University,_Alumni_-_icon.png)
![Dark Mode Icon](https://raw.githubusercontent.com/neutrinomuon/fetch_sdss_images/main/figures/Education_black_background-removebg.png)
This project was also created with a focus on educational purposes and it is still underdevelopment.
-->

<img src="https://github.com/neutrinomuon/fetch_sdss_images/blob/main/figures/Education,_Studying,_University,_Alumni_-_icon.png?raw=true#gh-light-mode-only" width="70px"><img src="https://github.com/neutrinomuon/fetch_sdss_images/blob/main/figures/Education_black_background-removebg.png?raw=true#gh-dark-mode-only" width="70px">This project was also created with a focus on educational purposes.

<img src="https://github.com/neutrinomuon/fetch_sdss_images/blob/main/figures/PEP8-StyleGuide.jpg?raw=true" width="70px"> Now, fetch_sdss_images has all its scripts in accordance with PEP 8 guidelines.

--------------------------------------------------------------------<br>
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)<br>

<hr>

#### <b>INSTALLATION</b>

You can easily install <a href=https://pypi.org/project/fetch_sdss_images/>fetch_sdss_images</a> by using pip - <a href='https://pypi.org/'>PyPI - The Python Package Index</a>:
<pre>
<code>
pip install fetch_sdss_images
</code>
</pre>
or by using a generated conda repository <a href='https://anaconda.org/neutrinomuon/fetch_sdss_images'>https://anaconda.org/neutrinomuon/fetch_sdss_images</a>:

[![badgetanaconda](https://anaconda.org/neutrinomuon/PyIntegral/badges/version.svg)](https://anaconda.org/neutrinomuon/feych_sdss_images/badges/version.svg)
[![badgetreleasedate](https://anaconda.org/neutrinomuon/PyIntegral/badges/latest_release_date.svg)](https://anaconda.org/neutrinomuon/fetch_sdss_images/badges/latest_release_date.svg)
[![badgetplatforms](https://anaconda.org/neutrinomuon/fetch_sdss_images/badges/platforms.svg
)](https://anaconda.org/neutrinomuon/fetch_sdss_images/badges/platforms.svg)
<pre>
<code>
conda install -c neutrinomuon fetch_sdss_images
</code>
</pre>
OBS.: Linux, OS-X ad Windows pre-compilations available in conda.

You can also clone the repository and install by yourself in your machine:
<pre>
<code>
git clone https://github.com/neutrinomuon/fetch_sdss_images
python setup.py install
</code>
</pre>

<hr>

<!-- #### <b>EXAMPLE</b>

<hr>

<form action="http://skyserver.sdss.org/dr16/en/tools/chart/list.aspx"
method="post">
<TEXTAREA name="paste">
    ra     dec  
159.815 -0.655
161.051  0.152
161.739  0.893
164.090 -0.889
</TEXTAREA>
<input type="submit">
</form> -->

#### <b>REFERENCES</b>

For the API/tools from SDSS, please check:
<a href="https://skyserver.sdss.org/dr18/en/help/docs/api.aspx">https://skyserver.sdss.org/dr18/en/help/docs/api.aspx</a>

<hr>

#### <b>STRUCTURE</b>
<pre>
#################################################
workspace
├── README.md
├── figures
│   ├── Education_white_background.png
│   ├── NGC5750.jpg
│   ├── Education_black_background.png
│   ├── Education,_Studying,_University,_Alumni_-_icon.png
│   ├── Fetch_SDSS_Images.png
│   ├── Education_black_background-removebg.png
│   ├── PEP8-StyleGuide.jpg
│   └── Fetch SDSS Images.png
├── src
│   ├── bash
│   │   ├── download_image_SDSS_DR18.sh
│   │   ├── download_image_SDSS_DR10.sh
│   │   ├── objects.txt
│   │   ├── download_image_SDSS_DR12.sh
│   │   ├── download_image_SDSS_DR16.sh
│   │   ├── download_image_SDSS_DR17.sh
│   │   ├── download_image_SDSS_DR7.sh
│   │   ├── download_image_SDSS_DR8.sh
│   │   ├── 0266.51602.001.jpg
│   │   ├── download_image_SDSS_DR15.sh
│   │   ├── download_image_SDSS_DR11.sh
│   │   ├── download_image_SDSS_DR9.sh
│   │   ├── 0271.51883.293.jpg
│   │   ├── download_image_SDSS_DR13.sh
│   │   ├── 1774.53759.272.jpg
│   │   ├── download_image_SDSS_DR14.sh
│   │   └── 1627.53473.303.jpg
│   └── python
│       ├── NGC1055.jpg
│       ├── NGC5750.jpg
│       ├── objects.txt
│       ├── spec-1627-53473-303.jpg
│       ├── __pycache__
│       │   ├── download_image_SDSS.cpython-39.pyc
│       │   └── download_sdss_images.cpython-39.pyc
│       ├── NGC3521.jpg
│       ├── 0266.51602.001.jpg
│       ├── NGC5145.jpg
│       ├── spec-1774-53759-272.jpg
│       ├── docstrings.py
│       ├── spec-9999-999-9999.jpg
│       ├── 0271.51883.293.jpg
│       ├── spec-271-51883-293.jpg
│       ├── __init__.py
│       ├── test_filenoIDS.jpg
│       ├── download_sdss_images.py
│       ├── 1774.53759.272.jpg
│       ├── 1627.53473.303.jpg
│       └── spec-266-51602-1.jpg
├── django
│   └── __init__.py
├── tree.out
├── LICENSE.txt
├── tutorial
│   ├── objects.txt
│   ├── NGC5145.jpg
│   ├── .virtual_documents
│   │   ├── Untitled.ipynb
│   │   └── Example_fetch_sdss_images.ipynb
│   ├── .ipynb_checkpoints
│   │   └── Example_fetch_sdss_images-checkpoint.ipynb
│   ├── NGC5145_without_info.jpg
│   └── Example_fetch_sdss_images.ipynb
├── dist
│   ├── fetch_sdss_images-0.0.2.tar.gz
│   └── fetch_sdss_images-0.0.2-py3.9.egg
├── version.txt
├── fetch_sdss_images_conda
│   ├── linux-aarch64
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── linux-armv6l
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── linux-s390x
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── meta.yaml
│   ├── win-arm64
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── linux-32
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── linux-64
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── win-32
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── linux-armv7l
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── linux-ppc64
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── linux-ppc64le
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── win-64
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── osx-arm64
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   ├── osx-64
│   │   └── fetch_sdss_images-0.0.1-py39_0.tar.bz2
│   └── List.txt
├── .github
│   └── workflows
│       ├── main.yml
│       └── pylint.yml
├── setup.py
├── fetch_sdss_images.egg-info
│   ├── top_level.txt
│   ├── dependency_links.txt
│   ├── requires.txt
│   ├── PKG-INFO
│   └── SOURCES.txt
├── .git
│   ├── objects
│   │   ├── info
│   │   └── pack
│   │       ├── pack-fa97c7887272fa4cd2607e2835c0060d0ae62f73.rev
│   │       ├── pack-fa97c7887272fa4cd2607e2835c0060d0ae62f73.pack
│   │       └── pack-fa97c7887272fa4cd2607e2835c0060d0ae62f73.idx
│   ├── info
│   │   └── exclude
│   ├── HEAD
│   ├── FETCH_HEAD
│   ├── refs
│   │   ├── heads
│   │   │   └── main
│   │   ├── remotes
│   │   │   └── origin
│   │   │       └── main
│   │   └── tags
│   ├── shallow
│   ├── branches
│   ├── index
│   ├── logs
│   │   ├── HEAD
│   │   └── refs
│   │       ├── heads
│   │       │   └── main
│   │       └── remotes
│   │           └── origin
│   │               └── main
│   ├── description
│   ├── hooks
│   │   ├── pre-rebase.sample
│   │   ├── pre-commit.sample
│   │   ├── sendemail-validate.sample
│   │   ├── pre-receive.sample
│   │   ├── update.sample
│   │   ├── commit-msg.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── applypatch-msg.sample
│   │   ├── pre-push.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   └── push-to-checkout.sample
│   └── config
└── build
    └── lib
        └── fetch_sdss_images
            ├── docstrings.py
            ├── __init__.py
            └── download_sdss_images.py

47 directories (0 symlink), 114 files (5 symlink)
#################################################
Generated: treehue_colored @2024 - © Jean Gomes -
#################################################
</pre>

download_sdss_images.py is a python script, originally based on bash script.

<hr>

#### <b>ISSUES AND CONTRIBUTIONS</b>

If you encounter any issues with this project, please feel free to submit an
issue on the GitHub repository. We appreciate your feedback and are committed
to improving the quality of our codebase.

If you'd like to contribute to this project, we welcome pull requests from the
community. Before submitting a pull request, please make sure to fork the
repository and create a new branch for your changes. Once your changes are
complete, submit a pull request and we'll review your code as soon as
possible.

For any questions or concerns about contributing, please contact the project
maintainer at
[antineutrinomuon@gmail.com](mailto:antineutrinomuon@gmail.com). Thank you for
your interest in contributing to our project!

<hr>

#### <b>LICENSE</b>

This software is provided "AS IS" (see DISCLAIMER below). Permission to use,
for non-commercial purposes is granted. Permission to modify for personal or
internal use is granted, provided this copyright and disclaimer are included
in ALL copies of the software. All other rights are reserved. In particular,
redistribution of the code is not allowed without explicit permission by the
author.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
