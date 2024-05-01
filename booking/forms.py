from django import forms
from .models import Booking, Room

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'email', 'room', 'start_time', 'end_time']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'number', 'capacity', 'description', 'image1', 'image2', 'image3']