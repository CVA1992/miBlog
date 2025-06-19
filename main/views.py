from django.shortcuts import render
from posts.models import Post

# Create your views here.
def index(request):
    publicaciones = Post.objects.all()
    contexto = {'publicaciones': publicaciones}
    return render(request, 'main/index.html', contexto)