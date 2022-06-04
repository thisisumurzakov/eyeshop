from rest_framework import serializers

from .models import Category, Product


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    title = serializers.CharField()
    price = serializers.FloatField()


class ProductDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    title = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField()