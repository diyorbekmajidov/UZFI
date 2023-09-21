from modeltranslation.translator import  TranslationOptions, register
from .models import (
    OpenData,
    FinancialStatements,
    Vacancies,
    Charter,
    Document,
    Councils,
    Requisites,
    Faculty,
    Dekan,
    Kafedra,
    KafedraManager,
    KafedraTeacher,
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

@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('name','body',)

@register(Dekan)
class DekanTranslationOptions(TranslationOptions):
    fields = ('name','faculty','acceptance','address','duties')

@register(Kafedra)
class KafedraTranslationOptions(TranslationOptions):
    fields = ('name','about',)

@register(KafedraManager)
class KafedraManagerTranslationOptions(TranslationOptions):
    fields = ('name','acceptance','address','duties')

@register(KafedraTeacher)
class KafedraTeacherTranslationOptions(TranslationOptions):
    fields = ('name','biography','address',)