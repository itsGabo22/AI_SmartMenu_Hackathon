"""Dataset expandido de productos del restaurante SmartMenu - 30 productos."""

MENU_PRODUCTS = {
    "desayuno": [
        {
            "id": "cafe_croissant",
            "name": "Café y Croissant",
            "description": "Café espresso con croissant recién horneado",
            "price": 5.99,
            "category": "Desayuno",
            "ingredients": ["café", "croissant", "mantequilla"],
            "prep_time": 5,
            "calories": 350
        },
        {
            "id": "huevos_revueltos",
            "name": "Huevos Revueltos con Tostadas",
            "description": "3 huevos revueltos con tostadas integrales y mermelada",
            "price": 7.99,
            "category": "Desayuno",
            "ingredients": ["huevos", "pan integral", "mantequilla", "mermelada"],
            "prep_time": 8,
            "calories": 420
        },
        {
            "id": "pancakes",
            "name": "Pancakes con Frutas",
            "description": "Stack de pancakes esponjosos con fresas, arándanos y miel",
            "price": 8.99,
            "category": "Desayuno",
            "ingredients": ["harina", "huevos", "leche", "fresas", "arándanos", "miel"],
            "prep_time": 10,
            "calories": 480
        },
        {
            "id": "omelet_queso_jamon",
            "name": "Omelet de Queso y Jamón",
            "description": "Omelet esponjoso relleno de queso fundido y jamón serrano",
            "price": 9.99,
            "category": "Desayuno",
            "ingredients": ["huevos", "queso", "jamón serrano", "mantequilla"],
            "prep_time": 8,
            "calories": 450
        },
        {
            "id": "yogur_granola",
            "name": "Yogur con Granola",
            "description": "Yogur griego cremoso con granola casera, miel y frutos secos",
            "price": 6.99,
            "category": "Desayuno",
            "ingredients": ["yogur griego", "granola", "miel", "almendras", "arándanos"],
            "prep_time": 2,
            "calories": 280
        },
        {
            "id": "bagel_salmon",
            "name": "Bagel de Salmón",
            "description": "Bagel tostado con salmón ahumado, queso crema y alcaparras",
            "price": 10.99,
            "category": "Desayuno",
            "ingredients": ["bagel", "salmón ahumado", "queso crema", "alcaparras", "cebolla"],
            "prep_time": 5,
            "calories": 380
        }
    ],
    "almuerzo": [
        {
            "id": "hamburguesa_clasica",
            "name": "Hamburguesa Clásica",
            "description": "Hamburguesa de carne 100% angus con queso cheddar y vegetales frescos",
            "price": 12.99,
            "category": "Almuerzo",
            "ingredients": ["carne angus", "queso cheddar", "lechuga", "tomate", "pan"],
            "prep_time": 12,
            "calories": 650
        },
        {
            "id": "hamburguesa_bbq",
            "name": "Hamburguesa BBQ",
            "description": "Hamburguesa con salsa BBQ casera, queso cheddar y tocino crujiente",
            "price": 14.99,
            "category": "Almuerzo",
            "ingredients": ["carne angus", "salsa BBQ", "queso cheddar", "tocino", "pan"],
            "prep_time": 13,
            "calories": 720
        },
        {
            "id": "ensalada_cesar",
            "name": "Ensalada César",
            "description": "Lechuga romana fresca con crutones, queso parmesano y aderezo césar",
            "price": 10.99,
            "category": "Almuerzo",
            "ingredients": ["lechuga romana", "crutones", "parmesano", "aderezo césar"],
            "prep_time": 8,
            "calories": 380
        },
        {
            "id": "ensalada_caprese",
            "name": "Ensalada Caprese",
            "description": "Tomate fresco, mozzarella tierna, albahaca y aceite de oliva premium",
            "price": 11.99,
            "category": "Almuerzo",
            "ingredients": ["tomate", "mozzarella fresca", "albahaca", "aceite de oliva"],
            "prep_time": 5,
            "calories": 290
        },
        {
            "id": "pizza_margarita",
            "name": "Pizza Margarita",
            "description": "Pizza artesanal con tomate, mozzarella fresca y albahaca",
            "price": 13.99,
            "category": "Almuerzo",
            "ingredients": ["masa", "salsa de tomate", "mozzarella", "albahaca"],
            "prep_time": 15,
            "calories": 720
        },
        {
            "id": "pizza_pepperoni",
            "name": "Pizza Pepperoni",
            "description": "Pizza con mozzarella, pepperoni y orégano italiano",
            "price": 14.99,
            "category": "Almuerzo",
            "ingredients": ["masa", "mozzarella", "pepperoni", "orégano"],
            "prep_time": 15,
            "calories": 780
        },
        {
            "id": "sandwich_pollo",
            "name": "Sándwich de Pollo",
            "description": "Filete de pollo a la parrilla con verduras frescas y mayonesa casera",
            "price": 11.99,
            "category": "Almuerzo",
            "ingredients": ["pechuga de pollo", "pan", "lechuga", "tomate", "mayonesa"],
            "prep_time": 10,
            "calories": 520
        },
        {
            "id": "tacos_pastor",
            "name": "Tacos al Pastor",
            "description": "Tres tacos de pollo marinado con piña, cebolla y cilantro fresco",
            "price": 12.99,
            "category": "Almuerzo",
            "ingredients": ["pollo", "tortilla", "piña", "cebolla", "cilantro"],
            "prep_time": 11,
            "calories": 580
        },
        {
            "id": "burrito_carne",
            "name": "Burrito de Carne",
            "description": "Burrito relleno de carne, arroz integral, frijoles negros y queso fundido",
            "price": 13.99,
            "category": "Almuerzo",
            "ingredients": ["tortilla", "carne", "arroz", "frijoles", "queso"],
            "prep_time": 12,
            "calories": 720
        }
    ],
    "merienda": [
        {
            "id": "torta_chocolate",
            "name": "Torta de Chocolate",
            "description": "Torta de chocolate belga con ganache y fresas frescas",
            "price": 5.99,
            "category": "Merienda",
            "ingredients": ["chocolate", "harina", "huevos", "leche", "fresas"],
            "prep_time": 2,
            "calories": 450
        },
        {
            "id": "cheesecake",
            "name": "Cheesecake",
            "description": "Cheesecake cremoso con salsa de frutas rojas casera",
            "price": 6.99,
            "category": "Merienda",
            "ingredients": ["queso crema", "galletas", "frutas rojas", "azúcar"],
            "prep_time": 2,
            "calories": 480
        },
        {
            "id": "frappuccino",
            "name": "Frappuccino de Vainilla",
            "description": "Bebida helada de café con leche y esencia de vainilla pura",
            "price": 5.49,
            "category": "Merienda",
            "ingredients": ["café", "leche", "hielo", "vainilla"],
            "prep_time": 5,
            "calories": 280
        },
        {
            "id": "cafe_latte_helado",
            "name": "Café Latte Helado",
            "description": "Café espresso con leche helada, hielo y caramelo",
            "price": 5.99,
            "category": "Merienda",
            "ingredients": ["café", "leche", "hielo", "caramelo"],
            "prep_time": 5,
            "calories": 240
        },
        {
            "id": "brownie",
            "name": "Brownie de Nueces",
            "description": "Brownie casero de chocolate con nueces tostadas",
            "price": 4.99,
            "category": "Merienda",
            "ingredients": ["chocolate", "harina", "huevos", "nueces"],
            "prep_time": 2,
            "calories": 380
        },
        {
            "id": "muffin_arandano",
            "name": "Muffin de Arándano",
            "description": "Muffin casero esponjoso con arándanos frescos",
            "price": 4.49,
            "category": "Merienda",
            "ingredients": ["harina", "huevos", "arándanos", "azúcar", "mantequilla"],
            "prep_time": 3,
            "calories": 340
        },
        {
            "id": "smoothie_fresa",
            "name": "Smoothie de Fresa",
            "description": "Smoothie refrescante de fresa, yogur, miel e hielo",
            "price": 6.49,
            "category": "Merienda",
            "ingredients": ["fresa", "yogur", "miel", "hielo"],
            "prep_time": 4,
            "calories": 220
        }
    ],
    "cena": [
        {
            "id": "salmon_parrilla",
            "name": "Salmón a la Parrilla",
            "description": "Filete de salmón salvaje a la parrilla con limón y hierbas aromáticas",
            "price": 18.99,
            "category": "Cena",
            "ingredients": ["salmón", "limón", "hierbas", "aceite de oliva"],
            "prep_time": 18,
            "calories": 550
        },
        {
            "id": "trucha_almendrada",
            "name": "Trucha Almendrada",
            "description": "Trucha fresca rellena de almendras con salsa de limón blanco",
            "price": 19.99,
            "category": "Cena",
            "ingredients": ["trucha", "almendras", "limón", "perejil", "mantequilla"],
            "prep_time": 18,
            "calories": 480
        },
        {
            "id": "camarones_ajillo",
            "name": "Camarones al Ajillo",
            "description": "Camarones frescos salteados con ajo, limón y perejil",
            "price": 17.99,
            "category": "Cena",
            "ingredients": ["camarones", "ajo", "limón", "perejil", "aceite de oliva"],
            "prep_time": 12,
            "calories": 320
        },
        {
            "id": "carne_asada",
            "name": "Carne Asada",
            "description": "Corte premium de carne de res asada con papas y verduras a la parrilla",
            "price": 22.99,
            "category": "Cena",
            "ingredients": ["carne premium", "papa", "espárrago", "champiñones"],
            "prep_time": 20,
            "calories": 780
        },
        {
            "id": "pechuga_pollo_rellena",
            "name": "Pechuga de Pollo Rellena",
            "description": "Pechuga de pollo rellena de queso y jamón con salsa de champiñones",
            "price": 16.99,
            "category": "Cena",
            "ingredients": ["pollo", "queso", "jamón", "champiñones", "salsa"],
            "prep_time": 16,
            "calories": 620
        },
        {
            "id": "pasta_bolognesa",
            "name": "Pasta a la Boloñesa",
            "description": "Pasta fresca casera con salsa de carne y queso parmesano rallado",
            "price": 14.99,
            "category": "Cena",
            "ingredients": ["pasta", "carne molida", "tomate", "queso parmesano"],
            "prep_time": 16,
            "calories": 650
        },
        {
            "id": "risotto_champinones",
            "name": "Risotto de Champiñones",
            "description": "Risotto cremoso con champiñones frescos, trufa y queso parmesano",
            "price": 15.99,
            "category": "Cena",
            "ingredients": ["arroz arborio", "champiñones", "caldo", "trufa", "parmesano"],
            "prep_time": 18,
            "calories": 520
        },
        {
            "id": "costillas_bbq",
            "name": "Costillas BBQ",
            "description": "Costillas a la parrilla con salsa BBQ casera y especias ahumadas",
            "price": 21.99,
            "category": "Cena",
            "ingredients": ["costillas", "salsa BBQ", "especias", "ahumado"],
            "prep_time": 22,
            "calories": 750
        }
    ]
}


