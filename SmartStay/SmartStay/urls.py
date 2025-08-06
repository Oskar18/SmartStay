# SmartStay/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ✨ Login a logout views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('checkin.urls')),  # 🌐 Cesta do aplikace checkin
    path('login/', auth_views.LoginView.as_view(template_name='checkin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
