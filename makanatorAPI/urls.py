from django.contrib import admin
from django.urls import path, include  # ← tambahkan include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),  # ← sambungkan ke urls.py di dalam api
]
