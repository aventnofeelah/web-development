from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

#/api/products/
class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#/api/products/<int:id>/
class ProductDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(Product, id=id)
    def get(self, request, id, format=None):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#/api/categories/
class CategoriesList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#/api/categories/<int:id>/
class CategoryDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(Category, id=id)
    def get(self, request, id, format=None):
        category = self.get_object(id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        category = self.get_object(id)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        category = self.get_object(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#/api/categories/<int:id>/products/
class CategoryProducts(APIView):
    def get(self, request, id, format=None):
        category = get_object_or_404(Category, id=id)

        products = category.products.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)