"""Módulo de predicción de demanda."""
import pandas as pd
from pathlib import Path

def predict(features: dict) -> dict:
    """
    Predice la demanda de productos basándose en la hora.
    En una versión real, aquí iría un modelo de ML entrenado.
    """
    hour = features.get("hour", 12)
    
    # Lógica de negocio simple basada en franjas horarias
    if 6 <= hour < 11:
        producto = "Café y Croissant"
        demanda = "moderada"
        cantidad = 15
    elif 11 <= hour < 16:
        producto = "Ensalada César"
        demanda = "alta"
        cantidad = 25
    elif 16 <= hour < 19:
        producto = "Torta de Chocolate"
        demanda = "baja"
        cantidad = 10
    else:
        producto = "Hamburguesa Clásica"
        demanda = "muy alta"
        cantidad = 40
        
    return {
        "producto_estrella": producto,
        "demanda": demanda,
        "cantidad_estimada": cantidad,
        "hora_prediccion": hour
    }
