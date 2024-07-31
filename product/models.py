from django.db import models
from django.core.exceptions import ValidationError
from store.models import Store
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import Users
from catalog.models import Category,SubCategory,Brand,Attribute,AttributeValue


class ProductUnit(models.Model):
    created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='ProductUnit',null=True,blank=True)
    updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    unit=models.CharField(max_length=500,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return str(self.unit)

class ProductVariant(models.Model):
    created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='ProductVariant',null=True,blank=True)
    updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    name=models.CharField(max_length=500,null=True,blank=True) #frontend required
    description=models.TextField(null=True,blank=True)
    unit = models.ForeignKey(ProductUnit,on_delete=models.CASCADE,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True)
    store=models.ForeignKey(Store,on_delete=models.CASCADE,null=True,blank=True)
    images = models.JSONField(default=list)
    selling_price = models.FloatField(default=0)
    minimum_stock_quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_top_sale = models.BooleanField(default=False)
    is_upcoming = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    show_in_ecommerce = models.BooleanField(default=True)

    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    ordering = models.PositiveIntegerField(default=0)
    weight = models.FloatField(blank=True,null=True,help_text="Weight of this specific variant")


    def __str__(self) :
        return str(self.id)


class ProductVariantAttribute(models.Model):
    created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='ProductVariantAttribute',null=True,blank=True)
    updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,null=True,blank=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE,null=True,blank=True)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE,null=True,blank=True)
    
    price_increment = models.FloatField(blank=True,null=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'product_vairant_attributes'
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return str(self.id) 
    

class ProductVariantReview(models.Model):
    created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='ProductVariantReview',null=True,blank=True)
    updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,null=True,blank=True)
    #order = models.ForeignKey(to='orders.Order', on_delete=models.CASCADE, null=True)
    review = models.TextField(blank=True,null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    images = models.JSONField(default=list,blank=True,null=True)
    is_active = models.BooleanField(default=True)



    def __str__(self):
        return str(self.rating)
    