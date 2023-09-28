from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *


class NewsCategoryListCreate(ListCreateAPIView):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer


class NewsContentApiview(APIView):
    def get(self, request):
        news_content = News_Content.objects.all()
        serializer = NewsContentSerializer(news_content, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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