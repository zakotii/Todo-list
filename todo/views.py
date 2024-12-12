from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Task, Tag
from .forms import TaskForm, TagForm
from django.utils.timezone import now

class HomeView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_filter = self.request.GET.get('tag')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        tasks = Task.objects.all()
        
        if tag_filter:
            tasks = tasks.filter(tags__name=tag_filter)
        
        if start_date:
            tasks = tasks.filter(created_at__gte=start_date)
        if end_date:
            tasks = tasks.filter(created_at__lte=end_date)
        
        context['tasks'] = tasks.order_by('is_done', '-created_at')
        context['completed_count'] = tasks.filter(is_done=True).count()
        context['near_deadline_tasks'] = tasks.filter(deadline__isnull=False, deadline__lte=now()).exclude(is_done=True)
        context['tags'] = Tag.objects.all()
        return context

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('home')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('home')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('home')

class TaskToggleView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('home')


class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('tag_list')

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('tag_list')

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'todo/tag_confirm_delete.html'
    success_url = reverse_lazy('tag_list')
