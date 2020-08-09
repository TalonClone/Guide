from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleList, ArticleDetail

app_name = 'apps.api_basic'

urlpatterns = [
    path('article/', ArticleList.as_view()),
    path('article/<int:pk>', ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

