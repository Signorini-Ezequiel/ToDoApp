from django.shortcuts import render

# Create your views here.
from django.views.generic.base import templateview


class HomeView(TemplateView):
    template_name = "home/home.html"
