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
    
    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        user = self.request.user
        if user.store:
            return Response({"message": "Can not create more than one store"},status=status.HTTP_403_FORBIDDEN)
        
        name = self.request.data['name']
        request.data['is_active']=False
        # request.data['district'] = get_object_or_404(
        #     District, id=request.data['district']).id 
        # request.data['division'] = get_object_or_404(
        #     Division, id=request.data['division']).id
        request.data['created_by'] = self.request.user.id
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        store = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        user.store = store
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class VendorStoreGetAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreSerializer
    queryset = Store.objects.filter()
    search_fields = ['name']
    
    def get_queryset(self):
        store = self.request.user.store
        return self.queryset.none() if not store else self.queryset.filter(id=store.id)
    
    
class VendorStoreRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreSerializer
    queryset = Store.objects.filter()
    lookup_field = 'id'




class PublicStoreListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = StoreLiteSerializer
    queryset = Store.objects.filter(shown_in_website=True)
    search_fields = [ 'name','store_category__slug']
    #filterset_class = StoreFilter
   
    