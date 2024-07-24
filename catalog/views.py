from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from catalog.models import Category,SubCategory,Brand
from catalog.serializers import CategorySerializer,SubCategorySerializer,BrandSerializer,AllCategoryChildSerializer
from rest_framework.views import APIView
import json
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.request import Request
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import  Prefetch, F, Sum


class CategoryListCreateAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='id'



class SubCategoryListCreateAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=SubCategory.objects.all()
    serializer_class=SubCategorySerializer

class SubCategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=SubCategory.objects.all()
    serializer_class=SubCategorySerializer
    lookup_field='id'



class BrandListCreateAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer

class BrandRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
    lookup_field='id'



class PublicAllCategoryListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AllCategoryChildSerializer
    search_fields = ['name','is_active']
    queryset = Category.objects.all().order_by('-created_at')