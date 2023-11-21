from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from UZFI.models import Dekan,KafedraManager,Leadership
from django.core.exceptions import ValidationError

class NewsCategory(models.Model):
    new_category = models.CharField(max_length=255)

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
    dekan         = models.ForeignKey(Dekan, on_delete=models.CASCADE, blank=True, null=True)
    kafedramanager= models.ForeignKey(KafedraManager, on_delete=models.CASCADE, blank=True, null = True)
    leadership    = models.ForeignKey(Leadership, on_delete=models.CASCADE, blank=True, null = True)
    title         = models.CharField(max_length=255)
    img           = models.ImageField(upload_to='img/', validators=[validate_file_size])
    body          = RichTextUploadingField()
    views         = models.IntegerField(default=0)
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Vedio_New(models.Model):
    title         = models.CharField(max_length=255)
    vedio         = models.CharField(max_length = 10055)
    body          = models.ImageField(upload_to='img/', validators=[validate_file_size]) 
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
    popular = models.ForeignKey(PopularStudents,on_delete=models.CASCADE )
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size])

    def __str__(self) -> str:
        return self.popular.student_name

    
class PendingEvents(models.Model):
    event_name    = models.CharField(max_length=150)
    place         = models.CharField(max_length=150)
    start_date    = models.DateField()
    views         = models.IntegerField(default=0)
    body          = RichTextUploadingField()
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size])
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) ->str:
        return self.event_name