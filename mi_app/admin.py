# mi_app/admin.py
from django.contrib import admin
from .models import Restaurante

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_cocina', 'calificacion', 'activo')
    list_filter = ('tipo_cocina', 'activo')
    search_fields = ('nombre', 'direccion')
    ordering = ('nombre',)