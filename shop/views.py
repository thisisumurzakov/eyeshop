from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CategoryListSerializer, ProductListSerializer
from .models import Category, Product


class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Category.objects.filter(gender=self.kwargs['gender'])


class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['pk'])

class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (AllowAny,)


class ProductListAllView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        products = Product.objects.all()
        return Response(status=200, data=ProductListSerializer(products, many=True).data)


