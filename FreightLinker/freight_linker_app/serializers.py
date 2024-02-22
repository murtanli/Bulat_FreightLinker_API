import base64
import os
import uuid

from django.core.files.base import ContentFile

from .models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['login', 'password', 'role']

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ['pk', 'brand', 'max_weight', 'transport_type']

class ProfileDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_driver
        fields = ['origin', 'destination', 'fio', 'number_phone', 'status', 'about_me', 'transport', 'user_id']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = ['fio', 'number_phone', 'user_id']

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['pk', 'profile_id', 'name_cargo', 'departure_time', 'arrival_time', 'origin', 'destination']