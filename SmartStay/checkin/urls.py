# checkin/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 🏠 Domovská stránka
    path('add-guest/', views.add_guest, name='add_guest'),  # 🧾 Zapsat hosta
    path('guests/', views.guest_list, name='guest_list'),  # 📄 Seznam hostů
    path('add-property/', views.add_property, name='add_property'),  # ➕ Nová nemovitost
    path('properties/', views.property_list, name='property_list'),  # 🏠 Seznam nemovitostí
    path('register/', views.register, name='register'),  # 👤 Registrace
]
