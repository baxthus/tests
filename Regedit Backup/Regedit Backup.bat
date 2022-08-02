@echo off
echo.
echo Running...
echo.
cd C:\
if not exist C:\backup (
    mkdir backup
)
cd C:\backup
if exist C:\backup\backup.reg (
    del backup.reg
)
REG EXPORT "HKCR" 1.reg
REG EXPORT "HKCU" 2.reg
REG EXPORT "HKLM" 3.reg
REG EXPORT "HKU" 4.reg
REG EXPORT "HKCC" 5.reg
copy 1.reg+2.reg+3.reg+4.reg+5.reg backup.reg
del 1.reg 2.reg 3.reg 4.reg 5.reg
cls
echo Backup completed successfully
echo.
explorer.exe C:\Backup
pause