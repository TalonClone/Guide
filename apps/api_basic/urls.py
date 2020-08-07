from django.urls import path
from .views import article_list

app_name = 'apps.api_basic'

urlpatterns = [
    path('article/', article_list),
]
