from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,ListAPIView
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class NewsPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


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
    
class GetUserNews(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get(self, request):
        user = request.user
        dekan = Dekan.objects.get(dekan=user)
        news = News_Content.objects.filter(dekan=dekan)
        print(news)
        # for i in news:
        #     print(type(i.dekan))
        #     if i.dekan == user:
        #         print('adf')
        return Response({"ok":200})