from rest_framework import serializers
from stock.models import Stock,StockHistory

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields='__all__'

class StockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=StockHistory
        fields='__all__'