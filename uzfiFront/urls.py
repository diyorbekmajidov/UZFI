from .views import (
    Index, 
    Charter,
    Documents,
    Councils,
    CouncilsItems,
    FinancialReports
)
from django.urls import path
urlpatterns = [
    path('', Index.as_view()),
    path('front/charter/', Charter.as_view()),
    path('front/documents/', Documents.as_view()),
    path('front/councils/', Councils.as_view()),
    path('front/councils/<int:id>/', CouncilsItems.as_view()),
    path('front/financial-reports/', FinancialReports.as_view()),
]
