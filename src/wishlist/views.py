from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from wishlist.serializers import WishlistSeriallizer
from wishlist.models import Wishlist
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
from django.utils.timezone import now,timedelta
from campaign.models import Campaign,CampaignMember,DealOfTheWeek
import logging
from django.db.models import Min, Max, Sum, Q, Count, F, Prefetch, Avg
from helper.decorators import entries_to_remove

logger = logging.getLogger('django')




class UserWishlistListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Wishlist.objects.all()
    serializer_class=WishlistSeriallizer
    search_fields=['product_variant__name','product_variant__id']
    
    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        product_variant_id=data.get('product_variant')
        if product_variant_id:
            if Wishlist.objects.filter(product_variant__id=product_variant_id).exists():
                return Response({"message":"This productVariant is already added your wishlist!"},status=status.HTTP_400_BAD_REQUEST)


        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.id)
    
    def get_queryset(self):
        qs=Wishlist.objects.filter(created_by=self.request.user)
        return qs



class UserWislistListRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Wishlist.objects.all()
    serializer_class=WishlistSeriallizer
    lookup_field='id'
    
    def get_queryset(self):
        qs=Wishlist.objects.filter(created_by=self.request.user)
        return qs

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": True, "message": "This Item deleted from Wishlist, successfully."}, status=status.HTTP_204_NO_CONTENT)