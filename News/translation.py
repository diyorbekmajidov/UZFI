from modeltranslation.translator import  TranslationOptions, register
from .models import (
    NewsCategory,
    News_Content)

@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('new_category',)

@register(News_Content)
class News_ContentTranslationOptions(TranslationOptions):
    fields = ('title','body',)