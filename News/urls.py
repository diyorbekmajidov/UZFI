from django.urls import path
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers, permissions
from News import views



schema_view = get_schema_view(
    openapi.Info(
        title="MyApp API",
        default_version='v1',
        description="API documentation for MyApp",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from .views import (
    NewsContentView,
    news_items,
    PopularStudentsView,
    NewsContentCategoryView,
    VedioNewsView,
    PendingEventById,
    PendingEvent,
    Contact,

    NewsContentApiView,
    NewsCategoryApiView,
    VideoNewsApiView,
    EventApiView,
    applyfogrant
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # api views
    path('newscontent/api/', NewsContentApiView.as_view()),
    path('newscontent/api/<int:pk>/', NewsContentApiView.as_view()),

    path('newscategory/api/', NewsCategoryApiView.as_view()),
    path('newscategory/api/<int:pk>/', NewsCategoryApiView.as_view()),

    path('videonews/api/', VideoNewsApiView.as_view()),
    path('videonews/api/<int:pk>/', VideoNewsApiView.as_view()),

    path('event/api/', EventApiView.as_view()),
    path('event/api/<int:pk>/', EventApiView.as_view()),



    # Categories
    path('category/<int:category>/', NewsContentCategoryView.as_view()),

    # Content
    path('content/', NewsContentView.as_view(), name='news_content_list_create'),
    path('content/<int:pk>/', news_items, name='news_content_detail'),

    path('popular-students/', PopularStudentsView.as_view()),
    path('popular-students/<int:pk>/', PopularStudentsView.as_view()),

    path('video-gallery/', VedioNewsView.as_view()),
    path('video-gallery/<int:pk>/', VedioNewsView.as_view()),

    path('events/', PendingEvent.as_view()),
    path('events/<int:pk>/', PendingEventById.as_view()),

    path('contact/', Contact.as_view()),
    path('redistribution/', applyfogrant, name='apply_for_grant'),

]