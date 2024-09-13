from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from store.models import Store,StorePaymentMethod
from store.serializers import StoreSerializer,StoreLiteSerializer,StorePaymentMethodSerializer
from rest_framework.views import APIView
from helper.tokens import create_tokens
from helper.caching import set_cache,get_cache,delete_cache
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


class VendorStoreCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = StoreSerializer
    queryset = Store.objects.filter()
    search_fields = ['name']
    
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
        serializer.save(created_by=self.request.user.id)



class VendorStoreListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreSerializer
    queryset = Store.objects.filter()
    search_fields = ['name','is_active','email']
    
    def get_queryset(self):
        store = self.request.user.store
        return self.queryset.none() if not store else self.queryset.filter(id=store.id)
    
    
class VendorStoreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreSerializer
    queryset = Store.objects.filter()
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Store deleted successfully."}, status=status.HTTP_200_OK)




class PublicStoreListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = StoreLiteSerializer
    queryset = Store.objects.filter(shown_in_website=True)
    search_fields = [ 'name','is_active','email']
    #filterset_class = StoreFilter
   
class PublicStoreRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = StoreLiteSerializer
    queryset = Store.objects.filter(shown_in_website=True)
    search_fields = [ 'name','is_active','email']
    lookup_field='id'