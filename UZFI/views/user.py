from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models import *
from UZFI.serializers import *
from News.models import *

from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
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

class Dashboard(TemplateView):
    def get(self, request):
        user = self.request.user
        dekan = Dekan.objects.filter(dekan=user).first()
        if dekan:
            data = News_Content.objects.filter(dekan=dekan)
            dekan_data = Dekan.objects.get(dekan=dekan)
            serializers = GetDekanSerializer(dekan_data)
            return render(request, 'dashboard.html',{"data":data},{'dekan':serializers.data})
        else :
            return redirect('/login/')
    
class Login(TemplateView):
    def get(self, request, *args, **kwargs):
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            print(self.request.user)
            return HttpResponseRedirect(reverse_lazy('dashboard'))
        return HttpResponse('dsa')
    

