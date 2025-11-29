"""Define todos los endpoints de la API."""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any, Optional
from datetime import datetime

from src.ml.predictor import predict
from src.ml.agent import create_agent
from src.data.products import get_all_products, search_products, get_products_by_category

# Crear una única instancia del agente para ser reutilizada en toda la aplicación
agent = create_agent()

router = APIRouter()

# --- Modelos de Datos (Pydantic) ---
class PredictRequest(BaseModel):
    features: dict

class ChatUserRequest(BaseModel):
    message: str
    menu_context: Optional[Dict[str, Any]] = None

class ChatRestaurantRequest(BaseModel):
    message: str
    prediction_data: Optional[Dict[str, Any]] = None

# --- Endpoints ---
@router.get("/health")
def health():
    """Endpoint para verificar que la API está funcionando."""
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

@router.get("/menu/products")
def get_menu_products():
    """Endpoint para obtener todos los productos del menú."""
    return {"products": get_all_products()}

@router.get("/menu/products/category/{category}")
def get_category_products(category: str):
    """Endpoint para obtener productos por categoría."""
    products = get_products_by_category(category)
    return {"category": category, "products": products}

@router.get("/menu/search")
def search_menu(q: str):
    """Endpoint para buscar productos en el menú."""
    results = search_products(q)
    return {"query": q, "results": results, "count": len(results)}

@router.post("/predict")
def predict_endpoint(req: PredictRequest):
    """Endpoint para hacer predicciones basadas en la hora del día."""
    result = predict(req.features)
    return {"prediction": result}

@router.post("/chat/user")
def chat_user_endpoint(req: ChatUserRequest):
    """Endpoint para el chatbot del cliente."""
    # Si no se proporciona contexto del menú, usamos todos los productos
    menu_context = req.menu_context or {"items": get_all_products()}
    response = agent.chat_user(req.message, menu_context)
    return {"response": response}

@router.post("/chat/restaurant")
def chat_restaurant_endpoint(req: ChatRestaurantRequest):
    """Endpoint para el chatbot del restaurante."""
    result = agent.chat_restaurant(req.message, req.prediction_data)
    return result
