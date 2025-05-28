@echo off
cd /d %~dp0
uvicorn main:app --reload
pause