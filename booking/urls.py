from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', get_rooms_list, name='rooms'),
    path('<int:pk>/', get_room_details, name='room'),
    path('booking/<int:pk>/', get_booking_details, name='booking-detail'),
    path('booking/', get_booking_form, name='booking-form'),
    path('bookings/', booking_list, name='booking_list'),
    path('bookings/<int:booking_id>/edit/', booking_edit, name='booking_edit'),
    path('bookings/<int:booking_id>/delete/', booking_delete, name='booking_delete'),
    path('availability/<int:pk>/', get_room_avaibility, name='room-availability-calendar'),
    path('rooms/', room_list, name='room_list'),
    path('rooms/<int:room_id>/edit/', room_edit, name='room_edit'),
    path('rooms/<int:room_id>/delete/', room_delete, name='room_delete'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('createroom/', create_room, name='room-create'),
]
