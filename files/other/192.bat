@echo off
echo Executing 192.py ...
python 192.py
if %errorlevel% neq 0 (
    echo Execution failed, error code: %errorlevel%
    pause
    exit /b %errorlevel%
)
echo Execution successful!