def get_all_products():
    """Retorna todos los productos en formato de lista."""
    all_products = []
    for category, products in MENU_PRODUCTS.items():
        all_products.extend(products)
    return all_products


def get_products_by_category(category: str):
    """Retorna productos de una categoría específica."""
    category_lower = category.lower()
    if category_lower in MENU_PRODUCTS:
        return MENU_PRODUCTS[category_lower]
    return []


def get_product_by_id(product_id: str):
    """Busca un producto por su ID."""
    for products in MENU_PRODUCTS.values():
        for product in products:
            if product["id"] == product_id:
                return product
    return None


def search_products(query: str):
    """
    Busca productos por nombre, descripción o ingredientes.
    Retorna una lista ordenada por relevancia.
    """
    query_lower = query.lower()
    results = []
    
    for products in MENU_PRODUCTS.values():
        for product in products:
            # Buscar en nombre (mayor peso)
            if query_lower in product["name"].lower():
                results.append((product, 3))
                continue
            
            # Buscar en descripción (peso medio)
            if query_lower in product["description"].lower():
                results.append((product, 2))
                continue
            
            # Buscar en ingredientes (peso bajo)
            if any(query_lower in ingredient.lower() for ingredient in product["ingredients"]):
                results.append((product, 1))
    
    # Ordenar por relevancia (mayor peso primero)
    results.sort(key=lambda x: x[1], reverse=True)
    return [product for product, _ in results]
