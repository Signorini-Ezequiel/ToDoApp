from django.shortcuts import render

# Create your views here.
from .models import States
from django.views.generic.list import ListView

class StatesListView(ListView):
    model = States
    template_name = "states/states.html"