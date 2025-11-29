from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json

@csrf_exempt
def get_restaurantes(request):
    if request.method == 'GET':
        try:
            with connection.cursor() as cursor:
                # Consulta para obtener solo los restaurantes (sin menú por ahora)
                query = """
                SELECT 
                    id,
                    nombre,
                    direccion,
                    telefono,
                    calificacion,
                    tiempo_entrega_promedio,
                    tipo_cocina,
                    costo_envio,
                    pedido_minimo
                FROM mi_app_restaurante
                WHERE activo = 1
                ORDER BY nombre
                """
                cursor.execute(query)
                columns = [col[0] for col in cursor.description]
                results = []
                
                for row in cursor.fetchall():
                    row_dict = dict(zip(columns, row))
                    restaurante = {
                        'id': row_dict['id'],
                        'nombre': row_dict['nombre'],
                        'direccion': row_dict['direccion'],
                        'telefono': row_dict['telefono'],
                        'calificacion': row_dict['calificacion'],
                        'tiempo_entrega': f"{row_dict['tiempo_entrega_promedio']} min" if row_dict['tiempo_entrega_promedio'] else '30-45 min',
                        'tipo_cocina': row_dict['tipo_cocina'] or 'Comida variada',
                        'costo_envio': f"₡{row_dict['costo_envio']:,}" if row_dict['costo_envio'] else 'Gratis',
                        'pedido_minimo': f"₡{row_dict['pedido_minimo']:,}" if row_dict['pedido_minimo'] else 'Sin mínimo',
                        'menu': []  # Menú vacío por ahora
                    }
                    results.append(restaurante)
                
                return JsonResponse({'restaurantes': results}, safe=False)
                
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método no permitido'}, status=405)