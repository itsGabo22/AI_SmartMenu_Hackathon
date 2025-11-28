"""Punto de entrada principal de la aplicación FastAPI."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.endpoints import router

app = FastAPI(
    title="AI SmartMenu API",
    description="API para el motor de inteligencia de restaurantes.",
    version="1.0.0"
)

# Configurar CORS para permitir que el dashboard se comunique con la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, sé más específico: ["http://localhost:8501"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir el router con todos los endpoints
app.include_router(router, prefix="/api")

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bienvenido a la API de AI SmartMenu. Ve a /docs para la documentación."}
