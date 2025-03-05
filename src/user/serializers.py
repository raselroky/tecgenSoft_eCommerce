from rest_framework import serializers
from user.models import User,UserAddress,Roles,RolePermissions
from django.contrib.auth.models import Permission


class UsersSerializer2(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=False)
    role = serializers.PrimaryKeyRelatedField(queryset=Roles.objects.all(), many=True, required=False, allow_null=True)
    email=serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ('id', 'username','email', 'first_name', 'last_name', 'photo', 'is_superadmin', 'is_active', 'gender', 'password', 'permissions', 'role')

    

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','contact_number','password']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'username', 'email', 'contact_number', 'is_active']

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'

    
class RolesSerializer(serializers.ModelSerializer):
    #permissions = serializers.SerializerMethodField()
    class Meta:
        model = Roles
        fields = "__all__"

class PermissionSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"
class RolePermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermissions
        fields = "__all__"

class RolePermissionSerializer2(serializers.ModelSerializer):
    permission = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True)

    class Meta:
        model = RolePermissions
        fields = ['id', 'role', 'permission']

    def create(self, validated_data):
        permissions = validated_data.pop('permission')  # Get permissions
        role_permissions = RolePermissions.objects.create(**validated_data)  # Create RolePermissions instance
        role_permissions.permission.set(permissions)  # Add the permissions to the instance
        role_permissions.save()
        return role_permissions
    
class RolePermissionSerializerModify(serializers.ModelSerializer):
    permission = PermissionSerializer2(many=True)
    role=serializers.SerializerMethodField()
    def get_role(self,obj):
        if obj.role:
            return {
                "id":obj.role.id,
                "role":obj.role.title
            }
        return None
    class Meta:
        model = RolePermissions
        fields = ['id', 'role', 'permission']