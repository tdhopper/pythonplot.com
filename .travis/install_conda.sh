wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
rm -f miniconda.sh
hash -r
$HOME/miniconda/bin/conda config --set always_yes yes --set changeps1 no
$HOME/miniconda/bin/conda update -q conda
$HOME/miniconda/bin/conda info -a
$HOME/miniconda/bin/conda install --quiet pip
$HOME/miniconda/bin/conda install --quiet --channel r mro-base r-ggplot2