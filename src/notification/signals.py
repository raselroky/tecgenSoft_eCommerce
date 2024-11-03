from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.conf import settings
from django.db import transaction
from user.models import User
from .models import Notification
from rest_framework.response import Response


def send_notification(user_id, notification_message):
    try:
        if isinstance(notification_message, tuple):
            notification_message = ' '.join(notification_message)
        
        channel_layer = get_channel_layer()

        if channel_layer is not None:
            async_to_sync(channel_layer.group_send)(
                f'user_{user_id}', 
                {
                    'type': 'notify',
                    'message': notification_message
                }
            )
            response_data = {"status": 'Notification sent', "message": notification_message}
            print('okk,send success')
            return Response(response_data)

        return Response({'error': 'Channel layer is not available'}, status=500)

    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=404)



def create_notification(title,sender,recipients,verb,message):
    recipients = list(set(recipients))  # Ensure recipients are unique
    
    if recipients:
        for recipient in recipients:
            try:
                send_notification(recipient.id, message)
                
                Notification.objects.create(
                    title=title,
                    sender=sender,
                    recipient=recipient,
                    verb=verb,
                    message=message
                )
            except Exception as e:
                print(f"Error sending notification to user {recipient.id}: {e}")  # Debugging output
    else:
        print("No recipients to send notification.")
        #send_notification(i,message)
    


# @receiver(post_save, sender=OnlinePayment)
# def send_payment_notification(sender, instance, created, **kwargs):
#     """
#     This signal checks if the online payment is completed, canceled, or failed,
#     and sends notifications accordingly.
#     """
#     def create_notification_on_commit():
#         ord_items = OrderItem.objects.filter(order=instance.order)
#         recipients = [item.store.created_by for item in ord_items]
#         order = instance.order
#         #print('o',order)
#         if instance.status == 'successful':  # Payment is completed successfully
#             create_notification(
#                 'order (online_payment)',
#                 order.created_by,
#                 recipients,
#                 'created',
#                 f"{order.invoice_no} This Order has been placed successfully with online payment."
#             )
#         elif instance.status == 'failed' or instance.status == 'cancelled':  # Payment failed or canceled
#             create_notification(
#                 'order (incomplete_payment)',
#                 order.created_by,
#                 recipients,
#                 'incomplete_payment',
#                 f"{order.invoice_no} This Order was placed, but the payment failed or was canceled."
#             )

#     transaction.on_commit(create_notification_on_commit)


