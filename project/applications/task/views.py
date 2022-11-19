from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
from .models import Tasks

class TasksListView(ListView):
    model = Tasks
    template_name = "tasks/tasks.html"