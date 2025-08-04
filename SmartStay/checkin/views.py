from django.contrib.auth.decorators import login_required  # 🔐 Ověření přihlášení
from django.shortcuts import render, redirect  # 🧭 Zobrazení a přesměrování
from django.contrib.auth.forms import UserCreationForm  # 🧾 Formulář pro registraci
from django.contrib.auth import login  # 🔐 Automatické přihlášení po registraci

from .forms import GuestForm  # 📥 Formulář pro zadání hosta
from .models import Guest  # 🗃️ Model hosta


@login_required
def home(request):  # 🏠 Domácí stránka
    return render(request, 'checkin/home.html')  # 🎨 Vrací šablonu hlavní stránky


def register(request):  # 🆕 Registrace nového uživatele
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def guest_checkin(request):  # 📝 Formulář pro přidání hosta
    if request.method == 'POST':
        form = GuestForm(request.POST, user=request.user)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.user = request.user
            guest.save()
            return redirect('guest_list')
    else:
        form = GuestForm(user=request.user)
    return render(request, 'checkin/guest_form.html', {'form': form})


@login_required
def guest_list(request):  # 📋 Zobrazení hostů
    if request.user.is_superuser:  # 🛡️ Admin vidí všechny hosty
        guests = Guest.objects.all()
    else:
        guests = Guest.objects.filter(user=request.user)  # 👤 Pronajímatel vidí jen své

    return render(request, 'checkin/guest_list.html', {'guests': guests})  # 🎨 Vrátí šablonu s hosty
