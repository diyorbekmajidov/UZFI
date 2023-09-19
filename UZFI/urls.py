from django.urls import path
from . import views
from .views import (
    CharterListCreate
)

urlpatterns = [
    path('', views.home, name='home'),
    path('charter/', CharterListCreate.as_view(), name='charter')
]