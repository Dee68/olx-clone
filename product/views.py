from django.shortcuts import render
from rest_framework import views
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class CategoryApiView(views.APIView):

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.viewable()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ParentCategoryListView(views.APIView):
    def get(self, request, *args):
        parents = Category.objects.parentsonly()
        serializer = CategorySerializer(parents, many=True)
        return Response(serializer.data)


class CategorySingleApiView(views.APIView):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)


class ProductApiView(views.APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
