from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from rest_framework.reverse import reverse

from .models import *

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'login', 'password', 'role')

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('pk', 'brand', 'max_weight', 'transport_type')


@admin.register(Profile_driver)
class ProfileDriverAdmin(admin.ModelAdmin):
    list_display = ('pk', 'origin', 'destination', 'fio', 'number_phone', 'status', 'about_me', 'transport', 'user_id')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile_id', 'name_cargo', 'departure_time', 'arrival_time', 'origin', 'destination')

@admin.register(User_Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('fio', 'number_phone', 'user_id')
