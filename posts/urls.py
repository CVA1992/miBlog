from django.urls import path
from . import views

app_name= 'posts'
urlpatterns = [
    path('publicacion/<int:pk>', views.publicacion, name="publicacion"),
    path('post/new/', views.crear_publicacion,name='post_form'),
    path('publicacion/<int:pk>/editar/',views.publicacion_editar,name='publicacion_editar' )
]

