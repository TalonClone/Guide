from django.urls import path
from .views import MoviesView
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'apps.movies'

urlpatterns = [
    path('movies/', MoviesView.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)

