"""Dashboard interactivo dual para AI SmartMenu - Diseño tipo Rappi."""
import streamlit as st
import requests
from src.core.config import API_URL
from src.data.products import get_all_products, get_products_by_category, search_products

# --- Configuración de la Página ---
st.set_page_config(page_title="SmartMenu", page_icon="🍽️", layout="wide")

# --- Estilos CSS Personalizados (Diseño Rappi Premium) ---
st.markdown("""
<style>
    /* Colores principales - Paleta Rappi */
    :root {
        --primary-orange: #FF6B35;
        --dark-orange: #FF5722;
        --light-bg: #FFFFFF;
        --gray-light: #F5F5F5;
        --gray-medium: #E8E8E8;
        --gray-dark: #333333;
        --text-primary: #2C3E50;
        --text-secondary: #7F8C8D;
    }
    
    /* Fondo general */
    .stApp {
        background-color: #FFFFFF;
    }
    
    /* Botones naranjas con efectos Rappi */
    .stButton > button {
        background-color: #FF6B35 !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 14px 28px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(255, 107, 53, 0.2) !important;
    }
    
    .stButton > button:hover {
        background-color: #FF5722 !important;
        box-shadow: 0 6px 20px rgba(255, 107, 53, 0.4) !important;
        transform: translateY(-3px) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    
    /* Headers con estilo Rappi */
    h1, h2, h3 {
        color: #333333 !important;
        font-weight: 700 !important;
    }
    
    h1 {
        border-bottom: 3px solid #FF6B35 !important;
        padding-bottom: 12px !important;
        margin-bottom: 20px !important;
    }
    
    h2 {
        margin-top: 24px !important;
        margin-bottom: 16px !important;
    }
    
    /* Header gradient - texto oscuro */
    .stApp > header {
        background-color: transparent !important;
    }
    
    /* Asegurar contraste en header naranja */
    .header-gradient {
        color: #333333 !important;
    }
    
    .header-gradient h1 {
        color: #333333 !important;
        border: none !important;
    }
    
    .header-gradient p {
        color: #333333 !important;
    }
    
    /* Grid de categorías - Estilo Rappi */
    .category-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin: 20px 0;
    }
    
    .category-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-items: center;
        padding: 16px 12px;
        border-radius: 12px;
        text-align: center;
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
    }
    
    .category-item:hover {
        transform: translateY(-4px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    .category-desayuno { background-color: #FDE5D0; }
    .category-almuerzo { background-color: #F2FEAE; }
    .category-merienda { background-color: #FEE9C6; }
    .category-cena { background-color: #D3E9FF; }
    
    /* Tarjetas de productos */
    .product-card {
        background-color: #F9F9F9;
        border-radius: 12px;
        padding: 16px;
        margin: 12px 0;
        border: 1px solid #E8E8E8;
        border-left: 4px solid #FF6B35;
        transition: all 0.3s ease;
    }
    
    .product-card:hover {
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
        transform: translateY(-2px);
        border-left-width: 6px;
    }
    
    .product-title {
        font-weight: 700;
        color: #333333;
        font-size: 16px;
        margin-bottom: 6px;
    }
    
    .product-description {
        color: #666666;
        font-size: 13px;
        margin-bottom: 10px;
        line-height: 1.4;
    }
    
    .product-badges {
        display: flex;
        gap: 8px;
        margin-bottom: 10px;
        flex-wrap: wrap;
    }
    
    /* Chat messages */
    .chat-message {
        padding: 12px 16px;
        border-radius: 8px;
        margin: 10px 0;
        line-height: 1.5;
    }
    
    .chat-user {
        background-color: #FF6B35;
        color: white;
        border-radius: 16px 16px 4px 16px;
        margin-left: 20px;
        box-shadow: 0 2px 6px rgba(255, 107, 53, 0.2);
    }
    
    .chat-assistant {
        background-color: #F0F0F0;
        color: #333333;
        border-radius: 16px 16px 16px 4px;
        margin-right: 20px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border: 2px solid #E8E8E8 !important;
        border-radius: 12px !important;
        padding: 12px 14px !important;
        font-size: 14px !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border: 2px solid #FF6B35 !important;
        box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.1) !important;
    }
    
    /* Tabs - Estilo Rappi */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 2px solid #E8E8E8;
    }
    
    .stTabs [data-baseweb="tab-list"] button {
        color: #7F8C8D !important;
        border-bottom: 3px solid transparent !important;
        border-radius: 0 !important;
        font-weight: 600 !important;
        padding: 12px 16px !important;
        transition: all 0.3s ease !important;
    }
    
    .stTabs [aria-selected="true"] {
        color: #FF6B35 !important;
        border-bottom: 3px solid #FF6B35 !important;
    }
    
    /* Selectores */
    .stSelectbox > div > div {
        border: 2px solid #E8E8E8 !important;
        border-radius: 12px !important;
    }
    
    .stSelectbox > div > div:focus-within {
        border: 2px solid #FF6B35 !important;
    }
    
    /* Separadores */
    hr {
        border-color: #E8E8E8 !important;
        margin: 20px 0 !important;
    }
    
    /* Badges/Labels */
    .badge {
        background-color: #FF6B35;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 2px 6px rgba(255, 107, 53, 0.2);
    }
    
    .badge-secondary {
        background-color: #E8E8E8;
        color: #333333;
    }
    
    /* Contenedor principal */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* Panel de control */
    .control-panel {
        background: linear-gradient(135deg, #FF6B35 0%, #FF5722 100%);
        padding: 20px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(255, 107, 53, 0.2);
    }
    
    .control-panel h2 {
        color: white !important;
        border: none !important;
        margin-top: 0 !important;
    }
    
    .control-panel p {
        color: rgba(255, 255, 255, 0.9);
    }
    
    .price-badge {
        background-color: #4CAF50;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- Funciones de Inicialización y Ayuda ---
def initialize_session():
    """Inicializa las variables de estado de la sesión."""
    if 'user_role' not in st.session_state:
        st.session_state.user_role = "👤 Cliente"
    if 'chat_history_user' not in st.session_state:
        st.session_state.chat_history_user = []
    if 'chat_history_restaurant' not in st.session_state:
        st.session_state.chat_history_restaurant = []
    if 'last_prediction' not in st.session_state:
        st.session_state.last_prediction = None

def api_request(method, endpoint, **kwargs):
    """Función central para hacer peticiones a la API."""
    try:
        url = f"{API_URL}/api{endpoint}"
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error de conexión con la API: {e}")
        return None

# --- Funciones de Utilidad ---
def render_product_card(product):
    """Renderiza una tarjeta de producto con diseño premium Rappi."""
    st.markdown(f"""
    <div style='
        background-color: #F9F9F9;
        border: 1px solid #E8E8E8;
        border-left: 4px solid #FF6B35;
        border-radius: 12px;
        padding: 16px;
        margin: 12px 0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
    '>
        <div style='display: flex; justify-content: space-between; align-items: start;'>
            <div style='flex: 1;'>
                <h4 style='color: #333333; margin: 0 0 6px 0; font-size: 16px; font-weight: 700;'>
                    {product['name']}
                </h4>
                <p style='color: #666666; margin: 0 0 10px 0; font-size: 13px; line-height: 1.4;'>
                    {product['description']}
                </p>
                <div style='display: flex; gap: 8px; flex-wrap: wrap;'>
                    <span style='background-color: #FF6B35; color: white; padding: 6px 12px; border-radius: 20px; 
                    font-size: 12px; font-weight: 600; box-shadow: 0 2px 6px rgba(255, 107, 53, 0.2);'>
                        ⏱️ {product['prep_time']}min
                    </span>
                    <span style='background-color: #FF6B35; color: white; padding: 6px 12px; border-radius: 20px; 
                    font-size: 12px; font-weight: 600; box-shadow: 0 2px 6px rgba(255, 107, 53, 0.2);'>
                        🔥 {product['calories']}kcal
                    </span>
                    <span style='background-color: #4CAF50; color: white; padding: 6px 12px; border-radius: 20px; 
                    font-size: 12px; font-weight: 600; box-shadow: 0 2px 6px rgba(76, 175, 80, 0.2);'>
                        $ {product['price']:.2f}
                    </span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()

# --- Interfaces de Usuario ---
def show_user_interface():
    """Muestra la interfaz para el cliente (estilo Rappi)."""
    
    # Header atractivo
    st.markdown("""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #FF6B35, #FF5722); border-radius: 12px; color: #333333; margin-bottom: 20px;'>
        <h1 style='color: #333333; margin: 0;'>SmartMenu</h1>
        <p style='margin: 5px 0 0 0; color: #333333;'>Descubre los mejores platos con nuestro asistente inteligente</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs para diferentes secciones
    tab1, tab2, tab3 = st.tabs(["Conversa con IA", "Menú Completo", "Buscar"])
    
    with tab1:
        st.subheader("Asistente Inteligente")
        st.markdown('<p style="color:#333333;">Conversa conmigo para encontrar el plato perfecto para ti</p>', unsafe_allow_html=True)
        
        # Contenedor de chat
        chat_container = st.container(height=400)
        with chat_container:
            for msg in st.session_state.chat_history_user:
                if msg["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message chat-user" style='text-align: right;'>
                        {msg['content']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message chat-assistant">
                        {msg['content']}
                    </div>
                    """, unsafe_allow_html=True)
        
        st.divider()
        
        # Input del usuario
        col1, col2 = st.columns([4, 1])
        with col1:
            prompt = st.text_input("¿Qué te apetece hoy?", placeholder="Ej: Algo saludable y rápido...")
        with col2:
            send_button = st.button("Enviar", use_container_width=True)
        
        if send_button and prompt:
            st.session_state.chat_history_user.append({"role": "user", "content": prompt})

            payload = {"message": prompt, "menu_context": {"items": get_all_products()}}
            response_data = api_request("post", "/chat/user", json=payload)
            
            if response_data:
                response = response_data.get("response", "Lo siento, no pude procesar tu solicitud.")
                st.session_state.chat_history_user.append({"role": "assistant", "content": response})
                st.rerun()
    
    with tab2:
        st.subheader("Nuestro Menú Completo")
        
        # Grid de categorías estilo Rappi
        if 'selected_category' not in st.session_state:
            st.session_state.selected_category = "almuerzo"
        
        st.markdown("""
        <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 20px 0;'>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        categories_info = [
            ("desayuno", "Desayuno", "#FDE5D0"),
            ("almuerzo", "Almuerzo", "#F2FEAE"),
            ("merienda", "Merienda", "#FEE9C6"),
            ("cena", "Cena", "#D3E9FF")
        ]
        
        cols = [col1, col2, col3, col4]
        for (cat_id, cat_name, cat_color), col in zip(categories_info, cols):
            with col:
                st.markdown(f"""
                <div style='background-color: {cat_color}; padding: 16px 12px; border-radius: 12px; 
                text-align: center; font-weight: 600; color: #333333; cursor: pointer; 
                transition: all 0.3s ease; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);'>
                    {cat_name}
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Ver {cat_name}", use_container_width=True, key=f"cat_{cat_id}"):
                    st.session_state.selected_category = cat_id
                    st.rerun()
        
        st.divider()
        
        products = get_products_by_category(st.session_state.selected_category)
        
        if products:
            st.markdown(f"### {len(products)} Platos Disponibles en {st.session_state.selected_category.title()}")
            for product in products:
                render_product_card(product)
    
    with tab3:
        st.subheader("Buscar en el Menú")
        search_query = st.text_input("Escribe el nombre o ingrediente que buscas...", placeholder="Ej: pizza, salmón, saludable...")
        
        if search_query and len(search_query) >= 2:
            results = search_products(search_query)
            
            if results:
                st.success(f"Se encontraron {len(results)} resultados")
                for product in results:
                    render_product_card(product)
            else:
                st.info("No se encontraron productos con ese término. Intenta con otras palabras.")

def show_restaurant_interface():
    """Muestra la interfaz para el gerente del restaurante."""
    
    # Header del restaurante
    st.markdown("""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #FF6B35, #FF5722); border-radius: 12px; color: #333333; margin-bottom: 20px;'>
        <h1 style='color: #333333; margin: 0;'>Panel de Control</h1>
        <p style='margin: 5px 0 0 0; color: #333333;'>Gestiona tu restaurante con inteligencia</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sección de predicción
    st.subheader("Predicción de Demanda")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        hour = st.slider("Selecciona una hora para predecir:", 0, 23, 19, label_visibility="collapsed")
    with col2:
        if st.button("Predecir", use_container_width=True):
            payload = {"features": {"hour": hour}}
            response_data = api_request("post", "/predict", json=payload)
            if response_data:
                st.session_state.last_prediction = response_data.get("prediction")
                st.success("Predicción generada!")

    # Mostrar la predicción actual
    if st.session_state.last_prediction:
        pred = st.session_state.last_prediction
        st.divider()
        
        st.markdown("""
        <div style='
            background: linear-gradient(135deg, #FF6B35 0%, #FF5722 100%);
            padding: 20px;
            border-radius: 12px;
            color: white;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(255, 107, 53, 0.2);
        '>
            <h3 style='color: white; border: none; margin-top: 0;'>Análisis Predictor</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Hora", f"{pred.get('hora_prediccion', 'N/A')}:00")
        with col2:
            st.metric("Producto Estrella", pred.get('producto_estrella', 'N/A'))
        with col3:
            demanda = pred.get('demanda', 'N/A')
            st.metric("Demanda", demanda.capitalize())
        with col4:
            st.metric("Unidades Est.", f"~{int(pred.get('cantidad_estimada', 0))}")
    
    st.divider()

    # Vista de inventario
    st.subheader("Inventario de Productos")
    
    categories = ["desayuno", "almuerzo", "merienda", "cena"]
    for category in categories:
        with st.expander(f"{category.upper()}", expanded=(category == "almuerzo")):
            products = get_products_by_category(category)
            
            if products:
                for product in products:
                    render_product_card(product)
    st.divider()

    # Chat para el restaurante
    st.subheader("Asesor de Operaciones IA")
    st.write("Consulta a tu asistente IA sobre operaciones del restaurante")
    
    # Contenedor de chat
    chat_container = st.container(height=300)
    with chat_container:
        for msg in st.session_state.chat_history_restaurant:
            if msg["role"] == "user":
                st.markdown(f"""
                <div style='
                    background-color: #FF6B35;
                    color: white;
                    padding: 12px 16px;
                    border-radius: 16px 16px 4px 16px;
                    margin: 10px 0;
                    margin-left: 20px;
                    box-shadow: 0 2px 6px rgba(255, 107, 53, 0.2);
                '>
                    {msg['content']}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style='
                    background-color: #F0F0F0;
                    color: #333333;
                    padding: 12px 16px;
                    border-radius: 16px 16px 16px 4px;
                    margin: 10px 0;
                    margin-right: 20px;
                    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
                '>
                    {msg['content']}
                </div>
                """, unsafe_allow_html=True)
    
    st.divider()
    
    # Input del asesor
    col1, col2 = st.columns([4, 1])
    with col1:
        prompt = st.text_input("Consulta a tu asesor...", placeholder="Ej: ¿Cuántas hamburguesas debo preparar?", key="rest_input")
    with col2:
        send_button = st.button("Enviar", use_container_width=True, key="restaurant_send")
    
    if send_button and prompt:
        st.session_state.chat_history_restaurant.append({"role": "user", "content": prompt})

        payload = {"message": prompt, "prediction_data": st.session_state.last_prediction}
        response_data = api_request("post", "/chat/restaurant", json=payload)
        
        if response_data:
            response = response_data.get("response", "No pude generar una recomendación.")
            st.session_state.chat_history_restaurant.append({"role": "assistant", "content": response})
            st.rerun()

# --- Aplicación Principal ---
def main():
    initialize_session()
    
    # Selector de rol en el sidebar
    st.sidebar.markdown("### Selecciona tu rol")
    role = st.sidebar.radio("", ["Cliente", "Restaurante"], label_visibility="collapsed")
    st.session_state.user_role = role
    
    st.sidebar.divider()
    st.sidebar.markdown("""
    **SmartMenu v1.0**
    
    Sistema inteligente para restaurantes
    impulsado por IA
    """)
    
    if st.session_state.user_role == "Cliente":
        show_user_interface()
    else:
        show_restaurant_interface()

if __name__ == "__main__":
    main()
