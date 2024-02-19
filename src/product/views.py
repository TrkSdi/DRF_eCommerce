from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    Viewset for all categories
    """
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    Viewset for all brands
    """
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
class ProductViewSet(viewsets.ViewSet):
    """
    Viewset for all products
    """
    queryset = Product.objects.all()
    lookup_field = "slug"
    
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug), many=True)
        return Response(serializer.data)
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @action(methods=["GET"], 
            detail=False, # List
            url_path=f"category/(?P<cat_name>\w+)")
    def list_product_by_category(self, request, cat_name=None):
        """
        Endpoint to return product by category
        """
        serializer = ProductSerializer(
        self.queryset.filter(category__name=cat_name), many=True)
        return Response(serializer.data)