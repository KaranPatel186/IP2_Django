from django.db import models


class UserAccount(models.Model):
    username = models.TextField()
    password = models.TextField()
