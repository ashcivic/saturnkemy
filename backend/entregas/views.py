from django.shortcuts import render, redirect
from .models import Delivery
from .forms import DeliveryForm
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def delivery_index(request):
    deliveries = Delivery.objects.all()
    filter_date = request.GET.get('date', date.today())
    deliveries = deliveries.filter(delivery_date=filter_date)
    
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entregas:delivery_index')
    else:
        form = DeliveryForm()

    return render(request, "entregas/gestao/index.html", {"form": form, "deliveries": deliveries, "filter_date": filter_date})

@login_required
def consultas_index(request):
    return render(request, "entregas/consultas/index.html")