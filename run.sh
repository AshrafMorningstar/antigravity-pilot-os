#!/usr/bin/env bash
# OmniPilot OS Launcher for Linux and macOS
set -e

echo "==================================================="
echo "  Starting OmniPilot OS (Autonomous 9-Doc Studio)"
echo "==================================================="

if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed."
    exit 1
fi

echo "Launching server on http://127.0.0.1:8765 ..."

# Open browser if supported
if command -v xdg-open &> /dev/null; then
    xdg-open "http://127.0.0.1:8765" &
elif command -v open &> /dev/null; then
    open "http://127.0.0.1:8765" &
fi

python3 server.py
