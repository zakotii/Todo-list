from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Tag
from .forms import TaskForm, TagForm
from django.utils.timezone import now


def home(request):
    # Фильтры
    tag_filter = request.GET.get('tag')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    tasks = Task.objects.all()

    # Фильтрация по тегу
    if tag_filter:
        tasks = tasks.filter(tags__name=tag_filter)
    
    # Фильтрация по диапазону дат
    if start_date:
        tasks = tasks.filter(created_at__gte=start_date)
    if end_date:
        tasks = tasks.filter(created_at__lte=end_date)

    # Статистика
    completed_count = tasks.filter(is_done=True).count()

    # Уведомления о приближающемся дедлайне
    near_deadline_tasks = tasks.filter(deadline__isnull=False, deadline__lte=now()).exclude(is_done=True)

    context = {
        'tasks': tasks.order_by('is_done', '-created_at'),
        'completed_count': completed_count,
        'near_deadline_tasks': near_deadline_tasks,
    }
    return render(request, 'home.html', context)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('home')


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


def tag_list(request):
    return render(request, 'tag_list.html')

def add_task(request):
    return render(request, 'task_form.html')


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Получаем задачу по её первичному ключу (id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после обновления
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('home')
