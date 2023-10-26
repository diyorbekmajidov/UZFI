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
    

class Dashboard(TemplateView):
    def get(self, request):
        user = self.request.user
        if user.role == 'DEKAN':
            dekan = Dekan.objects.filter(dekan=user).first()
            data = News_Content.objects.filter(dekan=dekan)
            serializers = UserNewsSerializer(data, many = True)
            serializers1 = GetDekanSerializer(dekan)
            return render(request, 'dashboard.html',
            {'data_news':serializers.data,
            'data':serializers1.data
                       })
        if user.role == 'MANAGER':
            manager = KafedraManager.objects.filter(kafedra = user )
            serializers = GetKafedraManagerSerializer(manager , many = True)

            news_manager = News_Content.objects.filter(kafedramanager = manager)
            serializers1 = UserNewsSerializer(news_manager)
            return render(request, 'dashboard.html',
            {'data':serializers.data,
             "data_news":serializers1.data
                       })
        if user.role == 'REKTOR':
            rektor = Leadership.objects.filter(rector=user).last()
            serializers = LeadershipSerializer(rektor)

            new_rektor = News_Content.objects.filter(leadership=rektor)
            serializers1 = UserNewsSerializer(new_rektor, many=True)

            scientific_work = ScientificWork.objects.filter(user = user)
            serializers3 = ScientificWorkSerializer(scientific_work, many=True)
            return render(request, 'dashboard.html', {
                "data":serializers.data,
                "data_news":serializers1.data,
                "scientificwork":serializers3.data,
                })

        return render(request, 'dashboard.html')
    
class Login(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('dashboard'))
        return HttpResponse('dsa')
    

