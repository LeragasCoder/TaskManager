from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Task
from .forms import TaskForm

def task_list(request):
    """Main page showing task list sorted by deadline and priority"""
    tasks = Task.objects.all().order_by('deadline_days', '-priority', 'created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    """Show task details with description"""
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):
    """Create new task"""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Task "{task.title}" created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Create New Task'
    })

def task_update(request, task_id):
    """Update existing task"""
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Task "{task.title}" updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': f'Edit Task: {task.title}',
        'task': task
    })

def task_delete(request, task_id):
    """Delete task"""
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task_title = task.title
        task.delete()
        messages.success(request, f'Task "{task_title}" deleted successfully!')
        return redirect('task_list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
