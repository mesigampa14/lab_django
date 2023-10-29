from django.urls import path
from .views import login_view

urlpatterns = [
    # Otras URLs de tu aplicación
    path('', login_view, name='login'),
]
