import os
import google.generativeai as genai
from django.conf import settings
from .models import Restaurante # Asumo que esta clase está definida en models.py

class ChatAssistant:
    def __init__(self):
        self.available = False
        self.model = None
        # Usamos gemini-2.5-flash como el modelo recomendado para aplicaciones de chat
        self.MODEL_NAME = 'gemini-2.5-flash' 
        try:
            print("Inicializando ChatAssistant...")
            print(f"GEMINI_API_KEY en settings: {getattr(settings, 'GEMINI_API_KEY', 'No encontrada')}")
            
            if not hasattr(settings, 'GEMINI_API_KEY') or not settings.GEMINI_API_KEY:
                print("ADVERTENCIA: No se encontró GEMINI_API_KEY en la configuración")
                return
                
            print("Configurando API de Gemini...")
            genai.configure(api_key=settings.GEMINI_API_KEY)
            
            # Intentar inicializar el modelo
            try:
                print(f"Intentando usar el modelo: {self.MODEL_NAME}")
                self.model = genai.GenerativeModel(self.MODEL_NAME)
                self.available = True
                print(f"✅ ChatAssistant inicializado correctamente con {self.MODEL_NAME}")
                
            except Exception as e:
                # Si falla, podemos intentar listar modelos o simplemente dejarlo como no disponible
                print(f"Error al inicializar el modelo {self.MODEL_NAME}: {str(e)}")
                # Opcional: Listar modelos solo si la inicialización falla para depuración
                try:
                    models = genai.list_models()
                    print("Modelos disponibles (solo nombres):")
                    for model in models:
                         print(f"- {model.name}")
                except Exception as e_list:
                    print(f"Error al listar modelos: {str(e_list)}")
                    
                import traceback
                print(traceback.format_exc())
                self.available = False
                
        except Exception as e:
            import traceback
            print(f"Error al inicializar ChatAssistant: {str(e)}")
            print("Traceback completo:")
            print(traceback.format_exc())

    def get_restaurant_context(self):
        """Obtiene información de restaurantes para el contexto"""
        try:
            # Usar .select_related() si hay relaciones, pero aquí simplificamos
            restaurantes = Restaurante.objects.all()[:10] 
            if not restaurantes.exists():
                return "No hay restaurantes disponibles en este momento."
                
            return "\n".join([
                f"- {r.nombre}: {r.tipo_cocina} ⭐{r.calificacion} | 🕒{r.tiempo_entrega_promedio}min | 📍{r.direccion}"
                for r in restaurantes
            ])
        except Exception as e:
            # Si falla la base de datos (PostgreSQL), esto lo capturará
            print(f"Error al obtener restaurantes: {str(e)}")
            return "No se pudo obtener la información de los restaurantes."

    def generate_response(self, user_message: str) -> str:
        try:
            if not self.available or not self.model:
                print("Modelo no disponible o no inicializado")
                # Intenta dar información de restaurantes aunque el modelo de IA no esté
                restaurantes_info = self.get_restaurant_context() 
                return ("Lo siento, el servicio de IA no está disponible en este momento. " +
                        "Aquí tienes algunos restaurantes disponibles:\n\n" + 
                        restaurantes_info)
            
            print("Generando respuesta con el modelo...")
            restaurantes_info = self.get_restaurant_context()
            print("Contexto de restaurantes obtenido:", restaurantes_info[:200] + "..." if restaurantes_info else "Ningún restaurante encontrado")
            
            prompt = f"""
            Ere un asistente virtual para un servicio de entrega de comida llamado "Rapid".
            Tu único objetivo es responder preguntas sobre los restaurantes disponibles o mantener una conversación.
            Tienes información sobre los siguientes restaurantes:
            
            {restaurantes_info}
            
            Usa esta información para responder preguntas sobre restaurantes.
            Si la pregunta es general (saludo, etc.), responde de forma natural.
            Si no tienes la información necesaria, sé honesto y di que no lo sabes, y sugiere ver la lista de restaurantes.
            
            Pregunta del usuario: {user_message}
            """
            
            print("Enviando prompt a la API de Gemini...")
            response = self.model.generate_content(prompt)
            print("Respuesta recibida correctamente")
            return response.text
            
        except Exception as e:
            import traceback
            print(f"Error al generar la respuesta: {str(e)}")
            print("Traceback completo:")
            print(traceback.format_exc())
            return "Lo siento, estoy teniendo problemas para responder. Por favor, inténtalo de nuevo más tarde."