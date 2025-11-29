"""Agente de IA Inteligente para SmartMenu con OpenAI SDK."""
import os
import sys
from typing import Dict, Any, Optional, List
from dotenv import load_dotenv
from src.data.products import get_all_products, search_products

# Cargar .env desde la raíz del proyecto
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
env_path = os.path.join(project_root, '.env')
load_dotenv(env_path)

OPENAI_AVAILABLE = False
openai_client = None

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    print("⚠️ OpenAI SDK no está disponible. Instala con: pip install openai")
    pass


class SmartMenuAgent:
    """Agente conversacional inteligente con OpenAI SDK."""
    
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.use_openai = OPENAI_AVAILABLE and bool(api_key)
        self.user_chat_history: List[Dict[str, str]] = []
        self.restaurant_chat_history: List[Dict[str, str]] = []
        self.client = None
        self.all_products = get_all_products()
        
        print(f"🔧 Cargando agente...")
        print(f"   Ruta .env: {env_path}")
        print(f"   .env existe: {os.path.exists(env_path)}")
        print(f"   API Key presente: {bool(api_key)}")
        print(f"   OpenAI disponible: {OPENAI_AVAILABLE}")
        
        if self.use_openai:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=api_key)
                print("✅ Agente iniciado con OpenAI GPT-3.5-turbo")
            except Exception as e:
                print(f"❌ Error inicializando OpenAI: {e}")
                print(f"   Verifica que OPENAI_API_KEY esté configurado correctamente en .env")
                self.use_openai = False
        else:
            if not api_key:
                print("⚠️ OPENAI_API_KEY no encontrado en .env")
            if not OPENAI_AVAILABLE:
                print("⚠️ OpenAI SDK no está disponible")
            print("✅ Agente iniciado en modo local inteligente")

    def _get_context_for_user(self) -> str:
        """Crea un contexto con información del menú para el agente."""
        products_info = ""
        for product in self.all_products[:10]:  # Primeros 10 productos
            products_info += f"- {product['name']}: ${product['price']} ({product['prep_time']}min, {product['calories']}kcal)\n"
        
        return f"""Eres un asistente amigable de restaurante experto en recomendar platos.
Tienes acceso a este menú:

{products_info}

Cuando el cliente pregunte:
- Sé amigable, entusiasta y personalizado
- Recomienda basándote en sus preferencias explícitas
- Incluye precios, tiempo de preparación y calorías
- Sugiere combinaciones complementarias
- Si piden algo específico, busca opciones similares

Responde siempre en español, de forma conversacional y natural."""

    def _get_context_for_restaurant(self) -> str:
        """Crea un contexto para el asesor del restaurante."""
        return """Eres un asesor experto en operaciones de restaurantes.
Tu tono es profesional, directo y basado en datos.
Cuando el gerente pregunte:
- Proporciona recomendaciones operativas prácticas
- Analiza datos de demanda y predicciones
- Sugiere acciones concretas para mejorar eficiencia
- Considera costo-beneficio
- Proporciona insights sobre gestión del personal y stock

Responde siempre en español, de forma clara y accionable."""

    def chat_user(self, user_message: str, menu_context: Optional[Dict] = None) -> str:
        """Chat para clientes con OpenAI."""
        print(f"\n📝 chat_user llamado")
        print(f"   use_openai: {self.use_openai}")
        print(f"   client exists: {self.client is not None}")
        
        if self.use_openai and self.client is not None:
            try:
                print(f"   ➜ Usando OpenAI (gpt-3.5-turbo)")
                # Construir historial de mensajes
                messages: List[Dict[str, str]] = [
                    {
                        "role": "system",
                        "content": self._get_context_for_user()
                    }
                ]
                
                # Añadir historial reciente
                for msg in self.user_chat_history[-6:]:
                    messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })
                
                # Añadir mensaje actual
                messages.append({
                    "role": "user",
                    "content": user_message
                })
                
                print(f"   📤 Enviando a OpenAI con {len(messages)} mensajes")
                # Invocar OpenAI
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,  # type: ignore
                    temperature=0.7,
                    max_tokens=500
                )
                result = (response.choices[0].message.content or "").strip()
                print(f"   ✅ Respuesta de OpenAI recibida ({len(result)} chars)")
                
                # Guardar en historial
                self.user_chat_history.append({"role": "user", "content": user_message})
                self.user_chat_history.append({"role": "assistant", "content": result})
                
                return result
            except Exception as e:
                error_msg = str(e)
                print(f"   ❌ Error con OpenAI: {error_msg}")
                if "insufficient_quota" in error_msg or "429" in error_msg:
                    print(f"   ⚠️  Tu cuenta OpenAI ha agotado la cuota.")
                    print(f"   📋 Visita: https://platform.openai.com/account/billing/overview")
                # Fallback a modo local
                print(f"   ➜ Fallback a modo local")
                return self._chat_local_user(user_message)
        else:
            # Modo local si no hay OpenAI
            print(f"   ➜ Usando modo local (use_openai={self.use_openai}, client={self.client})")
            return self._chat_local_user(user_message)

    def _chat_local_user(self, user_message: str) -> str:
        """Chat local inteligente para clientes."""
        msg_lower = user_message.lower()
        
        # Saludos
        if any(word in msg_lower for word in ["hola", "buenos", "buenas", "hi", "hey"]):
            response = "¡Hola! 👋 Bienvenido a nuestro restaurante. ¿Qué tipo de comida te apetece hoy? Tenemos opciones deliciosas para todos los gustos. 😊"
        
        # Búsqueda específica de productos
        elif "qué" in msg_lower or "recomienda" in msg_lower or "sugiere" in msg_lower:
            products = self._find_relevant_products(user_message)
            response = self._generate_smart_recommendation(products, user_message)
        
        # Búsqueda por precio
        elif "precio" in msg_lower or "barato" in msg_lower or "caro" in msg_lower:
            products = self._find_relevant_products(user_message)
            response = self._recommend_by_price(products, msg_lower)
        
        # Búsqueda por salud
        elif "saludable" in msg_lower or "sano" in msg_lower or "ligero" in msg_lower:
            products = self._find_relevant_products(user_message)
            response = self._recommend_healthiest(products)
        
        # Búsqueda por velocidad
        elif "rápido" in msg_lower or "rápida" in msg_lower or "prisa" in msg_lower:
            products = self._find_relevant_products(user_message)
            response = self._recommend_fastest(products)
        
        else:
            # Buscar y describir
            products = search_products(user_message)
            if products:
                response = self._describe_product_detailed(products[0])
            else:
                response = f"Estoy buscando opciones para '{user_message}'... 🔍\n\nNuestros platos más populares son: Hamburguesa Clásica, Ensalada César, Salmón a la Parrilla.\n\n¿Alguno de estos te llama la atención?"
        
        self.user_chat_history.append({"role": "user", "content": user_message})
        self.user_chat_history.append({"role": "assistant", "content": response})
        
        return response

    def _find_relevant_products(self, query: str, limit: int = 5) -> List[Dict]:
        """Busca productos relevantes."""
        query_lower = query.lower()
        
        # Búsqueda directa
        direct = search_products(query)
        if direct:
            return direct[:limit]
        
        # Búsqueda por palabra clave
        keywords = {
            "desayuno": ["café", "huevos", "pancakes"],
            "almuerzo": ["hamburguesa", "ensalada", "pizza", "sándwich"],
            "merienda": ["torta", "frappuccino", "brownie"],
            "cena": ["salmón", "carne", "pasta"],
            "saludable": ["ensalada", "salmón"],
            "rápido": ["hamburguesa", "sándwich"],
        }
        
        for keyword, products_ids in keywords.items():
            if keyword in query_lower:
                relevant = [p for p in self.all_products 
                           if any(pid in p.get("name", "").lower() for pid in products_ids)]
                if relevant:
                    return relevant[:limit]
        
        return self.all_products[:limit]

    def _generate_smart_recommendation(self, products: List[Dict], user_msg: str) -> str:
        """Genera recomendación inteligente."""
        if not products:
            return "Disculpa, no encuentro ese producto. ¿Qué tipo de comida prefieres?"
        
        best = products[0]
        response = f"🌟 **Mi recomendación: {best['name']}**\n\n"
        response += f"{best['description']}\n\n"
        response += f"💰 ${best['price']:.2f} | ⏱️ {best['prep_time']} min | 🔥 {best['calories']} kcal\n"
        response += f"🥘 Con: {', '.join(best['ingredients'][:3])}\n"
        
        if len(products) > 1:
            response += f"\n📌 También te recomendaría: **{products[1]['name']}** (${products[1]['price']:.2f})"
        
        response += "\n\n¿Quieres algo más?"
        return response

    def _recommend_by_price(self, products: List[Dict], msg: str) -> str:
        """Recomienda por precio."""
        sorted_products = sorted(products, key=lambda x: x.get("price", 999))
        best = sorted_products[0]
        
        response = f"💰 **Opción económica: {best['name']}**\n"
        response += f"Precio: ${best['price']:.2f}\n"
        response += f"{best['description']}\n"
        response += f"⏱️ {best['prep_time']} min | 🔥 {best['calories']} kcal"
        
        return response

    def _recommend_healthiest(self, products: List[Dict]) -> str:
        """Recomienda lo más saludable."""
        sorted_products = sorted(products, key=lambda x: x.get("calories", 999))
        best = sorted_products[0]
        
        response = f"🥗 **Opción más saludable: {best['name']}**\n\n"
        response += f"{best['description']}\n"
        response += f"🔥 {best['calories']} kcal | 💰 ${best['price']:.2f} | ⏱️ {best['prep_time']} min"
        
        return response

    def _recommend_fastest(self, products: List[Dict]) -> str:
        """Recomienda lo más rápido."""
        sorted_products = sorted(products, key=lambda x: x.get("prep_time", 999))
        best = sorted_products[0]
        
        response = f"⚡ **La más rápida: {best['name']}**\n"
        response += f"Tiempo: {best['prep_time']} minutos\n"
        response += f"{best['description']}\n"
        response += f"💰 ${best['price']:.2f}"
        
        return response

    def _describe_product_detailed(self, product: Dict) -> str:
        """Describe un producto en detalle."""
        response = f"**{product['name']}** ✨\n\n"
        response += f"📝 {product['description']}\n\n"
        response += f"💰 Precio: ${product['price']:.2f}\n"
        response += f"⏱️ Tiempo de preparación: {product['prep_time']} minutos\n"
        response += f"🔥 Calorías: {product['calories']} kcal\n"
        response += f"🥘 Ingredientes: {', '.join(product['ingredients'])}\n"
        
        return response

    def chat_restaurant(self, user_message: str, prediction_data: Optional[Dict] = None) -> Dict[str, Any]:
        """Chat para gerentes con OpenAI."""
        print(f"\n📝 chat_restaurant llamado")
        print(f"   use_openai: {self.use_openai}")
        print(f"   client exists: {self.client is not None}")
        
        if self.use_openai and self.client is not None:
            try:
                print(f"   ➜ Usando OpenAI (gpt-3.5-turbo)")
                # Incluir datos de predicción en el contexto
                context = self._get_context_for_restaurant()
                if prediction_data:
                    context += f"\n\nDatos actuales de predicción:\n"
                    context += f"- Producto estrella: {prediction_data.get('producto_estrella', 'N/A')}\n"
                    context += f"- Demanda: {prediction_data.get('demanda', 'N/A')}\n"
                    context += f"- Cantidad estimada: {prediction_data.get('cantidad_estimada', 'N/A')}\n"
                
                messages: List[Dict[str, str]] = [
                    {
                        "role": "system",
                        "content": context
                    }
                ]
                
                # Historial
                for msg in self.restaurant_chat_history[-6:]:
                    messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })
                
                messages.append({
                    "role": "user",
                    "content": user_message
                })
                
                print(f"   📤 Enviando a OpenAI con {len(messages)} mensajes")
                # Invocar OpenAI
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,  # type: ignore
                    temperature=0.5,
                    max_tokens=600
                )
                result = (response.choices[0].message.content or "").strip()
                print(f"   ✅ Respuesta de OpenAI recibida ({len(result)} chars)")
                
                # Guardar
                self.restaurant_chat_history.append({"role": "user", "content": user_message})
                self.restaurant_chat_history.append({"role": "assistant", "content": result})
                
                return {"response": result}
            except Exception as e:
                error_msg = str(e)
                print(f"   ❌ Error con OpenAI: {error_msg}")
                if "insufficient_quota" in error_msg or "429" in error_msg:
                    print(f"   ⚠️  Tu cuenta OpenAI ha agotado la cuota.")
                    print(f"   📋 Visita: https://platform.openai.com/account/billing/overview")
                print(f"   ➜ Fallback a modo local")
                return self._chat_local_restaurant(user_message, prediction_data)
        else:
            print(f"   ➜ Usando modo local (use_openai={self.use_openai}, client={self.client})")
            return self._chat_local_restaurant(user_message, prediction_data)

    def _chat_local_restaurant(self, user_message: str, prediction_data: Optional[Dict] = None) -> Dict[str, Any]:
        """Chat local para restaurante."""
        msg_lower = user_message.lower()
        pred = prediction_data or {}
        producto = pred.get("producto_estrella", "N/A")
        demanda = pred.get("demanda", "desconocida")
        cantidad = pred.get("cantidad_estimada", 10)
        
        if any(word in msg_lower for word in ["preparar", "stock", "ingredientes", "cocina"]):
            response = (
                f"📦 **Plan de Preparación:**\n\n"
                f"Producto destacado: **{producto}**\n"
                f"Demanda predicha: **{demanda.upper()}**\n"
                f"Unidades proyectadas: **~{int(cantidad * 1.5)}**\n\n"
                f"✅ Acciones:\n"
                f"1. Pre-calienta la estación\n"
                f"2. Verifica {int(cantidad * 1.5)} porciones\n"
                f"3. Ten 5 extra listas\n"
            )
        else:
            response = (
                f"📊 **Estado operativo:**\n\n"
                f"Horario: {pred.get('hora_prediccion', '?')}:00\n"
                f"Producto trending: {producto}\n"
                f"Demanda: {demanda.upper()}\n"
                f"Proyección: {cantidad} unidades\n"
            )
        
        self.restaurant_chat_history.append({"role": "user", "content": user_message})
        self.restaurant_chat_history.append({"role": "assistant", "content": response})
        
        return {"response": response}


def create_agent() -> SmartMenuAgent:
    """Factory para crear una instancia del agente."""
    return SmartMenuAgent()
