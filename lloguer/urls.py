# vehicles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('automobils/', views.automobil_list, name='automobil_list'),
]
