from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from stock.models import Stock,StockHistory
from stock.serializers import StockSerializer,StockHistorySerializer
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



class StockListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Stock.objects.all()
    serializer_class=StockSerializer

class StockRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Stock.objects.all()
    serializer_class=StockSerializer
    lookup_field='id'

    def update(self, request, *args, **kwargs):
        data = request.data.copy()  # This makes the QueryDict mutable

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


class StockHistoryListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=StockHistory.objects.all()
    serializer_class=StockHistorySerializer


class StockHistoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=StockHistory.objects.all()
    serializer_class=StockHistorySerializer
    lookup_field='id'

    def update(self, request, *args, **kwargs):
        data = request.data.copy()  # This makes the QueryDict mutable

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