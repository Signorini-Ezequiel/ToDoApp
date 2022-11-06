from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    path('todo/', include('applications.todo.urls')),
    path('doing/', include('applications.doing.urls')),
    path('done/', include('applications.done.urls')),
]