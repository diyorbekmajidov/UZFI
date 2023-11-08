from django.views.generic import TemplateView
from django.shortcuts import render

class InternationalCooperation(TemplateView):
    template_name = "xalqaro/international-cooperation-relations.html"

class InternationalMemorandum(TemplateView):
    template_name = "xalqaro/international-scientific-relations.html"

