from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tag, Race, Puppy
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect


@login_required
def new_puppy(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        races = Race.objects.all()
        return render(request, "new_puppy.html", {'tags': tags, 'races': races})
    elif request.method == "POST":
        picture = request.FILES.get('picture')
        name = request.POST.get('name')
        description = request.POST.get('description')
        state = request.POST.get('state')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        tags = request.POST.getlist('tags')
        race = request.POST.get('race')
        return redirect('/publish/your_puppies')
        

    puppy = Puppy(
        user = request.user,
        picture = picture,
        name = name,
        description=description,
        state=state,
        city=city,
        phone=phone,
        race_id=race,
    )
    puppy.save()

    for tag_id in tags:
        tag = Tag.objects.get(id=tag_id)
        puppy.tags.add(tag)

        puppy.save()
        tags = Tag.objects.all()
        races = Race.objects.all()
        messages.add_message(request, constants.SUCCESS, 'New puppy registered')
        return render(request, 'new_puppy.html', {'tags': tags, 'races': races})
    
@login_required
def your_puppies(request):
    if request.method == "GET":
        puppies = Puppy.objects.filter(user=request.user)
        return render(request, 'your_puppies.html', {'puppies': puppies})


def delete_puppy(request, id):
    puppy = Puppy.objects.get(id=id)
    
    if not puppy.user == request.user:
        messages.add_message(request, constants.ERROR, 'Not authorized action')
        return redirect('/publish/your_puppies')
    else:
        puppy.delete()
        messages.add_message(request, constants.ERROR, 'The puppy has been deleted')
        return redirect('/publish/your_puppies')