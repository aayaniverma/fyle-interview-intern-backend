@echo off
REM Stop on first error
setlocal enabledelayedexpansion
if errorlevel 1 exit /b 1

REM Delete older .pyc files
REM for /r %%i in (*.pyc) do del %%i

REM Run required migrations
set FLASK_APP=core/server.py

REM flask db init -d core/migrations/
REM flask db migrate -m "Initial migration." -d core/migrations/
REM flask db upgrade -d core/migrations/

REM Run server
python -m waitress --host=127.0.0.1 --port=8000 core.server:app
