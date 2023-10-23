from modeltranslation.translator import  TranslationOptions, register
from .models import (
    NewsCategory,
    News_Content,
    Vedio_New,
    PopularStudents,
    )

@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('new_category',)

@register(News_Content)
class News_ContentTranslationOptions(TranslationOptions):
    fields = ('title','body',)

@register(Vedio_New)
class Vedio_NewTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(PopularStudents)
class PopularStudentsTranslationOptions(TranslationOptions):
    fields = ('body',)