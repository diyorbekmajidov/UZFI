from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from .user import User
from .models import ScientificWork

class Rektor(models.Model):
    rector       = models.OneToOneField(User, on_delete=models.CASCADE , related_name="rector")
    scientific_work = models.ForeignKey(ScientificWork, on_delete=models.CASCADE, blank=True,null=True)
    first_name   = models.CharField(max_length=200, blank=True, null=True)
    email        = models.CharField(max_length=100, blank=True, null=True)
    phone        = models.CharField(max_length=100, blank=True, null=True)
    address      = models.CharField(max_length=100, blank=True, null=True)
    acceptance   = models.CharField(max_length=200, blank=True, null=True)
    img          = models.ImageField(upload_to='img/',blank=True, null=True)
    duties       = RichTextUploadingField(blank=True, null=True)
    biography    = RichTextUploadingField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name
    

class Prorektor(models.Model):
    prorektor = models.OneToOneField(User, on_delete=models.CASCADE, related_name="prorektor")
    first_name = models.CharField(max_length=150, blank=True, null=True)
    email        = models.CharField(max_length=100, blank=True, null=True)
    phone        = models.CharField(max_length=100, blank=True, null=True)
    address      = models.CharField(max_length=100, blank=True, null=True)
    acceptance   = models.CharField(max_length=200, blank=True, null=True)
    img          = models.ImageField(upload_to='img/',blank=True, null=True)
    duties       = RichTextUploadingField(blank=True, null=True)
    biography    = RichTextUploadingField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)