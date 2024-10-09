from django.db import models
from helper.models import CustomQuerySetManager,BaseModel



class Category(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)


    name=models.CharField(max_length=500,null=True,blank=True)
    show_in_ecommerce=models.BooleanField(default=False)
    ordering = models.PositiveIntegerField(default=0)
    icon=models.JSONField(default=list)
    logo=models.JSONField(default=list)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class SubCategory(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    
    name=models.CharField(max_length=500,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    show_in_ecommerce=models.BooleanField(default=False)
    ordering = models.PositiveIntegerField(default=0)
    icon=models.JSONField(default=list)
    logo=models.JSONField(default=list)
    is_active=models.BooleanField(default=True)



    def __str__(self):
        return str(self.name)



class Brand(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)


    name=models.CharField(max_length=500,null=True,blank=True)
    #category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True)
    show_in_ecommerce=models.BooleanField(default=False)
    ordering = models.PositiveIntegerField(default=0)
    icon=models.JSONField(default=list)
    logo=models.JSONField(default=list)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
    



class Attribute(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    

    class Meta:
        ordering = ['-created_at']
        db_table = 'attributes'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return str(self.name)


class AttributeValue(BaseModel):
    # created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    # updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='updated_%(class)ss',null=True,blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'attribute_values'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return str(self.name)