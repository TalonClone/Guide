from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.api_basic.urls')),
    path('', include('apps.movies.urls')),
]
