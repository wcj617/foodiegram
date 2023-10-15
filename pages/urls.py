from django.urls import path
from .views import image_upload_view, load_test_data, search_results, HomePageView, FoodAutocomplete

urlpatterns = [
    path('autocomplete/', FoodAutocomplete.as_view(), name='food-autocomplete'),
    path('load_data/', load_test_data),
    path('upload/', image_upload_view),
    path('', search_results, name='search_results'),
]
