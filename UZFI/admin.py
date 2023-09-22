from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Charter)
admin.site.register(Document)
admin.site.register(Councils)
admin.site.register(Requisites)
admin.site.register(FinancialStatements)
admin.site.register(OpenData)
admin.site.register(Vacancies)
admin.site.register(Faculty)
admin.site.register(Dekan)
admin.site.register(Kafedra)
admin.site.register(KafedraManager)
admin.site.register(KafedraTeacher)