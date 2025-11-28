@echo off
REM Script para configurar AI SmartMenu por primera vez

echo.
echo ==========================================
echo   AI SmartMenu - Setup Inicial
echo ==========================================
echo.

REM Crear entorno virtual
echo Creando entorno virtual...
python -m venv .venv
if errorlevel 1 goto error

echo.
echo Activando entorno virtual...
call .venv\Scripts\activate.bat
if errorlevel 1 goto error

echo.
echo Instalando dependencias...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 goto error

echo.
echo.
echo ==========================================
echo   ✅ Instalación completada exitosamente
echo ==========================================
echo.
echo Próximos pasos:
echo.
echo 1. Copia .env.example a .env:
echo    copy .env.example .env
echo.
echo 2. Edita .env y añade tu clave de OpenAI:
echo    OPENAI_API_KEY="sk-tu-clave-aqui"
echo.
echo 3. En dos terminales diferentes, ejecuta:
echo    Terminal 1: run_api.bat
echo    Terminal 2: run_dashboard.bat
echo.
echo 4. Abre en tu navegador: http://localhost:8501
echo.
echo ==========================================
echo.
pause
goto end

:error
echo.
echo ❌ Error durante la instalación
echo.
pause
goto end

:end
