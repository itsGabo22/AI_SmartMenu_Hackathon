from django.core.management.base import BaseCommand
from mi_app.models import Restaurante
from datetime import time
# Se eliminó la importación de 'random' ya que no se utiliza

class Command(BaseCommand):
    help = 'Popula la base de datos con datos de ejemplo de restaurantes'

    def handle(self, *args, **kwargs):
        restaurantes = [
            {
                'nombre': 'La Buena Mesa',
                'tipo_cocina': 'Italiana',
                'tiempo_entrega_promedio': 35,
                'calificacion': 4.5,
                'direccion': 'Av. Principal 123, San José',
                'telefono': '22334455',
                'costo_envio': 1500.00,
                'pedido_minimo': 8000.00,
                'horario_apertura': time(11, 0),
                'horario_cierre': time(22, 0)
            },
            {
                'nombre': 'Sabor Oriental',
                'tipo_cocina': 'China',
                'tiempo_entrega_promedio': 25,
                'calificacion': 4.2,
                'direccion': 'Calle 5, San Pedro',
                'telefono': '22445566',
                'costo_envio': 1200.00,
                'pedido_minimo': 5000.00,
                'horario_apertura': time(10, 30),
                'horario_cierre': time(23, 0)
            },
            {
                'nombre': 'El Asadero',
                'tipo_cocina': 'Argentina',
                'tiempo_entrega_promedio': 40,
                'calificacion': 4.7,
                'direccion': 'Paseo Colón, San José',
                'telefono': '22556677',
                'costo_envio': 1800.00,
                'pedido_minimo': 10000.00,
                'horario_apertura': time(12, 0),
                'horario_cierre': time(23, 30)
            },
            {
                'nombre': 'Sushi Roll',
                'tipo_cocina': 'Japonesa',
                'tiempo_entrega_promedio': 30,
                'calificacion': 4.6,
                'direccion': 'Escazú Village, Escazú',
                'telefono': '22778899',
                'costo_envio': 2000.00,
                'pedido_minimo': 12000.00,
                'horario_apertura': time(11, 30),
                'horario_cierre': time(22, 30)
            },
            {
                'nombre': 'La Esquina de Tito',
                'tipo_cocina': 'Típica Costarricense',
                'tiempo_entrega_promedio': 20,
                'calificacion': 4.3,
                'direccion': 'Barrio Escalante, San José',
                'telefono': '22223344',
                'costo_envio': 1000.00,
                'pedido_minimo': 5000.00,
                'horario_apertura': time(7, 0),
                'horario_cierre': time(21, 0)
            },
            {
                'nombre': 'Parrillada El Gaucho',
                'tipo_cocina': 'Parrilla',
                'tiempo_entrega_promedio': 45,
                'calificacion': 4.4,
                'direccion': 'Curridabat, San José',
                'telefono': '22334455',
                'costo_envio': 2000.00,
                'pedido_minimo': 15000.00,
                'horario_apertura': time(11, 30),
                'horario_cierre': time(23, 0)
            }, # <--- ¡Aquí faltaba una coma! Ya fue añadida.
            {
                'nombre': 'Rincón La Esquina de Tito Familiar 1',
                'tipo_cocina': 'Caribeña',
                'tiempo_entrega_promedio': 19,
                'calificacion': 4.4,
                'direccion': 'Calle 79, Alajuela',
                'telefono': '22998877',
                'costo_envio': 1000.0,
                'pedido_minimo': 7000.0,
                'horario_apertura': time(7, 30),
                'horario_cierre': time(21, 30)
            },
            {
                'nombre': 'La Casona La Buena Mesa 2',
                'tipo_cocina': 'Americana',
                'tiempo_entrega_promedio': 32,
                'calificacion': 4.4,
                'direccion': 'Calle 28, Heredia',
                'telefono': '22112233',
                'costo_envio': 1500.0,
                'pedido_minimo': 11000.0,
                'horario_apertura': time(11, 30),
                'horario_cierre': time(22, 0)
            },
            {
                'nombre': 'Sabor Oriental Artesanal 3',
                'tipo_cocina': 'China',
                'tiempo_entrega_promedio': 26,
                'calificacion': 4.3,
                'direccion': 'Calle 55, Cartago',
                'telefono': '22554433',
                'costo_envio': 1400.0,
                'pedido_minimo': 5000.0,
                'horario_apertura': time(10, 0),
                'horario_cierre': time(23, 0)
            },
            {
                'nombre': 'El Asadero Gourmet 4',
                'tipo_cocina': 'Mexicana',
                'tiempo_entrega_promedio': 45,
                'calificacion': 4.5,
                'direccion': 'Calle 10, San José',
                'telefono': '22776655',
                'costo_envio': 2200.0,
                'pedido_minimo': 10000.0,
                'horario_apertura': time(11, 30),
                'horario_cierre': time(23, 0)
            },
            {
                'nombre': 'Delicioso Sushi Roll 5',
                'tipo_cocina': 'Japonesa',
                'tiempo_entrega_promedio': 33,
                'calificacion': 4.7,
                'direccion': 'Calle 92, Escazú',
                'telefono': '22887766',
                'costo_envio': 1800.0,
                'pedido_minimo': 9000.0,
                'horario_apertura': time(11, 30),
                'horario_cierre': time(22, 0)
            },
            {
                'nombre': 'El Gran La Esquina de Tito 6',
                'tipo_cocina': 'Típica Costarricense',
                'tiempo_entrega_promedio': 22,
                'calificacion': 4.5,
                'direccion': 'Calle 3, San Pedro',
                'telefono': '22665544',
                'costo_envio': 1300.0,
                'pedido_minimo': 5000.0,
                'horario_apertura': time(7, 0),
                'horario_cierre': time(20, 30)
            },
            {
                'nombre': 'Parrillada El Gaucho Internacional 7',
                'tipo_cocina': 'Parrilla',
                'tiempo_entrega_promedio': 41,
                'calificacion': 4.6,
                'direccion': 'Calle 40, Curridabat',
                'telefono': '22443322',
                'costo_envio': 1800.0,
                'pedido_minimo': 12000.0,
                'horario_apertura': time(12, 0),
                'horario_cierre': time(23, 0)
            },
            {
                'nombre': 'Aromas de La Buena Mesa 8',
                'tipo_cocina': 'Italiana',
                'tiempo_entrega_promedio': 30,
                'calificacion': 4.6,
                'direccion': 'Calle 12, Heredia',
                'telefono': '22556677',
                'costo_envio': 1700.0,
                'pedido_minimo': 8000.0,
                'horario_apertura': time(10, 30),
                'horario_cierre': time(21, 30)
            },
            {
                'nombre': 'Mundo Sabor Oriental 9',
                'tipo_cocina': 'Tailandesa',
                'tiempo_entrega_promedio': 25,
                'calificacion': 4.3,
                'direccion': 'Calle 80, San José',
                'telefono': '22778899',
                'costo_envio': 1500.0,
                'pedido_minimo': 6000.0,
                'horario_apertura': time(10, 0),
                'horario_cierre': time(23, 30)
            },
            {
                'nombre': 'El Asadero Artesanal 10',
                'tipo_cocina': 'Argentina',
                'tiempo_entrega_promedio': 38,
                'calificacion': 4.8,
                'direccion': 'Calle 25, Alajuela',
                'telefono': '22990011',
                'costo_envio': 2000.0,
                'pedido_minimo': 15000.0,
                'horario_apertura': time(12, 30),
                'horario_cierre': time(23, 30)
            },
            {
                'nombre': 'Fusión Sushi Roll Familiar 11',
                'tipo_cocina': 'Peruana',
                'tiempo_entrega_promedio': 27,
                'calificacion': 4.5,
                'direccion': 'Calle 7, Cartago',
                'telefono': '22113355',
                'costo_envio': 1900.0,
                'pedido_minimo': 12000.0,
                'horario_apertura': time(11, 0),
                'horario_cierre': time(22, 0)
            },
            {
                'nombre': 'La Esquina de Tito 24/7 12',
                'tipo_cocina': 'Española',
                'tiempo_entrega_promedio': 23,
                'calificacion': 4.2,
                'direccion': 'Calle 60, Escazú',
                'telefono': '22335577',
                'costo_envio': 1100.0,
                'pedido_minimo': 5000.0,
                'horario_apertura': time(7, 30),
                'horario_cierre': time(20, 30)
            },
            {
                'nombre': 'Rincón Parrillada El Gaucho 13',
                'tipo_cocina': 'Americana',
                'tiempo_entrega_promedio': 43,
                'calificacion': 4.5,
                'direccion': 'Calle 18, San Pedro',
                'telefono': '22557799',
                'costo_envio': 2200.0,
                'pedido_minimo': 14000.0,
                'horario_apertura': time(11, 30),
                'horario_cierre': time(22, 30)
            },
            {
                'nombre': 'Delicioso La Buena Mesa Tico 14',
                'tipo_cocina': 'Vegetariana',
                'tiempo_entrega_promedio': 34,
                'calificacion': 4.6,
                'direccion': 'Calle 45, Curridabat',
                'telefono': '22779911',
                'costo_envio': 1400.0,
                'pedido_minimo': 9000.0,
                'horario_apertura': time(11, 0),
                'horario_cierre': time(22, 30)
            },
            {
                'nombre': 'Sabor Oriental Gourmet 15',
                'tipo_cocina': 'China',
                'tiempo_entrega_promedio': 28,
                'calificacion': 4.4,
                'direccion': 'Calle 33, San José',
                'telefono': '22991133',
                'costo_envio': 1200.0,
                'pedido_minimo': 7000.0,
                'horario_apertura': time(10, 30),
                'horario_cierre': time(23, 0)
            },
            {
                'nombre': 'La Casona El Asadero Express 16',
                'tipo_cocina': 'Mexicana',
                'tiempo_entrega_promedio': 40,
                'calificacion': 4.7,
                'direccion': 'Calle 8, Heredia',
                'telefono': '22113355',
                'costo_envio': 1800.0,
                'pedido_minimo': 11000.0,
                'horario_apertura': time(12, 0),
                'horario_cierre': time(23, 30)
            },
            {
                'nombre': 'Mundo Sushi Roll 17',
                'tipo_cocina': 'Japonesa',
                'tiempo_entrega_promedio': 31,
                'calificacion': 4.5,
                'direccion': 'Calle 50, Alajuela',
                'telefono': '22335577',
                'costo_envio': 2100.0,
                'pedido_minimo': 10000.0,
                'horario_apertura': time(11, 0),
                'horario_cierre': time(22, 30)
            },
            {
                'nombre': 'El Gran La Esquina de Tito 18',
                'tipo_cocina': 'Típica Costarricense',
                'tiempo_entrega_promedio': 21,
                'calificacion': 4.3,
                'direccion': 'Calle 99, Cartago',
                'telefono': '22557799',
                'costo_envio': 1000.0,
                'pedido_minimo': 5000.0,
                'horario_apertura': time(6, 30),
                'horario_cierre': time(21, 0)
            },
            {
                'nombre': 'Parrillada El Gaucho Familiar 19',
                'tipo_cocina': 'Parrilla',
                'tiempo_entrega_promedio': 42,
                'calificacion': 4.6,
                'direccion': 'Calle 1, Escazú',
                'telefono': '22779911',
                'costo_envio': 2000.0,
                'pedido_minimo': 16000.0,
                'horario_apertura': time(12, 0),
                'horario_cierre': time(23, 30)
            },
            {
                'nombre': 'Aromas de La Buena Mesa Express 20',
                'tipo_cocina': 'Italiana',
                'tiempo_entrega_promedio': 36,
                'calificacion': 4.7,
                'direccion': 'Calle 70, San Pedro',
                'telefono': '22991133',
                'costo_envio': 1600.0,
                'pedido_minimo': 8000.0,
                'horario_apertura': time(11, 30),
                'horario_cierre': time(22, 0)
            },
            {
                'nombre': 'Rincón Sabor Oriental 21',
                'tipo_cocina': 'India',
                'tiempo_entrega_promedio': 24,
                'calificacion': 4.5,
                'direccion': 'Calle 15, Curridabat',
                'telefono': '22113355',
                'costo_envio': 1300.0,
                'pedido_minimo': 5000.0,
                'horario_apertura': time(10, 30),
                'horario_cierre': time(22, 30)
            },
            {
                'nombre': 'Delicioso El Asadero 22',
                'tipo_cocina': 'Argentina',
                'tiempo_entrega_promedio': 39,
                'calificacion': 4.8,
                'direccion': 'Calle 30, San José',
                'telefono': '22335577',
                'costo_envio': 1900.0,
                'pedido_minimo': 10000.0,
                'horario_apertura': time(11, 30),
                'horario_cierre': time(23, 0)
            },
            {
                'nombre': 'Sushi Roll Artesanal 23',
                'tipo_cocina': 'Japonesa',
                'tiempo_entrega_promedio': 30,
                'calificacion': 4.6,
                'direccion': 'Calle 88, Heredia',
                'telefono': '22557799',
                'costo_envio': 2000.0,
                'pedido_minimo': 13000.0,
                'horario_apertura': time(11, 30),
                'horario_cierre': time(22, 30)
            },
            {
                'nombre': 'La Casona La Esquina de Tito Tico 24',
                'tipo_cocina': 'Típica Costarricense',
                'tiempo_entrega_promedio': 18,
                'calificacion': 4.4,
                'direccion': 'Calle 5, Alajuela',
                'telefono': '22779911',
                'costo_envio': 1000.0,
                'pedido_minimo': 6000.0,
                'horario_apertura': time(7, 0),
                'horario_cierre': time(21, 30)
            },
            {
                'nombre': 'Parrillada El Gaucho Gourmet 25',
                'tipo_cocina': 'Caribeña',
                'tiempo_entrega_promedio': 46,
                'calificacion': 4.7,
                'direccion': 'Calle 100, Cartago',
                'telefono': '22991133',
                'costo_envio': 2300.0,
                'pedido_minimo': 15000.0,
                'horario_apertura': time(11, 0),
                'horario_cierre': time(23, 0)
            },
            {
                'nombre': 'Mundo La Buena Mesa 26',
                'tipo_cocina': 'Tailandesa',
                'tiempo_entrega_promedio': 32,
                'calificacion': 4.5,
                'direccion': 'Calle 22, Escazú',
                'telefono': '22113355',
                'costo_envio': 1500.0,
                'pedido_minimo': 9000.0,
                'horario_apertura': time(11, 0),
                'horario_cierre': time(22, 0)
            },
            {
                'nombre': 'El Gran Sabor Oriental Express 27',
                'tipo_cocina': 'China',
                'tiempo_entrega_promedio': 27,
                'calificacion': 4.3,
                'direccion': 'Calle 40, San Pedro',
                'telefono': '22335577',
                'costo_envio': 1200.0,
                'pedido_minimo': 5000.0,
                'horario_apertura': time(10, 0),
                'horario_cierre': time(23, 30)
            },
            {
                'nombre': 'Fusión El Asadero Internacional 28',
                'tipo_cocina': 'Peruana',
                'tiempo_entrega_promedio': 41,
                'calificacion': 4.6,
                'direccion': 'Calle 77, Curridabat',
                'telefono': '22557799',
                'costo_envio': 1800.0,
                'pedido_minimo': 12000.0,
                'horario_apertura': time(12, 30),
                'horario_cierre': time(23, 0)
            },
            {
                'nombre': 'Sushi Roll Tico 29',
                'tipo_cocina': 'Japonesa',
                'tiempo_entrega_promedio': 29,
                'calificacion': 4.4,
                'direccion': 'Calle 55, San José',
                'telefono': '22779911',
                'costo_envio': 1700.0,
                'pedido_minimo': 10000.0,
                'horario_apertura': time(11, 0),
                'horario_cierre': time(22, 30)
            },
            {
                'nombre': 'Aromas de La Esquina de Tito 30',
                'tipo_cocina': 'Típica Costarricense',
                'tiempo_entrega_promedio': 20,
                'calificacion': 4.5,
                'direccion': 'Calle 33, Heredia',
                'telefono': '22991133',
                'costo_envio': 1000.0,
                'pedido_minimo': 5000.0,
                'horario_apertura': time(7, 30),
                'horario_cierre': time(21, 0)
            }
        ]

        # Elimina todos los restaurantes existentes antes de poblar la base de datos (opcional, pero útil para datos de prueba limpios)
        # self.stdout.write(self.style.WARNING('Eliminando restaurantes existentes...'))
        # Restaurante.objects.all().delete()
        # self.stdout.write(self.style.SUCCESS('Restaurantes eliminados.'))

        for restaurante_data in restaurantes:
            restaurante, created = Restaurante.objects.get_or_create(
                # Usamos el nombre para verificar si ya existe
                nombre=restaurante_data['nombre'],
                defaults=restaurante_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Creado restaurante: {restaurante.nombre}'))
            else:
                # Opcionalmente, puedes actualizar los datos si ya existe, en lugar de solo advertir
                # Restaurante.objects.filter(nombre=restaurante.nombre).update(**restaurante_data)
                self.stdout.write(self.style.WARNING(f'El restaurante {restaurante.nombre} ya existe'))

        self.stdout.write(self.style.SUCCESS('¡Datos de ejemplo cargados exitosamente!'))