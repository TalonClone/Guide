from django.urls import path
from .views import article_list, article_detail

app_name = 'apps.api_basic'

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>', article_detail),
]
