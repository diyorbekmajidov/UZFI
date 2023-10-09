from django.urls import path, include
from .views import (
    NewsCategoryListCreate,
    NewsContentListAPIView,
    NewsContentApiviewGet,
    GetUserNews,
)

urlpatterns = [
    path('category/', NewsCategoryListCreate.as_view(), name='news_category_list_create'),
    path('content/', NewsContentListAPIView.as_view(), name='news_content_list_create'),
    path('content/<int:pk>/', NewsContentApiviewGet.as_view(), name='news_content_list_create'),
    path('getusernews/', GetUserNews.as_view(),)
]