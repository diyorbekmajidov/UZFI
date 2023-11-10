from django.urls import path, include
from .views import(
    InternationalRelationsViews,
    InternationalRelationsByIDViews,
    InternationalMemorandumViews,
    InternationalGrantViews,
)

urlpatterns = [
    #International Relation views
    path('internationalrelations/', InternationalRelationsViews.as_view(), name='international_relations'),
    # path('internationalrelations/<int:pk>', InternationalRelationsByIDViews.as_view()),
    path('internationalmemorandum/', InternationalMemorandumViews.as_view()),
    path('internationalgrant/', InternationalGrantViews.as_view()),
    
]
