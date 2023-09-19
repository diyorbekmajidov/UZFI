from django.urls import path
from . import views
from .views import (
    CharterListCreate,
    CharterRetrieveUpdate,
    DocumentCreate,
    DocumentRetrieveUpdate,
    CouncilsListCreate,
    CouncilsRetrieveUpdate
)

urlpatterns = [
    path('charter/', CharterListCreate.as_view(), name='charter'),
    path('charter/<int:pk>/', CharterRetrieveUpdate.as_view(), name='charter-detail'),

    path('document/', DocumentCreate.as_view(), name='document'),
    path('document/<int:pk>/', DocumentRetrieveUpdate.as_view(), name='document-detail'),

    path('councils/', CouncilsListCreate.as_view(), name='councils'),
    path('councils/<int:pk>/',CouncilsRetrieveUpdate.as_view() , name='council'),
]