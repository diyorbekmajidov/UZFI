from django.urls import path
from .abitur import urlpatterns as abitur_urlpatterns
from .views import (
    CharterApview,
    DocumentCreateApview,
    CouncilsApview,
    RequisitesApview,
    FinancialStatementsApview,
    VacanciesApview,
    OpenDataApview,
    FacultyApview,
    DirectionApview,
    DirectionMagistrApview,
    DekanById,
    KafedraApview,
    KafedraManagerById,
    ScientificWorkAPIView,
    Register,
    CentersDepartmentApiView,
    Login,
    Dashboard,
    LeadershipAPIView,
    LeadershipByIdAPIView,
    Indicators,
    TutorAPIView,
    TutorFilterAPIView

)

urlpatterns = [
    path('magistr/', DirectionMagistrApview.as_view(),),
    # path('', Index.as_view()),
    path('charter/', CharterApview.as_view(), name='charter'),

    path('documents/', DocumentCreateApview.as_view(), name='document'),

    path('councils/', CouncilsApview.as_view(), name='councils'),
    path('councils/<int:pk>/', CouncilsApview.as_view()),

    path('requisties/', RequisitesApview.as_view(), name='requisties'),

    path('financial-statements/', FinancialStatementsApview.as_view(), name='financial-statements'),

    path('leadership/', LeadershipAPIView.as_view(), name='leadership'),
    path('leadership/<int:pk>/', LeadershipByIdAPIView.as_view()),

    path('vacancies/', VacanciesApview.as_view(), name='vacancies'),
    path('vacancies/<int:pk>/', VacanciesApview.as_view()),

    path('open-data/', OpenDataApview.as_view(), name='opendata'),

    path('centers/', CentersDepartmentApiView.as_view()),
    path('centers/<int:pk>/', CentersDepartmentApiView.as_view()),

    path('faculty/', FacultyApview.as_view(), name='faculty'),
    path('faculty/<int:pk>/',FacultyApview.as_view()),

    path('direction/<int:pk>/', DirectionApview.as_view(), name='direction'),

    path('departments/', KafedraApview.as_view()),
    path('departments/<int:pk>/', KafedraApview.as_view()),

    path('scientificwork/', ScientificWorkAPIView.as_view()),

    path('dekan/<int:pk>/', DekanById.as_view()),
    
    path('department-manager/<int:pk>/', KafedraManagerById.as_view()),

    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    path('indicators/', Indicators.as_view()),

    path('tutor/', TutorAPIView.as_view()),
    path('tutorfaculty/<int:pk>/', TutorFilterAPIView.as_view(),name='tutor_det')
] + abitur_urlpatterns