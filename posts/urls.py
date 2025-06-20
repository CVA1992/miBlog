from django.urls import path
from . import views

app_name= 'posts'
urlpatterns = [
    path('publicacion/<int:pk>', views.publicacion, name="publicacion")
]

