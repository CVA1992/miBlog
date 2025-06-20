from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.
def perfil_usuario(request,user_id):
    perfil = get_object_or_404(User, id=user_id)
    contexto={
        'perfil':perfil
    }
    return render(request,'users/perfil_usuario.html',contexto)