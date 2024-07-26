from django.db import models
from user.models import Users
from django.utils.translation import gettext_lazy as _

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
    FLAT = 'flat', _('flat')
    PERCENTAGE = 'percentage', _('percentage')