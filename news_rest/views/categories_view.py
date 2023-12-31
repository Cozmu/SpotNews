from rest_framework import viewsets
from news_rest.serializers.categories_serializer import CategoriesSerializer
from news.models.category_model import Categories


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer