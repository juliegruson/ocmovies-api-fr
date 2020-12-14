from rest_framework import generics
from django_filters import rest_framework as filters

from movies.models import Genre
from movies.serializers import GenreSerializer
from api.v1.titles.pagination import TitleSetPagination
from .filters import GenreFilterSet


class GenreListView(generics.ListAPIView):
    """
    A simple **ViewSet** for viewing genres.
    ```
    essai
    ```
    """

    http_method_names = ['get']
    queryset = Genre.objects.order_by('name')
    serializer_class = GenreSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = GenreFilterSet
    pagination_class = TitleSetPagination
