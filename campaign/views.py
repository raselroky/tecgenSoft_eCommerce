from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from campaign.serializers import CampaignSerializer,CampaignMemberSerializer,DealOfTheWeekSerializer
from campaign.models import Campaign,CampaignMember,DealOfTheWeek
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


class CampaignListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Campaign.objects.all()
    serializer_class=CampaignSerializer

    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        if Campaign.objects.filter(name=request.data['name']):
            return Response({"message":"This name is already exist!"})
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
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Campaign deleted successfully."}, status=status.HTTP_200_OK)
    

class CampaignMemberListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=CampaignMember.objects.all()
    serializer_class=CampaignMemberSerializer

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

class CampaignMemberRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=CampaignMember.objects.all()
    serializer_class=CampaignMemberSerializer
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "CampaignMem deleted successfully."}, status=status.HTTP_200_OK)


class DealOfTheWeekListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=DealOfTheWeek.objects.all()
    serializer_class=DealOfTheWeekSerializer

class DealOfTheWeekRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=DealOfTheWeek.objects.all()
    serializer_class=DealOfTheWeekSerializer
    lookup_field='id'

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