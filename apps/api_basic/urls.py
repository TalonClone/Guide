from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleList, ArticleDetail

app_name = 'apps.api_basic'

urlpatterns = [
    path('api_basic/article/', ArticleList.as_view()),
    path('api_basic/article/<int:pk>', ArticleDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)

