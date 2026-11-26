@echo off
echo Executing sign.py ...
python sign.py
if %errorlevel% neq 0 (
    echo Execution failed, error code: %errorlevel%
    pause
    exit /b %errorlevel%
)
echo Execution successful!
