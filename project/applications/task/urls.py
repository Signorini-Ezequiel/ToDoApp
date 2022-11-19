from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'tasks/',
        views.TasksListView.as_view(),
        name='tasks'
    ),
]