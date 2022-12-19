@ECHO OFF
ECHO ----------------------Remove Old File----------------------
DEL C:\chick_0\chk.exe
ECHO ----------------------Start  Building----------------------
pyinstaller.exe --clean --onefile chk.py
ECHO ---------------------Move Build Output----------------------
move dist\chk.exe c:\chick_0\chk.exe

SET /p end=Press <Enter> to quit
