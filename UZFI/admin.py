from django.contrib import admin
from .models.models import *
from django.contrib.auth.admin import UserAdmin

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username','role','password')}),

    )
    search_fields =  ('username',)
    ordering = ('username','role')



admin.site.register(User, UserAdmin)
admin.site.register(Dekan)
admin.site.register(Charter)
admin.site.register(Document)
admin.site.register(Councils)
admin.site.register(Requisites)
admin.site.register(FinancialStatements)
admin.site.register(OpenData)
admin.site.register(Vacancies)
admin.site.register(Faculty)
admin.site.register(Direction)
admin.site.register(Kafedra)
admin.site.register(KafedraManager)
admin.site.register(ScientificWork)