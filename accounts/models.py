from django.db import models


class CounsellingSession(models.Model):
    client_name = models.CharField(max_length=200, null=True)
    session_date = models.DateField(null=True)
    session_time = models.TimeField(null=True)


class Counseller(models.Model):
    counseller_name = models.CharField(max_length=200, null=True)


class MoodTrackerData(models.Model):
    mood_value = models.IntegerField(null=True)
    additional_comments = models.CharField(max_length=500, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


class SessionChanges(models.Model):
    client_name = models.CharField(max_length=200, null=True)
    client_session_date = models.DateField(null=True)
    session_id = models.IntegerField(null=True)
    requested_changes = models.CharField(max_length=500, null=True)


