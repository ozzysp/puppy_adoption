from django.db import models
from django.contrib.auth.models import User

class Race(models.Model):
    race = models.CharField(max_length=50)

    def __str__(self):
        return self.race
    
class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
    

class Puppy(models.Model):
    choices_status = (('F', 'For adoption'),
                      ('A', 'Already adopted'))
    
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    picture = models.ImageField(upload_to="Puppies_Pictures")
    name = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    race = models.ForeignKey(Race, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status, default='F')
    
    def __str__(self):
        return self.name
    