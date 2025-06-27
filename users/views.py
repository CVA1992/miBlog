from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, PerfilForm
from .models import User

# Create your views here.
def perfil_usuario(request,user_id):
    perfil = get_object_or_404(User, id=user_id)
    contexto={
        'perfil':perfil
    }
    return render(request,'users/perfil_usuario.html',contexto)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:index')  # Cambia esto
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')  # Cambia esto
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('main:index') 
@login_required
def editar_perfil(request,user_id):
    perfil = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if form.is_valid():
            form.save()
            
            return redirect('users:perfil_usuario', user_id=perfil.id)
    else:
        form = PerfilForm(instance=perfil)
    return render(request,'users/editar_perfil.html',{'form':form, 'perfil':perfil})
    