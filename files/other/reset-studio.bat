@echo off
title Terminate STS Backend Process
echo Searching and terminating sts_back_end.exe process...

:: Method 1: Terminate by process name
taskkill /F /IM sts_back_end.exe 2>nul

:: Method 2: Terminate by full path (more precise)
for /f "tokens=2 delims=," %%a in ('wmic process where "name='sts_back_end.exe' and executablepath='C:\\Users\\huide\\.silabs\\slt\\installs\\archive\\v6-base-v6.1.0-224\\SimplicityStudio-6\\sts_back_end\\sts_back_end.exe'" get processid /format:csv 2^>nul') do (
    if not "%%a"=="" (
        echo Found process PID: %%a, terminating...
        taskkill /F /PID %%a 2>nul
    )
)

:: Verify if successfully terminated
tasklist /FI "IMAGENAME eq sts_back_end.exe" 2>nul | find /i "sts_back_end.exe" >nul
if errorlevel 1 (
    echo [SUCCESS] sts_back_end.exe process has been terminated.
) else (
    echo [FAILED] sts_back_end.exe process is still running, may require administrator privileges.
)
