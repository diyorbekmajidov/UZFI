from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models.models import *
from UZFI.serializers import *

from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from UZFI.models.user import User
class Register(APIView):
    def post(self, request):
        data = request.data
        data['password'] = make_password(request.data['password'])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            token = Token.objects.create(user=serializer.instance)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages)
    
class LogOut(APIView):
    authentication_classes = [TokenAuthentication]

    def post (self, request):
        request.user.auth_token.delete()
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
    
class Login(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        role = User.objects.get(username = user).role
        token = Token.objects.get_or_create(user=user)
        if token:
            token[0].delete()
        token= Token.objects.create(user=user)
        return Response({"token": token.key,"role":role}, status=status.HTTP_200_OK)
    
# class GetUserRole(APIView):
#     def get(self, request):
#         role = User.objects.all()
#         serializer = UserSerializer1(role, many=True)
#         return Response(serializer.data)
