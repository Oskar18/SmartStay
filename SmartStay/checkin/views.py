from django.shortcuts import render
from .forms import GuestForm

def home(request):
    return render(request, 'checkin/home.html')

def guest_checkin(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'checkin/success.html')
    else:
        form = GuestForm()

    return render(request, 'checkin/guest_form.html', {'form': form})
