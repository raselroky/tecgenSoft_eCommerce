import datetime
from typing import Tuple
import jwt
from django.conf import settings
from user.models import User


def generate_access_token(user: User) -> str:
    token_data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email':user.email,
        'is_active': user.is_active,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=48),
        'token_type': 'access'
    }
    raw_token = jwt.encode(payload=token_data, key=settings.SECRET_KEY, algorithm='HS256')
    token = raw_token
    return token


def generate_refresh_token(user: User) -> str:
    token_data = {
        'username': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(weeks=1),
        'token_type': 'refresh'
    }
    raw_token = jwt.encode(payload=token_data, key=settings.SECRET_KEY, algorithm='HS256')
    token = raw_token
    return token


def create_tokens(user: User) -> Tuple[str, str]:
    return generate_access_token(user=user), generate_refresh_token(user=user)



from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
def generate_tokens_for_user(user,expiration=None):
    refresh = RefreshToken.for_user(user)
    if expiration:
        refresh.set_exp(lifetime=timedelta(seconds=expiration))
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
        
    }