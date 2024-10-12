from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from catalog.models import Category,SubCategory,Brand,Attribute,AttributeValue
from catalog.serializers import CategorySerializer,SubCategorySerializer,BrandSerializer,AllCategoryChildSerializer,AttributeSerializer,AttributeValueSerializer
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
    searh_fields=['name']
    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        if Category.objects.filter(name=request.data['name']):
            return Response({"message":"This name is already exist!"})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Category deleted successfully."}, status=status.HTTP_200_OK)




class UserCateogryAllListAPIView(ListAPIView):
    permission_classes=[AllowAny,]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class SubCategoryListCreateAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=SubCategory.objects.all()
    serializer_class=SubCategorySerializer
    searh_fields=['name']
    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        if SubCategory.objects.filter(name=request.data['name']):
            return Response({"message":"This name is already exist!"})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SubCategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=SubCategory.objects.all()
    serializer_class=SubCategorySerializer
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "SubCategory deleted successfully."}, status=status.HTTP_200_OK)

class UserSubCateogryAllListAPIView(ListAPIView):
    permission_classes=[AllowAny,]
    queryset=SubCategory.objects.all()
    serializer_class=SubCategorySerializer


class BrandListCreateAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
    searh_fields=['name']
    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        if Brand.objects.filter(name=request.data['name']):
            return Response({"message":"This name is already exist!"})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class BrandRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Brand deleted successfully."}, status=status.HTTP_200_OK)


class UserBrandAllListAPIView(ListAPIView):
    permission_classes=[AllowAny,]
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer


class PublicAllCategoryListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AllCategoryChildSerializer
    search_fields = ['name','is_active']
    queryset = Category.objects.all().order_by('-created_at')




class AttributeListCreateAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=Attribute.objects.all()
    serializer_class=AttributeSerializer
    searh_fields=['name']

    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        if Attribute.objects.filter(name=request.data['name']):
            return Response({"message":"This name is already exist!"})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AttributeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=Attribute.objects.all()
    serializer_class=AttributeSerializer
    searh_fields=['name']
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Attribute deleted successfully."}, status=status.HTTP_200_OK)



class AttributevalueListCreateAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=AttributeValue.objects.all()
    serializer_class=AttributeValueSerializer
    searh_fields=['name']

    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        if AttributeValue.objects.filter(name=request.data['name']):
            return Response({"message":"This name is already exist!"})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class AttributevalueRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=AttributeValue.objects.all()
    serializer_class=AttributeValueSerializer
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "AttributeValue deleted successfully."}, status=status.HTTP_200_OK)