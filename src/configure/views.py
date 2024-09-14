from django.shortcuts import render
from .models import Banner,Country,MultipleAddress,PlatformCoupon,AllUsedCoupon
from .serializers import BannerSerializer,CountrySerializer,MultipleAddressSerializer
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
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now



class BannerListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    #@method_decorator(exception_handler)
    def create(self, request, *args, **kwargs):
        data = request.data.copy()  # Create a mutable copy of request.data
        
        data['created_by'] = request.user.id
        if Banner.objects.filter(name=request.data['name']).exists():
            return Response({"message": "This name already exists!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
         
        serializer.save(created_by=self.request.user.id)
       


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
        serializer.save(created_by=self.request.user.id)

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




class MultipleAddressListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=MultipleAddress.objects.all()
    serializer_class=MultipleAddressSerializer
    
    
    def create(self, request, *args, **kwargs):
        request.data['created_by'] = request.user.pk  # Save user's primary key

        # Create a serializer instance with the modified request data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the instance and return the response
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_queryset(self):
        #print(self.request.user)
        return MultipleAddress.objects.filter(created_by=self.request.user)
class MultipleAddressAllListAPIView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=MultipleAddress.objects.all()
    serializer_class=MultipleAddressSerializer
    
    
    def get_queryset(self):
        return MultipleAddress.objects.filter(created_by=self.request.user)

class MultipleAddressRetreiveUpdateDestroyListAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=MultipleAddress.objects.all()
    serializer_class=MultipleAddressSerializer
    lookup_field='id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        
        if data.get('is_active') is True:
            MultipleAddress.objects.filter(created_by=request.user, is_active=True).exclude(id=instance.id).update(is_active=False)
        
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.created_by != request.user:
            return Response({"message": "You do not have permission to delete this address."}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({"message": "address deleted successfully."}, status=status.HTTP_200_OK)




class ApplyCouponView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # tmp_coupon = 
        # tmp_amount = None
        coupon=request.data['coupon']
        
        try:
            tmp_coupon = PlatformCoupon.objects.get(code=coupon)
        except ObjectDoesNotExist:
            return Response(
                {"data": {"message": "Coupon : {}, Not Found.".format(coupon)}},
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        try:
            tmp_amount = float(tmp_coupon.value)
        except:
            return Response(
                {
                    "data": {
                        "message": "Amount : {}, Not possible to convert.".format(
                            tmp_coupon.value
                        )
                    }
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        #print(tmp_coupon,tmp_amount)
        if(tmp_coupon.used>=tmp_coupon.use_limit):
                return Response({"message":"Your minimum coupon usage limitation is over!"},status=status.HTTP_400_BAD_REQUEST)
        if tmp_coupon.status == False or tmp_coupon.type == 0:
            return Response(
                {
                    "data": {
                        "message": "Coupon : {}, Not Active or Invalid.".format(coupon)
                    }
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        # if tmp_coupon.active_eligibility and (tmp_amount > tmp_coupon.eligibility):
        #     print('dhuksee')
        #     return Response(
        #         {
        #             "data": {
        #                 "message": "Coupon : {}, Amount : {}, Minimum Order Amount : {}, not met.".format(
        #                     coupon, tmp_amount, tmp_coupon.eligibility
        #                 )
        #             }
        #         },
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
        if tmp_coupon.active_expiration and tmp_coupon.expire_date < now():
            return Response(
                {"data": {"message": "Coupon : {}, expired.".format(coupon)}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        
        

        if tmp_coupon.type == 1:  # FIXED/FLAT
            if(tmp_coupon.used>=tmp_coupon.use_limit):
                return Response({"message":"Your minimum coupon usage limitation is over!"},status=status.HTTP_400_BAD_REQUEST)
            tmp_discount =float(tmp_coupon.value)
            #print(tmp_coupon.value)
            if tmp_coupon.active_limitation and tmp_discount >= tmp_coupon.limitation:
                tmp_discount = tmp_coupon.limitation
            tmp_coupon.used += 1
            tmp_coupon.save()
            return Response(
                {
                    "data": {
                        "message": "Coupon : {}, Applied.".format(coupon),
                        "amount": float(tmp_discount),
                        "use_limit":tmp_coupon.use_limit,
                        "used":tmp_coupon.used
                        
                    }
                },
                status=status.HTTP_200_OK,
            )
        elif tmp_coupon.type == 2:  # PERCENTAGE
            if(tmp_coupon.used>tmp_coupon.use_limit):
                return Response({"message":"Your minimum coupon usage limitation is over!"},status=status.HTTP_400_BAD_REQUEST)
            tmp_discount = (float(tmp_coupon.value) / 100) * tmp_amount
            if tmp_coupon.active_limitation and tmp_discount >= tmp_coupon.limitation:
                tmp_discount = tmp_coupon.limitation
            tmp_coupon.used += 1
            tmp_coupon.save()
            return Response(
                {
                    "data": {
                        "message": "Coupon : {}, Applied.".format(coupon),
                        "amount": float(tmp_discount),
                        "use_limit":tmp_coupon.use_limit,
                        "used":tmp_coupon.used
                    }
                },
                status=status.HTTP_200_OK,
            )
        return Response({"data":"not found"},status=status.HTTP_204_NO_CONTENT)