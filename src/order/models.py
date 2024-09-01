from django.db import models
from helper.models import DeliveryOptions,PaymentStatusOptions,OrderStatusOptions,PaymentTypeOrderOptions,DiscountTypeChoices,OrderItemStatusOptions
from configure.models import Country
from product.models import ProductVariant,ProductVariantAttribute,ProductUnit
from store.models import Store,StorePaymentMethod
from helper.models import BaseModel
from django.contrib.auth import get_user_model
from user.models import User

class Order(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    invoice_no = models.CharField(max_length=500, unique=True)    
    delivery_method = models.CharField(
        max_length=100, choices=DeliveryOptions.choices, default=DeliveryOptions.HOME_DELIVERY)
    payment_status = models.CharField(
        choices=PaymentStatusOptions.choices, max_length=100, default=PaymentStatusOptions.UNPAID)
    status = models.CharField(
        max_length=50, choices=OrderStatusOptions.choices, default=OrderStatusOptions.PENDING)
    payment_type = models.CharField(
        max_length=30, choices=PaymentTypeOrderOptions.choices, default=PaymentTypeOrderOptions.CASH_ON_DELIVERY)
    
    # customer and receiver info
    customer = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    receiver_name = models.CharField(max_length=500,null=True,blank=True)
    receiver_contact = models.CharField(max_length=15,null=True,blank=True)
    note = models.TextField(null=True, blank=True)
    address = models.TextField(null=True,blank=True)
    
    # order items
    items_total_discount = models.FloatField(default=0) #total discount of items
    items_total_price_without_discount = models.FloatField(default=0) #only items total price
    items_total_price = models.FloatField(default=0) #total price of items after deducting discount
    
    # discounts
    promo_code=models.CharField(max_length=1000,null=True,blank=True)
    promo_deductable_amount = models.FloatField(default=0) #amount that has been decreased by using promo
    order_total_discount_amount = models.FloatField(default=0) #final discount of order including all type of discounts

    order_net_amount = models.FloatField(default=0) #shipping charges may be included
    order_due_amount = models.FloatField(default=0) #shipping charges may be included
    order_paid_amount = models.FloatField(null=True,blank=True) # overall paid amount
    order_net_amount_without_shipping = models.FloatField(default=0,null=True) #order price without shipping charge
    
    # # extra charges
    # additional_charge = models.FloatField(default=0)
    # total_tax_amount = models.FloatField(default=0)

    # advance_payment_percentage = models.FloatField(default=0)
    advance_payment = models.FloatField(default=0)
    # is_advance_payment_done = models.BooleanField(default=False)
    is_shipping_charge_added = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        db_table = 'orders'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status']),
            models.Index(fields=['payment_status']),
            models.Index(fields=['delivery_method']),
        ]

    def __str__(self):
        return self.invoice_no
    
    @property
    def get_total_item_count(self):
        return self.orderitem_set.all().count()



class OrderItem(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=True)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,null=True,blank=True)
    store = models.ForeignKey(Store,on_delete=models.CASCADE,null=True,blank=True)
    
    product_variant_attributes = models.ManyToManyField(ProductVariantAttribute,null=True,blank=True)
    item_unit_type = models.ForeignKey(ProductUnit,on_delete=models.CASCADE,null=True,blank=True)
    
    
    quantity = models.IntegerField(default=0)
    selling_price = models.FloatField(default=0)
    unit_price = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    
    discount_amount = models.FloatField(default=0)
    discount_value = models.FloatField(default=0)
    discount_type = models.CharField(max_length=10, choices=DiscountTypeChoices.choices, null=True, blank=True)
    
    campaign_member_discount = models.FloatField(default=0)
    deal_of_the_week_discount = models.FloatField(default=0)
    
    # overall discount(discount_amount+campaign_member_discount+deal_of_the_week_discount)
    total_discount = models.FloatField(default=0)
    # selling_price(attribute price added if exists) * quantity
    sub_total = models.FloatField(default=0)

    additional_charge = models.FloatField(default=0)
    shipping_charge = models.FloatField(default=0)
    total_weight = models.FloatField(help_text="Product Variant Weight * Quantity")
    
    status = models.CharField(max_length=20,null=True,blank=True,choices=OrderItemStatusOptions.choices)
    
    
    commission_calculation=models.TextField(null=True,blank=True,default="No calculation")
    
    
    class Meta:
        unique_together = ['order','product_variant','country']
        ordering = ['-created_at']
        db_table = 'order_items'
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return str(self.id)


class OrderPayment(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    payment_voucher = models.CharField(max_length=150, null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    payment_method = models.ForeignKey(StorePaymentMethod, on_delete=models.CASCADE, null=True,blank=True)

    paid_amount = models.FloatField(default=0)
    online_payment = models.ForeignKey('payment.OnlinePayment', on_delete=models.CASCADE, null=True,blank=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'order_payments'
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return str(self.id)