@echo off
cd /d %~dp0
cd app
uvicorn main:app --reload
pause