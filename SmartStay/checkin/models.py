from django.db import models
from django.contrib.auth.models import User  # ← přidáme pro vazbu na uživatele

class Guest(models.Model):
    # spojení s přihlášeným uživatelem
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # ← každý host patří konkrétnímu uživateli

    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=50)
    email = models.EmailField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.email})"

# 💬 Vysvětlivka:
# - `owner = ForeignKey(...)` znamená, že každý záznam hosta je propojený s jedním uživatelem (např. admin, martin...)
# - `on_delete=models.CASCADE` zajistí, že když se smaže uživatel, smažou se i jeho hosté
