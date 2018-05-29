## Instructions
### Easy (online)

The Aristeia calculator can be run from [this website](https://mybinder.org/v2/gh/jvivian/aristeia-calculator/master)

### Harder (local)

1. Download and install [Anaconda](https://www.anaconda.com/download) for your OS
2. Download [Aristeia calculator](https://github.com/jvivian/aristeia-calculator) and unzip
    1. Or download via `git clone https://github.com/jvivian/aristeia-calculator`
3. Open terminal (Mac OSx) or command line (Windows) and `cd` into the directory
4. Type `conda env create` to create environment from **environment.yml** file
5. Type `source activate aristeia-calculator` to activate environment or `activate aristeia-calcalator` if on windows.
    1. If `direnv` is installed, I included a `.envrc` file, just type `direnv allow` and re-`cd` back into the directory.
6. Type `jupyter notebook` and open a browser go to `localhost:8000` if the windows doesn't open automatically.
7. Open `Aristeia-Dice-Calculator.ipynb` and execute code 
