from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import (NewsCategory, News_Content, Vedio_New, PopularStudents, PopularStudentImg,  PendingEvents)
from django.views import View

from .serializers import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
from UZFI.models import Requisites 
from django.shortcuts import get_object_or_404
from UZFI.serializers import RequisitesSerializer

# class NewsPagination(PageNumberPagination):
#     page_size = 1
#     page_size_query_param = 'page_size'
#     max_page_size = 10000

class NewsContentView(TemplateView):
    template_name = 'news/news.html'
    paginate_by = 9

    def get(self, request):
        context = self.get_context_data(request)
        return render(request, self.template_name, context)

    def get_context_data(self, request):
        context = {}
        try:
            context['category'] = NewsCategory.objects.all()
            news_content = News_Content.objects.all().order_by("-date_created")
            paginator = Paginator(news_content, self.paginate_by)

            page_num = request.GET.get('page', 1)
            try:
                context['page_obj'] = paginator.page(page_num)
            except PageNotAnInteger:
                context['page_obj'] = paginator.page(1)

            context['last_news'] = News_Content.objects.order_by('-date_created')[:3]
        except Exception as e:
            print(f"Error retrieving news content: {e}")

        return context

class NewsContentCategoryView(TemplateView):
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


class NewsContentByIdView(TemplateView):
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


class PopularStudentsView(TemplateView):
    template_name = 'news/popular-students.html'

    def get(self, request, pk=None):
        if pk is not None:
            try:
                popular = PopularStudents.objects.get(id=pk)
                popular_serializer = PopularStudentsSerializer(popular)
                # Get the last 5 popular students
                last_populars = PopularStudents.objects.order_by('-date_created')[:5]
                last_populars_serializer = PopularStudentsSerializer(last_populars, many=True)
                context = {
                    "data": popular_serializer.data,
                    "populars": last_populars_serializer.data,
                }
                return render(request, 'news/popular-students-item.html', context)
            except PopularStudents.DoesNotExist:
                # Handle the case where the object does not exist
                return render(request, 'news/popular-students-item.html', {'error': 'Popular student not found'})
        try:
            populars = PopularStudents.objects.all().order_by('-date_created')
            serializer = PopularStudentsSerializer(populars, many=True)
            paginator = Paginator(serializer.data, 9)
            page_num = int(request.GET.get('page', 1))
            page_obj = paginator.get_page(page_num)
            
            context = {
                "page_obj": page_obj
            }
            return render(request, 'news/popular-students.html', context)
        except Exception as e:
            # Log the error properly
            print(e)
            return render(request, 'news/popular-students.html', {'error': 'An error occurred'})
            
        
class VedioNewsView(TemplateView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                video = Vedio_New.objects.get(id=pk)
                views = video.views+1
                video.views = views
                video.save()
                lastest = Vedio_New.objects.order_by("-id")[:5]
                lastest_serializer = VedioNewSerializer(lastest, many=True)
                return render(
                    request,
                    'news/video-gallery-item.html', 
                    {
                        "vedio_news":video,
                        "lastest":lastest_serializer.data
                    }
                )
            except Exception as e:
                print(e)
                return render(request,'news/video-gallery-item.html') 

        try:
            vedio_news = Vedio_New.objects.all().order_by("date_created")[::-1]
            page = Paginator(vedio_news, 9)
            page_num = int(request.GET.get('page', 1))
            return render(request,'news/video-gallery.html', {"page_obj":page.page(page_num)})
        except Exception as e:
            print(e)
            return render(request,'news/video-gallery.html')
    
# class VedioNewsByID(TemplateView):
#     def get(self, request,pk):
#         try:
#             vedio_new = Vedio_New.objects.get(id=pk)
#             views = video_vews.views + 1
#             vedio_new.views = views
#             serializers = VedioNewSerializer(vedio_new)
#             video_vews = Vedio_New.objects.all().order_by("id")
#             page = Paginator(video_vews, 9)
#             page_num = int(request.GET.get('page', 1))
#             return render(request,'news/video-gallery-item.html', {
#                 "vedio_news":serializers.data,
#                 "page_obj":page.page(page_num)})
#         except Exception as e:
#             print(e)
#             return render(request,'news/video-gallery-item.html') 
        
class SearchNews(TemplateView):
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
        

class PendingEvent(TemplateView):
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

    
class PendingEventById(TemplateView):
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
