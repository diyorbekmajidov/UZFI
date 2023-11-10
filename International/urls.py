from django.urls import path, include
from .views import(
    InternationalRelationsViews,
    InternationalMemorandumViews,
    InternationalGrantViews
)

urlpatterns = [
    #International Relation views
    path('internationalrelations/', InternationalRelationsViews.as_view(), name='international_relations'),
    path('internationalmemorandum/', InternationalMemorandumViews.as_view()),
    path('internationalgrant/', InternationalGrantViews.as_view()),
    
]
