from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class NewsCategory(models.Model):
    new_category = models.CharField(max_length=255,)

    def __str__(self) -> str:
        return self.new_category
    
def validate_file_size(value):
    filesize = value.size

    if filesize > 1000 * 2024:
        raise ValidationError("The maximum file size that can be uploaded is 2mb")
    else:
        return value
    
class News_Content(models.Model):
    category      = models.ManyToManyField(NewsCategory)
    title         = models.CharField(max_length=255)
    img           = models.ImageField(upload_to='img/', validators=[validate_file_size])
    body          = RichTextUploadingField()
    views         = models.IntegerField(default=0)
    date_created  = models.DateField()
    date_update   = models.DateField(auto_now=True)


    def __str__(self):
        return self.title or ""
    

class Vedio_New(models.Model):
    title         = models.CharField(max_length=255)
    vedio         = models.CharField(max_length = 10055)
    body          = models.ImageField(upload_to='img/') 
    views         = models.IntegerField(default=0)
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class PopularStudents(models.Model):
    student_name  = models.CharField(max_length=150)
    body          = RichTextUploadingField()
    description   = models.CharField(max_length=300)
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.student_name
    
class PopularStudentImg(models.Model):
    popular = models.ForeignKey(PopularStudents,on_delete=models.CASCADE)
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size])

    def __str__(self) -> str:
        return self.popular.student_name
    

class UploadFile(models.Model):
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=255)
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.file.name
    def get_file_link(self):
        return 'https://uzfi.uz/'+self.file.url

    
class PendingEvents(models.Model):
    event_name    = models.CharField(max_length=150)
    place         = models.CharField(max_length=150)
    start_date    = models.DateField()
    views         = models.IntegerField(default=0)
    body          = RichTextUploadingField()
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size])
    date_created  = models.DateField()
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) ->str:
        return self.event_name