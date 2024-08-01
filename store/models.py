from django.db import models
from user.models import User
from helper.models import PaymentMethodOptions
from helper.models import BaseModel

class Store(BaseModel):
    # created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    name=models.CharField(max_length=500,null=True,blank=True)
    email=models.EmailField(max_length=500,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    primary_phone=models.CharField(max_length=14,null=True,blank=True)
    map_link = models.URLField(blank=True,null=True)
    opening_time = models.TimeField(blank=True,null=True)
    closing_time = models.TimeField(blank=True,null=True)
    shown_in_website = models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    #off_days = ArrayField(models.CharField(max_length=15), default=list)

    logo = models.FileField(upload_to='images',null=True,blank=True)
    cover_photo = models.FileField(upload_to='images',null=True,blank=True)
    bio = models.CharField(max_length=100,null=True)
    about = models.TextField(null=True,blank=True)
    policies=models.TextField(null=True,blank=True)

    off_days = models.TextField(null=True, blank=True)  # Stores days as a comma-separated string

    def get_off_days(self):
        if self.off_days:
            return self.off_days.split(',')
        return None
    def __str__(self):
        return self.name


class StorePaymentMethod(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)
    
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=30, choices=PaymentMethodOptions.choices)
    name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self) :
        return self.store.name