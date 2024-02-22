from modeltranslation.translator import  TranslationOptions, register
from .models import (
    InternationalRelation,
    InternationalMemorandum,
    InternationalGrant,
    StudentGroups,
    Abitur
    )


@register(InternationalRelation)
class InternationalRelationTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)


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
