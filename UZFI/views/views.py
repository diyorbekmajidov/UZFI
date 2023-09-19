from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models import *
from UZFI.serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

def home(request):
    return render("vhxkbjnflam")

class CharterListCreate(ListCreateAPIView):
    queryset = Charter.objects.all()
    serializer_class = CharterSerializer
