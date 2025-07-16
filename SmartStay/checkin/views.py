from django.shortcuts import render
from .forms import GuestForm
from .models import Guest

def home(request):  # 🟢 Domovská stránka
    return render(request, 'checkin/home.html')

def guest_checkin(request):  # 🟢 Formulář pro check-in hosta
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'checkin/success.html')
    else:
        form = GuestForm()
    return render(request, 'checkin/checkin_form.html', {'form': form})

def success(request):  # 🟢 Potvrzení po úspěšném odeslání formuláře
    return render(request, 'checkin/success.html')

def guest_list(request):  # 🟦 Výpis všech hostů v systému
    guests = Guest.objects.all()
    return render(request, 'checkin/guest_list.html', {'guests': guests})
