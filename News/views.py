from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,ListAPIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class NewsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class NewsCategoryListCreate(ListCreateAPIView):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer


class NewsContentListAPIView(ListAPIView):
    queryset = News_Content.objects.all()
    serializer_class = NewsContentSerializer
    pagination_class = NewsPagination
    

class NewsContentApiviewGet(APIView):
    def get(self, request, pk):
        news_content = News_Content.objects.get(pk=pk)
        views = news_content.views+1
        news_content.views = views
        news_content.save()
        serializer = NewsContentSerializer(news_content)
        return Response(serializer.data)

    def put(self, request, pk):
        news_content = News_Content.objects.get(pk=pk)
        serializer = NewsContentSerializer(news_content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        news_content = News_Content.objects.get(pk=pk)
        news_content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

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
        
class GetUserNewsTemplateView(TemplateView):
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