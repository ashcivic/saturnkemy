from django.urls import path
from . import views

app_name='trello'

urlpatterns = [
    path('', views.index, name='index'),
    path('^logout/$', views.signout, name='logout'),
    path('^login/$', views.signin, name='login'),
    path('^register/$', views.register, name='register'),
    path('^search/$', views.search_page, name='search')
    ]
