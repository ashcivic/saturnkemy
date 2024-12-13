from django import forms
from .models import Delivery
from django.contrib.auth.models import User

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['address', 'responsible', 'observation', 'driver', 'delivery_date', 'order']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'responsible': forms.TextInput(attrs={'class': 'form-control'}),
            'observation': forms.Textarea(attrs={'class': 'form-control'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'delivery_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }