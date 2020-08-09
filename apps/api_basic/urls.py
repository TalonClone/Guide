from django.urls import path
from .views import article_list, article_detail, ArticleAPIView

app_name = 'apps.api_basic'

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>', article_detail),
]
