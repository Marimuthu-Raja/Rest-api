from django.shortcuts import render
from .serializers import UserDetailsSerializer
from .models import UserDetails
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response


class UserDetailAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = UserDetailsSerializer
    queryset = UserDetails.objects.all()


    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
