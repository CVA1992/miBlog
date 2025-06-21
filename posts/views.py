from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, Comment
from .forms import PostForm

# Create your views here.
def publicacion(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    comentarios = publicacion.comments.filter(active=True).order_by('-created')
    contexto= {
        'publicacion': publicacion,
        'comentarios': comentarios
    }
    return render(request,'posts/publicacion.html',contexto)
def crear_publicacion(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:publicacion', pk=post.pk)
    else:
        form=PostForm()
    return render(request,'posts/post_form.html',{'form':form})