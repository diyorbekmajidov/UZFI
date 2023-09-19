from modeltranslation.translator import  TranslationOptions, register
from .models import OpenData

@register(OpenData)
class OpenDataTranslationOptions(TranslationOptions):
        fields = ('name',)