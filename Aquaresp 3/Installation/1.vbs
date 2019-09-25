


dim xHttp: Set xHttp = createobject("Microsoft.XMLHTTP")
dim bStrm: Set bStrm = createobject("Adodb.Stream")
xHttp.Open "GET", "https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe", False
xHttp.Send

scriptdir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)


with bStrm
    .type = 1 '//binary
    .open
    .write xHttp.responseBody
    .savetofile scriptdir & "\Installer.exe", 2 '//overwrite
end with


