# checkin/forms.py

from django import forms
from .models import Guest, Property

class PropertyForm(forms.ModelForm):  # 🏠 Formulář pro nemovitosti
    class Meta:
        model = Property
        fields = ['name', 'location']  # 📍 Název + lokalita

class GuestForm(forms.ModelForm):  # 🧍‍♂️ Formulář pro hosty
    class Meta:
        model = Guest
        fields = ['name', 'date_of_birth', 'property']  # 🧾 Nezobrazujeme user

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # 🧍‍♂️ Získáme přihlášeného uživatele
        super().__init__(*args, **kwargs)
        if user:
            # 🔒 Omezíme výběr nemovitostí na ty, které vlastní daný uživatel
            self.fields['property'].queryset = Property.objects.filter(user=user)
