from django.urls import path
from .views import proyecto_lista, proyecto_crear

app_name = 'persona'
urlpatterns = [
    path('', proyecto_lista, name='proyecto_lista'),
    path('proyecto_crear', proyecto_crear, name='proyecto_crear'),
]
