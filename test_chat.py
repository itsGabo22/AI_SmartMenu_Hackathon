import requests
import json

def test_chat(message):
    url = "http://127.0.0.1:8000/api/chat/"
    data = {"message": message}
    response = requests.post(url, json=data)
    return response.json()

# Ejemplos de preguntas para probar
preguntas = [
    "Hola, ¿qué restaurantes me recomiendas?",
    "¿Cuáles son los restaurantes más rápidos?",
    "Busca restaurantes de comida italiana",
    "¿Qué restaurantes tienen mejor calificación?",
    "Recomiéndame algo de comida japonesa"
]

for pregunta in preguntas:
    print(f"\nTú: {pregunta}")
    respuesta = test_chat(pregunta)
    print(f"Bot: {respuesta.get('response', 'No se pudo obtener respuesta')}")