from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from .user import User
from .models import ScientificWork,Faculty, Kafedra

class Leadership(models.Model):
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
    

class Dekan(models.Model):
    dekan        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dekan')
    faculty      = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='faculty')
    scientific_work = models.ForeignKey(ScientificWork, on_delete=models.CASCADE, blank=True,null=True)
    name         = models.CharField(max_length=100, blank=True, null=True)
    email        = models.CharField(max_length=100, blank=True, null=True)
    phone        = models.CharField(max_length=100, blank=True, null=True)
    acceptance   = models.CharField(max_length=200, blank=True, null=True)
    address      = models.CharField(max_length=100, blank=True, null=True)
    img          = models.ImageField(upload_to='img/',blank=True, null=True)
    duties       = RichTextUploadingField(blank=True, null=True)
    biography    = RichTextUploadingField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class KafedraManager(models.Model):
    kafedramanager = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kafedramanager')
    kafedra        = models.ForeignKey(Kafedra, on_delete=models.CASCADE, related_name='kafedra')
    scientific_work = models.ForeignKey(ScientificWork, on_delete=models.CASCADE, blank=True,null=True)
    name           = models.CharField(max_length=100, blank=True, null=True)
    email          = models.CharField(max_length=100, blank=True, null=True)
    phone          = models.CharField(max_length=100, blank=True, null=True)
    acceptance     = models.CharField(max_length=200, blank=True, null=True)
    address        = models.CharField(max_length=100, blank=True, null=True)
    img            = models.ImageField(upload_to='img/', blank=True, null=True)
    duties         = RichTextUploadingField(blank=True, null=True)
    date_created   = models.DateTimeField(auto_now_add=True)
    date_update    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 