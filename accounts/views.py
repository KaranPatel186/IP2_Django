from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import CreateUserForm


def home(request):
    return render(request, 'accounts/moodtracker.html')


def counselling(request):
    return render(request, 'accounts/counselling.html')


def meditation(request):
    return render(request, 'accounts/meditation.html')


def moodtracker(request):
    return render(request, 'accounts/moodtracker.html')


def counsellingBooking(request):
    return render(request, 'accounts/counsellingBooking.html')


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
