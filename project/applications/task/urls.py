from django.urls import path, include
from . import views

app_name = 'task_app'

urlpatterns = [
    path(
        'tasks/',
        views.TasksListView.as_view(),
        name='tasks'
    ),
]