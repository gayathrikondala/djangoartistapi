# artist/urls.py

from django.urls import path
from .views import (
    RegisterAPIView,
    WorkListAPIView,
    WorkCreateAPIView,
    WorkFilterByTypeView,
    WorkSearchByArtistView
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('works/', WorkListAPIView.as_view(), name='work-list'),
    path('works/create/', WorkCreateAPIView.as_view(), name='work-create'),
    path('works/filter/', WorkFilterByTypeView.as_view(), name='work-filter-by-type'),
    path('works/search/', WorkSearchByArtistView.as_view(), name='work-search-by-artist'),
    # Add other URL patterns for your API views
]
