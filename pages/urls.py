from django.urls import path
from .views import image_upload_view, load_test_data
from .views import HomePageView, FoodAutocomplete

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('autocomplete/', FoodAutocomplete.as_view(), name='food-autocomplete'),
    path('load_data/', load_test_data),
    path('upload/', image_upload_view)
]
