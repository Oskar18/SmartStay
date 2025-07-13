from django.shortcuts import render  # ← načteme funkci pro renderování HTML šablon
from .forms import GuestForm         # ← importujeme náš formulář pro check-in

def guest_checkin(request):  # ← hlavní funkce, která obsluhuje check-in stránku
    if request.method == 'POST':  # ← kontrola, jestli uživatel odeslal formulář
        form = GuestForm(request.POST)  # ← vytvoření instance formuláře s daty od uživatele
        if form.is_valid():  # ← pokud všechna data ve formuláři splňují validaci
            form.save()  # ← uložíme data do databáze
            return render(request, 'checkin/success.html')  # ← zobrazíme stránku s potvrzením
    else:
        form = GuestForm()  # ← pokud zatím není POST, vytvoříme prázdný formulář

    return render(request, 'checkin/guest_checkin.html', {'form': form})  # ← pošleme formulář do šablony

