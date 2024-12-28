from django.shortcuts import render, get_object_or_404, redirect
from .models import TaskList, Card
from rest_framework import viewsets
from .serializers import TaskListSerializer, CardSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def index(request):
    if request.user.is_authenticated:
        return render(request, 'trello/index.html')
    else:
        return HttpResponseRedirect('/login')


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


def signout(request):
    if request.POST:
        return logout(request, request.POST["logout"])
    else:
        logout(request)
        return render(request, 'trello/logout.html')


def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'trello/login.html')


def search_page(request):
    pass


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, prefix='user')
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            return HttpResponseRedirect('/')
    else:
        user_form = UserCreationForm(prefix='user')
    context = {'userform': user_form}
    return render(request, 'trello/register.html', context)
