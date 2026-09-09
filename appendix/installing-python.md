(content:installing-python)=

# Installing Python

## Installing Python and the course software

You need two things: **pixi**, a small program that manages Python and all course packages for you, and the **course folder**, which tells pixi exactly what to install.
If you have other Python installations on your system, including Anaconda, it won't interfere, but don't use its "Anaconda Prompt"; use the normal terminal as described below.)

### Step 1 — Open a terminal

- **Windows:** open the Start menu, type `terminal`, and open **Terminal**. This is a window into which you type commands.
- **macOS:** press Cmd+Space, type `terminal`, press Enter.

### Step 2 — Install pixi

You only need to do this once. Copy the line for your system, paste it into the terminal, and press Enter:

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

**macOS / Linux:**

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

Then **close the terminal, open a new terminal**, and check that Pixi is installed and working, by typing:

```
pixi --version
```

### Step 3 — Download the course folder

Download [`modelling-energy-systems-course.zip`](https://github.com/sjpfenninger/modelling-course-env/releases/latest/download/modelling-energy-systems-course.zip), unzip it, and move the resulting `modelling-energy-systems` folder somewhere you'll keep your work, for example into `Documents`.
This folder defines the course software and is also where your code will live.

```{warning}
It is best not to put the folder in a location synced by OneDrive, Dropbox or iCloud.
The course software is several hundred megabytes. Syncing it will be slow and can make the installation fail partway through.
```

### Step 4 — Check that everything works

In the terminal, move into the folder, then run the check.

```{tip}
If you are new to the terminal, the important thing to remember is that you typically want to move to the folder that you want to work in first. The `cd` (change directory) command does that.
```

Assuming you unzipped the folder into "Documents" (adjust the path as needed):

On Windows:

```powershell
cd Documents\modelling-energy-systems
pixi run check-setup
```

On macOS or Linux:

```bash
cd Documents/modelling-energy-systems
pixi run check-setup
```

The first time, pixi downloads Python and all course packages.
This can take a few minutes.
Every later start is instant and works offline.

After installing everything, the check prints the version of each package, solves two small optimisation problems, and finishes with:

```
Everything works!
```

If you see that, your setup is complete.
If you see something else, look at the troubleshooting section below.

## Using the installed tools

### Start JupyterLab

```bash
pixi run jupyter-lab
```

JupyterLab opens in your browser, showing the contents of the course folder.

It is recommended to keep your own notebooks and exercise files in the `notebooks` folder.
It is empty to start with. Feel free to use your own folder structure, of course.

When you're done working, close the browser tab and press **Ctrl+C** in the terminal.

### Start Calliope Studio

Assuming you have a Calliope model with a `model.yaml` file in `my-model-folder`, you can simply run:

```bash
pixi run calliope-studio my-model-folder
```

Alternatively, to see the model chooser, run Calliope Studio without providing a model folder at all:

```bash
pixi run calliope-studio
```

It opens in your browser like JupyterLab does. To stop it close the browser tab and press **Ctrl+C** in the terminal.

## Using VS Code or other editors

JupyterLab is all you need and the recommended way to work here, but if you prefer working in [Visual Studio Code](https://code.visualstudio.com/), you can point it at the course software by following the approach below.
You should be able to use other editors or IDEs by following a similar approach.

```{tip}
Run `pixi run check-setup` (Step 4) at least once before you start, because that forces pixi to actually install everything.
```

In VS Code, open the Extensions panel and make sure that Microsoft's **Python** and **Jupyter** extensions are installed.

Choose **File → Open Folder** and select the `modelling-energy-systems` folder that you unzipped (that is, the folder that contains the `pixi.toml` file).

Now you need to tell VS Code to use the Python version installed by Pixi.
Press **Ctrl+Shift+P** (**Cmd+Shift+P** on macOS), type `Python: Select Interpreter`, and choose the entry whose path is inside `.pixi/envs/default`.
If it is not in the list, choose **Enter interpreter path…** and type the path yourself.

On Windows:

```powershell
.pixi\envs\default\python.exe
```

On macOS or Linux:

```bash
.pixi/envs/default/bin/python
```

To work in a notebook from VS Code, open a `.ipynb` file, click **Select Kernel** at the top right, choose **Python Environments…**, and pick that same environment.

## Troubleshooting

| Problem                                                   | Solution                                                                                                                                                                                                                                                    |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pixi` is not recognized / command not found              | You didn't open a fresh terminal after Step 2.                                                                                                                                                                                                              |
| `No such file or directory` after `cd`                    | The folder isn't where the path says it is; make sure you are using the folder where you unzipped everything on your computer.                                                                                                                              |
| `pixi` says it cannot find a `pixi.toml` or workspace     | You are one folder too high. Unzipping on Windows often nests the course folder inside a folder named after the zip, giving `Documents\modelling-energy-systems-course\modelling-energy-systems`. `cd` into whichever folder directly contains `pixi.toml`. |
| Installing fails, or `pixi run update-course` won't start | Every `pixi run` command installs the course software first, so none of them can run if that install is broken. Download the course folder again from Step 3, then copy your `notebooks` folder into the new one.                                           |
| `No module named pyomo` inside a notebook                 | JupyterLab wasn't started with `pixi run jupyter-lab` from inside the course folder, or, in VS Code, the wrong interpreter or kernel is selected.                                                                                                           |
| VS Code doesn't list the course environment               | You haven't run `pixi run check-setup` yet, or you opened the wrong folder. Follow the instructions for VS Code above.                                                                                                                                      |
| The install is very slow, or fails partway through        | Check that the folder is not inside OneDrive, Dropbox or iCloud (see the warning in Step 3). Moving it to a normal local folder and running `pixi run check-setup` again may fix this.                                                                      |
| Something else                                            | Run `pixi run check-setup` and bring the output to a class tutorial session.                                                                                                                                                                                |
