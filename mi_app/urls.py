# mi_app/urls.py
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('api/restaurantes/', views.get_restaurantes, name='get_restaurantes'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]