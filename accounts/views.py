from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

# Create your views here.
from .decorators import allowed_users, unauthenticated_user
from .models import *
from .forms import CreateUserForm


@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')

            return redirect('../login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('../moodtracker')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'accounts/loginPage.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/moodtracker.html')


@login_required(login_url='login')
def counselling(request):
    return render(request, 'accounts/counselling.html')


@login_required(login_url='login')
def meditation(request):
    return render(request, 'accounts/meditation.html')


@login_required(login_url='login')
def moodtracker(request):
    return render(request, 'accounts/moodtracker.html')


@login_required(login_url='login')
def moodtrackerData(request):
    return render(request, 'accounts/moodtrackerData.html')


@login_required(login_url='login')
def counsellingBooking(request):
    return render(request, 'accounts/counsellingBooking.html')
