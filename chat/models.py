# from django.db.models import CharField
# from django_mysql.models import ListCharField
from django.db import models
import datetime

# Create your models here.
# in django id is already inbuilt generated.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    # users = ListCharField(
    #     base_field = CharField(max_length=10),
    #     max_length=(6000)
    # )
    
    def __str__(self):
        return "Room: " + self.name

    
    
class Message(models.Model):
    value = models.CharField(max_length=1000000)

    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=100000)
    
    time = models.TextField(default=datetime.datetime.now().strftime("%I:%M%p"))
    date = models.TextField(default=datetime.datetime.now().strftime("%B %d, %Y"))
    
    def __str__(self):
        return "User: " + self.user + " Room: " + self.room
    
    
class User(models.Model):
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return "User: " + self.username 