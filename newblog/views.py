from django.shortcuts import render


def index(request):
    return render(request, 'login.html')


def chat(request):
    return render(request, 'chat.html')
