import subprocess,os
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
apppat = mainpath + os.sep +"temp" + os.sep + "dataviewer" + os.sep + "app" + os.sep


subprocess.Popen(apppat + "app.exe")
