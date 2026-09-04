@echo off
title OmniPilot OS Launcher
echo ===================================================
echo   Starting OmniPilot OS (Autonomous 9-Doc Studio)
echo ===================================================
echo Checking Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3 is not found in PATH. Please install Python 3.
    pause
    exit /b 1
)

echo Launching server on http://127.0.0.1:8765 ...
start "" "http://127.0.0.1:8765"
python server.py
pause
