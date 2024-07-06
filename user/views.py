from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from user.models import Users,UserAddress
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


class UserListCreateAPIView(APIView):

    # def get(self,request):
    #     users=User.objects.filter(username=request.user.username)
    #     serializer=UserSerializer(users)
    #     return Response({"data":serializer.data})
    permission_classes=[AllowAny,]
    def post(self,request):

        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user=user_serializer.save()


            access_token, refresh_token = create_tokens(user=user)
            data = {
                'access_token': access_token,
                'refresh_token': refresh_token,
                }
            set_cache(key=f'{user.username}_token_data', value=json.dumps(UserTokenSerializer(user).data), ttl=5*60*60)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([AllowAny])
def login_with_password(request: Request) -> Response:
    username = request.data['username']
    password = request.data['password']
    if not username or not password:
        raise ValidationError(detail='contact number and password is required', code=status.HTTP_400_BAD_REQUEST)
    try:
        x=str(username)
        y=x[0]+x[1]+x[2]
       
        if(y=='+88'):
            usernamea=x
            usernameb=x[3:14]
            if(Users.objects.filter(username=usernamea).exists()):
                user = Users.objects.get(username__exact=usernamea)
                #print('+88')
            elif(Users.objects.filter(username=usernameb).exists()):
                user = Users.objects.get(username__exact=usernameb)
                #print('013',user)
            else:
                raise ValidationError(detail="User Doesn't exist.",code=status.HTTP_404_NOT_FOUND)
        else:
            usernamea=x
            usernameb='+88'+x
            if(Users.objects.filter(username=usernamea).exists()):
                user = Users.objects.get(username__exact=usernamea)
            elif(Users.objects.filter(username=usernameb).exists()):
                user = Users.objects.get(username__exact=usernameb)
            else:
                raise ValidationError(detail="User Doesn't exist.",code=status.HTTP_404_NOT_FOUND)
        
        if not user.check_password(raw_password=password):
            raise ValidationError(detail='invalid password',code=status.HTTP_400_BAD_REQUEST)
        if not user.is_active:
            raise ValidationError(detail='inactive account',code=status.HTTP_403_FORBIDDEN)
        access_token, refresh_token = create_tokens(user=user)
        data = {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
        set_cache(key=f'{user}_token_data', value=json.dumps(UserTokenSerializer(user).data), ttl=5*60*60)
        return Response(data=data, status=status.HTTP_201_CREATED)
    except Users.DoesNotExist:
        raise ValidationError(detail="User Doesn't exist.",code=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request: Request) -> Response:
    username = request.user.username
    delete_cache(f'{username}_token_data')
    return Response({"message": "Successfully logged out"})


# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         request.user.auth_token.delete()
#         return Response({'message': 'Successfully logged out.'})

@api_view(['POST'])
@permission_classes([AllowAny])
def refreshed_token(request: Request) -> Response:
    refreshed_token = request.data.get('refresh_token')
    try:
        payload = jwt.decode(jwt=refreshed_token, key=settings.SECRET_KEY, algorithms='HS256', verify=True)
        if payload['token_type'] != 'refresh':
            return JsonResponse(data={
                'message': 'no refresh token provided',
                'success': False
            }, status=400)
        user_name = payload.get('username')
        user_obj = get_object_or_404(Users, username=user_name)
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