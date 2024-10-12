from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from user.models import UserAddress,User
from user.serializers import UserSerializer,UserAddressSerializer,UserTokenSerializer
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
            token=generate_tokens_for_user(user,expiration=24*60*60)
            data = {
                'token': token,
                'username': user.username,
                'email': user.email
                }
            
            cache_key = f'{user.username}_token_data'
            set_cache(key=cache_key, value=json.dumps(UserTokenSerializer(user).data), ttl=2*24*60*60)
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
            token=generate_tokens_for_user(user,expiration=2*24*60*60)
            data = {
                'token': token,
                'username': user.username,
                'email': user.email
                }
            
            cache_key = f'{user.username}_token_data'
            set_cache(key=cache_key, value=json.dumps(UserTokenSerializer(user).data), ttl=2*24*60*60)
           
            cached_data = get_cache(cache_key)

            return Response(data, status=status.HTTP_201_CREATED)
        
            
        #print('user doesnot exist')
        return Response({"message": "This username is not found, please sign up!"}, status=status.HTTP_404_NOT_FOUND)
    


class Logout(APIView):
    permission_classes=(IsAuthenticated,)

    # @swagger_auto_schema(
    #         request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         properties={
    #             'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username or contact number of the user'),
    #         },
    #         required=['username']
    #     ),
    #     responses={
    #         200: openapi.Response('Successfully logged out', openapi.Schema(
    #             type=openapi.TYPE_OBJECT,
    #             properties={
    #                 'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message')
    #             }
    #         )),
    #     }
    # )
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