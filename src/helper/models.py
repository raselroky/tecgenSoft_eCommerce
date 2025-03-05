from django.db import models
from django.utils.translation import gettext_lazy as _


from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='created_%(class)ss', null=True, blank=True)
    updated_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='updated_%(class)ss', null=True, blank=True)

    class Meta:
        abstract = True
    
    


class CustomQuerySetManager(models.QuerySet):
    def filter_by_query(self,query_dict):
        return self.filter(**query_dict)
    
class PaymentMethodOptions(models.TextChoices):
    CASH_ON_DELIVERY = 'cash_on_delivery', 'cash_on_delivery'
    CASH = 'cash', 'cash'
    BANK = 'bank', 'Bank'
    CARD = 'card', 'card'
    MOBILE_BANK = 'mobile_bank', 'mobile_bank'
    ONLINE = 'online', 'online'

class DiscountTypeChoices(models.TextChoices):
    SELECT = 'select', _('select')
    FLAT = 'flat', _('flat')
    PERCENTAGE = 'percentage', _('percentage')

class PaymentStatusOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    UNPAID = 'unpaid', 'unpaid'
    PAID = 'paid', 'paid'
    DUE = 'due', 'due'

class OnlinePaymentStatusOptions(models.TextChoices):
    VALID = 'valid', 'valid'
    CANCELLED = 'cancelled', 'cancelled'
    UNATTEMPTED = 'unattempted', 'unattempted'
    FAILED = 'failed', 'failed'
    SUCCESSFUL = 'successful', 'successful'
    EXPIRED = 'expired', 'expired'

class DeliveryOptions(models.TextChoices):
    HOME_DELIVERY = 'home_delivery', ('home_delivery')
    STORE_PICKUP = 'store_pickup', ('store_pickup')
    STORE_SALE = 'store_sale', ('store_sale') 

class PaymentTypeOrderOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    CASH_ON_DELIVERY = 'cash_on_delivery', 'cash_on_delivery'
    ONLINE_PAYMENT = 'online_payment', 'online_payment'


class OrderStatusOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    PENDING = 'pending', 'pending'
    ON_PROCESS = 'on_process', 'on_process'
    COMPLETED = 'completed', 'completed'
    CANCELLED = 'cancelled', 'cancelled'


class OrderItemStatusOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    PENDING = 'pending', 'pending'
    CONFIRMED = 'confirmed', 'confirmed'
    OUT_FOR_DELIVERY = 'out_for_delivery', 'out_for_delivery'
    DELIVERED = 'delivered', 'delivered'
    CANCELLED = 'cancelled', 'cancelled'
    RETURNED = 'returned', 'returned'

class OnlinePaymentMethodOptions(models.TextChoices):
    SSL_ECOMMERCE = 'ssl_ecommerce', 'ssl_ecommerce'
    AAMARPAY = 'aamarpay', 'aamarpay'

class OnlinePaymentStatusOptions(models.TextChoices):
    VALID = 'valid', 'valid'
    CANCELLED = 'cancelled', 'cancelled'
    UNATTEMPTED = 'unattempted', 'unattempted'
    FAILED = 'failed', 'failed'
    SUCCESSFUL = 'successful', 'successful'
    EXPIRED = 'expired', 'expired'

class TransactionTypes(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    PURCHASE_RETURN = 'purchase_return', 'purchase_return'
    PURCHASE = 'purchase', 'purchase'
    STORE_SELL = 'store_sell', 'store_sell'
    ECOMMERCE_SELL = 'ecommerce_sell', 'ecommerce_sell'
    ECOMMERCE_RETURN = 'ecommerce_return', 'ecommerce_return'
    TRANSFERRED_IN = 'transferred_in', 'transferred_in'
    TRANSFERRED_OUT = 'transferred_out', 'transferred_out'
    IN = 'stock_in', 'stock_in'
    OUT = 'stock_out', 'stock_out'
    ADJUSTMENT = 'adjustment', 'adjustment'