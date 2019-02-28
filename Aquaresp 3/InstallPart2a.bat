SET mypath=%~dp0
echo %mypath:~0,-1%
cd %mypath
InstallPython.exe InstallAllUsers=0 PrependPath=1 Include_test=0
pause
