from django.db import models


class Users(models.Model):
    STATUS_CHOICES = (
        ('Водитель', 'Водитель'),
        ('Отправитель', 'Отправитель'),
    )
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)

class Transport(models.Model):
    STATUS_CHOICES = (
        ('Фура', 'Фура'),
        ('Автосцепка', 'Автосцепка'),
        ('Автоцистерна', 'Автоцистерна'),
        ('Открытая платформа', 'Открытая платформа'),
    )
    brand = models.CharField(max_length=30)
    max_weight = models.IntegerField(max_length=10)
    transport_type = models.CharField(max_length=50, choices=STATUS_CHOICES)


class Profile_driver(models.Model):
    STATUS_CHOICES = (
        ('Занят', 'Занят'),
        ('Ожидаю груз', 'Ожидаю груз'),
        ('Пустой', 'Пустой'),
    )
    origin = models.CharField(max_length=30, null=True, blank=True)
    destination = models.CharField(max_length=30, null=True, blank=True)
    fio = models.CharField(max_length=150)
    number_phone = models.CharField(max_length=30)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    about_me = models.TextField(max_length=200, null=True, blank=True)
    transport = models.ForeignKey(Transport, models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(Users, models.CASCADE, null=True, blank=True)

class User_Profile(models.Model):
    fio = models.CharField(max_length=150)
    number_phone = models.CharField(max_length=30)
    user_id = models.ForeignKey(Users, models.CASCADE, null=True, blank=True)

class Cargo(models.Model):
    profile_id = models.ForeignKey(User_Profile, models.CASCADE, null=True, blank=True)
    name_cargo = models.CharField(max_length=200)
    departure_time = models.DateField()
    arrival_time = models.DateField()
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)


