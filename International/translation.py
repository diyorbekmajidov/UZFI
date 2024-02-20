from modeltranslation.translator import  TranslationOptions, register
from .models import (
    InternationalRelations,
    InternationalMemorandum,
    InternationalGrant,
    StudentGroups,
    Abitur
    )

@register(InternationalRelations)
class InternationalRelationsTranslationOptions(TranslationOptions):
    fields = ('title','body',)

@register(Abitur)
class AbiturTranslationOptions(TranslationOptions):
    fields = ('title',"body",)

@register(InternationalMemorandum)
class InternationalMemorandumTranslationOptions(TranslationOptions):
    fields = ('title','body',)

@register(InternationalGrant)
class InternationalGrantTranslationOptions(TranslationOptions):
    fields = ('title','body',)

@register(StudentGroups)
class StudentGroupsTranslationOptions(TranslationOptions):
    fields = ('title','body',)
