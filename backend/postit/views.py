from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import PostIt

@login_required
def listar_postits(request):
    postits = PostIt.objects.filter(usuario=request.user)
    return render(request, 'postit/listar.html', {'postits': postits})

@login_required
def adicionar_postit(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        cor = request.POST.get('cor')
        PostIt.objects.create(titulo=titulo, conteudo=conteudo, cor=cor, usuario=request.user)
        return redirect('listar_postits')
    return render(request, 'postit/adicionar.html')

@login_required
def editar_postit(request, id):
    postit = get_object_or_404(PostIt, id=id, usuario=request.user)
    if request.method == 'POST':
        postit.titulo = request.POST.get('titulo')
        postit.conteudo = request.POST.get('conteudo')
        postit.cor = request.POST.get('cor')
        postit.save()
        return redirect('postits')
    return render(request, 'postit/editar.html', {'postit': postit})

@login_required
def excluir_postit(request, id):
    postit = get_object_or_404(PostIt, id=id, usuario=request.user)
    if request.method == 'POST':
        postit.delete()
        return redirect('postits')
    return render(request, 'postit/excluir.html', {'postit': postit})
