from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from modeltranslation.admin import TranslationAdmin
from .models.models import User
from .models import *

class MyUserAdmin(UserAdmin):
    model = User

    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2','role')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
    )

admin.site.register(User,MyUserAdmin)

@admin.register(OpenData)
class OpenDataAdmin(TranslationAdmin):
    list_display = ('name',)

@admin.register(FinancialStatements)
class FinancialStatementsAdmin(TranslationAdmin):
    list_display = ('report_type','quarter',)

@admin.register(Vacancies)
class VacanciesAdmin(TranslationAdmin):
    list_display = ('name','body',)

@admin.register(Charter)
class CharterAdmin(TranslationAdmin):
    list_display = ('title','body',)

@admin.register(Document)
class DocumentAdmin(TranslationAdmin):
    list_display = ('document_type','document_name',)

@admin.register(Councils)
class CouncilsAdmin(TranslationAdmin):
    list_display = ('title','body')

@admin.register(Requisites)
class RequisitesAdmin(TranslationAdmin):
    list_display = ('unversit_name','address')

@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    list_display = ('name','body',)

@admin.register(Dekan)
class DekanAdmin(TranslationAdmin):
    list_display = ('acceptance','address','duties')

@admin.register(Kafedra)
class KafedraAdmin(TranslationAdmin):
    list_display = ('name','about',)

@admin.register(KafedraManager)
class KafedraManagerAdmin(TranslationAdmin):
    list_display = ('acceptance','address','duties')

@admin.register(Direction)
class DirectionAdmin(TranslationAdmin):
    list_display = ('name','about',)

@admin.register(ScientificWork)
class ScientificWorkAdmin(TranslationAdmin):
    list_display = ("article_name","article_level",)

@admin.register(Leadership)
class LeadershipAdmin(TranslationAdmin):
    list_display = ("address","acceptance","biography", "duties")

@admin.register(CentersDepartments)
class CentersDepartmentAdmin(TranslationAdmin):
    list_display = ("name","body")

@admin.register(CentersDepartmentsManager)
class CentersDepartmentManagerAdmin(TranslationAdmin):
    list_display = ("address","tasks","acceptance")


@admin.register(Tutor)
class TutorAdmin(TranslationAdmin):
    list_display = ("address",)
