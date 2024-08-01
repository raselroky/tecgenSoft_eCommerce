from django.shortcuts import render
from .models import Banner,Country
from .serializers import BannerSerializer,CountrySerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from rest_framework.views import APIView
from helper.tokens import create_tokens
from helper.caching import set_cache,get_cache,delete_cache
from helper.decorators import exception_handler
import json
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.request import Request
import jwt
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.utils.functional import SimpleLazyObject


class BannerListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    #@method_decorator(exception_handler)
    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        if Banner.objects.filter(name=request.data['name']):
            return Response({"message":"This name is already exist!"})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BannerRetrieveUpdateDestroyAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    lookup_field = 'id'
    
    def patch(self, request, *args, **kwargs):
        request.data['updated_by'] = request.user.id
        return super(BannerRetrieveUpdateDestroyAPIView, self).patch(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message":"Successfully Deleted!"}, status=status.HTTP_200_OK)
class BannerAllListAPIView(ListAPIView):
    permission_classes=(AllowAny,)
    queryset=Banner.objects.all()
    serializer_class=BannerSerializer


###Country
class CountryListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Country.objects.all()
    serializer_class=CountrySerializer

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

class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        request.data['updated_by'] = request.user.id
        return super(CountryRetrieveUpdateDestroyAPIView, self).patch(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Country deleted successfully."}, status=status.HTTP_200_OK)
class CountryAllListAPIView(ListAPIView):
    permission_classes=(AllowAny,)
    queryset=Country.objects.all()
    serializer_class=CountrySerializer
