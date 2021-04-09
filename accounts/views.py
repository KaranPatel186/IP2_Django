from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from .decorators import allowed_users, unauthenticated_user
from .models import *
from .forms import CreateUserForm
from .forms import *


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
            return redirect('../moodtracker/')
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


print('MoodTrackerData:', MoodTrackerData)


@login_required(login_url='login')
def counselling(request, pk):
    client = User.objects.get(id=pk)

    counsellingData = client.counsellingsession_set.all()

    return render(request, 'accounts/counselling.html', {'CounsellingData': counsellingData})


@login_required(login_url='login')
def meditation(request):
    return render(request, 'accounts/meditation.html')


@login_required(login_url='login')
def moodtracker(request):
    form = MoodTrackerForm(initial={'client': request.user})

    if request.method == 'POST':

        form = MoodTrackerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/moodtracker.html', context)


@login_required(login_url='login')
def moodtrackerData(request, pk):
    client = User.objects.get(id=pk)

    moodtrackerdata = client.moodtrackerdata_set.all()

    context = {'moodtrackerdata': moodtrackerdata, 'client': client}
    return render(request, 'accounts/moodtrackerData.html', context)


@login_required(login_url='login')
def counsellingBooking(request):
    form = CounsellingBookingForm(initial={'client': request.user})
    if request.method == 'POST':
        form = CounsellingBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/counsellingBookingConfirm')
    print(Group.objects.get(name='Counsellers').user_set.all())
    context = {'form': form}
    return render(request, 'accounts/counsellingBooking.html', context)


@login_required(login_url='login')
def counsellingBookingConfirm(request):
    return render(request, 'accounts/counsellingBookingConfirm.html')


@login_required(login_url='login')
def counsellingChanges(request):
    form = CounsellingChangesForm()
    if request.method == 'POST':
        form = CounsellingChangesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/counselling')

    context = {'form': form}

    return render(request, 'accounts/counsellingChanges.html', context)
