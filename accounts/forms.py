from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from accounts.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class MoodTrackerData(ModelForm):
    class Meta:
        model = MoodTrackerData
        fields = ['mood_value', 'additional_comments']


class CounsellingSessions(ModelForm):
    class Meta:
        model = CounsellingSession
        fields = ['session_date', 'session_time']
