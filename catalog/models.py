from django.db import models
from user.models import Users
from helper.models import CustomQuerySetManager

# class BaseModel(models.Model):
#     created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
#     updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    name=models.CharField(max_length=500,unique=True)
    show_in_ecommerce=models.BooleanField(default=False)
    ordering = models.PositiveIntegerField(default=0)
    icon=models.FileField(upload_to='iamges',null=True,blank=True)
    logo=models.FileField(upload_to='images',null=True,blank=True)
    is_active=models.BooleanField(default=0)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    
    name=models.CharField(max_length=500,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    show_in_ecommerce=models.BooleanField(default=False)
    ordering = models.PositiveIntegerField(default=0)
    icon=models.FileField(upload_to='iamges',null=True,blank=True)
    logo=models.FileField(upload_to='images',null=True,blank=True)
    is_active=models.BooleanField(default=0)



    def __str__(self):
        return self.name



class Brand(models.Model):
    created_by=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='created_%(class)ss',null=True,blank=True)
    updated_by=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    name=models.CharField(max_length=500,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True)
    show_in_ecommerce=models.BooleanField(default=False)
    ordering = models.PositiveIntegerField(default=0)
    icon=models.FileField(upload_to='iamges',null=True,blank=True)
    logo=models.FileField(upload_to='images',null=True,blank=True)
    is_active=models.BooleanField(default=0)

    def __str__(self):
        return self.name