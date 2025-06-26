from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User  # Importa tu modelo de usuario personalizado

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Ajusta según tus campos

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User