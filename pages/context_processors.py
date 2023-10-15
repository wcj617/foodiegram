from django.conf import settings

def get_key(request):
    print(request.body)
    return {
        "GOOGLE_MAP_API_KEY": settings.GOOGLE_MAPS_API_KEY
    }