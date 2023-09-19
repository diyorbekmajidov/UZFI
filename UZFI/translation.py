from modeltranslation.translator import  TranslationOptions, register
from .models import (
    OpenData,
    FinancialStatements,
    Vacancies,
    Charter,
    Document,
    Councils,
    Requisites
)

@register(OpenData)
class OpenDataTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(FinancialStatements)
class FinancialStatementsTranslationOptions(TranslationOptions):
    fields = ('report_type','quarter',)

@register(Vacancies)
class VacanciesTranslationOptions(TranslationOptions):
    fields = ('name','body','department',)

@register(Charter)
class CharterTranslationOptions(TranslationOptions):
    fields = ('title','body',)

@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('document_type','document_name',)

@register(Councils)
class CouncilsTranslationOptions(TranslationOptions):
    fields = ('title','body')

@register(Requisites)
class RequisitesTranslationOptions(TranslationOptions):
    fields = ('unversit_name','address')