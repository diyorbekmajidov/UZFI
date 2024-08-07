from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.views.generic import ListView
from .models import *
from django.views import View

from .serializers import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
from UZFI.models import Requisites 
from django.shortcuts import get_object_or_404
from UZFI.serializers import RequisitesSerializer

class NewsPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000

class NewsContentListAPIView(View):  
    def get(self, request, *args, **kwargs):
        try:
            category = NewsCategory.objects.all()
            news_content = News_Content.objects.all().order_by("-date_created")
            paginator = Paginator(news_content, 9)

            page_num = request.GET.get('page', 1)
            

            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

            last_news = News_Content.objects.order_by('-date_created')[:3]

            return render(request, 'news/news.html', {
                "category": category,
                "last_news": last_news,
                "page_obj": page_obj,
            })
        except Exception as e:
            print(e)
            return render(request, 'news/news.html')
            

class NewsContentCategoryAPIView(ListView):
    def get(self, request, category):
        try:
            all_category = NewsCategory.objects.all()
            cat = NewsCategory.objects.filter(id=category).last()
            data = News_Content.objects.filter(category=cat).order_by("date_created")[::-1]
            serializer1 = NewsCategorySerializer(all_category, many = True)
            page = Paginator(data, 9)
            page_num = int(request.GET.get('page', 1))
                
            return render(request, 'news/news-category.html', {"page_obj":page.page(page_num), "category":serializer1.data, "current":cat.new_category})
        except Exception as e:
            print(e)
            return render(request,'news/news-category.html')


class NewsContentApiviewGet(TemplateView):
    template_name = 'news/news-item.html'
    
    def get(self, request, pk):
        news_content = get_object_or_404(News_Content, pk=pk)
        news_content.views += 1
        news_content.save()

        # Main content
        serializer = NewsContentSerializer(news_content)
        # Latest 5 items
        latest_queryset = News_Content.objects.order_by("-date_created")[:5]
        latest_serializer = NewsContentSerializer(latest_queryset, many=True)

        context = {
            "data": serializer.data,
            "latest": latest_serializer.data
        }
        return render(request, self.template_name, context)


class PopularStudentsApiView(TemplateView):
    def get(self, request):
        try:
            populars = PopularStudents.objects.all().order_by("date_created")[::-1]
            serializer = PopularStudentsSerializer(populars, many=True)
            page = Paginator(serializer.data, 9)
            page_num = int(request.GET.get('page', 1))
            return  render(request, 'news/popular-students.html', {"page_obj":page.page(page_num)})
        except Exception as e:
            print(e)
            return render(request,'news/popular-students.html')
            
class PopularStudentsById(TemplateView):
    def get(self, request, pk):
        try:
            populars = PopularStudents.objects.get(id=pk)
            serializers = PopularStudentsSerializer(populars)
            last_populars = PopularStudents.objects.order_by('-date_created')[:5]
            serializer2 = PopularStudentsSerializer(last_populars, many = True)
            return  render(request, 'news/popular-students-item.html', 
                           {"data":serializers.data,
                            "pouplar":serializer2.data,
                            })
        except Exception as e:
            print(e)
            return render(request,'news/popular-students-item.html')
        
class VedioNews(TemplateView):
    def get(self, request):
        try:
            vedio_news = Vedio_New.objects.all().order_by("date_created")[::-1]
            page = Paginator(vedio_news, 9)
            page_num = int(request.GET.get('page', 1))
            return render(request,'news/video-gallery.html', {"page_obj":page.page(page_num)})
        except Exception as e:
            print(e)
            return render(request,'news/video-gallery.html')
    
class VedioNewsByID(TemplateView):
    def get(self, request,pk):
        try:
            vedio_new = Vedio_New.objects.get(id=pk)
            views = video_vews.views + 1
            vedio_new.views = views
            serializers = VedioNewSerializer(vedio_new)
            video_vews = Vedio_New.objects.all().order_by("id")
            page = Paginator(video_vews, 9)
            page_num = int(request.GET.get('page', 1))
            return render(request,'news/video-gallery-item.html', {
                "vedio_news":serializers.data,
                "page_obj":page.page(page_num)})
        except Exception as e:
            print(e)
            return render(request,'news/video-gallery-item.html') 
        
class SearchNewsApiView(ListAPIView):
    def get(self, request):
        try :
            queryset = News_Content.objects.filter(title__icontains=request.POST.get("key", ""))
            serializers = NewsContentSerializer(queryset, many = True)
            queryset1 = PendingEvents.objects.filter(event_name__icontains=request.POST.get("key", ""))
            serializers1 = PendingEventsSerializer(queryset1, many = True)
            return render(request, 'news/search.html', {
                "news":serializers.data,
                "events" : serializers1.data
                })
        except Exception as e:
            print(e)
            return render(request,'news/search.html')
        

class PendingEventApiviews(TemplateView):
    def get(self, request):
        try:
            pending_events = PendingEvents.objects.all().order_by("date_created")[::-1]
            paginator = Paginator(pending_events, 9)

            page_num = request.GET.get('page', 1)
            

            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            serializers = PendingEventsSerializer(pending_events, many = True)
            return render(request, 'news/events.html', {
                "data":serializers.data,
                "page_obj": page_obj,})
        except Exception as e:
            print(e)
            return render(request,'news/events.html')

    
class PendingEventByIdApiviews(TemplateView):
    def get(self, request, pk):
        try:
            pending_events = PendingEvents.objects.get(id = pk)
            views = pending_events.views+1
            pending_events.views = views
            serializers = PendingEventsSerializer(pending_events)

            queryset = PendingEvents.objects.order_by('date_created')[:3]
            serializer_class = PendingEventsSerializer(queryset , many = True)

            return render(request, 'news/events-item.html', {"data":serializers.data, "latest":serializer_class.data})
        except Exception as e:
            print(e)
            return render(request,'news/events-item.html')

class PendingEventSearchApiviews(ListAPIView):
    def get(self, request, text):
        try :
            queryset = PendingEvents.objects.filter(event_name__=text)
            serializers = PendingEventsSerializer(queryset, many = True)
            return render(request, '.html', {"data":serializers.data})
        except:
            return render(request,'50x.error.html')
        
class Contact(TemplateView):
    def get(self, request):
        try:
            contact = Requisites.objects.last()
            serializers = RequisitesSerializer(contact)
            print(serializers.data)
            return render(request, 'news/contacts.html', {"data":serializers.data})
        except Exception as e:
            print(e)
            return render(request,'news/contacts.html')
