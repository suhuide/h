@echo off
echo Executing full_s37.py ...
python full_s37.py
if %errorlevel% neq 0 (
    echo Execution failed, error code: %errorlevel%
    pause
    exit /b %errorlevel%
)
echo Execution successful!
