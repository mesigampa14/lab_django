from django.urls import path
from .views import estudiante_lista, estudiante_crear, estudiante_detalle, docente_lista, docente_crear, docente_detalle

app_name = 'persona'
urlpatterns = [
    path('estudiante_lista', estudiante_lista, name='estudiante_lista'),
    path('estudiante_crear', estudiante_crear, name='estudiante_crear'),
    path('estudiante_<int:pk>/', estudiante_detalle, name='estudiante_detalle'),

    path('docente_lista', docente_lista, name='docente_lista'),
    path('docente_crear', docente_crear, name='docente_crear'),
    path('docente_<int:pk>/', docente_detalle, name='docente_detalle'),
]
