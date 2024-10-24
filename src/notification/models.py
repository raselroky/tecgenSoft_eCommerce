from django.db import models
from user.models import User
from helper.models import BaseModel,DiscountTypeChoices

class Notification(BaseModel):
    title=models.CharField(max_length=255,null=True,blank=True)
    sender = models.ForeignKey(User, related_name='sent_notifications', on_delete=models.CASCADE,null=True,blank=True)
    recipient=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    verb = models.CharField(max_length=500,null=True,blank=True)
    message=models.CharField(max_length=1000,null=True,blank=True)
    is_read=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        
        verbose_name_plural = "Notification"
        ordering = ["-id"]
        db_table = "notification"
    
    def __str__(self) :
        return str(self.title)+' '+str(self.sender.username)
