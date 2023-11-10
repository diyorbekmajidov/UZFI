from django.urls import path, include
from .views import(
    InternationalRelationsViews,
    InternationalMemorandumViews,
    InternationalGrantViews
)

urlpatterns = [
    #International Relation views
    path('internationalrelations/', InternationalRelationsViews.index, name='international_relations'),
    path('internationalmemorandum/', InternationalMemorandumViews.add, name='add_international_relation'),
    path('internationalgrant/', InternationalGrantViews.as_view()),
    
]
