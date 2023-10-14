from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from UZFI.models import Dekan

class NewsCategory(models.Model):
    new_category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.new_category
    
class News_Content(models.Model):
    yangiliklar   = models.ManyToManyField(NewsCategory)
    dekan         = models.ForeignKey(Dekan, on_delete=models.CASCADE, blank=True, null=True)
    title         = models.CharField(max_length=255)
    body          = RichTextUploadingField()
    views         = models.IntegerField(default=0)
    date_created  = models.DateTimeField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Vedio_New(models.Model):
    title         = models.CharField(max_length=255)
    body          = RichTextUploadingField(null=True, config_name = 'default')
    views         = models.IntegerField(default=0)
    date_created  = models.DateTimeField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class PopularStudents(models.Model):
    student_name  = models.CharField(max_length=150)
    body          = RichTextUploadingField()
    img           = models.ImageField(upload_to='img')
    date_created  = models.DateTimeField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.student_name