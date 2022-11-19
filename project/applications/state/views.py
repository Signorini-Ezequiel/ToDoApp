from django.shortcuts import render

# Create your views here.
from .models import State
from django.views.generic.list import ListView

class StatesListView(ListView):
    model = State
    template_name = "states/states.html"