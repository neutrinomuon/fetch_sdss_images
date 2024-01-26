<p align="left">
  <img src="https://github.com/neutrinomuon/fetch_sdss_images/blob/main/figures/Fetch_SDSS_Images.png?raw=true" alt="Fetch SDSS Images" width="120px">
</p>

### fetch_sdss_images

####  A Python package for downloading SDSS images from distinct releases easily!
email: [antineutrinomuon@gmail.com](mailto:antineutrinomuon@gmail.com), [jean@astro.up.pt](mailto:jean@astro.up.pt)

© Copyright ®

J.G. - Jean Gomes

last stable version: 0.0.1
<!-- https://zenodo.org/badge/doi/10.5281/zenodo.10433044.svg -->
<!-- [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.10433044.svg)](https://zenodo.org/badge/doi/10.5281/zenodo.10433044.svg) -->

<hr>

![My Skills](https://skillicons.dev/icons?i=python,bash,numpy&theme=light)<br>
<a href="https://www.djangoproject.com">
  <img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" alt="DJANGO" width="50">
</a><br>
<!-- [![DJANGO](https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif)](https://www.djangoproject.com)<br>-->
[![python3](https://img.shields.io/pypi/pyversions/fetch_sdss_images)](https://img.shields.io/pypi/pyversions/PyIntegral)
[![badgetlicense](https://anaconda.org/neutrinomuon/fecth_sdss_images/badges/license.svg)](https://anaconda.org/neutrinomuon/fetch_sdss_images/badges/license.svg)

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

#### <b>EXAMPLE</b>

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
</form>

#### <b>REFERENCES</b>

For the API/tools from SDSS, please check:
<a href="https://skyserver.sdss.org/dr18/en/help/docs/api.aspx">https://skyserver.sdss.org/dr18/en/help/docs/api.aspx</a>

<hr>

#### <b>STRUCTURE</b>
<pre>
#################################################
workspace
├── LICENSE.txt
├── django
│   └── __init__.py
├── tmp
│   ├── get_SDSS_image.tar.bz2
│   └── get_SDSS_image
│       ├── get_image.sh
│       ├── ra_dec.txt
│       └── .smhist
├── .git
│   ├── HEAD
│   ├── objects
│   │   ├── eb
│   │   │   └── 5d6fdab220f7b55c1cbf81a92f26e74e76d0a7
│   │   ├── c2
│   │   │   └── b5501122099bcae8ac3808a6fd8d29203db15a
│   │   ├── 48
│   │   │   └── 0b58b0d9c996156a9f525b9a537a0ad919b6fd
│   │   ├── 24
│   │   │   └── 649e5b8598fd7f7b89400fe768aa8a710f97d6
│   │   ├── pack
│   │   ├── 86
│   │   │   └── 18cc14d13a39c6c0c89241da2654f7e68c7c24
│   │   ├── df
│   │   │   └── bf73e506d96d058dbe3d3a7cbdbf17e6322c59
│   │   ├── b6
│   │   │   ├── 12ba5da622a5287bcb8ef75e2ea02bb9cb4885
│   │   │   └── 1b2c05538fcc3b37a7d1dc3a4a6bdb9385f68e
│   │   ├── 30
│   │   │   └── 6105783304f1550204ed2b0efeac569c815891
│   │   ├── 05
│   │   │   └── b91ee76136bbb7dd14b24192962a313fe2d451
│   │   ├── b4
│   │   │   └── f75c13ebf506203ff9c5152bbbe56c9aa29405
│   │   ├── 5c
│   │   │   └── a26c62289e4651a026150f7753fa2483bbafea
│   │   ├── 4b
│   │   │   └── 78de8412ead24bacca881f0c2ef83b9a13ba35
│   │   ├── f2
│   │   │   └── 144e2e4feeb7e58d1c61ae617f55e487910c24
│   │   ├── 2a
│   │   │   └── da05b74d691ff04f8e75e571abe35b6b6413b7
│   │   ├── e3
│   │   │   └── fd2b66856f47c5a493130e89bd48cf4b5443b4
│   │   ├── 6d
│   │   │   └── 3fa7d701ca9e659b3c8c7e4bdefa97cb8f07f3
│   │   ├── fe
│   │   │   └── 53f10f99a8c6a2f22ae5aa1ca26bd430afe020
│   │   ├── 71
│   │   │   └── 5dde02a154e818b07a5c7f14604e55dbdd9d93
│   │   ├── af
│   │   │   └── fc1306f71b0ea5acffa3198e33435bd987ac20
│   │   ├── 4d
│   │   │   └── 23e6f1efde562a258a0f52339b91b32215959c
│   │   ├── 9d
│   │   │   └── 1dcfdaf1a6857c5f83dc27019c7600e1ffaff8
│   │   ├── info
│   │   ├── aa
│   │   │   └── 2e2fe106d94ab5d31fd53c0d044e8f98721802
│   │   ├── 14
│   │   │   └── 86763056eb428aeda8a5bff03c263f4d28a248
│   │   ├── c9
│   │   │   └── c2de91a00f9040682898df6122b9b55125ae5d
│   │   ├── 3b
│   │   │   └── d3b5a80009b500e3e466ba237cbd6b49c60ec5
│   │   ├── f5
│   │   │   └── 81682dc124640dda0a73f46d3b70a8d4428666
│   │   ├── 68
│   │   │   └── b8f02c4191339cfea296e8aefc93887d09c223
│   │   ├── b3
│   │   │   └── 69968545ed8b865255d084c94482dab84de77e
│   │   ├── 8f
│   │   │   └── 2ec7e171ec8857b703a7bdbca6c98021183a3c
│   │   ├── 6b
│   │   │   └── 235cfec2aa3378fa28a0c3f0b53bf2799e0a33
│   │   ├── 07
│   │   │   └── 2713a421e96f0cc7d70de650d148f1512df51a
│   │   ├── 73
│   │   │   └── ef608d3fce54f94842103ede91efb00cbeb9e7
│   │   ├── 1f
│   │   │   ├── a48ae0e50fb31364b07fd3996813f31c539878
│   │   │   └── acfbac556f8e938d75ba6e53d8be00eb5c2ae6
│   │   ├── ae
│   │   │   └── ae96ff2706a3d404c5b543b4a5d365dbfe9220
│   │   ├── 9c
│   │   │   └── dc770b03bcffc191d3ffba72ca3cf14efa07b5
│   │   ├── f3
│   │   │   └── 87f3feeece7071386cb18f9f2c061217bc34ea
│   │   ├── e6
│   │   │   └── 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│   │   ├── db
│   │   │   ├── 7fdfb788f537f810039ead90c68683c249ea1d
│   │   │   └── 9548855f3905fc0741ca345c88c1525396a32d
│   │   ├── 06
│   │   │   └── 9c8284db0873361ee777d18950419e37a35732
│   │   ├── cc
│   │   │   └── de2165ce1bc9103a28396ae93fb24db3fa3d44
│   │   ├── fd
│   │   │   └── dfb41eb4a26aaca8b57fd277dcf8b0a55cd606
│   │   ├── 3c
│   │   │   └── e79c0c72edae8b7b7a3af5cea99c4b9ca2ebe2
│   │   ├── 0d
│   │   │   └── 045100985e33446f4ded2ad0512fb3b55ababd
│   │   ├── 90
│   │   │   └── 6359be19ecda8a95e89b4ea5d2994680ac6ee8
│   │   ├── 64
│   │   │   ├── dcbc5b4cb20d554a80edea0a5beecec37d68a0
│   │   │   └── 04f35d8b4708497e326380a9521d8cec071e11
│   │   ├── 1d
│   │   │   └── c6f6cba62933b7cc2f6be701620c32c53c583b
│   │   ├── d2
│   │   │   └── 28c32c7658afedb94521fa1a8e44d7c1c4bb2f
│   │   ├── 8a
│   │   │   └── cdd82b765e8e0b8cd8787f7f18c7fe2ec52493
│   │   ├── 12
│   │   │   └── d51e4d48c6b1a66539b830c1bc60e540b83040
│   │   ├── 83
│   │   │   └── 9fb8a37ba9243553e88b9e11e1fe1cf62dc95a
│   │   └── 0f
│   │       └── 8971bd9942a347ea402b0b5e5979b0405e1e30
│   ├── config
│   ├── FETCH_HEAD
│   ├── info
│   │   └── exclude
│   ├── hooks
│   │   ├── push-to-checkout.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── pre-rebase.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-push.sample
│   │   ├── pre-commit.sample
│   │   ├── applypatch-msg.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── pre-receive.sample
│   │   ├── pre-applypatch.sample
│   │   ├── commit-msg.sample
│   │   ├── sendemail-validate.sample
│   │   └── update.sample
│   ├── shallow
│   ├── refs
│   │   ├── heads
│   │   │   └── main
│   │   ├── remotes
│   │   │   └── origin
│   │   │       └── main
│   │   └── tags
│   ├── description
│   ├── branches
│   ├── logs
│   │   ├── HEAD
│   │   └── refs
│   │       ├── heads
│   │       │   └── main
│   │       └── remotes
│   │           └── origin
│   │               └── main
│   └── index
├── version.txt
├── figures
│   ├── Education_white_background.png
│   ├── Fetch SDSS Images.png
│   ├── Education_black_background.png
│   ├── NGC5750.jpg
│   ├── PEP8-StyleGuide.jpg
│   ├── Education_black_background-removebg.png
│   └── Education,_Studying,_University,_Alumni_-_icon.png
├── README.md
├── src
│   ├── python
│   │   ├── download_image_sdss.py
│   │   ├── 0266.51602.001.jpg
│   │   ├── spec-1774-53759-272.jpg
│   │   ├── spec-266-51602-1.jpg
│   │   ├── spec-271-51883-293.jpg
│   │   ├── __pycache__
│   │   │   └── download_image_SDSS.cpython-39.pyc
│   │   ├── objects.txt
│   │   ├── test_filenoIDS.jpg
│   │   ├── 1774.53759.272.jpg
│   │   ├── NGC5750.jpg
│   │   ├── 1627.53473.303.jpg
│   │   ├── NGC3521.jpg
│   │   ├── NGC1055.jpg
│   │   ├── spec-1627-53473-303.jpg
│   │   └── 0271.51883.293.jpg
│   └── bash
│       ├── download_image_SDSS_DR13.sh
│       ├── download_image_SDSS_DR17.sh
│       ├── 0266.51602.001.jpg
│       ├── download_image_SDSS_DR12.sh
│       ├── download_image_SDSS_DR14.sh
│       ├── download_image_SDSS_DR10.sh
│       ├── download_image_SDSS_DR7.sh
│       ├── download_image_SDSS_DR16.sh
│       ├── download_image_SDSS_DR15.sh
│       ├── objects.txt
│       ├── download_image_SDSS_DR8.sh
│       ├── download_image_SDSS_DR9.sh
│       ├── 1774.53759.272.jpg
│       ├── download_image_SDSS_DR18.sh
│       ├── download_image_SDSS_DR11.sh
│       ├── 1627.53473.303.jpg
│       └── 0271.51883.293.jpg
└── .github
    └── workflows
        ├── main.yml
        └── pylint.yml
... length_limit, 1000, reached, counted:

298 directories, 761 files
#################################################
Generated with tree_colored @ 2023 - © Jean Gomes
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
