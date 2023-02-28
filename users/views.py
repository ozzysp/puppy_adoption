from django.shortcuts import render
from django.http import HttpResponse


def crud(request):
    if request.method == 'GET':
        return render(request, 'crud.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        retype = request.POST.get('retype')
        return HttpResponse('TESTE TESTE')



def login(request):
    return render(request, 'login.html')

