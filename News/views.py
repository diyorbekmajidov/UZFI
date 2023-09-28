from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *


class NewsCategoryListCreate(ListCreateAPIView):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer