from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

# Create your views here.
def publicacion(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    comentarios = publicacion.comments.filter(active=True).order_by('-created')
    contexto= {
        'publicacion': publicacion,
        'comentarios': comentarios
    }
    return render(request,'posts/publicacion.html',contexto)