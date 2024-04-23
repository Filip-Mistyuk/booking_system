from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from booking.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import BookingForm, RoomForm

@login_required(login_url='register-form')
def get_rooms_list(request):
    rooms = Room.objects.all()
    context = {
               'rooms': rooms,
    }
    return render(request, 'booking/rooms_list.html', context)

@login_required(login_url='register-form')
def get_room_details(request, pk):
    room = Room.objects.get(id=pk)
    context = {
               'room': room,
    }
    return render(request, 'booking/room_details.html', context)

def get_booking_details(request, pk):
    booking = Booking.objects.get(id=pk)
    context = {
                'booking': booking,
    }
    return render(request, 'booking/booking_details.html', context)

def get_booking_form(request):
    if request.method == "GET":
        return render(request, "booking/booking_form.html")
    else:
        room_number = request.POST.get("room_number")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        
        # try:
        room = Room.objects.get(number=room_number)
        # except ValueError:
        #     return HttpResponse("Wrong room number", status=404)
        # except Room.DoesNotExist:
        #     return HttpResponse("Room doesn't exist", status=404)
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            start_time=start_time,
            end_time=end_time
        )
        return redirect("booking-detail", pk=booking.id)
    
@login_required
def booking_edit(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking_edit.html', {'form': form})

def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == "POST":
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking/booking_delete_confirm.html', {'booking': booking})

def room_availability_calendar(request):
    rooms = Room.objects.all()
    return render(request, 'availability_calendar.html', {'rooms': rooms})

def room_edit(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room_form.html', {'form': form})

def room_delete(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == "POST":
        room.delete()
        return redirect('room_list')
    return render(request, 'room_confirm_delete.html', {'room': room})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms_list.html', {'rooms': rooms})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('rooms')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def custom_logout(request):
    logout(request)
    return redirect('rooms') 

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def create_room(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = RoomForm(request.POST)
            if form.is_valid():
                room = form.save()
                return redirect('room', room.id)
        else:
            form = RoomForm()
        return render(request, 'booking/create_room.html', {'form': form})
    else:
        return redirect('login')