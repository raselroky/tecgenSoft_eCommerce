from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.generics import (
    ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
)
from .models import Division,District
from .serializers import DivisionSerializer,DistrictSerializer
from rest_framework.response import Response
from rest_framework import status


class AdminDivisionListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AdminDivisionListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    search_fields = ['name']

class AdminDivisionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DivisionSerializer
    queryset = Division.objects.filter()
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Division deleted successfully."}, status=status.HTTP_200_OK)




class AdminDistrictListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def create(self, request, *args, **kwargs):
        # Modify request data to include created_by
        data = request.data.copy()  # Create a mutable copy of request.data
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AdminDistrictListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    search_fields = ['name','division__name']

class AdminDistrictRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = District.objects.filter()
    serializer_class = DistrictSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "District deleted successfully."}, status=status.HTTP_200_OK)
    


#users

class UsersDivisionListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    search_fields = ['name']

class UsersDistrictListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    search_fields = ['name','division__name']