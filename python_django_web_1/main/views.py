from django.shortcuts import render, redirect

from .forms import TaskForm, RegisterForm
from .models import Task, User


def index(request):
    tasks = Task.objects.all()
    # tasks = Task.objects.orderby()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def about(request):
    tasks = Task.objects.all()
    return render(request, 'main/about.html', {'title': 'Про нас', 'tasks': tasks})


def sign_up(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма неверна'

    form = RegisterForm()
    context = {'form': form, 'title': 'Регистрация', 'error': error}
    return render(request, 'main/sign_up.html', context)


def add(request):
    Users = User.objects.all()
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'

    form = TaskForm()
    context = {'form': form, 'title': 'Добавление', 'error': error}
    return render(request, 'main/add.html', context)
