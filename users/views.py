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
        if len(name.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0 or len(retype.strip()) == 0:
            return render(request, 'crud.html')

        if password != retype:
            return  render(request, 'crud.html')



        return HttpResponse(f'{name}, {email}, {password}, {retype}')


def login(request):
    return render(request, 'login.html')

