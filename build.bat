@echo off
setlocal

REM 复制 7z 文件到源码目录（确保同目录有 7z.exe 和 7z.dll）
copy "7z\7z.exe" .
copy "7z\7z.dll" .

REM 使用 Nuitka 打包
call nuitka --standalone --onefile ^
       --include-data-file=7z.exe=7z.exe ^
       --include-data-file=7z.dll=7z.dll ^
       unzip.py

REM 清理工作区
del 7z.exe
del 7z.dll
rmdir /S /Q Unzip.build
rmdir /S /Q Unzip.dist
rmdir /S /Q Unzip.onefile-build