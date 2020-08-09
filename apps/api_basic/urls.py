from django.urls import path
from .views import ArticleList, ArticleDetail

app_name = 'apps.api_basic'

urlpatterns = [
    path('article/', ArticleList.as_view()),
    path('article/<int:pk>', ArticleDetail.as_view()),
]
