from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse

info = {'error': ''}
def checker(username, passwod, repeat_password, age, users):
    info = {}
    if passwod == repeat_password and age >= 18 and username not in users:
        info['access'] = f'Приветствуем, {username}!'
    elif age < 18:
        info['error'] = 'Вы должны быть старше 18'
    elif passwod != repeat_password:
        info['error'] = 'Пароли не совпадают'
    elif username in users:
        info['error'] = 'Пользователь уже существует'
    return info
    
def sign_up_by_django(request):
    users = ['user1', 'user2']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            info = checker(username, password, repeat_password, age, users)
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    users = ['user1', 'user2']
    info = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        age = int(request.POST['age'])
        info = checker(username, password, repeat_password, age, users)
    return render(request, 'fifth_task/registration_page.html', info)
    

