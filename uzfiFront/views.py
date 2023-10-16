from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, JsonResponse

from UZFI.models import (
    Charter as UZFI_Charter,
    Document as UZFI_Document,
    Councils as UZFI_Councils,
    FinancialStatements as UZFI_FinancialStatements,
)

# Create your views here.


class Index(TemplateView):
    template_name = 'en/index.html'
    
class Charter(View):
    def get(self, req: HttpRequest, *args, **kwargs):
        data = []
        MODEL_DATA = UZFI_Charter.objects.all()
        for i, z in zip(MODEL_DATA, range(MODEL_DATA.__len__())): data.append({'data': {'title_en':i.title_en,'title_uz':i.title_uz,'title_ru':i.title_ru,'body_en':i.body_en,'body_uz':i.body_uz,'body_ru':i.body_ru,}, 'id': z})
        
        return render(req, {'uz':'uz', 'ru':'ru', 'en':'en'}.get(req.GET.get('lang'), 'uz') + '/charter.html', {'data':data}) 
    
class Documents(View):
    def get(self, req: HttpRequest, *args, **kwargs):
        data = []
        MODEL_DATA = UZFI_Document.objects.all()
        for i, z in zip(MODEL_DATA, range(1, MODEL_DATA.__len__()+1)): data.append({'data': {'document_name_en':i.document_name_en,'document_name_uz':i.document_name_uz,'document_name_ru':i.document_name_ru,'document_type_en':i.document_type,'document_type_uz':i.document_type_uz,'document_type_ru':i.document_type_ru,'document':i.document.url, 'document_date':i.date_created.strftime('%d.%m.%Y')}, 'id': z})


        return render(req, {'uz':'uz', 'ru':'ru', 'en':'en'}.get(req.GET.get('lang'), 'uz') + '/documents.html', {'data':data}) 


class Councils(View):
    def get(self, req: HttpRequest, *args, **kwargs):
        data = []
        MODEL_DATA = UZFI_Councils.objects.all()
        for i, z in zip(MODEL_DATA, range(MODEL_DATA.__len__())): data.append({'data': {'id':i.id, 'title_en':i.title_en,'title_uz':i.title_uz,'title_ru':i.title_ru,'body_en':i.body_en,'body_uz':i.body_uz,'body_ru':i.body_ru, 'date_created':i.date_created.strftime('%d.%m.%Y')}, 'id': z})

        return render(req, {'uz':'uz', 'ru':'ru', 'en':'en'}.get(req.GET.get('lang'), 'uz') + '/councils.html', {'data':data}) 
    

class CouncilsItems(View):
    def get(self, req: HttpRequest, id, *args, **kwargs):
        data = []
        MODEL_DATA = UZFI_Councils.objects.filter(id = int(id))
        for i, z in zip(MODEL_DATA, range(MODEL_DATA.__len__())): data.append({'data': {'id':i.id, 'title_en':i.title_en,'title_uz':i.title_uz,'title_ru':i.title_ru,'body_en':i.body_en,'body_uz':i.body_uz,'body_ru':i.body_ru, 'date_created':i.date_created.strftime('%d.%m.%Y')}, 'id': z})
        return render(req, {'uz':'uz', 'ru':'ru', 'en':'en'}.get(req.GET.get('lang'), 'uz') + '/councils-item.html', {'data':data}) 
    

class FinancialReports(View):
    def get(self, req: HttpRequest, *args, **kwargs):
        data = []
        MODEL_DATA = UZFI_FinancialStatements.objects.all()
        for i, z in zip(MODEL_DATA, range(1, MODEL_DATA.__len__()+1)): data.append({'data': {'report_type_en':i.report_type_en,'report_type_uz':i.report_type_uz,'report_type_ru':i.report_type_ru,'quarter_en':i.quarter,'quarter_uz':i.quarter_uz,'quarter_ru':i.quarter_ru,'pdf_file':i.pdf_file.url, 'date':i.date_created.strftime('%d.%m.%Y')}, 'id': z})


        return render(req, {'uz':'uz', 'ru':'ru', 'en':'en'}.get(req.GET.get('lang'), 'uz') + '/financial.html', {'data':data}) 
