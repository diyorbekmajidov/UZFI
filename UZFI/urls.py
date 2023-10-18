from django.urls import path
from . import views
from .views import (
    CharterApview,
    DocumentCreateApview,
    CouncilsApview,
    CouncilsByIdApview,
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
    logout,
    Login,
    Dashboard

)

urlpatterns = [
    path('charter/', CharterApview.as_view(), name='charter'),

    path('documents/', DocumentCreateApview.as_view(), name='document'),

    path('councils/', CouncilsApview.as_view(), name='councils'),
    path('councils/<int:pk>/', CouncilsByIdApview.as_view()),

    path('requisites/', RequisitesApview.as_view(), name='requisites'),

    path('financial-reports/', FinancialStatementsApview.as_view(), name='financial-reports'),

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
    path('logout/', views.logout),
    path('login/', Login.as_view()),
    path('dashboard/', Dashboard.as_view(), name='dashboard')
]