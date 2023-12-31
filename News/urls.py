from django.urls import path, include
from .views import (
    NewsContentListAPIView,
    NewsContentApiviewGet,
    PopularStudentsApiView,
    PopularStudentsById,
    NewsContentCategoryAPIView,
    VedioNewsByID,
    VedioNews,
    SearchNewsApiView,
    PendingEventByIdApiviews,
    PendingEventApiviews,
    PendingEventSearchApiviews,
    Contact,
)

urlpatterns = [

    # Categories
    path('category/<int:category>/', NewsContentCategoryAPIView.as_view()),

    # Content
    path('content/', NewsContentListAPIView.as_view(), name='news_content_list_create'),
    path('content/<int:pk>/', NewsContentApiviewGet.as_view(), name='news_content_list_create'),

    path('popular-students/', PopularStudentsApiView.as_view()),
    path('popular-students/<int:pk>/', PopularStudentsById.as_view()),

    path('video-gallery/', VedioNews.as_view()),
    path('video-gallery/<int:pk>/', VedioNewsByID.as_view()),

    path('searchnews/', SearchNewsApiView.as_view()),

    path('events/', PendingEventApiviews.as_view()),
    path('events/<int:pk>/', PendingEventByIdApiviews.as_view()),
    path('events/<str:text>/', PendingEventSearchApiviews.as_view()),

    path('contact/', Contact.as_view()),

]