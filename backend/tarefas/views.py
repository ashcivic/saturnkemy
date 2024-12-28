from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa, Card, KanbanColumn
from django.http import HttpResponse, JsonResponse
from ics import Calendar, Event
from django.utils.timezone import make_aware
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json
import logging

#def tarefas(request):
    #tarefas = Tarefa.objects.all()
   # return render(request, 'tarefas/tarefas.html', {'tarefas': tarefas})

#def listar_tarefas(request):
    #tarefas = Tarefa.objects.all()
    #return render(request, 'tarefas/listar.html', {'tarefas': tarefas})

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


# ... outras views ...

def kanban_view(request):
    columns = KanbanColumn.objects.prefetch_related('cards').all()  # Busca colunas e cartões do DB
    return render(request, "tarefas/listar.html", {"columns": columns})

logger = logging.getLogger(__name__)
@csrf_exempt
def update_card(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        card_id = data.get('card_id')
        column_id = data.get('column_id')

        # Log para depuração
        print(f'Received card_id: {card_id}, column_id: {column_id}')

        if column_id is None:
            return JsonResponse({'success': False, 'error': 'column_id is None'})

        try:
            card = Card.objects.get(id=card_id)
            column = KanbanColumn.objects.get(id=column_id)
            card.column = column
            card.save()
            return JsonResponse({'success': True})
        except KanbanColumn.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'KanbanColumn matching query does not exist'})
        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Card matching query does not exist'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def create_column(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')

        if not title:
            return JsonResponse({'success': False, 'error': 'Título é obrigatório.'})

        column = KanbanColumn.objects.create(title=title)
        return JsonResponse({'success': True, 'column': {'id': column.id, 'title': column.title}})

    return JsonResponse({'success': False, 'error': 'Método inválido.'})

def delete_column(request, column_id):
    try:
        column = KanbanColumn.objects.get(id=column_id)
        column.delete()
        return JsonResponse({'success': True})
    except KanbanColumn.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Coluna não encontrada.'})

@csrf_exempt
def create_card(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        column_id = data.get('column_id')
        content = data.get('content')
        priority = data.get('priority')

        try:
            column = KanbanColumn.objects.get(id=column_id)
            card = Card.objects.create(column=column, content=content, priority=priority)
            return JsonResponse({'success': True, 'card': {'id': card.id, 'content': card.content, 'priority': card.priority, 'column_id': card.column.id}})
        except KanbanColumn.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Coluna não encontrada.'})

    return JsonResponse({'success': False, 'error': 'Método inválido.'})

@csrf_exempt
def edit_card(request, card_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        content = data.get('content')
        priority = data.get('priority')

        try:
            card = Card.objects.get(id=card_id)
            card.content = content
            card.priority = priority
            card.save()
            return JsonResponse({'success': True})
        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Cartão não encontrado.'})

    return JsonResponse({'success': False, 'error': 'Método inválido.'})

def delete_card(request, card_id):
    try:
        card = Card.objects.get(id=card_id)
        card.delete()
        return JsonResponse({'success': True})
    except Card.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Cartão não encontrado.'})

