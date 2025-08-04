from django import forms  # 🛠️ Práce s formuláři
from .models import Guest  # 📦 Import modelu hosta

class GuestForm(forms.ModelForm):  # 📝 Formulář založený na modelu Guest
    def __init__(self, *args, **kwargs):  # 🧠 Vlastní inicializace formuláře
        user = kwargs.pop('user')  # 🔍 Vytáhneme přihlášeného uživatele
        super().__init__(*args, **kwargs)  # 🧬 Základní inicializace
        self.fields['property'].queryset = user.property_set.all()  # 🏠 Jen nemovitosti tohoto uživatele

    class Meta:
        model = Guest  # 📦 Založeno na modelu Guest
        fields = ['name', 'date_of_birth', 'property']  # 🧾 Vyplňovaná pole
