from django.urls import path
from .views import HomeView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskToggleView, TagListView, TagCreateView, TagUpdateView, TagDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-task/', TaskCreateView.as_view(), name='add_task'),
    path('update-task/<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('delete-task/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('toggle-task-status/<int:pk>/', TaskToggleView.as_view(), name='toggle_task_status'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tags/add/', TagCreateView.as_view(), name='add_tag'),
    path('tags/update/<int:pk>/', TagUpdateView.as_view(), name='update_tag'),
    path('tags/delete/<int:pk>/', TagDeleteView.as_view(), name='delete_tag'),
]
