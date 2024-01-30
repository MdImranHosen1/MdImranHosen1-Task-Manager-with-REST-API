from django.urls import path, include  # Import path instead of url

taskurlpatterns = [
    path('api/v1/', include('djoser.urls')),  # Use path instead of url
    path('api/v1/', include('djoser.urls.authtoken')),  # Use path instead of url
]
