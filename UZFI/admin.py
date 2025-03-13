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

@admin.register(Menu)
class OpenDataAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(SubMenu)
class OpenDataAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(GreenInstitute)
class OpenDataAdmin(TranslationAdmin):
    list_display = ('title','body',)

@admin.register(OpenData)
class OpenDataAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(Charter)
class CharterAdmin(TranslationAdmin):
    list_display = ('title','body',)

@admin.register(Document)
class DocumentAdmin(TranslationAdmin):
    list_display = ('document_type','document_name',)

@admin.register(Councils)
class CouncilsAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(Requisites)
class RequisitesAdmin(TranslationAdmin):
    list_display = ('unversit_name','address')

@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    list_display = ('name',)

@admin.register(Dekan)
class DekanAdmin(TranslationAdmin):
    list_display = ('name',)

@admin.register(Kafedra)
class KafedraAdmin(TranslationAdmin):
    list_display = ('name',)

@admin.register(KafedraManager)
class KafedraManagerAdmin(TranslationAdmin):
    list_display = ("name",)

@admin.register(Direction)
class DirectionAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(Leadership)
class LeadershipAdmin(TranslationAdmin):
    list_display = ("first_name","id")

@admin.register(CentersDepartments)
class CentersDepartmentAdmin(TranslationAdmin):
    list_display = ("name",)

@admin.register(CentersDepartmentsManager)
class CentersDepartmentManagerAdmin(TranslationAdmin):
    list_display = ("email", "name","id")


@admin.register(Tutor)
class TutorAdmin(TranslationAdmin):
    list_display = ("phone", "full_name","id")
