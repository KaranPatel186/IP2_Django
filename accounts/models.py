import uuid

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms


class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Counseller(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class CounsellingSession(models.Model):
    COUNSELLERS = (
        ('John', 'John'),
        ('Mark', 'Mark'),
        ('Dave', 'Dave'),
    )
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=6)
    client_name = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    session_date = models.DateField(null=True)
    session_time = models.TimeField(null=True)
    counseller = models.CharField(max_length=200, null=True, choices=COUNSELLERS,)

    def __int__(self):
        return self.session_id


class MoodTrackerData(models.Model):
    MOOD = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    mood_value = models.IntegerField(null=True, choices=MOOD)
    additional_comments = models.CharField(max_length=2000, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


class SessionChanges(models.Model):
    client_name = models.CharField(max_length=200, null=True)
    client_session_date = models.DateField(null=True)
    session_id = models.IntegerField(null=True)
    requested_changes = models.CharField(max_length=500, null=True)
