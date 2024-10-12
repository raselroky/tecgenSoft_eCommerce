from django.db import models
from order.models import Order,OrderItem
from helper.models import OnlinePaymentMethodOptions,OnlinePaymentStatusOptions,PaymentMethodOptions
from user.models import User
from helper.models import BaseModel


class OnlinePayment(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    transaction_number = models.SlugField(max_length=200, blank=False, null=False, unique=True)
    payment_method = models.CharField(max_length=15, choices=OnlinePaymentMethodOptions.choices) # payment gateway choice
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    amount = models.FloatField(default=0) 
    status = models.CharField(max_length=15, choices=OnlinePaymentStatusOptions.choices)
    has_hit_ipn = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        db_table = 'online_payments'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status']),
            models.Index(fields=['payment_method']),
        ]

    def __str__(self):
        return str(self.transaction_number)

class OrderPaymentModel(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    paid_amount = models.FloatField(default=0)
    
    payment_method = models.CharField(max_length=30,choices=PaymentMethodOptions.choices)
    online_payment = models.ForeignKey(OnlinePayment, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return str(self.order.invoice_no)