@echo off

set nativesLocation=D:\RE_modding\REtool\re_chunk_000
set msgLocation=\natives\stm\message\sce
set lng1=ja
set lng2=en
set modName=dualsub_test_%lng1%_%lng2%


REM copy msg files from %nativesLocation%\%msgLocation%
call copy_msg.bat %nativesLocation% %msgLocation%

REM extract sub text from msg files
call export.bat %lng1% %lng2%

REM make dualsub text from txt files
txt_edit_tool\dist\make_dualsub.exe %~dp0\workdir %lng1% %lng2%

echo TXT editing was complete. If you want to edit texts yourself, open workdir and edit TXT files.
PAUSE

REM make msg files from txt files
call import.bat %modName% %lng1% %lng2% %msgLocation%

REM delete intermediate files
call clear_workdir.bat

echo Done! 
echo Mod files were exported in mods\%modName%.
echo Pack and apply your new dualsub mod!

PAUSE