from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# class CustomersAamarPayOnlineFullPaymentView(APIView):
#     permission_classes = (IsAuthenticated,)

#     @method_decorator(exception_handler)
#     def post(self, request, *args, **kwargs):
#         orders = get_object_or_404(Order, invoice_no=request.data['order'])
        
        
#         order_item=OrderItem.objects.filter(order=orders.id)
#         order_l=[]
#         pro_variant_l=[]
#         tmp_total=0
#         tmp=0
#         for i in order_item:
#             order_l.append(str(i))
#         for i in order_l:
#             order_itm=OrderItem.objects.get(id=i)
#             q=order_itm.quantity
#             x=order_itm.product_variant.id
#             y=order_itm.unit_price
#             #print(x,y,q)
#             cm=CampaignMember.objects.filter(product_variant__id=x).first()
#             deal=DealOfTheWeek.objects.filter(product_variant__id=x).first()
#             if cm:
#                 for j in range(0,q,1):
#                     tmp_total=float(get_overall_discount_calculated_values(x,y))
#                     tmp+=float(tmp_total)
#             elif(deal):
#                 for k in range(0,q,1):
#                     tmp_total=float(get_overall_discount_calculated_values(x,y))
#                     tmp+=float(tmp_total)
#             elif(order_itm.discount_type):
#                 discount_value=0
#                 if order_itm.discount_value>0:
#                     discount_value=0
#                 else:
#                     discount_value=order_itm.discount_value
#                 if order_itm.discount_type=='flat':
#                     for k in range(0,q,1):
#                         tmp_total=float(y)-float(discount_value)
#                         tmp+=float(tmp_total)
#                 elif order_itm.discount_type=='percentage':
#                     for k in range(0,q,1):
#                         tmp_total=float(y)-(float(discount_value)/100)
#                         tmp+=float(tmp_total)
#             else:
#                 tmp=float(y*q)
            
#             pro_variant_l.append(order_itm.product_variant.name)
#         #print(tmp)
#         s=''
#         cnt=0
#         for i in pro_variant_l:
#             cnt+=1
#             s+=str(i)
#             s+=', '
#         s=s[0:len(s)-2]
        
#         if not orders:
#             return Response({'message': 'order not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         due_amount = orders.order_due_amount
#         if due_amount <= 0:
#             return Response({'message': 'Payment already done for the order'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        
#         advance_payment=min(orders.order_due_amount,tmp)

       
#         transaction_number = identifier_builder(table_name='online_payments', prefix='OSL')
        
#         amarpay_data = {
#             'order_invoice':orders.invoice_no,
#             'opt_a': orders.id, #order id
#             'opt_b': request.user.username,
#             'number_of_item': orders.get_total_item_count,
#             'product_name':s,
#             'amount': advance_payment,
#             'tran_id': transaction_number,
#             'success_url': f'{settings.BACKEND_BASE_URL}/api/v1.0/payment/customer/advanced-payment-aamarpay-status',
#             'fail_url': f'{settings.BACKEND_BASE_URL}/api/v1.0/payment/customer/advanced-payment-aamarpay-status',
#             'cancel_url': f'{settings.BACKEND_BASE_URL}/api/v1.0/payment/customer/advanced-payment-aamarpay-status'
#         }
        
#         response = amarpay_payment_create(data=amarpay_data, customer=request.user)
#         if response.get('result') == 'true':
#             return Response({'payment_gateway_url': response['payment_url']}, status=status.HTTP_200_OK)
#         else:
#             error_response = {
#                 "message": "Error Response from Aamarpay",
#                 "code": "aamarpay_error",
#                 "detail": response
#             }
            
#             #pmd=Order.objects.filter(customer=self.request.user).first()
#             #print('user',self.request.user)
#             pmf=OnlinePayment.objects.filter(order__invoice_no=orders.invoice_no).first()
#             if(orders.order_due_amount>0 and pmf.status!='successful'):
#                 pmf.status='failed'
#                 pmf.save()
#             return Response(error_response, status=status.HTTP_417_EXPECTATION_FAILED)
