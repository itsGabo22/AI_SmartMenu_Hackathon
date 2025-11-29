# 🍽️ AI SmartMenu

Un sistema inteligente para restaurantes con API robusta y dashboard interactivo dual impulsado por IA predictiva y generativa.

## 📋 Características

- **API FastAPI**: Endpoints para predicciones y chat con IA
- **Dashboard Streamlit**: Interfaz para clientes y gerentes
- **Agente de IA**: Powered by LangChain y OpenAI
- **Predictor de Demanda**: Predicciones basadas en la hora del día
- **Dataset Integrado**: Menú completo con 15+ productos
- **Búsqueda de Productos**: Busca por nombre o descripción

## 🚀 Instalación Completa

### Paso 1: Clonar o descargar el proyecto

```bash
cd c:\Users\Gabriel\Desktop\Tareas\SmartMenu\AI_SmartMenu_Final
```

### Paso 2: Crear un entorno virtual

```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows
# source .venv/bin/activate  # En Mac/Linux
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar la API Key de OpenAI

**⚠️ IMPORTANTE: Este paso es necesario para usar la IA**

1. **Duplica el archivo `.env.example`** y renómbralo a `.env`
2. **Abre `.env`** con un editor de texto (Notepad, VS Code, etc.)

3. **Busca esta línea:**

   ```
   OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   ```

4. **Obtén tu clave de OpenAI:**

   - Ve a https://platform.openai.com/api-keys
   - Inicia sesión con tu cuenta de OpenAI
   - Haz clic en "Create new secret key"
   - Copia la clave (comienza con `sk-`)

5. **Reemplaza la clave en `.env`:**

   ```
   OPENAI_API_KEY="sk-tu-clave-real-aqui"
   ```

6. **Guarda el archivo** (Ctrl+S)

✅ El archivo `.env` está en `.gitignore`, así que **nunca se subirá a Git** (seguro).

## 📂 Dataset Incluido

El proyecto viene con un **menú completo integrado** en `src/data/products.py`:

### Categorías:

- **Desayuno**: Café y Croissant, Huevos Revueltos, Pancakes
- **Almuerzo**: Hamburguesa Clásica, Ensalada César, Pizza, Sándwich
- **Merienda**: Torta de Chocolate, Frappuccino, Brownie
- **Cena**: Salmón a la Parrilla, Carne Asada, Pasta Boloñesa

Cada producto incluye:

- Nombre y descripción
- Precio
- Tiempo de preparación
- Calorías
- Ingredientes

### Funciones disponibles:

```python
from src.data.products import (
    get_all_products(),           # Todos los productos
    get_products_by_category(),   # Por categoría
    get_product_by_id(),          # Producto específico
    search_products()             # Buscar por nombre
)
```

## 🔧 Cómo Añadir más Productos

Edita `src/data/products.py` y añade nuevos productos al diccionario `MENU_PRODUCTS`:

```python
"nueva_categoria": [
    {
        "id": "identificador_unico",
        "name": "Nombre del Plato",
        "description": "Descripción detallada",
        "price": 9.99,
        "category": "Categoría",
        "ingredients": ["ingrediente1", "ingrediente2"],
        "prep_time": 10,  # en minutos
        "calories": 450
    }
]
```

## 📂 Estructura del Proyecto

```
/AI_SmartMenu_Final/
├── .env.example          # Plantilla de variables de entorno
├── .env                  # Tu configuración (NO subir a Git)
├── .gitignore
├── README.md
├── requirements.txt
├── run_api.bat
├── run_dashboard.bat
└── src/
    ├── __init__.py
    ├── main.py           # App FastAPI
    ├── api/
    │   ├── __init__.py
    │   └── endpoints.py  # Todos los endpoints REST
    ├── core/
    │   ├── __init__.py
    │   └── config.py     # Configuración centralizada
    ├── dashboard/
    │   ├── __init__.py
    │   └── app.py        # Dashboard Streamlit dual
    ├── data/
    │   ├── __init__.py
    │   └── products.py   # Dataset de productos
    └── ml/
        ├── __init__.py
        ├── agent.py      # Agente de IA con fallback
        └── predictor.py  # Predictor de demanda
```

## 🏃 Ejecución

### Opción 1: Usar los scripts batch (Windows) - **RECOMENDADO**

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

## 📍 Acceso a la Aplicación

- **API Docs (Swagger)**: http://localhost:8000/docs
- **API Alternativa (ReDoc)**: http://localhost:8000/redoc
- **Dashboard**: http://localhost:8501

## 🔌 Endpoints API

### Salud

- `GET /api/health` - Verificar estado de la API

### Menú

- `GET /api/menu/products` - Todos los productos
- `GET /api/menu/products/category/{category}` - Por categoría
- `GET /api/menu/search?q=hamburguesa` - Buscar productos

### Predicciones

- `POST /api/predict` - Predicción de demanda
  ```json
  { "features": { "hour": 19 } }
  ```

### Chat

- `POST /api/chat/user` - Chat para clientes

  ```json
  {"message": "¿Qué me recomiendas?", "menu_context": {...}}
  ```

- `POST /api/chat/restaurant` - Chat para gerentes
  ```json
  {"message": "¿Cómo preparo?", "prediction_data": {...}}
  ```

## 🤖 Modos de Funcionamiento

### Modo IA (Con OpenAI)

Si tienes una clave de OpenAI válida, el agente usará GPT-3.5-turbo para conversaciones naturales y contextuales.

### Modo Respaldo (Sin OpenAI)

Si no tienes clave o las librerías no están disponibles, el agente usará lógica predefinida inteligente.

## 🛠️ Solución de Problemas

### "API connection error"

- Verifica que `run_api.bat` esté ejecutándose en otra terminal
- Asegúrate de que el puerto 8000 no esté en uso

### "ImportError: langchain"

- Ejecuta: `pip install -r requirements.txt`
- Asegúrate de que `.venv` está activado

### "OPENAI_API_KEY not found"

- Crea un archivo `.env` (cópialo de `.env.example`)
- Añade tu clave real de OpenAI
- Reinicia las terminales

### "No module named 'src'"

- Asegúrate de ejecutar desde la carpeta raíz del proyecto
- Verifica que tienes archivos `__init__.py` en todas las carpetas

## 📚 Ejemplo de Uso

```bash
# 1. Activar entorno
.venv\Scripts\activate

# 2. Iniciar API
start cmd /k "run_api.bat"

# 3. Iniciar Dashboard
start cmd /k "run_dashboard.bat"

# 4. Abre el navegador
# http://localhost:8501
```

## 🔐 Seguridad

- ✅ `.env` está en `.gitignore`
- ✅ CORS habilitado para localhost (ajusta en producción)
- ✅ Las claves API nunca se loguean

## 📄 Licencia

Este proyecto es educativo y de código abierto.

---

**¡Hecho con ❤️ para restaurantes inteligentes!**

**Próximas mejoras:**

- [ ] Base de datos (SQLAlchemy + PostgreSQL)
- [ ] Autenticación (JWT)
- [ ] Historial de pedidos
- [ ] Análisis de ventas en tiempo real
- [ ] Recomendaciones personalizadas basadas en IA
