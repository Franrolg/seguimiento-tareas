from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

def autenticar_usuario(request, usuario, contrasena):
    user = authenticate(request, username=usuario, password=contrasena)
    if user: login(request, user)
    return True if user is not None else False

def iniciar_sesion(request):
    if request.method == 'POST':
        messages.success(request, "¡Has iniciado sesión!") if autenticar_usuario(request, request.POST['usuario'], request.POST['contrasena']) else messages.error(request, "¡Error al iniciar sesión!")
        return redirect('landing')
    return False