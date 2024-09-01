from rest_framework import serializers
from payment.models import OnlinePayment,OrderPaymentModel


class OnlinePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlinePayment
        fields = '__all__'

        

class OrderPaymentSerializer(serializers.ModelSerializer):
    
    online_payment = OnlinePaymentSerializer(read_only=True)
    class Meta:
        model = OrderPaymentModel
        fields = '__all__'