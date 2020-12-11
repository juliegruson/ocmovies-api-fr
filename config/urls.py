"""OCMovies-API URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/genres/', include('api.v1.genres.urls', namespace='genres')),
    path('api/v1/scores/', include('api.v1.scores.urls', namespace='scores')),
    path('api/v1/titles/', include('api.v1.titles.urls', namespace='titles')),
]
