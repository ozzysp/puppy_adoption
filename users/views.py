from django.shortcuts import render
from django.http import HttpResponse


def crud(request):
    return render(request, 'crud.html')


def login(request):
    return render(request, 'login.html')

