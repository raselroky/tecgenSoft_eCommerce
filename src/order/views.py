from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from product.serializers import ProductUnitSeriaizer,ProductVariantSeriaizer,ProductvariantAttributeSeriaizer,ProductVariantReviewSeriaizer
from product.models import ProductUnit,ProductVariant,ProductVariantAttribute,ProductVariantReview
from user.models import User
from order.models import Order,OrderItem
from order.serializers import OrderCreateSerializer,OrderItemCreateSerializer,SellSerializer,SellItemListLiteSerializer
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
from helper.decorators import UnprocessableEntity
from helper.func_cal import remove_duplicate_from_list,entries_to_remove
from django.db import transaction
from configure.models import PlatformCoupon


class UserOrderCreateListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Order.objects.all()
    serializer_class=OrderCreateSerializer


    def get_serializer_class(self):
        if self.request.method.upper() == 'GET':
            return SellSerializer
        return self.serializer_class
    
    def has_exceeded_maximum_item_limit(self,raise_exception=False):
        if raise_exception:
            if len(self.request.data.get('sell_order_items')) > self.max_item_limit:
                raise UnprocessableEntity({"message": f"Maximum order item limit is {self.max_item_limit}"})
        else:
            assert len(self.request.data.get('sell_order_items')) < self.max_item_limit, (
                "maximum order item limit is %s" %self.max_item_limit
            )
        
    
    def create(self, request, *args, **kwargs):
        self.has_exceeded_maximum_item_limit(raise_exception=True)
        self.request.data['sell_order_items'] = list(remove_duplicate_from_list(
            self.request.data['sell_order_items'],lambda d: (d['product_variant'],d['country'])))
        
        process_obj = request.data
        if not process_obj.is_valid_order():
            return Response({"message":"Unprocessable Order."}, status=status.HTTP_400_BAD_REQUEST)
        
        returned_dict = process_obj.return_data()
        if returned_dict['discount_value_overlaps']:
            return Response({"message":"Discount Should Not be more than selling Price!"}, status=status.HTTP_400_BAD_REQUEST)
        if returned_dict['overlapped_product_variant_id_list']:
            raise UnprocessableEntity({
                "message": "Stock Limit Exeeded",
                "code": "stock_limit_exceed",
                "details":returned_dict['overlapped_product_variant_id_list']
            })
        # promo_code = self.request.data.get('code')
        # print('promo_code',promo_code)
        # promo_check=PlatformCoupon.objects.filter(code=promo_code).exists()
        # print('promo_check--:',promo_check)
        # if promo_check==False:
        #     return Response({'message': 'Promo is Not Valid With That Promo Code'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        requested_data = returned_dict['requested_data']
        requested_data['customer_type'] = request.user.customer_type
        order_serializer = self.serializer_class(data = requested_data)
        order_serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            order = order_serializer.save()
            for sell_item in requested_data['sell_order_items']:
                sell_item.update({'order': order.id})
                
            order_items_serializer = OrderItemCreateSerializer(data=requested_data['sell_order_items'], many=True)
            order_items_serializer.is_valid(raise_exception=True)
            order_items_serializer.save()

            
                     
           
        code=requested_data['promo']
        promo=PlatformCoupon.objects.filter(code=code)
        x=bool
        if(promo.exists()):
            promo=PlatformCoupon.objects.get(code=code)
            promo_amount=promo.value
            orders=Order.objects.filter(invoice_no=requested_data['invoice_no']).first()
            orders.order_net_amount=float(orders.order_net_amount)-float(promo_amount)
            orders.promo_deductable_amount=float(promo_amount)
            orders.order_due_amount=orders.order_net_amount
            orders.save()
        

        

        return Response({"payment_type":order.payment_type, 'invoice_no': order.invoice_no}, status=status.HTTP_201_CREATED)
        



class UserOnlineOrderListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SellItemListLiteSerializer
    queryset = Order.objects.select_related('customer', 'created_by', 'updated_by', 'terms_conditions').prefetch_related('orderitem_set').order_by('-created_at')
    
    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)