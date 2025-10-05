@echo off
cd /d %~dp0
cd app
uvicorn main:app --reload --port 8010
pause