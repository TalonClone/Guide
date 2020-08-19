from django.urls import path
from .views import MoviesView, MoviesDetailView
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'apps.movies'

urlpatterns = [
    path('movies/', MoviesView.as_view()),
    path('movies/<slug:slug>/', MoviesDetailView.as_view(), name="movie_detail"),
]

#urlpatterns = format_suffix_patterns(urlpatterns)

