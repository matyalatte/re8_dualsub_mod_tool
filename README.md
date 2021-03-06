# re8_dualsub_mod_tool
My tool for generating Dualsub Mod RE8.

### What's Dualsub Mod RE8?
**Dualsub Mod RE8** is one of mods for Resident Evil Village. <br>
This mod displays JPN sub and ENG sub at the same time.<br>
You can download it from [here](https://www.nexusmods.com/residentevilvillage/mods/82).<br>
<img src="https://staticdelivery.nexusmods.com/mods/3669/images/82/82-1621313421-1666838186.jpeg" width="512"><br>
You can make your own dualsub mod with this tool.

## How to Use
### STEP1: Download REngine_Text-Tool
**REngine_Text-Tool** is a msg editing tool for Resident Evil games.<br>
Download from [here](https://zenhax.com/viewtopic.php?t=13337) and unpack into the same folder as README. <br>
Now, The structure of your current directory will be like this.<br>
<br>
re8_dualsub_mod_tool<br>
+-- .git<br>
+-- .gitignore<br>
+-- txt_edit_tool<br>
+-- REngine_Text-Tool<br>
+-- clear_workdir.bat<br>
+-- etc...<br>

### STEP2: Unpack Resources
You should unpack the game files to get msg files have message data.<br>
Unpack .pak with unpacking tools like [RETool](https://residentevilmodding.boards.net/thread/10567/pak-tex-editing-tool)

### STEP3: Edit make_dualsub_mod.bat
You should setup parameters of my tools.<br>
![howto](https://user-images.githubusercontent.com/69258547/119158385-1dec9400-ba91-11eb-8884-e434aad3f5cf.png)<br>
Open 'make_dualsub_mod.bat' with an editor, and edit these parameters.
- nativesLocation : Where you unpacked .pak. (ex. C:\REtool\re_chunk_000)
- msgLocation : Where are msg files you want to mod in unpacked game files. (ex. natives\stm\message\sce) 
- lng1 : The language you want to use as the display language. Assign by language id.
- lng2 : The language you want to see subs in. Assign by language id.
- modName : The folder name of dualsub mod you make.

#### Language ID
Japanese: ja, English: en, French: fr, Italian: it, German: de, Spanish: es, Russian: ru<br>
Polish: pl, Portuguese Brasilian: ptBR, Korean: ko, Chinese (traditional): zhTW,<br>
Chinese (Simplified): zhCN, Arabic: ar, Thai: th<br>
<br>
ex. If you want to assign Japanese to lng1, set lng1 as ja.
### STEP4: Run make_dualsub_mod.bat
Run 'make_dualsub_mod.bat'.<br>
Your dualsub mod will be outputted into 're8_dualsub_mod_tool/mods'.

### STEP5: Pack and Install Your New Mod
Convert your new mod folder into rar. (You need a packing tool like WinRAR.)<br>
And install the rar file with [Fluffy Manager](https://www.nexusmods.com/residentevilvillage/mods/18).

### STEP6: Done!
Now, you can use your dualsub mod!<br>
Launch RE8 and check if your mod works fine!
