from django.db import models

# Create your models here.

class Room(models.Model):
    #host =
    #topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null= True, blank=True)
    #participants = active users
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)#autonowadd is for time stamp only for the first time


    def __str__(self):
        return self.name


    