# @receiver(post_save, sender=Order)
# def send_order_notification(sender, instance, created, **kwargs):
#     if created and instance.payment_type != 'online_payment':
#         def create_notification_on_commit():
#             ord_items = OrderItem.objects.filter(order=instance)
#             recipients = [item.store.created_by for item in ord_items]
#             #print('done')
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification(
#                 'order',
#                 sender,
#                 recipients,
#                 'created',
#                 f"{instance.invoice_no} This Order has just been placed by {sender}."
#             )
#         transaction.on_commit(create_notification_on_commit)



# @receiver(post_save, sender=ProductVariantReview)
# def send_review_notification(sender, instance, created, **kwargs):
#     #print('dhukse')
#     if created:
#         #print('okk')
#         def create_notification_on_commit():
            
#             ord_items =ProductVariantReview.objects.filter(order__invoice_no=instance.order)
#             #print('ord',ord_items)
#             recipients = [item.product_variant.store.created_by for item in ord_items]
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification('reviews', sender, recipients, 'created',str(instance.order)+" This order has reviewed for "+str(instance.product_variant.name)+" by " +str(sender))
#             #print('done')
#         transaction.on_commit(create_notification_on_commit)



# @receiver(post_save, sender=ReturnItemRequest)
# def send_returnitem_notification(sender, instance, created, **kwargs):
    
#     if created:
#         def create_notification_on_commit():
#             ord_items =ReturnItemRequest.objects.filter(invoice_no=instance.invoice_no)
#             recipients = [item.product_variant.store.created_by for item in ord_items]
            
#             create_notification('return', instance.customer, recipients, 'created',str(instance.invoice_no)+" This order product is return"+str(instance.product_variant.name)+" by " +str(instance.customer))
#         transaction.on_commit(create_notification_on_commit)
        
            


# @receiver(post_save, sender=ProductCategory)
# def send_productcategory_notification(sender, instance, created, **kwargs):
   
#     if created:
#         def create_notification_on_commit():
            
#             admin_user=User.objects.filter(is_superuser=True,is_staff=True)
#             recipients = list(admin_user)
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification('productCategory', sender, recipients, 'created',str(instance.name)+" This productCategory is created by " +str(sender)+" and under this "+str(instance.group)+" Group.")
#         transaction.on_commit(create_notification_on_commit)


# @receiver(post_save, sender=ProductSubCategory)
# def send_productsubcategory_notification(sender, instance, created, **kwargs):
   
#     if created:
#         def create_notification_on_commit():
#             admin_user=User.objects.filter(is_superuser=True,is_staff=True)
#             recipients = list(admin_user)
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification('productSubcategory', sender, recipients, 'created',str(instance.name)+" This productSubcategory is created by " +str(sender)+" and under this "+str(instance.group)+" Group and "+str(instance.category)+" Category.")
#         transaction.on_commit(create_notification_on_commit)


# @receiver(post_save, sender=ProductBrand)
# def send_productbrand_notification(sender, instance, created, **kwargs):
   
#     if created:
#         def create_notification_on_commit():
#             admin_user=User.objects.filter(is_superuser=True,is_staff=True)
#             recipients = list(admin_user)
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification('productBrand', sender, recipients, 'created',str(instance.name)+" This productBrand is created by " +str(sender))
#         transaction.on_commit(create_notification_on_commit)


# @receiver(post_save, sender=Attribute)
# def send_attribute_notification(sender, instance, created, **kwargs):
   
#     if created:
#         def create_notification_on_commit():
#             admin_user=User.objects.filter(is_superuser=True,is_staff=True)
#             recipients = list(admin_user)
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification('attribute', sender, recipients, 'created',str(instance.name)+" This attribute is created by " +str(sender))
#         transaction.on_commit(create_notification_on_commit)


# @receiver(post_save, sender=AttributeValue)
# def send_attributevalue_notification(sender, instance, created, **kwargs):
   
#     if created:
#         def create_notification_on_commit():
#             admin_user=User.objects.filter(is_superuser=True,is_staff=True)
#             recipients = list(admin_user)
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification('attributeValue', sender, recipients, 'created',str(instance.name)+" This attributeValue is created by " +str(sender))
#         transaction.on_commit(create_notification_on_commit)


# @receiver(post_save, sender=ProductVariantAttribute)
# def send_productvariantattribute_notification(sender, instance, created, **kwargs):
   
#     if created:
#         def create_notification_on_commit():
#             admin_user=User.objects.filter(is_superuser=True,is_staff=True)
#             recipients = list(admin_user)
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification('productVariantAttribute', sender, recipients, 'created',str(instance.attribute.name)+'-'+str(instance.attribute_value.name)+" This productVariantAttribute is created by " +str(sender))
#         transaction.on_commit(create_notification_on_commit)


# @receiver(post_save, sender=Product)
# def send_product_notification(sender, instance, created, **kwargs):
   
#     if created:
#         def create_notification_on_commit():
#             admin_user=User.objects.filter(is_superuser=True,is_staff=True)
#             recipients = list(admin_user)
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification('baseProduct', sender, recipients, 'created',str(instance.name)+" This baseProduct is created by " +str(sender))
#         transaction.on_commit(create_notification_on_commit)



# @receiver(post_save, sender=Store)
# def send_store_notification(sender, instance, created, **kwargs):
   
#     if created:
#         def create_notification_on_commit():
#             admin_user=User.objects.filter(is_superuser=True,is_staff=True)
#             recipients = list(admin_user)
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification('store', sender, recipients, 'created',str(instance.name)+" This Store is created by " +str(sender))
#         transaction.on_commit(create_notification_on_commit)



# @receiver(post_save, sender=ProductVariant)
# def send_productvariant_notification(sender, instance, created, **kwargs):
   
#     if created:
#         def create_notification_on_commit():
#             admin_user=User.objects.filter(is_superuser=True,is_staff=True)
#             recipients = list(admin_user)
#             if instance.created_by:
#                 sender=instance.created_by
#             else:
#                 sender=None
#             create_notification('productVariant', sender, recipients, 'created',str(instance.name)+" This productVariant is created by " +str(sender))
#         transaction.on_commit(create_notification_on_commit)


# @receiver(post_save, sender=User)
# def send_users_notification(sender, instance, created, **kwargs):
   
#     if created:
#         print(instance)
#         def create_notification_on_commit():
#             admin_user=User.objects.filter(is_superuser=True,is_staff=True)
#             recipients = list(admin_user)
            
#             create_notification('user', instance, recipients, 'created',"This user Account is created by " +str(instance.username))
#         transaction.on_commit(create_notification_on_commit)