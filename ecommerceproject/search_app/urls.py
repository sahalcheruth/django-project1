# search_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('rr/', views.SearchResult, name='SearchResult'),  # Pass the function directly
]
