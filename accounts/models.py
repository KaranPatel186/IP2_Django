from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class CounsellingSession(models.Model):
    client_name = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    session_date = models.DateField(null=True)
    session_time = models.TimeField(null=True)


class Counseller(models.Model):
    counseller_name = models.CharField(max_length=200, null=True)


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
