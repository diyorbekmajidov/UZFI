from django.urls import path
from . import views
from .views import (
    CharterApview,
    DocumentCreateApview,
    CouncilsApview,
    RequisitesApview,
    FinancialStatementsApview,
    VacanciesApview,
    OpenDataApview,
    FacultyApview,
    DirectionListCreate,
    DekanGetApiview,
    AllDekan,
    GetDekanById,
    KafedraManagerGet,
    KafedraManagerApview,
    GetAllKafedraManager,
    ScientificWorkAPIView,
    Register,
    LogOut,
    Login,

)

urlpatterns = [
    path('charter/', CharterApview.as_view(), name='charter'),

    path('document/', DocumentCreateApview.as_view(), name='document'),

    path('councils/', CouncilsApview.as_view(), name='councils'),

    path('requisites/', RequisitesApview.as_view(), name='requisites'),

    path('financial_statements/', FinancialStatementsApview.as_view(), name='financial_statements'),

    path('vacancies/', VacanciesApview.as_view(), name='vacancies'),

    path('opendata/', OpenDataApview.as_view(), name='opendata'),

    path('faculty/', FacultyApview.as_view(), name='faculty'),

    path('direction/', DirectionListCreate.as_view(), name='direction'),

    path('scientificwork/', ScientificWorkAPIView.as_view()),

    path('dekanget/', DekanGetApiview.as_view()),
    path('alldekan/', AllDekan.as_view()),
    path('getdekanbyid/<int:pk>/', GetDekanById.as_view()),
    
    path('kafedramanagerget/<int:pk>/', KafedraManagerGet.as_view()),
    path('getallkafedramanager/', GetAllKafedraManager.as_view()),
    path('kafedramanager/', KafedraManagerApview.as_view(),),

    path('register/', Register.as_view()),
    path('logout/', LogOut.as_view()),
    path('login/', Login.as_view()),
]