from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,ListAPIView
from django.views.generic import ListView
from .models import *
from .serializers import *
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class NewsPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000


class NewsCategoryListCreate(ListCreateAPIView): 
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer


class NewsContentListAPIView(ListView):
    
    def get(self, request, *args, **kwargs):
        category = NewsCategory.objects.all()
        news_content = News_Content.objects.all()
        page = Paginator(news_content, 10)
        serializer1 = NewsCategorySerializer(category, many = True)
        return render(request, 'news.html', {
            "category":serializer1.data,
            "page_obj":page.page(int(request.GET.get('page', 1)))
                    })

class NewsContentCategoryAPIView(ListView):
    def get(self, request, category):
        cat = NewsCategory.objects.filter(new_category=category).last()
        data = News_Content.objects.filter(category=cat)
        page = Paginator(data, 10)
        # serializers = NewsContentSerializer(data, many = True)
        return render(request, '.html', {"page_obj":page.page(int(request.GET.get('page', 1)))
                    })


class NewsContentApiviewGet(TemplateView):
    def get(self, request, pk):
        news_content = News_Content.objects.get(pk=pk)
        views = news_content.views+1
        news_content.views = views
        news_content.save()
        serializer = NewsContentSerializer(news_content)
        queryset = News_Content.objects.order_by('-date_created')[:10]
        serializer_class = NewsContentSerializer(queryset , many = True)
        return render(request, 'news-item.html', {"data":serializer.data,
                                                  "latest":serializer_class.data})

class GetUserNews(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = NewsPagination
    serializer_class = UserNewsSerializer

    def get_queryset(self):
        user = self.request.user
        dekan = Dekan.objects.filter(dekan=user).first()
        if dekan:
            return News_Content.objects.filter(dekan=dekan)
        else:
            return News_Content.objects.none()
        


class LastNewsApiview(ListAPIView):
    queryset = News_Content.objects.order_by('-date_created')[:10]
    serializer_class = NewsContentSerializer