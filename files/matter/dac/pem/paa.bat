@echo off
rem Check if openssl is available
where openssl >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: openssl not found. Please install and add to PATH.
    pause
    exit /b 1
)

rem Check if paa.pem exists
if not exist "paa.pem" (
    echo Error: paa.pem not found in current directory.
    pause
    exit /b 1
)

rem Execute parsing command
echo Parsing paa.pem certificate...
echo openssl x509 -in paa.pem -text -noout
openssl x509 -in paa.pem -text -noout

echo.
echo Parsing completed.
pause