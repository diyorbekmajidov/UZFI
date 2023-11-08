
from django.urls import path
from .views.abitur import (
    RegulationOnSecondaryEducation,
    WorkWithTheAnswerSheet,
    FAQs,
    Acceptance,
    Regulation,
    Commission
)

urlpatterns = [
    path("regulation-on-secondary-education/", RegulationOnSecondaryEducation.as_view()),
    path("work-with-the-answer-sheet/", WorkWithTheAnswerSheet.as_view()),
    path("faqs/", FAQs.as_view()),
    path("acceptance/", Acceptance.as_view()),
    path("commission/", Commission.as_view()),
    path('regulation/', Regulation.as_view()),
]