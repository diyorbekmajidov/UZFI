from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.
from .models.models import *

class DekanAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'email', 'phone', 'acceptance']
    list_filter = ['dekan__role']  # dekan roli uchun filtrlash
    # search_fields = ['name', 'email', 'phone', 'acceptance']


admin.site.register(User)
admin.site.register(Dekan,DekanAdmin)
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
admin.site.register(KafedraTeacher)