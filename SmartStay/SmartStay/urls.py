from django.contrib import admin
from django.urls import path, include  # ← přidali jsme include!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('checkin.urls')),  # ← tohle jsme přidali
]
