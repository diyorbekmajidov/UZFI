from django.urls import path
from . import views
from .views import (
    CharterListCreate,
    CharterRetrieveUpdate,
    DocumentCreate,
    DocumentRetrieveUpdate,
    CouncilsListCreate,
    CouncilsRetrieveUpdate,
    RequisitesListCreate,
    RequisitesRetrieveUpdate,
    FinancialStatementsListCreate,
    FinancialStatementsRetrieveUpdate,
    VacanciesListCreate,
    VacanciesListCreate,
    OpenDataListCreate,
    OpenDataRetrieveUpdate,
)

urlpatterns = [
    path('charter/', CharterListCreate.as_view(), name='charter'),
    path('charter/<int:pk>/', CharterRetrieveUpdate.as_view(), name='charter-detail'),

    path('document/', DocumentCreate.as_view(), name='document'),
    path('document/<int:pk>/', DocumentRetrieveUpdate.as_view(), name='document-detail'),

    path('councils/', CouncilsListCreate.as_view(), name='councils'),
    path('councils/<int:pk>/',CouncilsRetrieveUpdate.as_view() , name='council'),

    path('requisites/', RequisitesListCreate.as_view(), name='requisites'),
    path('requisites/<int:pk>/',RequisitesRetrieveUpdate.as_view() , name='requisites'),

    path('financial_statements/', FinancialStatementsListCreate.as_view(), name='financial_statements'),
    path('financial_statements/<int:pk>/', FinancialStatementsRetrieveUpdate.as_view(), name='financial_statements'),

    path('vacancies/', VacanciesListCreate.as_view(), name='vacancies'),
    path('vacancies/<int:pk>/', VacanciesListCreate.as_view(), name='vacancies'),

    path('opendata/', OpenDataListCreate.as_view(), name='opendata'),
    path('opendata/<int:pk>/', OpenDataRetrieveUpdate.as_view(), name='opendata'),
]