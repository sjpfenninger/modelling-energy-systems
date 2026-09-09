(content:installing-python)=

# Installing Python

You need two things: **pixi**, a small program that manages Python and all course packages for you, and the **course folder**, which tells pixi exactly what to install.
If you have other Python installations on your system, including Anaconda, it won't interfere, but don't use its "Anaconda Prompt" and don't launch Jupyter Lab via Anaconda Navigator. Use the terminal as described below.

These instructions have two parts:

- {ref}`Part 1 <content:installing-python:install>` is the installation, which you only have to do once.
- {ref}`Part 2 <content:installing-python:every-time>` is what you do every time you want to run the course software.

(content:installing-python:install)=

## Part 1 — Install the course software (you do this once)

### Step 1 — Install pixi

::::{tab-set}

:::{tab-item} Windows
:sync: windows

Open the Start menu, type `terminal`, and open **Terminal**.
This is a window into which you type commands.

Copy the line below, paste it into the terminal, and press Enter:

```powershell
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

Then **close the terminal, open a new terminal**, and check that pixi is installed and working, by typing:

```powershell
pixi --version
```

:::

:::{tab-item} macOS / Linux
:sync: unix

Press Cmd+Space, type `terminal`, press Enter.
This is a window into which you type commands.

Copy the line below, paste it into the terminal, and press Enter:

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

Then **close the terminal, open a new terminal**, and check that pixi is installed and working, by typing:

```bash
pixi --version
```

:::

::::

### Step 2 — Download the course folder

Download [`modelling-energy-systems-course.zip`](https://github.com/sjpfenninger/modelling-course-env/releases/latest/download/modelling-energy-systems-course.zip).

Then unzip it, and move the resulting `modelling-energy-systems` folder somewhere you'll keep your work, for example into `Documents`.

This folder defines the course software and is also where your code will live.

```{warning}
It is best not to put the folder in a location synced by OneDrive, Dropbox or iCloud.
The course software is several hundred megabytes. Syncing it will be slow and can make the installation fail partway through.
```

(content:installing-python:terminal-in-folder)=

### Step 3 — Open a terminal in the course folder

Every course command is run from inside the course folder, so the terminal has to be pointed at it first.
The easiest way is to let your file manager open the terminal for you.

::::{tab-set}

:::{tab-item} Windows
:sync: windows

In **File Explorer**, right-click the `modelling-energy-systems` folder that you unzipped, and choose **Open in Terminal**.

A terminal window opens that is already pointed at the right folder.

```{note}
**Open in Terminal** exists only Windows 11 and later. On Windows 10, you can follow the manual steps explained below.
```

To confirm you are in the right place, type `dir` and press Enter. This shows you a listing of files in the current directory, which should include `pixi.toml`.

:::

:::{tab-item} macOS / Linux
:sync: unix

In **Finder**, right-click (or Ctrl-click) the `modelling-energy-systems` folder and choose **Services → New Terminal at Folder**.

A terminal window opens that is already pointed at the right folder.

```{note}
If you don't see **New Terminal at Folder**, switch it on first under System Settings → Keyboard → Keyboard Shortcuts… → Services → Files and Folders.
```

To confirm you are in the right place, type `ls` and press Enter. This shows you a listing of files in the current directory, which should include `pixi.toml`.

:::

::::

```{tip}
If you prefer typing, you can move the terminal into the folder yourself with the `cd` (change directory) command.
Assuming you unzipped the folder into `Documents`, that is `cd Documents\modelling-energy-systems` on Windows, or `cd Documents/modelling-energy-systems` on macOS or Linux.
```

### Step 4 — Run the setup check

In the terminal you just opened, type:

```bash
pixi run check-setup
```

This checks your setup and confirms that it works.
Importantly, the first time, pixi also downloads Python and all course packages.
This can take a few minutes and it might seem like nothing is happening in your terminal window, but you should wait until you see the "Everything works!" confirmation.
After the lengthy first-time installation, starting will be instant.

After installing everything, the check prints the version of each package, solves two small optimisation problems, and finishes with:

```
Everything works!
```

If you see that, your setup is complete.
If you see something else, look at the troubleshooting section below.

(content:installing-python:every-time)=

## Part 2 — Every time you want to work

Once the installation is done, working on the course is always the same four steps:

1. Open a terminal in the course folder, as described in {ref}`content:installing-python:terminal-in-folder`.
2. Start the tool you want with `pixi run …` (see below).
3. Do your work in the browser window that opens.
4. When you're done, close the browser tab and press **Ctrl+C** in the terminal.

### Start JupyterLab

```bash
pixi run jupyter lab
```

JupyterLab opens in your browser, showing the contents of the course folder.

It is recommended to keep your own notebooks and exercise files in the `notebooks` folder.
It is empty to start with. Feel free to use your own folder structure, of course.

### Start Calliope Studio

Assuming you have a Calliope model with a `model.yaml` file in `my-model-folder`, you can simply run:

```bash
pixi run calliope-studio my-model-folder
```

Alternatively, to see the model chooser, run Calliope Studio without providing a model folder at all:

```bash
pixi run calliope-studio
```

It opens in your browser like JupyterLab does, and you stop it the same way.

(content:installing-python:updating)=

### Updating the course software

When a new version of the course software is announced, update your installation by running, again from inside the course folder:

```bash
pixi run update-course
```

This updates the course packages. Your own files in the `notebooks` folder are not touched.

## Using VS Code or other editors

JupyterLab is all you need and the recommended way to work here, but if you prefer working in [Visual Studio Code](https://code.visualstudio.com/), you can point it at the course software by following the approach below.
You should be able to use other editors or IDEs by following a similar approach.

```{tip}
Run `pixi run check-setup` (Step 4) at least once before you start, because that forces pixi to actually install everything.
```

In VS Code, open the Extensions panel and make sure that Microsoft's **Python** and **Jupyter** extensions are installed.

Choose **File → Open Folder** and select the `modelling-energy-systems` folder that you unzipped (that is, the folder that contains the `pixi.toml` file).

Now you need to tell VS Code to use the Python version installed by pixi.
Press **Ctrl+Shift+P** (**Cmd+Shift+P** on macOS), type `Python: Select Interpreter`, and choose the entry whose path is inside `.pixi/envs/default`.
If it is not in the list, choose **Enter interpreter path…** and type the path yourself:

::::{tab-set}

:::{tab-item} Windows
:sync: windows

```powershell
.pixi\envs\default\python.exe
```

:::

:::{tab-item} macOS / Linux
:sync: unix

```bash
.pixi/envs/default/bin/python
```

:::

::::

To work in a notebook from VS Code, open a `.ipynb` file, click **Select Kernel** at the top right, choose **Python Environments…**, and pick that same environment.

## Troubleshooting

| Problem                                                   | Solution                                                                                                                                                                                                          |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pixi` is not recognized / command not found              | You didn't open a fresh terminal after Step 1.                                                                                                                                                                    |
| `No such file or directory` after `cd`                    | The folder isn't where the path says it is; make sure you are using the folder where you unzipped everything on your computer. Opening the terminal from File Explorer or Finder (Step 3) avoids this altogether. |
| `pixi` says it cannot find a `pixi.toml` or workspace     | You are one folder too high. Open the terminal in whichever folder directly contains `pixi.toml` (see Step 2).                                                                                                    |
| Installing fails, or `pixi run update-course` won't start | Every `pixi run` command installs the course software first, so none of them can run if that install is broken. Download the course folder again from Step 2, then copy your `notebooks` folder into the new one. |
| `No module named pyomo` inside a notebook                 | JupyterLab wasn't started with `pixi run jupyter-lab` from inside the course folder, or, in VS Code, the wrong interpreter or kernel is selected.                                                                 |
| VS Code doesn't list the course environment               | You haven't run `pixi run check-setup` yet, or you opened the wrong folder. Follow the instructions for VS Code above.                                                                                            |
| The install is very slow, or fails partway through        | Check that the folder is not inside OneDrive, Dropbox or iCloud (see the warning in Step 2). Moving it to a normal local folder and running `pixi run check-setup` again may fix this.                            |
| Something else                                            | Run `pixi run check-setup` and bring the output to a class tutorial session.                                                                                                                                      |
