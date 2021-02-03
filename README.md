# Just an app to remind you that you're a badass
### Run this for yourself to see :) </br>

### How To Run:
Download src/ to your selected directory. </br>
Open Terminal and navigate to said directory. </br>
While in the selected directory </br>
(the level containing the src/ directory, not in the src/ directory itself), </br>
create a virtual environment to manage dependencies. </br>
    (you only need to create the virtual environment once.)
```
python3 -m venv <your_venv_name>
```
Now you will activate this vitrual environment. </br>
    (when you come back to run this app a second time, this is where you will begin.) </br>
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
    (when you come back to run this app a second time, you only need to use ```fbs run```.)
```
pip3 install PyQt5==5.15.2
```
Finally, install fbs and run
```
pip install fbs
fbs run
```
Shoutout to Michael Herrmann for creating fbs !!! https://github.com/mherrmann

**When you are ready to leave your virtual environment use ```ctrl+d``` or ```exit```** </br>
**SECRET SAUCE ALERT: I personally like using ```deactivate``` so I can continue using my terminal with having to start a new session.**
