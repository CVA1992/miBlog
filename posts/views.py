from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def publicacion(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    comentarios = publicacion.comments.filter(active=True).order_by('-created')

    contexto= {
        'publicacion': publicacion,
        'comentarios': comentarios,
        'es_autor': request.user== publicacion.author
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
@login_required
def publicacion_editar(request,pk):
    publicacion = get_object_or_404(Post, pk=pk)

    if request.user != publicacion.author:
        messages.error(request,'no tienes permiso para editar esta publicacion')
        return redirect('posts:publicacion', pk=publicacion.pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=publicacion)

        if form.is_valid():
            form.save()
            messages.success(request,'Publicacion actualizada correctamente')
            return redirect('posts:publicacion', pk=publicacion.pk)
    else:
        form = PostForm(instance=publicacion)
    return render(request,'posts/publicacion_editar.html',{'form':form, 'publicacion':publicacion})
@login_required
def eliminar(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    
    # Verificar si el usuario es el autor
    if request.user != publicacion.author:
        messages.error(request, 'No tienes permiso para eliminar esta publicación')
        return redirect('posts:publicacion', pk=publicacion.pk)
    
    if request.method == 'POST':
        publicacion.delete()
        messages.success(request, 'Publicación eliminada correctamente')
        return redirect('main:index')
    
    return render(request, 'posts/publicacion_confirm_delete.html', {'publicacion': publicacion})
@login_required
def comentar(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.author = request.user
            comentario.post = publicacion
            comentario.save()
            return redirect('posts:publicacion', pk=publicacion.pk)
    else:
        form=CommentForm()
    return render(request,'posts/comentario_form.html', {'form':form})