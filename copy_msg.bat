
REM %1:natives' location (ex. C:\REtool\re_chunk_000)
REM %2:msg folder's location (ex. natives\stm\message\sce) 

echo %1\%2
mkdir mods\vanilla\%2 > NUL 2>&1
mkdir workdir> NUL 2>&1
copy %1\%2 workdir
copy %1\%2 mods\vanilla\%2