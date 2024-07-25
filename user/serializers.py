from rest_framework import serializers
from user.models import Users,UserAddress


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = Users
        fields = ['username', 'first_name','password']

    def create(self, validated_data):
        user = Users.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'contact_number', 'is_active']

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'