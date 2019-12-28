wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
rm -f miniconda.sh
hash -r
$HOME/miniconda/bin/conda config --set always_yes yes --set changeps1 no
$HOME/miniconda/bin/conda update -q conda
$HOME/miniconda/bin/conda info -a
conda install --quiet pip readline r-essentials
conda install --quiet --channel r rpy2
wget --quiet https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage -O orca.AppImage
chmod +x orca.AppImage
