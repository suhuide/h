@echo off
rem Check if openssl is available
where openssl >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: openssl not found. Please install and add to PATH.
    pause
    exit /b 1
)

rem Check if pai.pem exists
if not exist "pai.pem" (
    echo Error: pai.pem not found in current directory.
    pause
    exit /b 1
)

rem Execute parsing command
echo Parsing pai.pem certificate...
echo openssl x509 -in pai.pem -text -noout
openssl x509 -in pai.pem -text -noout

echo.
echo Parsing completed.
pause