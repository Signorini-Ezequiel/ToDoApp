from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
from .models import Task

class TasksListView(ListView):
    model = Task
    template_name = "tasks/tasks.html"