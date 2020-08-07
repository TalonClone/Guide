from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']





