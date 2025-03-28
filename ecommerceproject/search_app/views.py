# search_app/views.py
from django.shortcuts import render

def SearchResult(request):
    # Your view logic here
    return render(request, 'search_app/search_results.html')

