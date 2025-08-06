# checkin/models.py

from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):  # 🏘️ Model pro nemovitosti
    name = models.CharField(max_length=100)  # 🏷️ Název nemovitosti
    location = models.CharField(max_length=100)  # 📍 Umístění (např. město nebo oblast)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 👤 Vlastník (pronajímatel)

    def __str__(self):
        return self.name  # 🔤 Zobrazení názvu v administraci

class Guest(models.Model):  # 🧍‍♂️ Model pro hosty
    name = models.CharField(max_length=100)  # 🧾 Jméno hosta
    date_of_birth = models.DateField(null=True, blank=True)  # 🎂 Datum narození hosta
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 👤 Vlastník (pronajímatel)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)  # 🏠 Nemovitost

    def __str__(self):
        return self.name  # 🔤 Zobrazení jména hosta
