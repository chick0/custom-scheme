@ECHO OFF
ECHO ----------------------Remove Old File----------------------
DEL C:\p-launcher\client.exe
DEL C:\p-launcher\game.exe
ECHO ----------------------Start  Building----------------------
pyinstaller.exe --clean --onefile client.py
pyinstaller.exe --clean --onefile game.py
ECHO ---------------------Move Build Output----------------------
move dist\client.exe c:\p-launcher\client.exe
move dist\game.exe c:\p-launcher\game.exe

SET /p end=Press <Enter> to quit
