from .models import Notification
from rest_framework import serializers


class AdminNotificationSerializer(serializers.ModelSerializer):
    recipient=serializers.SerializerMethodField()
    sender=serializers.SerializerMethodField()
    unread_count=serializers.SerializerMethodField()
    read_count=serializers.SerializerMethodField()
    order_invoice=serializers.SerializerMethodField()
    store=serializers.SerializerMethodField()

    def get_store(self,obj):
        sender = obj.sender
        if sender and hasattr(sender, 'store') and sender.store:
            return {
            'id': sender.store.id,
            'name': sender.store.name,
            'slug': sender.store.slug,
            'address': sender.store.address
        }
        return None
    def get_order_invoice(self,obj):
        y=''
        x=str(obj.message)
        for i in range(0,len(x),1):
            if x[i]==' ':
                break
            y+=x[i]
        return y
    def get_unread_count(self,obj):
        unread_count=0
        unread_count = Notification.objects.filter(is_read=False).count()
        return unread_count
    def get_read_count(self,obj):
        read_count=0
        read_count = Notification.objects.filter(is_read=True).count()
        return read_count
    def get_sender(self,obj):
        #print('sener',obj.sender)
        sender = obj.sender
        
        if sender:  
            return {
            "sender_username": sender.username,
            "sender_name": f"{sender.first_name} {sender.last_name}",
            "sender_address": sender.address,
            "sender_type": sender.type,
            }
    
    
        return None
        
        
    def get_recipient(self,obj):
        #print(obj.recipient)
        recipients = obj.recipient
        
        if recipients and recipients.type:
            types=recipients.type
            return {
            "recipient_username":recipients.username,
            "recipient_name":f"{recipients.first_name} {recipients.last_name}",
            "recipient_address":recipients.address,
            "recipient_type":types
        }
        else:
            types="Admin"
            return {
                "recipient_username":"Admin",
                "recipient_type":types
             }
        return None
    class Meta:
        model=Notification
        fields="__all__"
    