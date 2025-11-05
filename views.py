from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import CreateUserForm, TaskForm

# ---------------- AUTH VIEWS ----------------

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'todo/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# ---------------- TASK VIEWS ----------------

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect('index')

    form = TaskForm()
    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})


@login_required
def update_task(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('index')


@login_required
def delete_task(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return redirect('index')


@login_required
def clear_completed(request):
    Task.objects.filter(user=request.user, completed=True).delete()
    return redirect('index')
