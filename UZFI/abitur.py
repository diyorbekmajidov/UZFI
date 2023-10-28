
from django.urls import path
from .views.abitur import (
    RegulationOnSecondaryEducation,
    WorkWithTheAnswerSheet,
    FAQs
)

urlpatterns = [
    path("regulation-on-secondary-education/", RegulationOnSecondaryEducation.as_view()),
    path("work-with-the-answer-sheet/", WorkWithTheAnswerSheet.as_view()),
    path("faqs/", FAQs.as_view()),
]