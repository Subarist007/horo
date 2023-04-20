from django.shortcuts import render

def login(request):
    context = {
        'title': 'Вход',
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Регистрация',
    }
    return render(request, 'users/registration.html', context)
