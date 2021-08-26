@echo off

REM %1:mod name
REM %2:language1
REM %3:language2
REM %4:msg file's location (ex natives\stm\message\sce)

setlocal enabledelayedexpansion

mkdir mods\%1\%4 > NUL 2>&1

for %%f in (workdir\*.17) do (
set file=%%f%
REngine_Text-Tool\REngine_Text-Tool.exe !file!.txt %2
move !file!.new !file!
REngine_Text-Tool\REngine_Text-Tool.exe !file!.txt %3
move !file!.new !file!
copy !file! mods\%1\%4
)
endlocal
