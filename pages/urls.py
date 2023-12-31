from django.urls import path
from .views import image_upload_view, search_results, load_test_data

from .views import FoodAutocomplete
urlpatterns = [
    path('autocomplete/', FoodAutocomplete.as_view(), name='food-autocomplete'),
    path('upload/', image_upload_view),
    path('', search_results, name='search_results'),
    path('load_data/', load_test_data),
]
