from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models import *
from UZFI.serializers import *

from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
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
    
def logout(request):
    logout(request)
    return render(request, 'endix.html')
    
class Login(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        role = User.objects.get(username = user).role
        token = Token.objects.get_or_create(user=user)
        if token:
            token[0].delete()
        token= Token.objects.create(user=user)
        return render(request, 'registration/login.html',{"user":user})
    

