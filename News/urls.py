from django.urls import path, include
from .views import (
    NewsCategoryListCreate,
    NewsContentListAPIView,
    NewsContentApiviewGet,
    PopularStudentsApiView,
    GetUserNews,
    PopularStudentsById,
    LastNewsApiview,
    NewsContentCategoryAPIView,
    VedioNewsByID,
    VedioNews
)

urlpatterns = [

    # Categories
    path('category/', NewsCategoryListCreate.as_view(), name='news_category_list_create'),
    path('category/<int:category>/', NewsContentCategoryAPIView.as_view()),

    # Content
    path('content/', NewsContentListAPIView.as_view(), name='news_content_list_create'),
    path('content/<int:pk>/', NewsContentApiviewGet.as_view(), name='news_content_list_create'),

    path('popular-students/', PopularStudentsApiView.as_view()),
    path('popular-students/<int:pk>/', PopularStudentsById.as_view()),

    path('video-gallery/', VedioNews.as_view()),
    path('video-gallery/<int:pk>/', VedioNewsByID.as_view()),

    path('getusernews/', GetUserNews.as_view(),),
    path('lastnews/', LastNewsApiview.as_view()),
]