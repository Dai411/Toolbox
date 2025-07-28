@echo off
echo [*] Building pass_forge.exe ...
pyinstaller --onefile --noconsole --icon=icon.ico pass_forge.py
echo [✓] Done. Check dist folder.
pause
