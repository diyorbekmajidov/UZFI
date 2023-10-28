
from django.urls import path
from .views.abitur import (
    RegulationOnSecondaryEducation,
    WorkWithTheAnswerSheet
)

urlpatterns = [
    path("regulation-on-secondary-education/", RegulationOnSecondaryEducation.as_view()),
    path("work-with-the-answer-sheet/", WorkWithTheAnswerSheet.as_view()),
]