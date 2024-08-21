from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.core.paginator import Paginator
from News.models import News_Content
from News.serializers import NewsContentSerializer
   

class AbiturViewsById(APIView):
    def get(self, request, pk):
        try:
            abi = Abitur.objects.get(id=pk)
            serializers = AbiturSerializers(abi)
            return render(request, 'abitur/int_det.html',{"data":serializers.data})
        except Exception as e:
            return render(request,'abitur/int_det.html')
        
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
class InternationalMemorandumViews(TemplateView):
    def get(self, request):
        try:
            internations = InternationalMemorandum.objects.all()
            serializers = InternationalMemorandumSerializers(internations, many = True)
            page = Paginator(serializers.data, 4)
            page_num = int(request.GET.get('page', 1))
            return  render(request, 'international/Internationalmemorandum.html', {"page_obj":page.page(page_num)})
        except Exception as e:
            print(e)
            return render(request,'international/Internationalmemorandum.html')
        
class InternationalMemorandumViewsById(TemplateView):
    def get(self, request, pk):
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