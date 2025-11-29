"""Módulo de configuración central.

Carga configuraciones desde variables de entorno o usa valores por defecto
para facilitar el desarrollo y el despliegue.
"""
import os

# Configuración de la API
API_HOST = os.getenv("API_HOST", "http://127.0.0.1")
API_PORT = int(os.getenv("API_PORT", 8000))
API_URL = f"{API_HOST}:{API_PORT}"
