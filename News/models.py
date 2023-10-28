from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from UZFI.models import Dekan,KafedraManager,Leadership

class NewsCategory(models.Model):
    new_category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.new_category
    
class News_Content(models.Model):
    category      = models.ManyToManyField(NewsCategory)
    dekan         = models.ForeignKey(Dekan, on_delete=models.CASCADE, blank=True, null=True)
    kafedramanager= models.ForeignKey(KafedraManager, on_delete=models.CASCADE, blank=True, null = True)
    leadership    = models.ForeignKey(Leadership, on_delete=models.CASCADE, blank=True, null = True)
    title         = models.CharField(max_length=255)
    img           = models.ImageField(upload_to='img/')
    body          = RichTextUploadingField()
    views         = models.IntegerField(default=0)
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Vedio_New(models.Model):
    title         = models.CharField(max_length=255)
    vedio         = RichTextUploadingField(null=True, config_name = 'default')
    body          = RichTextUploadingField(null=True,blank=True) 
    views         = models.IntegerField(default=0)
    date_created  = models.DateTimeField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class PopularStudents(models.Model):
    student_name  = models.CharField(max_length=150)
    body          = RichTextUploadingField()
    description   = models.CharField(max_length=300)
    img           = models.ImageField(upload_to='img')
    img1          = models.ImageField(upload_to='img', blank=True, null=True)
    img2          = models.ImageField(upload_to='img', blank=True, null=True)
    img3          = models.ImageField(upload_to='img', blank=True, null=True)
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.student_name
    
class PendingEvents(models.Model):
    event_name    = models.CharField(max_length=150)
    place         = models.CharField(max_length=150)
    start_date    = models.DateField()
    body          = RichTextUploadingField()
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) ->str:
        return self.event_name