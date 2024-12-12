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
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    #path('', views.home, name='home'),
    #path('add-task/', views.add_task, name='add_task'),
    #path('update-task/<int:pk>/', views.update_task, name='update_task'),
    #path('delete-task/<int:pk>/', views.delete_task, name='delete_task'),
    #path('toggle-task-status/<int:pk>/', views.toggle_task_status, name='toggle_task_status'),
    #path('tags/', views.tag_list, name='tag_list'),

    # Пути для работы с тегами
    #path('tags/add/', views.add_tag, name='add_tag'),
    #path('tags/update/<int:pk>/', views.update_tag, name='update_tag'),  # Путь для обновления тега
    #path('tags/delete/<int:pk>/', views.delete_tag, name='delete_tag'),  # Путь для удаления тега
]
