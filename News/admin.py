from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

@admin.register(NewsCategory)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('new_category',)

@admin.register(News_Content)
class News_ContentAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(Vedio_New)
class Vedio_NewAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(PendingEvents)
class PendingEventsAdmin(TranslationAdmin):
    list_display = ('event_name',)


class PopularStudentImgInline(admin.TabularInline):
    model = PopularStudentImg
    

class PopularStudentsAdmin(TranslationAdmin):
    list_display = ('body','description')
    inlines = [PopularStudentImgInline]

admin.site.register(PopularStudents,PopularStudentsAdmin)


