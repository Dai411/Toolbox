@echo off
echo [*] Building pass_forge.exe ...
pyinstaller --onefile --noconsole --icon=icon.ico PassForge.py
echo [✓] Done. Check dist folder.
pause
