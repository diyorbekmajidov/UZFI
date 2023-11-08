
from django.urls import path
from .views.abitur import (
    RegulationOnSecondaryEducation,
    WorkWithTheAnswerSheet,
    FAQs,
    Acceptance,
    Regulation,
    Commission,
    Magistratura
)
from .views import(
    InternationalCooperation,
    InternationalMemorandum
)

urlpatterns = [
    path("regulation-on-secondary-education/", RegulationOnSecondaryEducation.as_view()),
    path("work-with-the-answer-sheet/", WorkWithTheAnswerSheet.as_view()),
    path("faqs/", FAQs.as_view()),
    path("admission-quota/", Acceptance.as_view()),
    path("commission/", Commission.as_view()),
    path('charter-admission/', Regulation.as_view()),
    path('magistrature/', Magistratura.as_view()),
]