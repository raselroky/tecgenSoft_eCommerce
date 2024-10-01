from django.db import models
from django.core.exceptions import ValidationError
from store.models import Store
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import User
from catalog.models import Category,SubCategory,Brand,Attribute,AttributeValue
from helper.models import BaseModel,DiscountTypeChoices
from configure.models import Country
from django.forms.models import model_to_dict

class ProductUnit(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    unit=models.CharField(max_length=500,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return str(self.unit)

class ProductVariant(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    name=models.CharField(max_length=500,null=True,blank=True) #frontend required
    description=models.TextField(null=True,blank=True)
    unit = models.ForeignKey(ProductUnit,on_delete=models.CASCADE,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True)
    store=models.ForeignKey(Store,on_delete=models.CASCADE,null=True,blank=True)
    images = models.JSONField(default=list)
    discount_type=models.CharField(max_length=500,choices=DiscountTypeChoices.choices,default='select')
    online_discount=models.FloatField(default=0)
    selling_price = models.FloatField(default=0)
    minimum_stock_quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_top_sale = models.BooleanField(default=False)
    is_upcoming = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    show_in_ecommerce = models.BooleanField(default=True)
    free_delivery=models.BooleanField(default=False)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    ordering = models.PositiveIntegerField(default=0)
    weight = models.FloatField(blank=True,null=True,help_text="Weight of this specific variant")

    promo=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self) :
        if self.name==None:
            return str(self.id)
        return str(self.name)
        




class ProductVariantAttribute(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    
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
    

class ProductVariantReview(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,null=True,blank=True)
    #order = models.ForeignKey(to='orders.Order', on_delete=models.CASCADE, null=True)
    review = models.TextField(blank=True,null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    images = models.JSONField(default=list,blank=True,null=True)
    is_active = models.BooleanField(default=True)



    def __str__(self):
        return str(self.rating)
    


class QuantityWiseProductVariantPrice(BaseModel):
    product_variant = models.ForeignKey(ProductVariant,on_delete=models.CASCADE,null=True,blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=True)
    min_quantity = models.PositiveIntegerField(default=0)
    selling_price = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.product_variant.id)+' '+str(self.country.name)

class CountryWiseProductVariant(BaseModel):
        
    product_variant = models.ForeignKey(ProductVariant,on_delete=models.CASCADE,null=True,blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=True)
    
    customs_charge = models.FloatField(default=0)
   
    per_kg_charge = models.FloatField(null=True)
    shipment_charge = models.FloatField(null=True,blank=True)
    
    def __str__(self):
        return str(self.product_variant.name)+' '+str(self.country.name)

