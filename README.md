# 🍽️ AI SmartMenu

Un sistema inteligente para restaurantes con API robusta y dashboard interactivo dual impulsado por IA predictiva y generativa.

## 📋 Características

- **API FastAPI**: Endpoints para predicciones y chat con IA
- **Dashboard Streamlit**: Interfaz para clientes y gerentes
- **Agente de IA**: Powered by LangChain y OpenAI
- **Predictor de Demanda**: Predicciones basadas en la hora del día

## 🚀 Instalación

1. **Clonar o descargar el proyecto**

2. **Crear un entorno virtual**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   # source .venv/bin/activate  # En Mac/Linux
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   copy .env.example .env
   # Edita .env y agrega tu clave de OpenAI
   ```

## ⚙️ Configuración

### Variables de Entorno (.env)

```
OPENAI_API_KEY=sk-tu-clave-aqui
API_HOST=http://127.0.0.1
API_PORT=8000
```

## 🏃 Ejecución

### Opción 1: Usar los scripts batch (Windows)

1. **Terminal 1 - Ejecutar la API:**

   ```bash
   run_api.bat
   ```

2. **Terminal 2 - Ejecutar el Dashboard:**
   ```bash
   run_dashboard.bat
   ```

### Opción 2: Comando manual

**Terminal 1 - API:**

```bash
python -m uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
```

**Terminal 2 - Dashboard:**

```bash
python -m streamlit run src/dashboard/app.py
```

## 📍 Acceso

- **API Docs**: http://localhost:8000/docs
- **Dashboard**: http://localhost:8501

## 📂 Estructura del Proyecto

```
/AI_SmartMenu_Final/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── run_api.bat
├── run_dashboard.bat
└── src/
    ├── __init__.py
    ├── main.py
    ├── api/
    │   ├── __init__.py
    │   └── endpoints.py
    ├── core/
    │   ├── __init__.py
    │   └── config.py
    ├── dashboard/
    │   ├── __init__.py
    │   └── app.py
    └── ml/
        ├── __init__.py
        ├── agent.py
        └── predictor.py
```

## 🔧 API Endpoints

### Health Check

- `GET /api/health` - Verificar estado de la API

### Predicciones

- `POST /api/predict` - Obtener predicción de demanda

### Chat

- `POST /api/chat/user` - Chat para clientes
- `POST /api/chat/restaurant` - Chat para gerentes

## 🤖 Modos de Funcionamiento

### Modo IA (Con OpenAI)

Si tienes una clave de OpenAI válida, el agente usará GPT-3.5-turbo para conversaciones naturales.

### Modo Respaldo (Sin OpenAI)

Si no tienes clave o las librerías no están disponibles, el agente usará lógica predefinida.

## 📝 Notas de Desarrollo

- El proyecto está optimizado para desarrollo local
- CORS está habilitado para todas las direcciones (ajusta en producción)
- El agente mantiene un historial de conversación

## 📄 Licencia

Este proyecto es educativo y de código abierto.

---

**¡Hecho con ❤️ para restaurantes inteligentes!**
