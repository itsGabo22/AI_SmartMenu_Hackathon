# 🍽️ Aplicación de Restaurantes con IA

Aplicación web que muestra restaurantes con un asistente de IA integrado para recomendaciones.

## 🚀 Características

- Visualización de restaurantes con detalles completos
- Búsqueda y filtrado de restaurantes
- Asistente de IA integrado con Gemini
- Interfaz responsive
- Panel de administración Django

## 🛠️ Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

## 🚀 Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone [https://github.com/tu-usuario/nombre-repositorio.git](https://github.com/tu-usuario/nombre-repositorio.git)
   cd nombre-repositorio

Crear y activar entorno virtual:
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instalar dependencias:
bash
pip install -r requirements.txt
Configuración del entorno:
Copiar .env.example a .env
Configurar las variables necesarias en .env
Aplicar migraciones:
bash
python manage.py migrate
Crear superusuario (opcional):
bash
python manage.py createsuperuser
Iniciar servidor de desarrollo:
bash
python manage.py runserver
⚙️ Configuración
Variables de entorno
Crea un archivo .env en la raíz del proyecto con las siguientes variables:

env
DEBUG=True
SECRET_KEY=tu_clave_secreta_aqui
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
GEMINI_API_KEY=tu_api_key_de_gemini
Base de datos
Por defecto se usa SQLite. Para usar PostgreSQL:

env
DATABASE_URL=postgres://usuario:contraseña@localhost/nombre_bd
🚀 Despliegue
Vercel/Netlify (Frontend) + Render/Heroku (Backend)
Backend:
Configurar las variables de entorno
Usar el comando de inicio: gunicorn mi_proyecto.wsgi
Frontend:
Configurar la variable API_URL para que apunte a tu backend
Establecer la ruta de build como templates/
🛠️ Comandos útiles
bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Ejecutar tests
python manage.py test
🤖 Asistente de IA
El asistente de IA está integrado usando la API de Google Gemini. Para usarlo:

Obtén una API key de Google AI Studio
Configúrala en las variables de entorno como GEMINI_API_KEY
📄 Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

✨ Contribución
Las contribuciones son bienvenidas. Por favor, lee CONTRIBUTING.md para más detalles.

Hecho con ❤️ por NachoNar