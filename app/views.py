
from django.shortcuts import render, redirect
from .models import Task


# Display pending and completed tasks
def home(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)

    return render(request, 'app/home.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    })


# Add a new task
def addTask(request):
    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            Task.objects.create(task=task)

    return redirect('/')


# Mark task as completed
def complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()

    return redirect('/')


# Mark task as pending
def incomplete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = False
    task.save()

    return redirect('/')


# Edit task
def updateData(request, task_id):
    d = Task.objects.get(id=task_id)

    if request.method == "POST":
        d.task = request.POST.get('task')
        d.save()

        return redirect('/')

    return render(request, 'app/edit.html', {'d': d})


# Delete task
def deleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

    return redirect('/')
