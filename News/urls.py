from django.urls import path, include
from .views import (
    NewsCategoryListCreate,
    NewsContentApiview
)

urlpatterns = [
    path('category/', NewsCategoryListCreate.as_view(), name='news_category_list_create'),
    path('content/', NewsContentApiview.as_view(), name='news_content_list_create')
]