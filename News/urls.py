from django.urls import path, include
from .views import (
    NewsContentView,
    NewsContentByIdView,
    PopularStudentsView,
    # PopularStudentsById,
    NewsContentCategoryView,
    # VedioNewsByID,
    VedioNewsView,
    SearchNews,
    PendingEventById,
    PendingEvent,
    Contact,
)

urlpatterns = [

    # Categories
    path('category/<int:category>/', NewsContentCategoryView.as_view()),

    # Content
    path('content/', NewsContentView.as_view(), name='news_content_list_create'),
    path('content/<int:pk>/', NewsContentByIdView.as_view(), name='news_content_list_create'),

    path('popular-students/', PopularStudentsView.as_view()),
    path('popular-students/<int:pk>/', PopularStudentsView.as_view()),

    path('video-gallery/', VedioNewsView.as_view()),
    path('video-gallery/<int:pk>/', VedioNewsView.as_view()),

    path('searchnews/', SearchNews.as_view()),

    path('events/', PendingEvent.as_view()),
    path('events/<int:pk>/', PendingEventById.as_view()),

    path('contact/', Contact.as_view()),

]