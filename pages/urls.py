from django.urls import path
# from .views import image_upload_view

from .views import HomePageView, FoodAutocomplete
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # path('autocomplete/', FoodAutocomplete.as_view(), name='food-autocomplete'),
    # path('upload/', image_upload_view)
]
