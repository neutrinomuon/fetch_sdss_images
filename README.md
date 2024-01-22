<p align="left">
  <img src="https://raw.githubusercontent.com/neutrinomuon/fetch_sdss_images/main/figures/Fetch%20SDSS%20Images.png" alt="Fetch SDSS Images" width="120px">
</p>

### fetch_sdss_images

####  A Python package for downloading SDSS images from distinct releases easily!
email: [antineutrinomuon@gmail.com](mailto:antineutrinomuon@gmail.com), [jean@astro.up.pt](mailto:jean@astro.up.pt)

© Copyright ®

J.G. - Jean Gomes

last stable version: 0.0.X
<!-- https://zenodo.org/badge/doi/10.5281/zenodo.10433044.svg -->
<!-- [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.10433044.svg)](https://zenodo.org/badge/doi/10.5281/zenodo.10433044.svg) -->

<hr>

![My Skills](https://skillicons.dev/icons?i=python,bash,numpy&theme=light)<br>
<a href="https://www.djangoproject.com">
  <img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" alt="DJANGO" width="50">
</a><br>
<!-- [![DJANGO](https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif)](https://www.djangoproject.com)<br>-->
[![python3](https://img.shields.io/pypi/pyversions/PyIntegral)](https://img.shields.io/pypi/pyversions/PyIntegral)
[![badgetlicense](https://anaconda.org/neutrinomuon/PyIntegral/badges/license.svg)](https://anaconda.org/neutrinomuon/PyIntegral/badges/license.svg)

<hr>

<div align="center">
<img src='https://github.com/neutrinomuon/PyIntegral/blob/main/figures/Definite_Integral.png?raw=true' width="100%">
</div>

<hr>

#### <b>RESUME</b>

<img src="https://raw.githubusercontent.com/neutrinomuon/fetch_sdss_images/main/figures/NGC5750.jpg" width=120px>
Download images from SDSS. Read the
<a href='https://github.com/neutrinomuon/fetch_sdss_images/blob/main/LICENSE.txt'>LICENSE.txt</a> file.

$\color{#58A6FF}\textsf{\Large\&#x24D8;\kern{0.2cm}\normalsize Note}$

<!-- This does not work on github
![Light Mode Icon](https://raw.githubusercontent.com/neutrinomuon/fetch_sdss_images/main/figures/Education,_Studying,_University,_Alumni_-_icon.png)
![Dark Mode Icon](https://raw.githubusercontent.com/neutrinomuon/fetch_sdss_images/main/figures/Education_black_background-removebg.png)
This project was also created with a focus on educational purposes and it is still underdevelopment.
-->

<img src="https://raw.githubusercontent.com/neutrinomuon/fetch_sdss_images/main/figures/Education,_Studying,_University,_Alumni_-_icon.png#gh-light-mode-only" width="70px"><img src="https://raw.githubusercontent.com/neutrinomuon/fetch_sdss_images/main/figures/Education_black_background-removebg.png#gh-dark-mode-only" width="70px">This project was also created with a focus on educational purposes.


<img src="https://raw.githubusercontent.com/neutrinomuon/fetch_sdss_images/main/figures/PEP8-StyleGuide.jpg" width="70px"> Now, PyIntegral has all its scripts in accordance with PEP 8 guidelines.

--------------------------------------------------------------------<br>
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)<br>

<hr>

#### <b>INSTALLATION</b>

You can easily install <a href=https://pypi.org/project/PyIntegral/>PyIntegral</a> by using pip - <a href='https://pypi.org/'>PyPI - The Python Package Index</a>:
<pre>
<code>
pip install fetch_sdss_images
</code>
</pre>
or by using a generated conda repository <a href='https://anaconda.org/neutrinomuon/PyIntegral'>https://anaconda.org/neutrinomuon/PyIntegral</a>:

[![badgetanaconda](https://anaconda.org/neutrinomuon/PyIntegral/badges/version.svg)](https://anaconda.org/neutrinomuon/PyIntegral/badges/version.svg)
[![badgetreleasedate](https://anaconda.org/neutrinomuon/PyIntegral/badges/latest_release_date.svg)](https://anaconda.org/neutrinomuon/PyIntegral/badges/latest_release_date.svg)
[![badgetplatforms](https://anaconda.org/neutrinomuon/PyIntegral/badges/platforms.svg
)](https://anaconda.org/neutrinomuon/PyIntegral/badges/platforms.svg)
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

#### <b>REFERENCES</b>

<!-- <ol><il> William H. Press, Saul A. Teukolsky, William T. Vetterling, and Brian
P. Flannery. Numerical Recipes: The Art of Scientific Computing. William ISBN:
978-0521880688. Link: <a
href='https://numerical.recipes/'>https://numerical.recipes/</a></il> </ol> -->

<hr>

#### <b>STRUCTURE</b>

The main structure of the directories and files are:

<pre>
<code>
#################################################
XXXXXXX
├── PyIntegral
│   ├── win-32
│   ├── linux-armv7l
│   ├── win-arm64
│   ├── linux-armv6l
│   ├── linux-s390x
│   ├── linux-ppc64
│   ├── linux-aarch64
│   ├── linux-32
│   ├── linux-64
│   ├── osx-64
│   ├── meta.yaml
│   ├── win-64
│   ├── README.txt
│   ├── linux-ppc64le
│   └── osx-arm64
├── dist
│   └── pyintegral-0.0.12.2.tar.gz
├── README.md
├── showdown.min.js
├── figures
│   ├── Definite_Integral.png
│   ├── Example_Integration.png
│   ├── PyIntegral.png
│   ├── PEP8-StyleGuide.jpg
│   └── Education,_Studying,_University,_Alumni_-_icon.png
├── .github
│   └── workflows
├── scripts
│   └── update_readme.py
├── index.html
├── LICENSE.txt
├── setup.py
├── tutorials
│   ├── Definite_Integral.png
│   ├── Definite_Integral.py
│   ├── .ipynb_checkpoints
│   ├── example1_pyintegral.ipynb
│   ├── .virtual_documents
│   └── README.txt
├── src
│   ├── python
│   └── fortran
├── .DS_Store
├── version.txt
├── pyintegral.egg-info
│   ├── PKG-INFO
│   ├── dependency_links.txt
│   ├── SOURCES.txt
│   ├── top_level.txt
│   └── requires.txt
├── README_setup.txt
├── requirements.txt
├── build
│   ├── lib.linux-x86_64-cpython-39
│   ├── lib.macosx-11.1-arm64-cpython-39
│   ├── temp.macosx-11.1-arm64-cpython-39
│   ├── temp.linux-x86_64-cpython-39
│   ├── src.linux-x86_64-3.9
│   ├── temp.linux-x86_64-3.9
│   └── src.macosx-11.1-arm64-3.9
└── .git
    ├── branches
    ├── logs
    ├── info
    ├── index
    ├── description
    ├── FETCH_HEAD
    ├── HEAD
    ├── ORIG_HEAD
    ├── objects
    ├── packed-refs
    ├── hooks
    ├── COMMIT_EDITMSG
    ├── refs
    └── config

41 directories, 35 files
#################################################
Generated with tree_colored @ 2023 - © Jean Gomes
#################################################
</code>
</pre>

XXXXX.py ????  is a python wrapper to the library in Fortran called
pyintegral.flib. The Fortran directory can be compiled separately for each
individual subroutine.

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
