from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse, JsonResponse

from UZFI.models import (
    Charter as UZFI_Charter,
    Document as UZFI_Document,
    Councils as UZFI_Councils,
    FinancialStatements as UZFI_FinancialStatements,
)

class Index(TemplateView):
    template_name = 'en/index.html'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            print(self.request.user)
            return HttpResponseRedirect(reverse_lazy('charter'))
        return HttpResponse('dsa')
        

    