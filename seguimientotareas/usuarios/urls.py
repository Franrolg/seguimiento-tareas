from django.urls import path
from . import views

urlpatterns = [
    path('login', views.iniciar_sesion, name='iniciar sesion')
]
