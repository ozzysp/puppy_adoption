from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def crud(request):
    if request.user.is_authenticated:
        return redirect('publish/new_puppy')
    if request.method == 'GET':
        return render(request, 'crud.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        retype = request.POST.get('retype')
        if len(name.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0 or len(retype.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Fill all fields')
            return render(request, 'crud.html')

        if password != retype:
            messages.add_message(request, constants.WARNING, 'Passwords did not match')
            return  render(request, 'crud.html')
       
        try:  
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            messages.add_message(request, constants.SUCCESS, 'Account created successfully')
            return render(request, 'login.html')
        except:
            messages.add_message(request, constants.ERROR, 'SYSTEM ERROR')
            return render(request, 'crud.html')



def login(request):
    if request.user.is_authenticated:
        return redirect('publish/new_puppy')
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')           
        user = authenticate(username=name,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('/publish/new_puppy')
        else:
            messages.add_message(request, constants.ERROR, 'Unregistered user')
            return render(request, 'login.html')
    


