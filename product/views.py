from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from product.serializers import ProductUnitSeriaizer,ProductVariantSeriaizer,ProductvariantAttributeSeriaizer,ProductVariantReviewSeriaizer
from product.models import ProductUnit,ProductVariant,ProductVariantAttribute,ProductVariantReview
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



class ProductUnitListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=ProductUnit.objects.all()
    serializer_class=ProductUnitSeriaizer

    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductUnitRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=ProductUnit.objects.all()
    serializer_class=ProductUnitSeriaizer
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "ProductUnit deleted successfully."}, status=status.HTTP_200_OK)


class ProductVariantListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=ProductVariant.objects.all()
    serializer_class=ProductVariantSeriaizer

    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductVariantRetrieveUpdateDestroyListCreateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=ProductVariant.objects.all()
    serializer_class=ProductVariantSeriaizer
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "ProductVariant deleted successfully."}, status=status.HTTP_200_OK)


class ProductVariantAttributeListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=ProductVariantAttribute.objects.all()
    serializer_class=ProductvariantAttributeSeriaizer

    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductVariantAttributeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=ProductVariantAttribute.objects.all()
    serializer_class=ProductvariantAttributeSeriaizer
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "ProductVariantAttribute deleted successfully."}, status=status.HTTP_200_OK)

class ProductVariantReviewListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=ProductVariantReview.objects.all()
    serializer_class=ProductVariantReviewSeriaizer

    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductVariantReviewRetrieveUpdateDestroyAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=ProductVariantReview.objects.all()
    serializer_class=ProductVariantReviewSeriaizer
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "ProductVariantReview deleted successfully."}, status=status.HTTP_200_OK)







class PublicProductVariantListAPIView(ListAPIView):
    permission_classes=(AllowAny,)
    queryset=ProductVariant.objects.filter(is_active=True,show_in_ecommerce=True)
    serializer_class=ProductVariantSeriaizer
    search_fields=['name','is_active']
class PublicProductVariantRetrieveAPIView(RetrieveAPIView):
    permission_classes=(AllowAny,)
    queryset=ProductVariant.objects.filter(is_active=True,show_in_ecommerce=True)
    serializer_class=ProductVariantSeriaizer
    lookup_field='id'


class PublicProductVariantAttributeListAPIView(ListAPIView):
    permission_classes=(AllowAny,)
    queryset=ProductVariantAttribute.objects.filter(is_active=True)
    serializer_class=ProductvariantAttributeSeriaizer
    search_fields=['name','is_active']
class PublicProductVariantAttributeRetrieveAPIView(RetrieveAPIView):
    permission_classes=(AllowAny,)
    queryset=ProductVariantAttribute.objects.filter(is_active=True)
    serializer_class=ProductvariantAttributeSeriaizer
    lookup_field='id'

class PublicProductVariantReviewListAPIView(ListAPIView):
    permission_classes=(AllowAny,)
    queryset=ProductVariantReview.objects.filter(is_active=True)
    serializer_class=ProductVariantReviewSeriaizer
    search_fields=['name','is_active']
class PublicProductVariantReviewretRieveAPIView(RetrieveAPIView):
    permission_classes=(AllowAny,)
    queryset=ProductVariantReview.objects.filter(is_active=True)
    serializer_class=ProductVariantReviewSeriaizer
    lookup_field='id'