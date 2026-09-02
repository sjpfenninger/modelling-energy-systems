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

## Troubleshooting

- _`pixi` is not recognized / command not found_ — you didn't open a fresh terminal after Step 2.
- _`No such file or directory` after `cd`_ — the folder isn't where the path says it is; make sure you are using the folder where you unzipped everything on your computer.
- _`pixi` says it cannot find a `pixi.toml` or workspace_ — you are one folder too high. Unzipping on Windows often nests the course folder inside a folder named after the zip, giving `Documents\modelling-energy-systems-course\modelling-energy-systems`. `cd` into whichever folder directly contains `pixi.toml`.
- _Installing fails, or `pixi run update-course` won't start_ — every `pixi run` command installs the course software first, so none of them can run if that install is broken. Download the course folder again from Step 3, then copy your `notebooks` folder into the new one.
- _`No module named pyomo` inside a notebook_ — JupyterLab wasn't started with `pixi run jupyter-lab` from inside the course folder.
- _The install is very slow, or fails partway through_ — check that the folder is not inside OneDrive, Dropbox or iCloud (see the warning in Step 3). Moving it to a normal local folder and running `pixi run check-setup` again may fix this.
- _Something else_ — run `pixi run check-setup` and bring the output to a class tutorial session.
