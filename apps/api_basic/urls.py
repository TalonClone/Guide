from django.urls import path
from .views import ArticleAPIView, ArticleDetailsAPIView

app_name = 'apps.api_basic'

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>', ArticleDetailsAPIView.as_view()),
]
