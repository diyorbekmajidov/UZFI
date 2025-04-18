from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import (InternationalGrant, InternationalMemorandum,
                    Abitur, StudentGroups, CommonInfo
                      )
from .serializers import (AbiturSerializers, InternationalMemorandumSerializers,StudentGroupsSerializers, InternationalGrantSerializer)
from django.core.paginator import Paginator
from News.models import News_Content
from rest_framework.response import Response
from News.serializers import NewsContentSerializer
   

class AbiturViewsById(TemplateView):
    def get(self, request, pk):
        try:
            abi = Abitur.objects.get(id=pk)
            serializers = AbiturSerializers(abi)
            return render(request, 'abitur/int_det.html',{"data":serializers.data})
        except Exception as e:
            return render(request,'abitur/int_det.html')
        
class AbiturViewsByIdApi(APIView):
    def get(self, request, pk):
        try:
            abi = Abitur.objects.get(id=pk)
            serializers = AbiturSerializers(abi)
            return Response({"data":serializers.data})
        except Exception as e:
            return Response({403:"ma'lumot topilmadi"})
        
class XalqaroHamkorlik(TemplateView):
    def get(self, request) :
        try:
            category = News_Content.objects.filter(category=10).order_by("date_created")[::-1]
            serializer = NewsContentSerializer(category, many = True)
            page = Paginator(category, 9)
            page_num = int(request.GET.get('page', 1))
            return render(request, 'international/InternationalNews.html', {"page_obj":page.page(page_num), "category":serializer.data})
        except Exception as e:
            print(f"Error retrieving news content: {e}")
            return render(request,'international/internationalrelation.html')
        


class CorruptionEvent(TemplateView):
    def get(self, request) :
        try:
            category = News_Content.objects.filter(category=14).order_by("date_created")[::-1]
            serializer = NewsContentSerializer(category, many = True)
            page = Paginator(category, 9)
            page_num = int(request.GET.get('page', 1))
            return render(request, 'international/corruption-event.html', {"page_obj":page.page(page_num), "category":serializer.data})
        except Exception as e:
            print(f"Error retrieving news content: {e}")
            return render(request,'international/corruption-event.html')
        
class XalqaroHamkorlikApi(APIView):
    def get(self, request) :
        try:
            category = News_Content.objects.filter(category=10).order_by("date_created")[::-1]
            serializer = NewsContentSerializer(category, many = True)
            page = Paginator(category, 9)
            page_num = int(request.GET.get('page', 1))
            return Response({"page_obj":page.page(page_num), "category":serializer.data})
        except Exception as e:
            print(f"Error retrieving news content: {e}")
            return Response({403:"ma'lumot topilmadi"})
        
class InternationalMemorandumViews(TemplateView):
    def get(self, request, pk = None):
        if pk is None:
            try:
                internations = InternationalMemorandum.objects.all()
                serializers = InternationalMemorandumSerializers(internations, many = True)
                page = Paginator(serializers.data, 4)
                page_num = int(request.GET.get('page', 1))
                return  render(request, 'international/Internationalmemorandum.html', {"page_obj":page.page(page_num)})
            except Exception as e:
                print(e)
                return render(request,'international/Internationalmemorandum.html')
        try:
            internations = InternationalMemorandum.objects.get(id=pk)
            serializers = InternationalMemorandumSerializers(internations)
            new_lastthree = News_Content.objects.all().order_by('date_created')[:3:-1]
            serializers_news = NewsContentSerializer(new_lastthree, many = True)
            return  render(request, 'international/Internationalmemorandum_det.html',
                            {"data":serializers.data,
                             "last_news":serializers_news.data})
        except Exception as e:
            return render(request, '404.html')
        
class InternationalMemorandumApiViews(APIView):
    def get(self, request, pk = None):
        if pk is None:
            try:
                internations = InternationalMemorandum.objects.all()
                serializers = InternationalMemorandumSerializers(internations, many = True)
                page = Paginator(serializers.data, 4)
                page_num = int(request.GET.get('page', 1))
                return  Response({"page_obj":page.page(page_num)})
            except Exception as e:
                return Response({403:"ma'lumot topilmadi"})
        try:
            internations = InternationalMemorandum.objects.get(id=pk)
            serializers = InternationalMemorandumSerializers(internations)
            return  Response(
                            {"data":serializers.data})
        except Exception as e:
            return Response({403:"ma'lumot topilmadi"})
        
class StudentGroupsViews(TemplateView):
    def get(self, request):
        try:
            internations = StudentGroups.objects.all()
            serializers = StudentGroupsSerializers(internations, many = True)
            return  render(request, 'list-of-additional.html', {"data":serializers.data,})
        except Exception as e:
            return render(request,'list-of-additional.html')
        
class StudentGroupsApiViews(APIView):
    def get(self, request):
        try:
            internations = StudentGroups.objects.all()
            serializers = StudentGroupsSerializers(internations, many = True)
            return  Response({"data":serializers.data,})
        except Exception as e:
            return Response({403:"ma'lumot topilmadi"})
        
class InternationalGrantViews(TemplateView):
    def get(self, request):
        try:
            internations = InternationalGrant.objects.all()
            serializers = InternationalGrantSerializer(internations, many = True)
            return  render(request, 'international/international-grants.html', {"data":serializers.data,})
        except Exception as e:
            print(e)
            return render(request,'international/international-grants.html')
        
class InternationalGrantApiViews(APIView):
    def get(self, request):
        try:
            internations = InternationalGrant.objects.all()
            serializers = InternationalGrantSerializer(internations, many = True)
            return  render({"data":serializers.data,})
        except Exception as e:
            return Response({403:"ma'lumot topilmadi"})

def LibraryViews(request):
    libary = CommonInfo.objects.filter(status = 'Libary').first()
    return render(request, 'library.html', {"library":libary})


def TtjViews(request):
    ttj = CommonInfo.objects.filter(status = 'Ttj').first()
    return render(request, 'ttj.html', {"ttj":ttj})

class CorruptionLaw(TemplateView):
    template_name = 'international/corruption-law.html'