from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'states/',
        views.StatesListView.as_view(),
        name='states'
    ),
]