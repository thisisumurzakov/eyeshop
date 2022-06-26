from rest_framework import serializers

from .models import Category, Product


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'image', 'title', 'price')

    def get_photo_url(self, car):
        request = self.context.get('request')
        photo_url = car.photo.url
        return request.build_absolute_uri(photo_url)
    # id = serializers.IntegerField()
    # image = serializers.ImageField()
    # title = serializers.CharField()
    # price = serializers.FloatField()


class ProductDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    title = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField()