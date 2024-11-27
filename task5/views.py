from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegistr

# Create your views here.
users = ['user', 'username', 'truelogin']


def sign_up_by_html(request):
    error = None
    good = None
    if request.method == "POST":
        username = request.POST.get('username')
        if username in users:
            error = 'Такой логин уже существует.'
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if password != repeat_password:
            error = 'Пароли не совпадают.'
        age = request.POST.get('age')
        if int(age) < 18:
            error = 'Вы должны быть старше 18'
        if error is None:
            good = f'Приветствуем, {username}!'
        info = {'good': good, 'error': error}
        return render(request, 'fifth_task/registration_page.html', info)
    else:
        return render(request, 'fifth_task/registration_page.html')

def sign_up_by_django(request):
    error = None
    good = None
    if request.method == "POST":
        form = UserRegistr(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if username in users:
                error = 'Такой логин уже существует.'
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            if password != repeat_password:
                error = 'Пароли не совпадают.'
            age = form.cleaned_data['age']
            if int(age) < 18:
                error = 'Вы должны быть старше 18'
        if error == None:
            good = f'Приветствуем, {username}!'
        info = {'good': good, 'error': error}
        return render(request, 'fifth_task/registration_page.html', info)
    else:
        form = UserRegistr(request.POST)
        return render(request, 'fifth_task/registration_page.html')
