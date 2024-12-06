"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add-task/', views.task_create, name='add_task'),
    path('update-task/<int:pk>/', views.task_update, name='update_task'),
    path('delete-task/<int:pk>/', views.task_delete, name='delete_task'),
    path('toggle-task-status/<int:pk>/', views.task_toggle, name='toggle_task_status'),  # Изменение здесь
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/add/', views.add_tag, name='add_tag'),  # Добавить маршрут для добавления тега
]
