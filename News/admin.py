from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ("title",'get_file_link',)
@admin.register(NewsCategory)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('new_category','id',)

@admin.register(News_Content)
class News_ContentAdmin(TranslationAdmin):
    list_display = ('title', 'id',)

@admin.register(Vedio_New)
class Vedio_NewAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(PendingEvents)
class PendingEventsAdmin(TranslationAdmin):
    list_display = ('event_name',)


class PopularStudentImgInline(admin.TabularInline):
    model = PopularStudentImg
    

class PopularStudentsAdmin(TranslationAdmin):
    list_display = ('student_name',)
    inlines = [PopularStudentImgInline]

admin.site.register(PopularStudents,PopularStudentsAdmin)


