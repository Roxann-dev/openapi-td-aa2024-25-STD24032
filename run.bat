@echo off
echo
call env\Scripts\activate.bat
echo
uvicorn main:app --reload
pause
