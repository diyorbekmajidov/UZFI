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
from django.db.models import Q

class NewsPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000

class NewsContentListAPIView(ListView):
    
    def get(self, request, *args, **kwargs):
        category = NewsCategory.objects.all()
        news_content = News_Content.objects.all()
        page = Paginator(news_content, 10)

        serializer1 = NewsCategorySerializer(category, many = True)
        page_num = int(request.GET.get('page', 1))

        last_news = News_Content.objects.order_by('-date_created')[:3]
        serializer3 = NewsContentSerializer(last_news, many = True)
        return render(request, 'news/news.html', {
            "category":serializer1.data,
            "last_news":serializer3.data,
            "page_obj":page.page(page_num)})

class NewsContentCategoryAPIView(ListView):
    def get(self, request, category):

        all_category = NewsCategory.objects.all()
        cat = NewsCategory.objects.filter(id=category).last()
        data = News_Content.objects.filter(category=cat)
        serializer1 = NewsCategorySerializer(all_category, many = True)
        page = Paginator(data, 10)
        page_num = int(request.GET.get('page', 1))
            
        return render(request, 'news/news-category.html', {"page_obj":page.page(page_num), "category":serializer1.data, "current":cat.new_category})


class NewsContentApiviewGet(TemplateView):
    def get(self, request, pk):
        news_content = News_Content.objects.get(pk=pk)
        views = news_content.views+1
        news_content.views = views
        news_content.save()
        serializer = NewsContentSerializer(news_content)
        queryset = News_Content.objects.order_by('-date_created')[:10]
        serializer_class = NewsContentSerializer(queryset , many = True)
        return render(request, 'news/news-item.html', {"data":serializer.data,
                                                  "latest":serializer_class.data})

class PopularStudentsApiView(TemplateView):
        def get(self, request):
            try:
                populars = PopularStudents.objects.all()
                serializers = PopularStudentsSerializer(populars, many = True)
                return  render(request, 'news/popular-students.html', {"data":serializers.data,})
            except Exception as e:
                print(e)
                return render(request,'50x.error.html')
            
class PopularStudentsById(TemplateView):
    def get(self, request, pk):
        try: 
            populars = PopularStudents.objects.get(id=pk)
            serializers = PopularStudentsSerializer(populars)
            last_populars = PopularStudents.objects.order_by('-date_created')[:5]
            serializer2 = PopularStudentsSerializer(last_populars, many = True)
            return  render(request, 'news/popular-students-item.html', 
                           {"data":serializers.data,
                            "pouplar":serializer2.data
                            })
        except:
            return render(request,'50x.error.html')
        
class VedioNews(TemplateView):
    def get(self, request):
        vedio_news = Vedio_New.objects.all()
        page = Paginator(vedio_news, 10)
        page_num = int(request.GET.get('page', 1))
        return render(request,'news/video-gallery.html', {"page_obj":page.page(page_num)})
    
class VedioNewsByID(TemplateView):
    def get(self, request,pk):
        try:
            vedio_new = Vedio_New.objects.get(id=pk)
            serializers = VedioNewSerializer(vedio_new)
            vedio_news = Vedio_New.objects.all()
            page = Paginator(vedio_news, 10)
            page_num = int(request.GET.get('page', 1))
            return render(request,'video-gallery-item.html', {
                "vedio_news":serializers.data,
                "page_obj":page.page(page_num)})
        except:
            return render(request,'50x.error.html') 
        
class SearchNewsApiView(ListAPIView):
    def get(self, request, text):
        try :
            queryset = News_Content.objects.filter(title__icontains=text)
            serializers = NewsContentSerializer(queryset, many = True)
            return render(request, '.html', {"data":serializers.data})
        except:
            return render(request,'50x.error.html')
        
class GetUserNews(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = NewsPagination
    serializer_class = UserNewsSerializer

    def get_queryset(self, request):
        user = self.request.user
        dekan = Dekan.objects.filter(dekan=user).first()
        if dekan:
            return News_Content.objects.filter(dekan=dekan)
        else:
            return News_Content.objects.none()

class PendingEventApiviews(TemplateView):
    def get(self, request):
        pending_events = PendingEvents.objects.all()
        serializers = PendingEventsSerializer(pending_events, many = True)
        return render(request, '.html', {"data":serializers.data})
    
class PendingEventByIdApiviews(TemplateView):
    def get(self, request, pk):
        try:
            pending_events = PendingEvents.objects.get(id = pk)
            serializers = PendingEventsSerializer(pending_events)
            return render(request, '.html', {"data":serializers.data})
        except:
            return render(request,'50x.error.html')

class PendingEventSearchApiviews(ListAPIView):
    def get(self, request, text):
        try :
            queryset = PendingEvents.objects.filter(event_name__=text)
            serializers = PendingEventsSerializer(queryset, many = True)
            return render(request, '.html', {"data":serializers.data})
        except:
            return render(request,'50x.error.html')