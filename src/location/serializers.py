from .models import District,Division
from rest_framework import serializers



class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Division
        fields='__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields='__all__'