from django.urls import path, include
from .views import (
    NewsCategoryListCreate,
)

urlpatterns = [
    path('category/', NewsCategoryListCreate.as_view(), name='news_category_list_create'),
]