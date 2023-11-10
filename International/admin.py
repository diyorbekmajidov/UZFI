from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(InternationalRelations)
class InternationalRelationsAdmin(TranslationAdmin):
    list_display = ('title','body',)

@admin.register(InternationalMemorandum)
class InternationalMemorandumAdmin(TranslationAdmin):
    list_display = ('title','body',)

class InternationalGrantImgInline(admin.TabularInline):
    model = InternationalGrantImg

class InternationalGrantAdmin(TranslationAdmin):
    list_display = ('title','body')
    inlines = [InternationalGrantImgInline]

admin.site.register(InternationalGrant,InternationalGrantAdmin)

