from django.shortcuts import render, redirect
from .forms import GuestForm
from .models import Guest
from django.contrib.auth.decorators import login_required

@login_required  # 🟢 Zajistí, že stránka je přístupná jen přihlášeným uživatelům
def guest_checkin(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.user = request.user  # 🟢 Přiřadíme hosta aktuálnímu uživateli
            guest.save()
            return redirect('success')  # 🟢 Přesměrování na stránku po úspěšném odeslání
    else:
        form = GuestForm()
    return render(request, 'checkin/checkin_form.html', {'form': form})

@login_required
def success(request):
    return render(request, 'checkin/success.html')

@login_required
def guest_list(request):
    guests = Guest.objects.filter(user=request.user)  # 🟢 Vybere jen hosty přihlášeného uživatele
    return render(request, 'checkin/guest_list.html', {'guests': guests})

from django.shortcuts import render
from .models import Guest  # ← importujeme model Guest

def guest_list(request):
    guests = Guest.objects.all()  # ← vezmeme všechny hosty z databáze
    return render(request, 'checkin/guest_list.html', {'guests': guests})
    # ← zobrazíme šablonu a pošleme jí seznam hostů
