from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(NewsCategory)
admin.site.register(News_Content)
admin.site.register(Vedio_New)