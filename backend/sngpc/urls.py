from django.urls import path
from . import views

app_name = 'sngpc' 

urlpatterns = [
   path('sngpc/', views.sngpc_list, name='sngpc'), # noqa E501
    #path('', v.sngpc_list, name='sngpc_list'),  # noqa E501
]
