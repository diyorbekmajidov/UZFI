from django.urls import path
from .views import(
    InternationalMemorandumViews,InternationalMemorandumApiViews,
    InternationalGrantViews,InternationalGrantApiViews,
    StudentGroupsViews,StudentGroupsApiViews,
    LibraryViews,
    TtjViews,
    CorruptionEvent,
    CorruptionLaw,
    AbiturViewsById,AbiturViewsByIdApi,
    XalqaroHamkorlik,XalqaroHamkorlikApi
)

urlpatterns = [
    #api uchun
    path('abitur/api/<int:pk>/', AbiturViewsByIdApi.as_view()),
    path('internationalrelation/api/', XalqaroHamkorlikApi.as_view()),
    path('internationalmemorandum/api/', InternationalMemorandumApiViews.as_view()),
    path('internationalmemorandum/api/<int:pk>/', InternationalMemorandumApiViews.as_view()),
    path('studentgroups/api/', StudentGroupsApiViews.as_view()),
    path('internationalgrant/api/', InternationalGrantApiViews.as_view()),
    path('corruption/event/', CorruptionEvent.as_view()),
    # end api
    #International Relation views
    path('internationalrelation/', XalqaroHamkorlik.as_view()),
    path('internationalmemorandum/', InternationalMemorandumViews.as_view()),
    path('internationalmemorandum/<int:pk>/', InternationalMemorandumViews.as_view()),
    path('abitur/<int:pk>/', AbiturViewsById.as_view()),
    path('internationalgrant/', InternationalGrantViews.as_view()),
    path('studentgroups/', StudentGroupsViews.as_view()),
    path('library/', LibraryViews),
    path('ttj/', TtjViews),
    path('corruption/law/', CorruptionLaw.as_view())
]
