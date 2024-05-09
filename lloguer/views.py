# vehicles/views.py

from django.shortcuts import render
from .models import Automobil

def automobil_list(request):
    automobils = Automobil.objects.all()
    return render(request, 'lloguer/automobil_list.html', {'automobils': automobils})
