from django.db import models
from helper.models import BaseModel


class Banner(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_banners',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_banners',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=150)
    url = models.URLField(null=True,blank=True)
    image = models.FileField(upload_to='images',null=True,blank=True)
    size = models.CharField(max_length=10,null=True,blank=True)
    is_active = models.BooleanField(default=False)
    ordering = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ["ordering"]
        db_table = "banners"
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["is_active"]),
        ]

    def __str__(self):
        return self.name


class Country(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=500,null=True,blank=True)
    currency_code = models.CharField(max_length=500,null=True,blank=True)
    code = models.CharField(max_length=500,null=True,blank=True)
    flag = models.URLField(null=True,blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        db_table = "country"
        indexes = [
            models.Index(fields=["currency_code"]),
            models.Index(fields=["code"]),
        ]