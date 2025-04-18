from django.contrib import admin
from .models import (InternationalGrant, InternationalGrantImg, InternationalMemorandum,
                      InternationalRelation, Abitur, StudentGroups, CommonInfo
                      )
from modeltranslation.admin import TranslationAdmin

@admin.register(InternationalRelation)
class  InternationalRelationAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(CommonInfo)
class CommonInfoAdmin(TranslationAdmin):
    list_display = ('title', 'date_created',)

@admin.register(Abitur)
class AbiturAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(InternationalMemorandum)
class InternationalMemorandumAdmin(TranslationAdmin):
    list_display = ('title',)
@admin.register(StudentGroups)
class StudentGroupsAdmin(TranslationAdmin):
    list_display = ('title',)

class InternationalGrantImgInline(admin.TabularInline):
    model = InternationalGrantImg

class InternationalGrantAdmin(TranslationAdmin):
    list_display = ('title',)
    inlines = [InternationalGrantImgInline]

admin.site.register(InternationalGrant,InternationalGrantAdmin)

