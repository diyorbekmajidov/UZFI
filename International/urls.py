from django.urls import path, include
from .views import(
    InternationalRelationsViews,
    InternationalMemorandumViews
)

urlpatterns = [
    #International Relation views
    path('internationalrelations/', InternationalRelationsViews.index, name='international_relations'),
    path('internationalmemorandum/', InternationalMemorandumViews.add, name='add_international_relation'),
    
]
