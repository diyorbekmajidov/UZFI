from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Charter)
admin.site.register(Document)
admin.site.register(Councils)
admin.site.register(Requisites)
admin.site.register(FinancialStatements)
admin.site.register(OpenData)
admin.site.register(Vacancies)