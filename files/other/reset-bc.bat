@echo off
echo Deleting Beyond Compare 4 CacheID registry value...
reg delete "HKEY_CURRENT_USER\Software\Scooter Software\Beyond Compare 4" /v CacheID /f

if %errorlevel% equ 0 (
    echo Successfully deleted CacheID value.
) else (
    echo Deletion failed. The value may not exist or you may lack permissions.
)