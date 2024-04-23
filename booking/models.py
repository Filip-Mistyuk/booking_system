from django.db import models
from django.conf import settings

class Room(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=63)
    capacity = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.number
    

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="booked")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="booked")
    email = models.EmailField(default='example@example.com')

    
    def __str__(self):
        return self.room.number
