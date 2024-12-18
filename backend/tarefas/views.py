from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa
from django.http import HttpResponse
from ics import Calendar, Event
from django.utils.timezone import make_aware
from datetime import datetime

def tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/tarefas.html', {'tarefas': tarefas})

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/listar.html', {'tarefas': tarefas})

def adicionar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descricao = request.POST.get('descricao', '')
        status = request.POST['status']
        data_limite = request.POST.get('data_limite', None)

        Tarefa.objects.create(titulo=titulo, descricao=descricao, status=status, data_limite=data_limite)
        return redirect('tarefas')
    
    return render(request, 'tarefas/adicionar_tarefa.html')

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        tarefa.titulo = request.POST['titulo']
        tarefa.descricao = request.POST.get('descricao', '')
        tarefa.status = request.POST['status']
        tarefa.data_limite = request.POST.get('data_limite', None)
        tarefa.save()
        return redirect('tarefas')

    return render(request, 'tarefas/editar_tarefa.html', {'tarefa': tarefa})

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('tarefas')

def exportar_agenda(request):
    tarefas = Tarefa.objects.all()
    cal = Calendar()
    
    for tarefa in tarefas:
        event = Event()
        event.name = tarefa.titulo
        event.begin = tarefa.data_limite
        event.description = tarefa.descricao
        cal.events.add(event)
    
    response = HttpResponse(cal.serialize(), content_type='text/calendar')
    response['Content-Disposition'] = 'attachment; filename="tarefas.ics"'
    return response
