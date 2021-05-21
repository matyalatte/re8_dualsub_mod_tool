@echo off

REM %1:language1
REM %2:language2

setlocal enabledelayedexpansion

for %%f in (workdir\*.17) do (
set file=%%f%
REngine_Text-Tool\REngine_Text-Tool.exe !file! %1
move !file!.txt !file!.%1.txt
REngine_Text-Tool\REngine_Text-Tool.exe !file! %2
move !file!.txt !file!.%2.txt
)
endlocal
