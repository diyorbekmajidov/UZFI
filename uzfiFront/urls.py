from .views import (
    Index, 
    Charter,
    Documents,
    Councils,
    CouncilsItems,
    FinancialReports,
    Leadership,
    OrganizationStructure,
    Requisties,
    FamousGraduators,
    OpenData,
    Departments
)
from django.urls import path
urlpatterns = [
    path('', Index.as_view()),
    path('front/charter/', Charter.as_view()),
    path('front/documents/', Documents.as_view()),

    path('front/leadership/', Leadership.as_view()), #not completed
    path('front/organization-structure/', OrganizationStructure.as_view()), #not completed
    path('front/organization-structure/', OrganizationStructure.as_view()), #not completed

    path('front/councils/', Councils.as_view()),
    path('front/councils/<int:id>/', CouncilsItems.as_view()),

    path('front/requisties/', Requisties.as_view()), #not completed

    path('front/financial-reports/', FinancialReports.as_view()),

    path('front/famous-graduators/', FamousGraduators.as_view()), #not completed

    path('front/open-data/', OpenData.as_view()), 
    path('front/departments/', Departments.as_view()), 

]
