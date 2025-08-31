(content:installing-python)=

# Installing Python

## Recommended approach to install everything

These instructions should be equally valid for macOS, Linux, and Windows.

1. Follow the official instructions to download and install the [Anaconda Python distribution](https://www.anaconda.com/docs/getting-started/anaconda/install).
2. Download the environment file <a href="../_static/environment.yml">environment.yml</a>. This is a text file (feel free to have a closer look at it) that defines the version of Python and a set of third-party Python packages to install. Defining an environment this way makes it easy to ensure that you have exactly the correct Python components installed.
3. [Launch Anaconda Navigator](https://www.anaconda.com/docs/tools/anaconda-navigator/getting-started#starting-navigator) (included with the Anaconda Python distribution)
4. Create a new environment in Anaconda Navigator by importing the file `environment.yml` file that you downloaded in step 2, [as per the official documentation](https://www.anaconda.com/docs/tools/anaconda-navigator/tutorials/manage-environments#importing-an-environment). After this step is completed, you can delete the downloaded `environment.yml` file.

After these installation steps, you can use Anaconda Navigator to launch Jupyter Lab whenever you want to work in Python:

* Go to the "Home" tab in Anaconda Navigator, and click "JupyterLab" to launch Jupyter Lab. Make sure your newly-created environment is active on the "Environments" tab beforehand.
* Within the file browser, navigate to the directory where you want to keep the files for working on energy system modelling.
* To test that everything works, download the Jupyter notebook for {ref}`content:pyomo-basics` and try to open and run it on your computer.

```{tip}
If you have issues with JupyterLab not appearing in your list of installed tools, a possible workaround is to launch JupyterLab by launching a terminal from Anaconda Navigator and then typing `jupyter lab` in the terminal window that appears.
```

## Alternative instructions for more experienced users

### Using the terminal

The Anaconda Python distribution is optional, to make things easier for people with little Python experience. You can use any other installation of Python and just need to install the required packages. Assuming you have a working `conda` installation you can:

* Download the environment file <a href="../_static/environment.yml">environment.yml</a>, then in a terminal window, navigate to the downloaded file and install the requirements by executing: `conda env create -f environment.yml`
* Run Jupyter Lab from a location of your choosing - this way you don't have to manually navigate to the folder within Jupyter Lab: `cd path/to/my/directory; conda activate optimisation-course; jupyter lab`

If you prefer to manually configure your environment, this is the exact content of the downloadable `environment.yml` file, showing you the packages it will install:

```{literalinclude} ../_static/environment.yml
:language: yaml

```

### Using an editor

If you prefer working with an editor rather than Jupyter Lab, you can still use the provided `environment.yml` file to install all requirements.

#### Visual Studio Code

See the official documentation on [how to work with "conda" type Python environments](https://code.visualstudio.com/docs/python/environments).

#### PyCharm

See the official documentation on [configuring a conda virtual environment](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html#conda-requirements).
