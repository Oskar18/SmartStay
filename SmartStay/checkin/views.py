# checkin/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Guest, Property
from .forms import GuestForm, PropertyForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'checkin/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'checkin/home.html')

@login_required
def guest_list(request):
    if request.user.is_superuser:
        guests = Guest.objects.all()
    else:
        guests = Guest.objects.filter(user=request.user)
    return render(request, 'checkin/guest_list.html', {'guests': guests})

@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user
            property.save()
            return redirect('home')
    else:
        form = PropertyForm()
    return render(request, 'checkin/add_property.html', {'form': form})

@login_required
def property_list(request):  # 🏘️ Seznam nemovitostí pro přihlášeného uživatele
    if request.user.is_superuser:
        properties = Property.objects.all()
    else:
        properties = Property.objects.filter(user=request.user)
    return render(request, 'checkin/property_list.html', {'properties': properties})

@login_required
def add_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST, user=request.user)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.user = request.user
            guest.save()
            return redirect('guest_list')
    else:
        form = GuestForm(user=request.user)
    return render(request, 'checkin/add_guest.html', {'form': form})
