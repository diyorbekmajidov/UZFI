from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models.models import *
from UZFI.serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# class DekanApiview(APIView):
#     def post(self, request):
#         data = request.data
#         data['password'] = make_password(data['password'])
#         serializers = DekanSerializer(data=data)
#         if serializers.is_valid():
#             serializers.save()
#             token = Token.objects.create(user=serializers.instance)
#             return Response({'token': token.key}, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DekanGetApiview(APIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        dekan = Dekan.objects.get(dekan=request.user)
        print(dekan.faculty)
        serializers = DekanSerializer(dekan)
        return Response(serializers.data)