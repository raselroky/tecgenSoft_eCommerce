from django.db import models
from helper.models import BaseModel
from product.models import ProductVariant
from user.models import User

class Wishlist(BaseModel):
    product_variant = models.ForeignKey(ProductVariant,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    

    class Meta:
        ordering = ['-created_at']
        db_table = 'wishlist'
        unique_together = ['product_variant','user']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['product_variant']),
            models.Index(fields=['user'])
        ]
    