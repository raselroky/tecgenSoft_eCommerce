from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from user.models import UserAddress,User,Roles,RolePermissions
from user.serializers import UserSerializer,UserAddressSerializer,UserTokenSerializer,PermissionSerializer2,RolesSerializer,RolePermissionSerializer2,RolePermissionSerializerModify,RolePermissionsSerializer,UsersSerializer2
from django.contrib.auth.models import Permission
from rest_framework.views import APIView
from helper.tokens import create_tokens,generate_tokens_for_user
from helper.caching import set_cache,get_cache,delete_cache
import json
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.request import Request
import jwt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication
import logging
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.filters import SearchFilter, OrderingFilter


class UserListCreateAPIView(APIView):

    # def get(self,request):
    #     users=User.objects.filter(username=request.user.username)
    #     serializer=UserSerializer(users)
    #     return Response({"data":serializer.data})
    permission_classes=[AllowAny,]
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            201: openapi.Response('User created successfully', UserTokenSerializer),
            400: 'Invalid input'
        }
    )
    def post(self,request):
        
        username = request.data['username']
        email = request.data['email']
        users=User.objects.filter(username=username).exists()
        users_e=User.objects.filter(email=email).exists()
        if users:
            return Response({"message":"This username is already taken."})
        if users_e:
            return Response({"message":"This email is already taken."})
        user_serializer = UserSerializer(data=request.data)
        
        if user_serializer.is_valid():

            user_serializer.save()


            # access_token, refresh_token = create_tokens(user=user)
            # data = {
            #     'access_token': access_token,
            #     'refresh_token': refresh_token,
            #     }
            if User.objects.filter(username=username).exists():
                user=User.objects.get(username=username)
            token=generate_tokens_for_user(user)
            data = {
                'token': token,
                'username': user.username,
                'email': user.email
                }
            
            cache_key = f'{user.username}_token_data'
            set_cache(key=cache_key, value=json.dumps(UserTokenSerializer(user).data), ttl=2)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Login(APIView):
    permission_classes=(AllowAny,)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username or contact number of the user'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user'),
            },
            required=['username', 'password']
        ),
        responses={
            201: openapi.Response('Login successful', UserTokenSerializer),
            400: 'Invalid input',
            403: 'Inactive account',
            404: "User Doesn't exist"
        }
    )
    def post(self,request,*args, **kwargs):
    
        username = request.data['username']
        password = request.data['password']
        #print('user',username,password)
        if not username or not password:
            raise ValidationError(detail='username and password is required', code=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            #print('user exist')
            user = User.objects.get(username=username)
            
            if not user.check_password(password):
                #print('password not correct')
                return Response({"message": "Invalid Password."}, status=status.HTTP_400_BAD_REQUEST)
           # print('password is correct')      
            # access_token, refresh_token = create_tokens(user=user)
            # data = {
            #     'access_token': access_token,
            #     'refresh_token': refresh_token,
            # }
            token=generate_tokens_for_user(user)
            data = {
                'token': token,
                'username': user.username,
                'email': user.email,
                "role":user.role
                }
            
            cache_key = f'{user.username}_token_data'
            set_cache(key=cache_key, value=json.dumps(UserTokenSerializer(user).data), ttl=2)
           
            cached_data = get_cache(cache_key)

            return Response(data, status=status.HTTP_201_CREATED)
        
            
        #print('user doesnot exist')
        return Response({"message": "This username is not found, please sign up!"}, status=status.HTTP_404_NOT_FOUND)
    


class Logout(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self, request):
        
        user = self.request.user
        
        cache_key = f'{user.username}_token_data'
        cached_data = get_cache(cache_key)
        
        if cached_data:
            delete=delete_cache(cache_key)
            
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        return Response({"Message: you are already logout!"})
    




class ForgetPassword(APIView):
    permission_classes=(AllowAny,)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username or contact number of the user'),
                'date_of_birth': openapi.Schema(type=openapi.TYPE_STRING, description='date_of_birth of the user'),
                'new_password': openapi.Schema(type=openapi.TYPE_STRING, description='New Password of the user'),
            },
            required=['username','date_of_birth', 'new_password']
        ),
        responses={
            201: openapi.Response('New password set successful', UserTokenSerializer),
            400: 'Invalid input',
            403: 'Inactive account',
            404: "User Doesn't exist"
        }
    )
    def post(self,request):
        username=request.data['username']
        
        usr=User.objects.filter(username=username)
        if usr.exists():
            date_of_birth=request.data['date_of_birth']
            usr1=User.objects.filter(username=username,date_of_birth=date_of_birth)
            if usr1.exists():
                usr2=User.objects.filter(username=username,date_of_birth=date_of_birth).first()
                new_password=request.data['new_password']

                usr2.password=new_password
                usr2.save()
                return Response({"message":"Successfully set new Passowrd."},status=status.HTTP_200_OK)
            return Response({"message":"Date of Birth not correct,try again."},status=status.HTTP_404_NOT_FOUND)
        return Response({"message":"user doesn't exist,try again."},status=status.HTTP_404_NOT_FOUND)

        




class RefreshTokenAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token')
            },
            required=['refresh']
        ),
        responses={
            200: openapi.Response('Token refreshed successfully', openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access': openapi.Schema(type=openapi.TYPE_STRING, description='Access token'),
                }
            )),
            401: 'Invalid refresh token'
        }
    )
    def post(self, request, *args, **kwargs):
        
        refresh_token = request.data.get('refresh')
        
        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            new_access_token = str(refresh.access_token)

            return Response({
                'access': new_access_token
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)



class PermissionListAPIView(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer2
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'codename']
    pagination_class = None
    

    def get_queryset(self):
        role_id = self.request.query_params.get('role_id')
        if role_id:
            return Permission.objects.filter(roles__id=role_id)
        return super().get_queryset()

class RoleListCreateAPIView(ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    
class RoleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": True, "message": "Item is deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class RolePermissionsListCreateView(ListCreateAPIView):
    queryset = RolePermissions.objects.all()
    serializer_class = RolePermissionSerializer2
    permission_classes = [IsAuthenticated]  # You can add custom permission classes if needed


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class RolePermissionsListAPIView(ListAPIView):
    queryset = RolePermissions.objects.all()
    serializer_class = RolePermissionSerializerModify
    permission_classes = [IsAuthenticated] 


class RolePermissionsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = RolePermissions.objects.all()
    serializer_class = RolePermissionSerializer2
    permission_classes = [IsAuthenticated]
    lookup_field='id'


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": True, "message": "Item is deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



class RolePermissionsSearchCheckAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        id = request.data.get('id') 
        if not id:
            return Response({"error": "ID is required."}, status=400)

        checker = RolePermissions.objects.filter(role__id=id).first()
        if not checker:
            created_by_user = self.request.user
            checker = RolePermissions.objects.create(role_id=id,created_by=created_by_user)

        serializer = RolePermissionSerializerModify(checker)
        return Response(serializer.data, status=200)

class RolesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = RolesSerializer
    permission_classes = [IsAuthenticated,]
    queryset = Roles.objects.all()
    lookup_field='id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": True, "message": "Item is deleted successfully."}, status=status.HTTP_204_NO_CONTENT)




class UserGetRetrieve(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=User.objects.all()
    serializer_class=UsersSerializer2
    lookup_field='id'

    def get_queryset(self):
        user=self.request.user
        return User.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": True, "message": "Item is deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class UserListAPIView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=User.objects.all()
    serializer_class=UsersSerializer2
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id','email','first_name','last_name','age','phone','gender','username']
    
    def get_queryset(self):
        return User.objects.all()