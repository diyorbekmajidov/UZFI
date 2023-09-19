from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models import *
from UZFI.serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CharterListCreate(ListCreateAPIView):
    queryset = Charter.objects.all()
    serializer_class = CharterSerializer

class CharterRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Charter.objects.all()
    serializer_class = CharterSerializer

class DocumentCreate(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class CouncilsListCreate(ListCreateAPIView):
    queryset = Councils.objects.all()
    serializer_class = CouncilsSerializer

class CouncilsRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Councils.objects.all()
    serializer_class = CouncilsSerializer