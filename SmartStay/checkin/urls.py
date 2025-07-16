from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 🟢 Domovská stránka
    path('checkin/', views.guest_checkin, name='guest_checkin'),  # 🟢 Odeslání formuláře
    path('success/', views.success, name='success'),  # 🟢 Potvrzení odeslání
    path('guests/', views.guest_list, name='guest_list'),  # 🟦 Seznam hostů
]
