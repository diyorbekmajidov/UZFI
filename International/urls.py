from django.urls import path, include
from .views import(
    InternationalMemorandumViews,
    InternationalMemorandumViewsById,
    InternationalGrantViews,
    StudentGroupsViews,
    LibraryViews,
    TtjViews,
    AbiturViewsById,
    InternationalRelationViews,
    InternationalRelationByIdViews
)

urlpatterns = [
    #International Relation views
    # path('internationalrelations/', InternationalRelationsViews.as_view(), name='international_relations'),
    path('internationalrelation/', InternationalRelationViews.as_view()),
    path('internationalmemorandum/', InternationalMemorandumViews.as_view()),
    path('internationalmemorandum/<int:pk>/', InternationalMemorandumViewsById.as_view()),
    path('int_det/<int:pk>/', InternationalRelationByIdViews.as_view(),),
    path('abitur/<int:pk>/', AbiturViewsById.as_view(),),
    path('internationalgrant/', InternationalGrantViews.as_view()),
    path('studentgroups/', StudentGroupsViews.as_view()),
    path('library/', LibraryViews.as_view()),
    path('ttj/', TtjViews.as_view())
    
]
