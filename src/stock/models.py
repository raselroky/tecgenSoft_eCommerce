from django.db import models
from helper.models import BaseModel,TransactionTypes
from product.models import ProductVariant
from store.models import Store
from configure.models import Country


class Stock(BaseModel):
    """ country wise product variant stock model """
    
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,null=True,blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,null=True,blank=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
        db_table = 'stocks'
        unique_together = ('store','product_variant','country')
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.store.name


class StockHistory(BaseModel):
    type = models.CharField(max_length=20, choices=TransactionTypes.choices)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,null=True,blank=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE,null=True,blank=True)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,null=True,blank=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    
    invoice_no = models.CharField(max_length=1000,blank=True,null=True) #deprecated

    class Meta:
        ordering = ['-created_at']
        db_table = 'stock_histories'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['type']),
            models.Index(fields=['invoice_no']),
        ]
    def __str__(self):
        return f'{self.pk}'