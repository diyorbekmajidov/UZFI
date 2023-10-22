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
    FacultyByIdApview,
    DirectionApview,
    DekanGetApiview,
    AllDekan,
    GetDekanById,
    KafedraApview,
    KafedraManagerGet,
    KafedraManagerApview,
    GetAllKafedraManager,
    ScientificWorkAPIView,
    Register,
    logout,
    CentersDepartmentApiView,
    Login,
    Dashboard,
    LeadeshipAPIView

)

urlpatterns = [
    # path('', Index.as_view()),
    path('charter/', CharterApview.as_view(), name='charter'),

    path('documents/', DocumentCreateApview.as_view(), name='document'),

    path('councils/', CouncilsApview.as_view(), name='councils'),
    path('councils/<int:pk>/', CouncilsByIdApview.as_view()),

    path('requisties/', RequisitesApview.as_view(), name='requisties'),

    path('financial-statements/', FinancialStatementsApview.as_view(), name='financial-statements'),

    path('leadership/', LeadeshipAPIView.as_view(), name='leadership'),

    path('vacancies/', VacanciesApview.as_view(), name='vacancies'),

    path('opendata/', OpenDataApview.as_view(), name='opendata'),

    path('centersdepartment/', CentersDepartmentApiView.as_view()),

    path('faculty/', FacultyApview.as_view(), name='faculty'),
    path('faculty/<int:pk>/',FacultyByIdApview.as_view()),

    path('direction/<int:pk>/', DirectionApview.as_view(), name='direction'),
    path('kafedra/', KafedraApview.as_view()),

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