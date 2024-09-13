from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from campaign.serializers import CampaignSerializer,CampaignMemberSerializer,DealOfTheWeekSerializer
from campaign.models import Campaign,CampaignMember,DealOfTheWeek
from product.models import ProductVariant
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
from helper.decorators import entries_to_remove

class CampaignListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Campaign.objects.all()
    serializer_class=CampaignSerializer

    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        if Campaign.objects.filter(name=request.data['name']):
            return Response({"message":"This name is already exist!"})
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CampaignRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Campaign.objects.all()
    serializer_class=CampaignSerializer
    removeable_keys = ('slug',)
    lookup_field='id'

    def update(self, request, *args, **kwargs):
        data = request.data.copy()  # This makes the QueryDict mutable

        # Remove unwanted keys and add 'updated_by'
        updated_request_data = entries_to_remove(data, self.removeable_keys)
        data.update(updated_request_data)
        data['updated_by'] = self.request.user.id

        # Pass the mutable data to the serializer
        serializer = self.get_serializer(instance=self.get_object(), data=data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Campaign deleted successfully."}, status=status.HTTP_200_OK)
    

class CampaignMemberListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=CampaignMember.objects.all()
    serializer_class=CampaignMemberSerializer
    removeable_keys = ('slug',)
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['created_by'] = request.user.id

        product_id = data.get('product_variant') 
        if product_id:
            product = ProductVariant.objects.filter(id=product_id).first()
            deal=DealOfTheWeek.objects.filter(product_variant__id=product_id)
            if deal:
                deal=DealOfTheWeek.objects.filter(product_variant__id=product_id).first()
            else:
                deal=None
            if product and (product.online_discount or deal):
                return Response(
                    {"detail": "Cannot add campaign member as the product has an active discount or deal."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CampaignMemberRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=CampaignMember.objects.all()
    serializer_class=CampaignMemberSerializer
    lookup_field='id'
    removeable_keys = ('slug',)

    def update(self, request, *args, **kwargs):
        data = request.data.copy()  # This makes the QueryDict mutable

        product_id = data.get('product_variant')
        
        if product_id:
            product = ProductVariant.objects.filter(id=product_id).first()
            deal=DealOfTheWeek.objects.filter(product_variant__id=product_id)
            if deal:
                deal=DealOfTheWeek.objects.filter(product_variant__id=product_id).first()
            else:
                deal=None
            
            if product and (product.online_discount or deal):
                return Response(
                    {"detail": "Cannot add deal-of-the-week as the product has an active discount or campaign."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        data['updated_by'] = self.request.user.id
        # Pass the mutable data to the serializer
        serializer = self.get_serializer(instance=self.get_object(), data=data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "CampaignMem deleted successfully."}, status=status.HTTP_200_OK)


class DealOfTheWeekListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=DealOfTheWeek.objects.all()
    serializer_class=DealOfTheWeekSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['created_by'] = request.user.id

        product_id = data.get('product_variant') 
        if product_id:
            product = ProductVariant.objects.filter(id=product_id).first()
            deal=DealOfTheWeek.objects.filter(product_variant__id=product_id)
            if deal:
                deal=DealOfTheWeek.objects.filter(product_variant__id=product_id).first()
            else:
                deal=None
            if product and (product.online_discount or deal):
                return Response(
                    {"detail": "Cannot add deal-of-the-week as the product has an active discount or campaign."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class DealOfTheWeekRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=DealOfTheWeek.objects.all()
    serializer_class=DealOfTheWeekSerializer
    lookup_field='id'
    
    def update(self, request, *args, **kwargs):
        #instance = self.get_object()
        data = request.data.copy()  # This makes the QueryDict mutable

        # Remove unwanted keys and add 'updated_by'
        # updated_request_data = entries_to_remove(data, self.removeable_keys)
        # data.update(updated_request_data)
        

        product_id = data.get('product_variant') 
        #print('hey',product_id)
        if product_id:
            product = ProductVariant.objects.filter(id=product_id).first()
            deal=DealOfTheWeek.objects.filter(product_variant__id=product_id)
            if deal:
                deal=DealOfTheWeek.objects.filter(product_variant__id=product_id).first()
            else:
                deal=None
            if product and (product.online_discount or deal):
                return Response(
                    {"detail": "Cannot add deal-of-the-week as the product has an active discount or campaign."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        data['updated_by'] = self.request.user.id
        # Pass the mutable data to the serializer
        serializer = self.get_serializer(instance=self.get_object(), data=data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "DealOfTheWeek deleted successfully."}, status=status.HTTP_200_OK)



class PublicCampaignListAPIView(ListAPIView):
    permission_classes=(AllowAny,)
    queryset=Campaign.objects.filter(is_active=True)
    serializer_class=CampaignSerializer

class PublicCampaignMemberListAPIView(ListAPIView):
    permission_classes=(AllowAny,)
    queryset=CampaignMember.objects.filter(is_active=True)
    serializer_class=CampaignMemberSerializer

class PublicDealOfTheWeekListAPIView(ListAPIView):
    permission_classes=(AllowAny,)
    queryset=DealOfTheWeek.objects.filter(is_active=True)
    serializer_class=DealOfTheWeekSerializer