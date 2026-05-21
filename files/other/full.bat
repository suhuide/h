@echo off
echo Executing full.py ...
python full.py
if %errorlevel% neq 0 (
    echo Execution failed, error code: %errorlevel%
    pause
    exit /b %errorlevel%
)
echo Execution successful!
