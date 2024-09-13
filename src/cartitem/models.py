from django.db import models
from helper.models import BaseModel
from product.models import ProductVariant

class CartItem(BaseModel):
    product_variant=models.ForeignKey(ProductVariant,on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['-created_at']
        db_table = 'cart_item'
        indexes = [
            models.Index(fields=['-created_at']),
        ]
    def __str__(self):
        return str(self.product_variant.id)
