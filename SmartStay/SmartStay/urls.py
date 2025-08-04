from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 🛠️ Admin rozhraní
    path('', include('checkin.urls')),  # 📦 Připojení URL aplikace checkin
    path('accounts/', include('django.contrib.auth.urls')),  # 🔐 Přihlášení/odhlášení
]
