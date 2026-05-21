@echo off
echo Executing setup_payload.py ...
python setup_payload.py
if %errorlevel% neq 0 (
    echo Execution failed, error code: %errorlevel%
    pause
    exit /b %errorlevel%
)
echo Execution successful!
