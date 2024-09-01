from rest_framework import serializers
from order.models import Order,OrderItem
from user.serializers import UserLiteSerializer
from helper.models import OrderItemStatusOptions
from payment.models import OnlinePayment
from payment.serializers import OnlinePaymentSerializer,OrderPaymentSerializer
from django.db.models import Sum,Q
from campaign.models import Campaign,CampaignMember,DealOfTheWeek
from helper.func_cal import get_overall_discount_calculated_values


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class SellSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    payments = serializers.SerializerMethodField(read_only=True)
    total_items_count = serializers.SerializerMethodField(read_only=True)
    total_items_quantity_count = serializers.SerializerMethodField(read_only=True)
    total_refund = serializers.SerializerMethodField(read_only=True)
    payments=serializers.SerializerMethodField()
    
    def get_total_refund(self, obj):
        #print('objjj',obj.created_by)
        refund_instance = obj.orderpaymentrefund_set.all().last()
        return 0 if not refund_instance else refund_instance.refund_amount

    def get_total_items_count(self,obj):
        
        return obj.orderitem_set.filter(~Q(status=OrderItemStatusOptions.CANCELLED)).count()
    
    def get_total_items_quantity_count(self,obj):
        return obj.orderitem_set.filter(~Q(status=OrderItemStatusOptions.CANCELLED)).values('quantity').aggregate(Sum('quantity'))['quantity__sum']

    def get_payments(self,obj):
        op=OnlinePayment.objects.filter(order__invoice_no=obj.invoice_no)
        #print(obj.status,op)
        return OrderPaymentSerializer(op,many=True).data

    def get_customer(self, obj):
        return UserLiteSerializer(obj.customer, read_only=True, many=False).data

    class Meta:
        model = Order
        fields = '__all__'


class SellItemListLiteSerializer(serializers.ModelSerializer):
    total_items_count = serializers.SerializerMethodField(read_only=True)
    total_items_quantity_count = serializers.SerializerMethodField(read_only=True)
    total_refund = serializers.SerializerMethodField(read_only=True)
    order_net_amount=serializers.SerializerMethodField()
    order_due_amount=serializers.SerializerMethodField()
    
    
    def get_total_refund(self, obj):
        refund_instance = obj.orderpaymentrefund_set.all().last()
        return 0 if not refund_instance else refund_instance.refund_amount
    
    def get_total_items_count(self,obj):
        return obj.orderitem_set.filter(~Q(status=OrderItemStatusOptions.CANCELLED)).count()
    
    def get_total_items_quantity_count(self,obj):
        return obj.orderitem_set.filter(~Q(status=OrderItemStatusOptions.CANCELLED)).values('quantity').aggregate(Sum('quantity'))['quantity__sum']
    
    def get_order_net_amount(self,obj):
        tmp_total = 0
        tmp=0
        o=obj.id
        oi=OrderItem.objects.filter(order=o)
        dv=0
        if oi:
            for i in oi:
                q=i.quantity
                x=i.product_variant.id
                y=i.unit_price
                #print(x,y,q)
                cm=CampaignMember.objects.filter(product_variant__id=x).first()
                deal=DealOfTheWeek.objects.filter(product_variant__id=x).first()
                if cm:
                    for j in range(0,q,1):
                        tmp_total=float(get_overall_discount_calculated_values(x,y))
                        tmp+=float(tmp_total)
                elif(deal):
                
                    for k in range(0,q,1):
                        tmp_total=float(get_overall_discount_calculated_values(x,y))
                        tmp+=float(tmp_total)
                elif(i.discount_type):
                    discount_value=0
                    if i.discount_value>0:
                        discount_value=0
                    else:
                        discount_value=i.discount_value
                    if i.discount_type=='flat':
                        for k in range(0,q,1):
                            tmp_total=float(y)-float(discount_value)
                            tmp+=float(tmp_total)
                    elif i.discount_type=='percentage':
                        for k in range(0,q,1):
                            tmp_total=float(y)-(float(discount_value)/100)
                            tmp+=float(tmp_total)
                else:
                    tmp+=float(y*q)
            #print(obj,tmp)
            promo=Order.objects.filter(invoice_no=obj.invoice_no)
            if promo.exists():
                promos=Order.objects.get(invoice_no=obj.invoice_no)
                tmp-=float(promos.promo_deductable_amount)
            #print(tmp)
            return tmp
        return tmp
    def get_order_due_amount(self,obj):
        tmp_total=0
        tmp=0
        o=obj.id
        oi=OrderItem.objects.filter(order=o)
        dv=0
        if oi:
            for i in oi:
                q=i.quantity
                x=i.product_variant.id
                y=i.unit_price
                #print(x,y,q)
                cm=CampaignMember.objects.filter(product_variant__id=x).first()
                deal=DealOfTheWeek.objects.filter(product_variant__id=x).first()
                if cm:
                    for j in range(0,q,1):
                        tmp_total=float(get_overall_discount_calculated_values(x,y))
                        tmp+=float(tmp_total)
                elif(deal):
                
                    for k in range(0,q,1):
                        tmp_total=float(get_overall_discount_calculated_values(x,y))
                        tmp+=float(tmp_total)
                elif(i.discount_type):
                    discount_value=0
                    if i.discount_value>0:
                        discount_value=0
                    else:
                        discount_value=i.discount_value
                    if i.discount_type=='flat':
                        for k in range(0,q,1):
                            tmp_total=float(y)-float(discount_value)
                            tmp+=float(tmp_total)
                    elif i.discount_type=='percentage':
                        for k in range(0,q,1):
                            tmp_total=float(y)-(float(discount_value)/100)
                            tmp+=float(tmp_total)
                else:
                    tmp+=float(y*q)
            
            promo=Order.objects.filter(invoice_no=obj.invoice_no)
            if promo.exists():
                promos=Order.objects.get(invoice_no=obj.invoice_no)
                tmp-=float(promos.promo_deductable_amount)
            order=float(obj.order_paid_amount)
            if order>0:
                return float(tmp-order)
            else:
                return float(tmp)
        return tmp
    
    class Meta:
        model = Order
        fields = [
            'id',
            'invoice_no',
            'created_at',
            'order_net_amount',
            'order_due_amount',
            'is_advance_payment_done',
            'total_items_count',
            'total_items_quantity_count',
            'total_refund',
            'status',
            'payment_type'
        ] 


class OnlineSellCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'