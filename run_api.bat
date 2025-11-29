@echo off
echo Iniciando la API de AI SmartMenu...
REM Soluciona problemas de permisos y recarga en Windows
set PYTHONDONTWRITEBYTECODE=1
python -m uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
pause
