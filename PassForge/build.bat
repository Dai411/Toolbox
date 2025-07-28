@echo off
echo [*] Building PassForge.exe ...
pyinstaller --onefile --noconsole --clean --strip --icon=icon.ico PassForge.py
echo [✓] Done. Check dist folder.
pause
