from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tag, Race


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
        