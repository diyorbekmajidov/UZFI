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
    Direction,
    Dekan,
    Kafedra,
    KafedraManager,
    ScientificWork,
    Leadership,
    CentersDepartments,
    CentersDepartmentsManager,
    Tutor,
    Menu,
    SubMenu,
)

@register(Menu)
class MenuTranationOtions(TranslationOptions):
    fields = ('title',)

@register(SubMenu)
class SubMenuTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(OpenData)
class OpenDataTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(FinancialStatements)
class FinancialStatementsTranslationOptions(TranslationOptions):
    fields = ('report_type','quarter',)

@register(Vacancies)
class VacanciesTranslationOptions(TranslationOptions):
    fields = ('name','body',)

@register(Charter)
class CharterTranslationOptions(TranslationOptions):
    fields = ('title','body',)

@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('document_type','document_name',)

@register(Councils)
class CouncilsTranslationOptions(TranslationOptions):
    fields = ('title','body',)

@register(Requisites)
class RequisitesTranslationOptions(TranslationOptions):
    fields = ('unversit_name','address',)

@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('name','body',)

@register(Dekan)
class DekanTranslationOptions(TranslationOptions):
    fields = ('acceptance','address','duties', 'biography','name',)

@register(Kafedra)
class KafedraTranslationOptions(TranslationOptions):
    fields = ('name','about',)

@register(KafedraManager)
class KafedraManagerTranslationOptions(TranslationOptions):
    fields = ('acceptance','address','duties','biography',"name",)


@register(Direction)
class DirectionTranslationOptions(TranslationOptions):
    fields = ('name','about',)

@register(ScientificWork)
class ScientificWorkTranslationOptions(TranslationOptions):
    fields = ("article_name","article_level",)

@register(Leadership)
class LeadershipTranslationOptions(TranslationOptions):
    fields = ("address","acceptance","biography","duties","prorektor","first_name",)

@register(CentersDepartments)
class CentersDepartmentTranslationOptions(TranslationOptions):
    fields = ("name","body",)

@register(CentersDepartmentsManager)
class CentersDepartmentsManagerTranslationOptions(TranslationOptions):
    fields = ("address","acceptance","name","lavozim",)

@register(Tutor)
class TutorTranslationOptions(TranslationOptions):
    fields = ("address","Task_tutors","general_information",'full_name')