from django.db import models
from helper.models import BaseModel


class Division(BaseModel):
    name = models.CharField(max_length=1000,unique=True,blank=True,null=True)
    
    def __str__(self):
        return str(self.name)



class District(BaseModel):
    division = models.ForeignKey(Division,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=1000,unique=True,blank=True,null=True)
    

    def __str__(self):
        return str(self.name)