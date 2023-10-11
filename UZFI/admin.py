from django.contrib import admin
from .models.models import *
from django.contrib.auth.admin import UserAdmin
from .models.models import User

class MyUserAdmin(UserAdmin):
    model = User
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    # search_fields =  ('username',)
    # ordering = ('username','role')



admin.site.register(User, MyUserAdmin)
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