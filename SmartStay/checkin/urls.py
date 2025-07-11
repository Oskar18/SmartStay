from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checkin/', views.guest_checkin, name='guest_checkin'),
]
