from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('perfil_usuario/<int:user_id>',views.perfil_usuario,name="perfil_usuario")
]
