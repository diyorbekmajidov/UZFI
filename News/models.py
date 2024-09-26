from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from UZFI.models import Dekan,KafedraManager,Leadership
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

COMMON_FIELDS_TRANSLATIONS = {
    "title": _('title'),
    "new_category": _('new_category'),
    "category": _('category'),
    "kafedramanager": _('kafedramanager'),
    "leadership": _('leadership'),
    "body": _('body'),
    "views": _('views'),
    "student_name": _('student_name'),
    "description": _('description'),
    "popular": _('popular',), 
    "event_name": _('event_name'),
    "place": _('place'),
    "start_date": _("start_date")
}

class NewsCategory(models.Model):
    new_category = models.CharField(max_length=255, verbose_name=COMMON_FIELDS_TRANSLATIONS['new_category'])

    def __str__(self) -> str:
        return self.new_category
    
def validate_file_size(value):
    filesize = value.size

    if filesize > 1000 * 2024:
        raise ValidationError("The maximum file size that can be uploaded is 2mb")
    else:
        return value
    
class News_Content(models.Model):
    category      = models.ManyToManyField(NewsCategory, verbose_name=COMMON_FIELDS_TRANSLATIONS['category'])
    title         = models.CharField(max_length=255, verbose_name=COMMON_FIELDS_TRANSLATIONS['title'])
    img           = models.ImageField(upload_to='img/', validators=[validate_file_size])
    body          = RichTextUploadingField(verbose_name=COMMON_FIELDS_TRANSLATIONS['body'])
    views         = models.IntegerField(default=0, verbose_name=COMMON_FIELDS_TRANSLATIONS['views'])
    date_created  = models.DateField()
    date_update   = models.DateField(auto_now=True)

    VERBOSE_NAME = _('News_Content')  

    class Meta:
        verbose_name = _('News Content')
        verbose_name_plural = _('News Contents')

    def __str__(self):
        return self.title or ""
    

class Vedio_New(models.Model):
    title         = models.CharField(max_length=255, verbose_name=COMMON_FIELDS_TRANSLATIONS["title"])
    vedio         = models.CharField(max_length = 10055)
    body          = models.ImageField(upload_to='img/', validators=[validate_file_size], verbose_name=COMMON_FIELDS_TRANSLATIONS["body"]) 
    views         = models.IntegerField(default=0, verbose_name=COMMON_FIELDS_TRANSLATIONS['views'])
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class PopularStudents(models.Model):
    student_name  = models.CharField(max_length=150, verbose_name=COMMON_FIELDS_TRANSLATIONS["student_name"])
    body          = RichTextUploadingField(verbose_name=COMMON_FIELDS_TRANSLATIONS["body"])
    description   = models.CharField(max_length=300, verbose_name=COMMON_FIELDS_TRANSLATIONS['description'])
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.student_name
    
class PopularStudentImg(models.Model):
    popular = models.ForeignKey(PopularStudents,on_delete=models.CASCADE, verbose_name=COMMON_FIELDS_TRANSLATIONS['popular'])
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size])

    def __str__(self) -> str:
        return self.popular.student_name
    

class UploadFile(models.Model):
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=255, verbose_name=COMMON_FIELDS_TRANSLATIONS['title'])
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.file.name
    def get_file_link(self):
        return 'https://uzfi.uz/'+self.file.url

    
class PendingEvents(models.Model):
    event_name    = models.CharField(max_length=150, verbose_name=COMMON_FIELDS_TRANSLATIONS['event_name'])
    place         = models.CharField(max_length=150, verbose_name=COMMON_FIELDS_TRANSLATIONS['place'])
    start_date    = models.DateField(verbose_name=COMMON_FIELDS_TRANSLATIONS['start_date'])
    views         = models.IntegerField(default=0, verbose_name=COMMON_FIELDS_TRANSLATIONS['views'])
    body          = RichTextUploadingField(verbose_name=COMMON_FIELDS_TRANSLATIONS['body'])
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size])
    date_created  = models.DateField()
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) ->str:
        return self.event_name