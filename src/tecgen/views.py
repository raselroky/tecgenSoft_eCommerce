
from django.shortcuts import render
from rest_framework.response import Response
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

###
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
class ImageUploadView(APIView):
    permission_classes=(AllowAny,)
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        if 'image' not in request.FILES:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

        image = request.FILES['image']
        # Save the image
        file_name = image.name
        with open(f'media/{file_name}', 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)

        image_url = f'{request.build_absolute_uri(settings.MEDIA_URL)}{file_name}'
        return Response({'image_url': image_url}, status=status.HTTP_200_OK)