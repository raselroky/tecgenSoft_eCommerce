from django.db import models
from helper.models import DiscountTypeChoices
from user.models import Users
from product.models import ProductVariant


class Campaign(models.Model):
    created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='Campaign',null=True,blank=True)
    updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200, unique=True,null=True,blank=True)
    discount_type = models.CharField(max_length=20, choices=DiscountTypeChoices.choices)
    min_discount = models.FloatField(default=0)
    max_discount = models.FloatField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.URLField(null=True,blank=True)
    
    description = models.TextField(null=True,blank=True)
    terms_and_conditions = models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'campaigns'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active'])
        ]
        # Do we also need to index (start_date, end_date)

    def __str__(self):
        return str(self.name)


class CampaignMember(models.Model):

    created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='CampaignMember',null=True,blank=True)
    updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE,null=True,blank=True)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,null=True,blank=True)
    discount_type = models.CharField(max_length=10, choices=DiscountTypeChoices.choices)
    discount_value = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)


    class Meta:
        ordering = ['-created_at']
        db_table = 'campaign_members'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active'])
        ]

    def __str__(self):
        return str(self.campaign.name)


class DealOfTheWeek(models.Model):
    created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='DealOfTheWeek',null=True,blank=True)
    updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    product_variant = models.OneToOneField(ProductVariant, on_delete=models.CASCADE,null=True,blank=True)    
    discount_type = models.CharField(max_length=12, choices=DiscountTypeChoices.choices)
    discount_value = models.FloatField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
        db_table = 'deal_of_the_weeks'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active'])
        ]

    def __str__(self):
        return str(self.id)
