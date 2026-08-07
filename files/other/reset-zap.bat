@ECHO OFF

Echo "delete ZAP"
taskkill /f /im zap.exe
timeout /t 2 /nobreak >nul
rd /s /q "C:\Users\huide\.zap"
