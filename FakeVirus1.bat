REM Abysmal - abysmal26.github.io
REM HyPeRiS Group

@echo off
color 2
title Virus

:: Advertising
echo =================================================================
echo                 Powered by Ritzy
echo.
echo                 Twitter @RitzyVex
echo.
echo           Copyright RitzyDevelopment 2021
echo =================================================================

:: Echo
echo.
echo Are you sure you want to continue?
echo.

:: Option
set /p opcao=(Y/N)? = 

:: Config of option
if "%opcao%"=="y" goto virus
if "%opcao%"=="n" goto sair

:: Virus
:virus
cls
echo Iniciando...
cd/
tree > tree
type tree
del tree
:loop
driverquery
tasklist
goto loop

:: Exit
:sair
exit
