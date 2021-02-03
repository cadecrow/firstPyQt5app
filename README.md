# Just an app to remind you that you're a badass
### Run this for yourself to see :) </br>

### How To Run:
Download src/ to your selected directory. </br>
Open Terminal and navigate to said directory. </br>
While in the selected directory (the level containing the src/ directory), </br>
create a virtual environment to manage dependencies. </br>
```
python3 -m venv <your_venv_name>
```
on Windows:
```
call <your_venv_name>/scripts/activate.bat
```
On Mac and Linux:
```
source <your_venv_name>/bin/activate
```
You can see that the virtual environment is active by the (<your_venv_name>) prefix in your shell. </br>
</br>
Now install PyQt5 </br>
**Note: I installed using the following line with pip-21.0.1 and Python 3.8.2. You may need to install a different version.** </br>
```
pip3 install PyQt5==5.15.2
```
Finally, install fbs and run
```
pip install fbs
fbs run
```
Shoutout to Michael Herrmann for creating fbs !!! https://github.com/mherrmann
