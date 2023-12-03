# ArtistAPI/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('artist.urls')),  # Replace 'your_app' with the actual name of your API app
]
