from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todotasks/home.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
    return redirect('home')

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('home')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')
