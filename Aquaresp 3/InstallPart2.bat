SET mypath=%~dp0
echo %mypath:~0,-1%
cd mypath
InstallPython.exe InstallAllUsers=0 PrependPath=1 Include_test=0


python -m pip install --upgrade pip
python -m pip install bokeh
python -m pip install numpy
python -m pip install scipy
python -m pip install matplotlib
python -m pip install -U wxPython
python -m pip install mcculw
pause