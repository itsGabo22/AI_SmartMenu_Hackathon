# mi_app/models.py
from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_cocina = models.CharField(max_length=100)
    tiempo_entrega_promedio = models.PositiveIntegerField(help_text="Tiempo en minutos")
    calificacion = models.FloatField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    costo_envio = models.DecimalField(max_digits=6, decimal_places=2)
    pedido_minimo = models.DecimalField(max_digits=8, decimal_places=2)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    imagen = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']