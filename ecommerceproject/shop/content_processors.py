# shop/context_processors.py

from .models import Category

def all_categories(request):
    return {'categories': Category.objects.all()}  # Adjust to your model's structure
# shop/context_processors.py

def example_processor(request):
    return {'example_variable': 'value'}
