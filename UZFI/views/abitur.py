from django.views.generic import TemplateView
from django.shortcuts import render


class RegulationOnSecondaryEducation(TemplateView):
    template_name = "abitur/regulation-on-secondary-education.html"
    
class WorkWithTheAnswerSheet(TemplateView):
    template_name = "abitur/work-with-the-answer-sheet.html"

class FAQs(TemplateView):
    template_name = "abitur/faqs.html"