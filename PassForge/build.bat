@echo off
echo [*] Building PassForge.exe ...
pyinstaller --onefile --noconsole --icon=icon.ico PassForge.py
echo [✓] Done. Check dist folder.
pause
