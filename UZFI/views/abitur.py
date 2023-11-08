from django.views.generic import TemplateView
from django.shortcuts import render


class RegulationOnSecondaryEducation(TemplateView):
    template_name = "abitur/regulation-on-secondary-education.html"
    
class WorkWithTheAnswerSheet(TemplateView):
    template_name = "abitur/work-with-the-answer-sheet.html"

class FAQs(TemplateView):
    template_name = "abitur/faqs.html"

class Acceptance(TemplateView):
    template_name = "abitur/acceptance.html"

class Regulation(TemplateView):
    template_name = "abitur/regulation.html"

class Commission(TemplateView):
    template_name = "abitur/commission.html"

class Magistratura(TemplateView):
    template_name = 'magistr.html'

class Bakalavriar(TemplateView):
    template_name = 'bachelor.html'

