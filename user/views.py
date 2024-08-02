from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from user.models import UserAddress
from user.serializers import UserSerializer,UserAddressSerializer,UserTokenSerializer
from rest_framework.views import APIView
from helper.tokens import create_tokens
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

User = get_user_model()

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
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email
                }
            cache_key = f'{user.username}_token_data'
            set_cache(key=cache_key, value=json.dumps(UserTokenSerializer(user).data), ttl=5*60*60)
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
        if not username or not password:
            raise ValidationError(detail='username and password is required', code=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            
            if not user.check_password(password):
                return Response({"message": "Invalid Password."}, status=status.HTTP_401_UNAUTHORIZED)
                        
            # access_token, refresh_token = create_tokens(user=user)
            # data = {
            #     'access_token': access_token,
            #     'refresh_token': refresh_token,
            # }
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email
                }
            
            cache_key = f'{user.username}_token_data'
            set_cache(key=cache_key, value=json.dumps(UserTokenSerializer(user).data), ttl=5*60*60)
           
            # cached_data = get_cache(cache_key)
            # print('cache',cached_data)
            return Response(data, status=status.HTTP_201_CREATED)
        
            
        
        return Response({"message": "This username is not found, please sign up!"}, status=status.HTTP_404_NOT_FOUND)
    


class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=(AllowAny,)

    @swagger_auto_schema(
            request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username or contact number of the user'),
            },
            required=['username']
        ),
        responses={
            200: openapi.Response('Successfully logged out', openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message')
                }
            )),
        }
    )
    def post(self, request):
        username = request.data['username']
        key= request.data['key']
        if User.objects.filter(username=username).exists():
            user=User.objects.get(username=username)
        try:
            token = Token.objects.get(user=user,key=key)
            token.delete()
            delete_cache(username)
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"message": "Token not found"}, status=status.HTTP_404_NOT_FOUND)






class refreshed_token(APIView) :
    permission_classes=(AllowAny,)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token of the user'),
            },
            required=['refresh_token']
        ),
        responses={
            201: openapi.Response('Token refreshed successfully', openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access_token': openapi.Schema(type=openapi.TYPE_STRING, description='New access token'),
                    'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='New refresh token'),
                }
            )),
            400: 'No refresh token provided',
            401: 'User is not active or token is invalid'
        }
    )
    def post(self,request):
        refreshed_token = request.data.get('refresh_token')
        try:
            payload = jwt.decode(jwt=refreshed_token, key=settings.SECRET_KEY, algorithms='HS256', verify=True)
            if payload['token_type'] != 'refresh':
                return JsonResponse(data={
                    'message': 'no refresh token provided',
                    'success': False
                }, status=400)
            user_name = payload.get('username')
            user_obj = get_object_or_404(User, username=user_name)
            delete_cache(f'{user_obj.username}_token_data')
            if not user_obj.is_active:
                raise ValidationError(detail='user is not active', code=status.HTTP_401_UNAUTHORIZED)
            access_token, refresh_token = create_tokens(user=user_obj)
            data = {
                'access_token': access_token,
                'refresh_token': refresh_token,
            }
            set_cache(key=f'{user_obj.username}_token_data', value=json.dumps(UserTokenSerializer(user_obj).data), ttl=5*60*60)
            return Response(data=data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return JsonResponse(data={
                'message': f'{str(err)}',
                'success': False,
            }, status=401)