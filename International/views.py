from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.response import Response
from django.views.generic import ListView
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
   

class AbiturViewsById(APIView):
    def get(self, request, pk):
        try:
            abi = Abitur.objects.get(id=pk)
            serializers = AbiturSerializers(abi)
            return render(request, 'abitur/int_det.html',{"data":serializers.data})
        except Exception as e:
            return render(request,'abitur/int_det.html')

class InternationalRelationViews(APIView):
    def get(self, request):
        try:
            internations = InternationalRelation.objects.all().order_by("date_created")[::-1]
            serializers = InternationalRelationSerializers(internations, many=True)
            page = Paginator(serializers.data, 6)
            page_num = int(request.GET.get('page', 1))
            
            return  render(request, 'international/InternationalNews.html', 
                           {"page_obj":page.page(page_num)})
        except Exception as e:
            print(e)
            return  render(request, '404.html')

class InternationalRelationByIdViews(APIView):
    def get(self, request, pk):
        try:
            internations = InternationalRelation.objects.get(id=pk)
            serializers = InternationalRelationSerializers(internations)
            last_news = InternationalRelation.objects.order_by('date_created')[:3:-1]
            return  render(request, 'International/int_det.html', {"data":serializers.data,"last_news":last_news})
        except Exception as e:
            print(e)
            return render(request, 'International/int_det.html')
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
        
    

class LibraryViews(TemplateView):
    template_name = "library.html"

class TtjViews(TemplateView):
    template_name = "ttj.html"