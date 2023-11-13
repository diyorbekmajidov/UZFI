from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.response import Response
from django.views.generic import ListView
from .models import *
from .serializers import *
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


class InternationalRelationsViews(TemplateView):
    def get(self, request):
        try:
            internations = InternationalRelations.objects.all()
            serializers = InternationalRelationsSerializers(internations, many = True)
            return  render(request, 'international/InternationalRelations.html', {"data":serializers.data,})
        except Exception as e:
            print(e)
            return render(request,'international/InternationalRelations.html')

class InternationalRelationsByIDViews(TemplateView):
    def get(self, request, pk=1):
        try:
            internations = InternationalRelations.objects.filter(id=pk)
            serializers = InternationalRelationsSerializers(internations)
            return  render(request, '.html', {"data":serializers.data,})
        except Exception as e:
            print(e)
            return render(request,'.html')

class InternationalMemorandumViews(TemplateView):
    def get(self, request):
        try:
            internations = InternationalMemorandum.objects.all()
            serializers = InternationalMemorandumSerializers(internations, many = True)
            return  render(request, 'international/Internationalmemorandum.html', {"data":serializers.data,})
        except Exception as e:
            print(e)
            return render(request,'international/Internationalmemorandum.html')
        
class StudentGroupsViews(TemplateView):
    def get(self, request):
        try:
            internations = StudentGroups.objects.all()
            serializers = StudentGroupsSerializers(internations, many = True)
            return  render(request, 'list-of-additional.html', {"data":serializers.data,})
        except Exception as e:
            print(e)
            return render(request,'list-of-additional.html')
        
class InternationalGrantViews(TemplateView):
    def get(self, request):
        try:
            internations = InternationalGrant.objects.all()
            serializers = InternationalGrantSerializer(internations, many = True)
            return  render(request, 'international/international-grants.html', {"data":serializers.data,})
        except Exception as e:
            print(e)
            return render(request,'international/international-grants.html')