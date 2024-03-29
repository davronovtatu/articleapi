from .models import Article,Category
from rest_framework import serializers



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields="__all__"



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"