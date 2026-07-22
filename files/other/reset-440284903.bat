@echo off
commander device reset --serialno 440284903
if %errorlevel% equ 0 (
    echo Device reset successful
) else (
    echo Device reset failed, please check connection
)