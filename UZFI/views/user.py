from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models import *
from UZFI.serializers import *
from News.models import *
from News.serializers import *

from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth import logout
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
        if user.role == 'Dekan':
            dekan = Dekan.objects.filter(dekan=user).first()
            data = News_Content.objects.filter(dekan=dekan)
            serializers = UserNewsSerializer(data, many = True)
            dekan_data = Dekan.objects.filter(dekan=user)
            serializers1 = GetDekanSerializer(dekan_data , many = True)
            return render(request, 'dashboard.html',
            {'data_news':serializers.data,
            'dekan_data':serializers1.data
                       })
        if user.role == 'MANAGER':
            manager = KafedraManager.objects.filter(kafedra = user )

        
    
class Login(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        print('s')
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('dashboard'))
        return HttpResponse('dsa')
    

