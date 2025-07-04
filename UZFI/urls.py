from django.urls import path
from .abitur import urlpatterns as abitur_urlpatterns
from .views import (
    Charterview,
    DocumentCreateview,DocumentCreateApiview,
    Councilsview,CouncilsApiview,
    Requisitesview,RequisitesApiview,
    OpenDataview,OpenDataApiview,
    Facultyview,FacultyApiview,
    Directionview,DirectionApiview,
    DirectionMagistrview,DirectionMagistrApiview,
    DekanById,DekanByIdApi,
    Kafedraview,KafedraApiview,
    KafedraManagerById,KafedraManagerByIdApi,
    # Register,
    CentersDepartmentView,CentersDepartmentApiView,DepartmentsView,
    # Dashboard,
    LeadershipAPIView,
    LeadershipByIdAPIView,
    Indicators,
    TutorView,TutorApiView,
    TutorFilterView,
    green_institute,
    eco_students,

    # app api
    UzfiStatistika,
    RapidlyApps,

)

urlpatterns = [
    # api url uchun 
    path('statistics/api/', UzfiStatistika.as_view(), name='statistics'),
    path('rapidly/api/', RapidlyApps.as_view(), name='tezkor ilovallar'),

    path('documents/api/', DocumentCreateApiview.as_view(), name='document'),
    path('councils/api/', CouncilsApiview.as_view()),
    path('councils/api/<int:pk>/', CouncilsApiview.as_view()),
    path('requisties/api', RequisitesApiview.as_view(), name='requisties'),
    path('open-data/api', OpenDataApiview.as_view(), name='opendata'),
    path('faculty/api/', FacultyApiview.as_view(), name='faculty'),
    path('faculty/api/<int:pk>/',FacultyApiview.as_view()),
    path('dekan/api/<int:pk>/', DekanByIdApi.as_view()),
    path('direction/api/<int:pk>/', DirectionApiview.as_view(), name='direction'),
    path('direction/magistr/api/', DirectionMagistrApiview.as_view()),
    path('kafedra/api/', KafedraApiview.as_view()),
    path('kafedra/api/<int:pk>/', KafedraApiview.as_view()),
    path('kafedra-manager/<int:pk>/', KafedraManagerByIdApi.as_view()),
    path('centers/api/', CentersDepartmentApiView.as_view()),
    path('centers/api/<int:pk>/', CentersDepartmentApiView.as_view()),
    path('tutor/api/', TutorApiView.as_view()),
    path('tutor/api/<int:pk>/', TutorApiView.as_view()),
    ##### api end

    path('magistr/', DirectionMagistrview.as_view(),),
    path('charter/', Charterview.as_view(), name='charter'),

    path('documents/', DocumentCreateview.as_view(), name='document'),

    path('councils/', Councilsview.as_view(), name='councils'),
    path('councils/<int:pk>/', Councilsview.as_view()),

    path('requisties/', Requisitesview.as_view(), name='requisties'),


    path('leadership/', LeadershipAPIView.as_view(), name='leadership'),
    path('leadership/<int:pk>/', LeadershipByIdAPIView.as_view()),

    path('open-data/', OpenDataview.as_view(), name='opendata'),

    path('centers/', CentersDepartmentView.as_view()),
    path('departments/', DepartmentsView.as_view()),
    path('centers/<int:pk>/', CentersDepartmentView.as_view()),

    path('faculty/', Facultyview.as_view(), name='faculty'),
    path('faculty/<int:pk>/',Facultyview.as_view()),

    path('direction/<int:pk>/', Directionview.as_view(), name='direction'),

    path('department/', Kafedraview.as_view()),
    path('department/<int:pk>/', Kafedraview.as_view()),


    path('dekan/<int:pk>/', DekanById.as_view()),
    
    path('department-manager/<int:pk>/', KafedraManagerById.as_view()),

    path('green-institute/', green_institute),
    path('eco-students/', eco_students),

    path('indicators/', Indicators.as_view()),

    path('tutor/', TutorView.as_view()),
    path('tutor/<int:pk>/', TutorView.as_view()),
    path('tutorfaculty/<int:pk>/', TutorFilterView.as_view(),name='tutor_det')
] + abitur_urlpatterns