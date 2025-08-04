from django.urls import path  # 🛤️ Cesty URL
from . import views  # 📥 Importujeme views z aktuální složky

urlpatterns = [
    path('', views.home, name='home'),  # 🏠 Domácí stránka
    path('guests/', views.guest_list, name='guest_list'),  # 📋 Seznam hostů
    path('register/', views.register, name='register'),  # 🆕 Registrace
    path('checkin/', views.guest_checkin, name='guest_checkin'),  # 📝 Přidání hosta
]
