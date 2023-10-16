from django.urls import path
from .views import mi_vista, estudiante_lista, estudiante_crear

app_name = 'estudiante'
urlpatterns = [
    path('', estudiante_lista, name='estudiante_lista'),
    path('crear', estudiante_crear, name='estudiante_crear'),
    path('asdf/', mi_vista, name='ej'),
]
