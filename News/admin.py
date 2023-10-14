from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

# Register your models here.
from .models import *

admin.site.register(PopularStudents)

@admin.register(NewsCategory)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('new_category',)

@admin.register(News_Content)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('title','body',)

@admin.register(Vedio_New)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('title',)

