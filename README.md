# Just an app to remind you that you're a badass
Run this for yourself :)


### How To Run:
Download src/ to your selected directory.
Open Terminal and navigate to said directory.
While in the selected directory (the level containing the src/ directory),
create a virtual environment to manage dependencies.

{ python3 -m venv <your_venv_name> }

on Windows:
{ call <your_venv_name>/scripts/activate.bat }

On Mac and Linux:
{ source <your_venv_name>/bin/activate }

You can see that the virtual environment is active by the (<your_venv_name>) prefix in your shell

Now install PyQt5
Note: I installed using the following line with pip-21.0.1. You may need to install a different version.
{ pip3 install PyQt5==5.15.2 }

Finally, install fbs and run

{ pip install fbs
  fbs run }

