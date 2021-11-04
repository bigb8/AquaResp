# AquaResp
Automating Aquatic Respirometry. Focused on automating intermittent respirometry experiments for aquatic animals.

**Now compatible with the new firmware from PyroScience.** See and use [OxyLog](https://github.com/bigb8/AquaOxyLog)

The GUI and code controlling of the experiment, and the code calculating the results are licensed all licensed under GPL, any figures etc under Creative Commons BY-SA.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

Please cite the code when using the software

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2584015.svg)](https://doi.org/10.5281/zenodo.2584015)

Cite as:
Morten Bo Søndergaard Svendsen, Peter G. Bushnell, & John Fleng Steffensen. (2019, March 5). AquaResp 3 (Version V3.0). Zenodo. http://doi.org/10.5281/zenodo.2584015


## Oxygen sensor communication

The fundamental idea is that external software logs to a the oxygen folder, where Aquaresp then can read the data.

I have made a quick guide explaining usage of primarily PyroScience sensors in AquaResp. The approach for Firesting firmware <4, is the same for fibox - presens.


[PDF](https://github.com/bigb8/AquaResp/blob/master/Oxygen%20sensors%20in%20AquaResp.pdf)

[Online slides](https://docs.google.com/presentation/d/e/2PACX-1vRKApb----Bl-j2ZOM9y0zqdH17NzLXA690NrDP-PSPi9B-Z0NpHatC5fBXWHFSP98ulc9m-8D94u8h/pub?start=false&loop=false&delayms=3000)

## Installation

AquaResp is only supported on Windows 10 64 bit.


[Illustrated process SLIDES](https://docs.google.com/presentation/d/e/2PACX-1vRuaoCIWaseBiqeIY4hod_YPqSDzq25VY-STTsyQ2NTEkOmtC3Ywm4X5FOzqQxsIN5L8y9L3kfNrERv/pub?start=false&loop=false&delayms=3000)

[PDF - Installation Illustrated](https://github.com/bigb8/AquaResp/raw/master/Installation%20-%20Aquaresp.pdf)


Download Aquaresp by pressing "Clone or Download" button in the top right corner of this screen.

### Windows 10 - 64bit:

#### Step 1 - downloading Python
##### First run 1.vbs in the Installation folder
This downloads Python for you, the version that has been used for testing (3.7.4. - 64-bit)

#### Step 2 - installing Python and libraries
##### Run 2.bat
This initiates  Python installation for you.

If this fails, open the downloaded Python (InstallPython.exe), and make sure to enable the option "Add to PATH" during the first step of installation

#### After Python has been installed
##### Double click the CheckLibraries.py in the installation folder.
Click each button, this will check and install the libraries needed to run AquaResp 3.0 ASAP
The buttons will change to green and display "OK" when libraries are installed.


####Further:
We recommend setting either Mozilla Firefox or Google Chrome webbrowsers as default browser in Windows. The plotting feature does not work in Internet Explorer or Microsoft Edge browsers.

March 5 2021:
If you are experiencing trouble with running the software after installation. Try running the tool CheckLibraries.py in the Installation folder.
October 2021:
For newer win10 updates, run the CheckLibraries as administrator

---
If this step is failing, open the command prompt (WinButton + R, write "cmd", and press enter), and run the installation commands for the specific library. The following are needed for AQ3

python -m pip install bokeh==1.3.0

python -m pip install numpy

python -m pip install scipy

python -m pip install matplotlib

python -m pip install -U wxPython

python -m pip install mcculw

--


#### Step 3 - adding Icons to your desktop
##### Run Create Links on Desktop.vbs  (in the Aquaresp 3 main folder)
This creates icons on the desktop. You can do that manually aswell.



## Acknowledgements

Thank you to <a href = "https://www1.bio.ku.dk/english/staff/?pure=en/persons/158364">Bent Vismann</a> for testing of AquaResp and inputs on usage of AquaResp for invertebrates.

Thank you to <a href = "https://www.researchgate.net/profile/Denis_Chabot">Denis Chabot</a> for testing of AquaResp over many occasions and providing inputs on usage of AquaResp.

Thank you to <a href = "https://www.researchgate.net/profile/Heidrikur_Bergsson3">Heiðrikur Bergsson</a> for testing and using AquaResp.

Thank you to <a href = "http://saltnfish.dk/cv/">Emil Aputsiaq Christensen</a> for providing valuable usability input.

Thank you to [Lars Emil Juel Andersen](https://www.researchgate.net/profile/Lars-Emil-Juel-Andersen) for being exeptionally fast in trying new AquaResp versions and letting me know of any bugs.
