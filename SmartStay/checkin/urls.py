from django.urls import path  # ← importujeme funkci `path` pro tvorbu URL
from . import views           # ← importujeme náš views soubor

urlpatterns = [
    path('', views.guest_checkin, name='guest_checkin'),  # ← hlavní URL → spouští funkci guest_checkin
]
